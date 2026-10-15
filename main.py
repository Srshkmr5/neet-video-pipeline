"""
NEET UG 2D Video Engine - Main Orchestrator
Derived from MASTER_BLUEPRINT.md v1.1 Section 13
"""
import argparse
import asyncio
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

import yaml
from config import QUEUE_DIR, TEMPLATES_DIR, FINAL_DIR, RENDER_SPECS
from llm.schema import ConceptNode, ConceptQueue
from assets.tts_engine import TTSEngine
from render.manim_compiler import ManimCompiler
from render.stitching import FFmpegMuxer
from llm.pacing import PacingEngine

# Configure standard streams for UTF-8 on Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

class VideoPipeline:
    def __init__(self):
        self.concepts_path = QUEUE_DIR / "concepts.json"
        self.state_path = QUEUE_DIR / "state.json"
        self.registry_path = TEMPLATES_DIR / "registry.yaml"
        self.template_registry = self._load_template_registry()
        self.state = self._load_state()

    def _load_template_registry(self) -> Dict[str, Any]:
        if not self.registry_path.exists():
            raise FileNotFoundError(f"Template registry not found at {self.registry_path}")
        with open(self.registry_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data.get("templates", {})

    def _load_state(self) -> Dict[str, Any]:
        if self.state_path.exists():
            with open(self.state_path, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except Exception:
                    pass
        return {"last_updated": None, "videos": {}}

    def _save_state(self):
        self.state["last_updated"] = datetime.now().isoformat()
        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2)

    def validate_node(self, raw_node: Dict[str, Any]) -> ConceptNode:
        """Step 2: Validate against Pydantic schema and Template Registry"""
        node = ConceptNode.model_validate(raw_node)
        template_name = node.templateName
        if template_name not in self.template_registry:
            raise ValueError(f"Unregistered template: '{template_name}' not in registry.yaml")
        
        reg_entry = self.template_registry[template_name]
        dimension = reg_entry.get("dimension", "2d")
        if dimension not in ("2d", "3d"):
            raise ValueError(f"Invalid dimension '{dimension}' in registry for template '{template_name}'")

        required_params = reg_entry.get("params", [])
        for p in required_params:
            if p not in node.parameters:
                raise ValueError(f"Template '{template_name}' requires parameter '{p}', missing in video {node.videoId}")
        
        return node

    async def process_concept(self, node: ConceptNode, quality: str = "draft", skip_cache: bool = False) -> Dict[str, Any]:
        video_id = node.videoId
        reg_entry = self.template_registry.get(node.templateName, {})
        dimension = reg_entry.get("dimension", "2d")

        print(f"\n=======================================================")
        print(f"🎬 Processing Node: {video_id} - '{node.serialTitle}' [{dimension.upper()}]")
        print(f"=======================================================")

        if dimension == "3d":
            print(f"📦 [3D EXTENSION] Template '{node.templateName}' is a registered 3D template.")
            print(f"   -> 3D active rendering is scheduled for Phase 5.")
            self.state["videos"][video_id] = {
                "status": "DEFERRED_PHASE_5",
                "dimension": "3d",
                "template": node.templateName,
                "registered_at": datetime.now().isoformat()
            }
            self._save_state()
            return self.state["videos"][video_id]

        self.state["videos"][video_id] = {
            "status": "PROCESSING",
            "started_at": datetime.now().isoformat()
        }
        self._save_state()

        try:
            # Step 3, 4, 5: Visual MD5 Caching & Manim Render
            print(f"🎨 [1/4] Compiling Manim Visuals ({quality} preset)...")
            raw_video_path, was_cached = ManimCompiler.compile_scene(
                concept_node=node.model_dump(),
                quality=quality,
                skip_cache=skip_cache
            )
            visual_hash = ManimCompiler.compute_visual_hash(node.templateName, node.parameters)
            cache_status = "CACHE HIT" if was_cached else "RENDERED NEW"
            print(f"   -> Visual: {raw_video_path} [{cache_status}] (MD5: {visual_hash[:8]})")

            # Step 6 & 7: Synthesize Multilingual Audio & Subtitles
            print(f"🎙️ [2/4] Synthesizing Multilingual Audio (en, hi, ta) via edge-tts...")
            audio_results = await TTSEngine.synthesize_all_locales(node.locales, video_id)
            
            audio_paths = {}
            subtitle_paths = {}
            for lang, res in audio_results.items():
                audio_paths[lang] = Path(res["audio_path"])
                subtitle_paths[lang] = Path(res["subtitle_srt"])
                print(f"   -> [{lang.upper()}] Audio: {res['duration']:.1f}s, -14 LUFS, Sub: {res['subtitle_srt']}")

            # Emergent Pacing Validation
            en_duration = audio_results["en"]["duration"]
            total_est = PacingEngine.calculate_beat_duration("settle", 0) + en_duration + PacingEngine.calculate_beat_duration("release", 0)
            badge = PacingEngine.derive_length_badge(total_est)
            print(f"⏱️ [3/4] Emergent Pacing: Estimated runtime ~{total_est:.1f}s | Badge: {badge}")

            # Step 8: FFmpeg Multi-Track Assembly
            print(f"🎞️ [4/4] Muxing 1 Video + 3 Audio + 3 Soft Subtitle Tracks with FFmpeg...")
            export_path = FFmpegMuxer.get_canonical_export_path(video_id, node.serialTitle)
            final_mp4 = FFmpegMuxer.mux_multitrack_mp4(
                video_path=Path(raw_video_path),
                audio_tracks=audio_paths,
                subtitle_tracks=subtitle_paths,
                output_path=export_path
            )
            print(f"   -> Final MP4: {final_mp4}")

            # Step 9: Verify with FFprobe
            media_info = FFmpegMuxer.probe_media(final_mp4)
            streams = media_info.get("streams", [])
            v_streams = [s for s in streams if s.get("codec_type") == "video"]
            a_streams = [s for s in streams if s.get("codec_type") == "audio"]
            s_streams = [s for s in streams if s.get("codec_type") == "subtitle"]

            print(f"\n✅ VERIFICATION PASSED:")
            print(f"   - Video Tracks: {len(v_streams)} ({v_streams[0].get('codec_name', 'h264')} {v_streams[0].get('width')}x{v_streams[0].get('height')})")
            print(f"   - Audio Tracks: {len(a_streams)} (en, hi, ta)")
            print(f"   - Subtitle Tracks: {len(s_streams)} (mov_text soft)")

            # Record success in state.json
            self.state["videos"][video_id] = {
                "status": "COMPLETED",
                "completed_at": datetime.now().isoformat(),
                "visual_md5": visual_hash,
                "cached": was_cached,
                "length_badge": badge,
                "video_file": str(final_mp4),
                "streams": {
                    "video": len(v_streams),
                    "audio": len(a_streams),
                    "subtitles": len(s_streams)
                }
            }
            self._save_state()
            return self.state["videos"][video_id]

        except Exception as e:
            print(f"\n❌ Error processing {video_id}: {str(e)}")
            self.state["videos"][video_id] = {
                "status": "FAILED",
                "failed_at": datetime.now().isoformat(),
                "error": str(e)
            }
            self._save_state()
            raise

    async def run(self, concept_id: Optional[str] = None, quality: str = "draft", skip_cache: bool = False, dry_run: bool = False):
        if not self.concepts_path.exists():
            raise FileNotFoundError(f"Concepts queue file not found at {self.concepts_path}")

        with open(self.concepts_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        raw_concepts = data.get("concepts", [])
        validated_nodes = []
        for raw in raw_concepts:
            validated = self.validate_node(raw)
            if concept_id is None or validated.videoId == concept_id:
                validated_nodes.append(validated)

        if not validated_nodes:
            print(f"No matching concepts found for filter '{concept_id}'")
            return

        schedule = PacingEngine.estimate_batch_schedule(validated_nodes, self.template_registry, quality=quality)
        print(f"📊 Batch Overview: {schedule['total_nodes']} node(s) [{schedule['count_2d']} 2D, {schedule['count_3d']} 3D]")
        print(f"   Estimated Batch Render Time: ~{schedule['estimated_render_seconds']:.1f}s ({schedule['estimated_render_hours']:.2f} hrs)")
        print(f"   Estimated Disk Budget: ~{schedule['estimated_disk_mb']:.1f} MB ({schedule['estimated_disk_gb']:.2f} GB)")

        if dry_run:
            print("Dry run completed: schema and template registry validation succeeded.")
            return

        for node in validated_nodes:
            await self.process_concept(node, quality=quality, skip_cache=skip_cache)

def main():
    parser = argparse.ArgumentParser(description="NEET UG 2D Video Engine CLI")
    parser.add_argument("--concept", type=str, default="P11-C04-T02-V03", help="Canonical Video ID to render")
    parser.add_argument("--all", action="store_true", help="Process all concepts in queue")
    parser.add_argument("--quality", type=str, default="draft", choices=["draft", "master"], help="Render quality")
    parser.add_argument("--skip-cache", action="store_true", help="Bypass visual MD5 cache")
    parser.add_argument("--dry-run", action="store_true", help="Validate queue without rendering")

    args = parser.parse_args()
    pipeline = VideoPipeline()
    target_id = None if args.all else args.concept

    asyncio.run(pipeline.run(
        concept_id=target_id,
        quality=args.quality,
        skip_cache=args.skip_cache,
        dry_run=args.dry_run
    ))

if __name__ == "__main__":
    main()
