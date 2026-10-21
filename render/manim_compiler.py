"""
Manim Compiler & MD5 Visual Caching Subsystem
Derived from MASTER_BLUEPRINT.md v1.1 Section 8, 13, 18
"""
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any, Tuple

from config import RENDER_SPECS, RAW_VIDEO_DIR, BASE_DIR

class ManimCompiler:
    @staticmethod
    def compute_visual_hash(template_name: str, parameters: Dict[str, Any], dimension: str = "2d", theme: str = "") -> str:
        """
        Computes MD5 hash of template name, dimension, theme, and visual parameters.
        Visual cache skips render if parameters are identical.
        """
        payload = {
            "template": template_name,
            "dimension": dimension,
            "theme": theme,
            "params": parameters
        }
        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.md5(serialized.encode("utf-8")).hexdigest()

    @classmethod
    def get_cached_video_path(cls, video_id: str, visual_hash: str) -> Path:
        return RAW_VIDEO_DIR / f"{video_id}_{visual_hash}.mp4"

    @classmethod
    def compile_scene(
        cls,
        concept_node: Dict[str, Any],
        quality: str = "draft",
        skip_cache: bool = False
    ) -> Tuple[str, bool]:
        """
        Compiles the Manim scene for the given concept node (supports 2D and 3D).
        Returns: (output_video_path, was_cache_hit)
        """
        video_id = concept_node["videoId"]
        template_name = concept_node["templateName"]
        dimension = concept_node.get("dimension", "2d").lower()
        theme = concept_node.get("theme", "")
        parameters = concept_node.get("parameters", {})
        spec = RENDER_SPECS.get(quality, RENDER_SPECS["draft"])

        visual_hash = cls.compute_visual_hash(template_name, parameters, dimension=dimension, theme=theme)
        cached_path = cls.get_cached_video_path(video_id, visual_hash)
        canonical_raw_path = RAW_VIDEO_DIR / f"{video_id}_raw.mp4"

        if not skip_cache and cached_path.exists():
            shutil.copyfile(cached_path, canonical_raw_path)
            return str(canonical_raw_path), True

        # Render using manim CLI
        # Write temporary scene entrypoint file to ensure deterministic execution
        temp_runner = BASE_DIR / "render" / f"_run_{video_id}.py"
        temp_json = BASE_DIR / "render" / f"_node_{video_id}.json"

        with open(temp_json, "w", encoding="utf-8") as f:
            json.dump(concept_node, f, ensure_ascii=False)

        # Derive snake_name and class_name from template_name and dimension
        snake_name = "".join(["_" + c.lower() if c.isupper() else c for c in template_name]).lstrip("_")
        
        unit1_classes = {
            "BaseQuantitiesTable7": "BaseQuantitiesTable7Scene",
            "DerivedUnitsAlgebraicLadder": "DerivedUnitsAlgebraicLadderScene",
            "DimensionEquivalenceMatrix": "DimensionEquivalenceMatrixScene",
            "HomogeneityVanDerWaals": "HomogeneityVanDerWaalsScene",
            "MeasurementErrorDistribution": "MeasurementErrorDistributionScene",
            "PowerRuleCalculationTree": "PowerRuleCalculationTreeScene",
            "VernierDualScaleVisualizer": "VernierDualScaleVisualizerScene",
            "SignificantFiguresRulesBox": "SignificantFiguresRulesBoxScene"
        }

        if template_name in unit1_classes:
            import_stmt = f"from render.templates.unit_01_archetypes import {unit1_classes[template_name]} as ActiveBaseScene"
        elif dimension == "3d":
            snake_3d = f"{snake_name}_3d"
            class_3d = f"{template_name}3DScene" if not template_name.endswith("3DScene") else template_name
            mod_3d = BASE_DIR / "render" / "templates" / f"{snake_3d}.py"
            if mod_3d.exists():
                import_stmt = f"from render.templates.{snake_3d} import {class_3d} as ActiveBaseScene"
            else:
                raise ValueError(f"CRITICAL: 3D template '{template_name}' not found. Silent fallback forbidden!")
        else:
            class_name = f"{template_name}Scene" if not template_name.endswith("Scene") else template_name
            mod_file = BASE_DIR / "render" / "templates" / f"{snake_name}.py"
            if mod_file.exists():
                import_stmt = f"{import_stmt} as ActiveBaseScene"
            else:
                raise ValueError(f"CRITICAL: Template '{template_name}' module '{snake_name}.py' not found! Silent fallback forbidden.")

        code = f'''import sys
import json
from pathlib import Path
import manimpango

# Add project root to sys.path
sys.path.insert(0, {repr(str(BASE_DIR))})

# Pre-register all fonts before Manim initializes Pango
fonts_dir = Path({repr(str(BASE_DIR))}) / "assets" / "fonts"
for _f in fonts_dir.glob("*.*"):
    try:
        manimpango.register_font(str(_f.resolve()))
    except Exception:
        pass

{import_stmt}

json_path = Path({repr(str(temp_json))})
with open(json_path, "r", encoding="utf-8") as f:
    node_data = json.load(f)

class ActiveScene(ActiveBaseScene):
    def __init__(self, **kwargs):
        super().__init__(node_data=node_data, **kwargs)
'''
        with open(temp_runner, "w", encoding="utf-8") as f:
            f.write(code)

        media_dir = RAW_VIDEO_DIR / "manim_media"
        width, height = spec.get("resolution", (1920, 1080))
        fps = spec.get("fps", 30)

        cmd = [
            "manim",
            "render",
            "-r", f"{width},{height}",
            "--fps", str(fps),
            "--media_dir", str(media_dir),
            "-o", f"{video_id}_raw.mp4",
            str(temp_runner),
            "ActiveScene"
        ]

        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        except subprocess.CalledProcessError as err:
            err_msg = f"Manim render error:\nSTDOUT:\n{err.stdout}\nSTDERR:\n{err.stderr}"
            raise RuntimeError(err_msg) from err
        finally:
            if temp_runner.exists():
                temp_runner.unlink()
            if temp_json.exists():
                temp_json.unlink()

        # Locate the produced video in media_dir
        found_videos = list(media_dir.glob(f"**/{video_id}_raw.mp4"))
        if not found_videos:
            # Check for any .mp4 generated recently in media_dir
            mp4_candidates = sorted(media_dir.glob("**/*.mp4"), key=os.path.getmtime, reverse=True)
            if mp4_candidates:
                found_videos = [mp4_candidates[0]]
            else:
                raise RuntimeError(f"Manim render completed but video file was not found in {media_dir}")

        produced_path = found_videos[0]
        # Move/copy to canonical and cached paths
        shutil.copyfile(produced_path, canonical_raw_path)
        shutil.copyfile(produced_path, cached_path)

        return str(canonical_raw_path), False
