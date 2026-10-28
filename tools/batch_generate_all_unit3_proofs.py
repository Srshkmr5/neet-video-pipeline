"""
Batch Visual Storyboard Frame Generator for ALL 11 Concepts in Unit 3 (Laws of Motion).
Produces high-resolution 1080p still proof frames (PNGs for Beats 1-5).
Zero full video rendering.
Enforces the Visual Confirmation Protocol before any video render can be initiated.
"""

import sys
from pathlib import Path
BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
sys.path.insert(0, str(BASE_DIR))

import shutil
import subprocess
import csv
import time

BRAIN_DIR = BASE_DIR / "brain" / "d9fc2045-37b2-4535-b18a-d8358d69714d" / "storyboards_unit3"
BRAIN_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR_STATIC = BASE_DIR / "output" / "storyboards_unit3"
OUT_DIR_STATIC.mkdir(parents=True, exist_ok=True)
TEMP_DIR = BASE_DIR / "output" / "storyboard_temp_u3"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

from tools.render_multilingual_unit3 import ARCHETYPE_SCENE_MAP, load_concept_row

CONCEPTS = [
    "P11-C03-T01-V01",
    "P11-C03-T01-V02",
    "P11-C03-T01-V03",
    "P11-C03-T02-V04",
    "P11-C03-T02-V05",
    "P11-C03-T02-V06",
    "P11-C03-T03-V07",
    "P11-C03-T03-V08",
    "P11-C03-T03-V09",
    "P11-C03-T04-V10",
    "P11-C03-T04-V11"
]

def render_concept_proofs(cid: str, force: bool = False):
    concept = load_concept_row(cid)
    cls_name = ARCHETYPE_SCENE_MAP[cid]
    out_dir = BRAIN_DIR / cid
    out_dir.mkdir(parents=True, exist_ok=True)
    out_dir_static = OUT_DIR_STATIC / cid
    out_dir_static.mkdir(parents=True, exist_ok=True)

    expected = ["beat_1_intro.png", "beat_2_hero.png", "beat_3_scenarios.png", "beat_4_trap.png", "beat_5_teaser.png"]
    if not force and all((out_dir / f).exists() and (out_dir / f).stat().st_size > 5000 for f in expected):
        print(f"[{cid}] All 5 proof frames already exist. Skipping.")
        return True

    c_temp = TEMP_DIR / cid
    c_temp.mkdir(parents=True, exist_ok=True)

    runner_py = c_temp / f"runner_{cid}.py"
    code = f'''import sys
from pathlib import Path
BASE_DIR = Path({repr(str(BASE_DIR))})
sys.path.insert(0, str(BASE_DIR))

from manim import *
import manimpango
from config import FONTS_DIR
import render.templates.unit_03_archetypes as u3

for font_file in FONTS_DIR.glob("*.[tT][tT][fF]"):
    manimpango.register_font(str(font_file.resolve()))

NODE_DATA = {{
    "videoId": "{cid}_proof",
    "canonical_id": "{cid}",
    "serialTitle": "{concept['concept_title']}",
    "subject": "Physics",
    "grade": 11,
    "chapter_no": 3,
    "topic_no": int({concept.get('topic_no', 1)}),
    "video_no": int({concept.get('video_no', 1)}),
    "seq_chapter": int({concept.get('chapter_seq', 1)}),
    "total_chapter_videos": 11,
    "next_video_id": "{concept.get('next_video_id', '')}",
    "next_video_title": "{concept.get('next_video_title', '')}"
}}

class Beat1(u3.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_1())

class Beat2(u3.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_2())

class Beat3(u3.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_3())

class Beat4(u3.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_4())

class Beat5(u3.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_5())
'''
    runner_py.write_text(code, encoding="utf-8")

    media_dir = c_temp / "media"
    cmd = [
        "manim", "render",
        "-a", "-s",
        "-r", "1920,1080",
        "--media_dir", str(media_dir),
        str(runner_py)
    ]
    t0 = time.time()
    print(f"\n[{cid}] Rendering proofs for {concept['concept_title']} ({cls_name})...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[{cid}] ERROR:\n", res.stderr[-600:])
        return False

    name_map = {
        "Beat1": "beat_1_intro.png",
        "Beat2": "beat_2_hero.png",
        "Beat3": "beat_3_scenarios.png",
        "Beat4": "beat_4_trap.png",
        "Beat5": "beat_5_teaser.png"
    }

    found = 0
    for png in media_dir.rglob("*.png"):
        for b_cls, out_name in name_map.items():
            if b_cls in png.name:
                dst = out_dir / out_name
                shutil.copy2(png, dst)
                dst_static = out_dir_static / out_name
                shutil.copy2(png, dst_static)
                print(f"   [+] {out_name} -> {dst.name} & static ({dst.stat().st_size // 1024} KB)")
                found += 1
                break

    dt = time.time() - t0
    print(f"[{cid}] Finished in {dt:.1f}s: {found}/5 frames captured.")
    return found == 5

def main():
    import argparse
    from concurrent.futures import ThreadPoolExecutor

    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Force re-rendering of all proof frames")
    parser.add_argument("--concept", type=str, default=None, help="Target specific concept ID e.g. P11-C03-T01-V03 or comma-separated list")
    parser.add_argument("--workers", type=int, default=4, help="Number of concurrent rendering workers (default 4)")
    args = parser.parse_args()

    print("=" * 80)
    print("📸 MASTER STORYBOARD PROOF GENERATION ENGINE (UNIT 3: LAWS OF MOTION)")
    print("   Visual Confirmation Protocol (5 Still Frames per Concept, 55 Frames Total)")
    print("=" * 80)

    if args.concept:
        target_concepts = [c.strip() for c in args.concept.split(",") if c.strip()]
    else:
        target_concepts = CONCEPTS

    total_start = time.time()
    results = {}

    def _worker(cid):
        print(f">>> STARTING: {cid}")
        ok = render_concept_proofs(cid, force=args.force)
        return cid, ok

    if len(target_concepts) == 1:
        cid, ok = _worker(target_concepts[0])
        results[cid] = ok
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for cid, ok in pool.map(_worker, target_concepts):
                results[cid] = ok

    total_time = time.time() - total_start
    print("\n" + "=" * 80)
    print(f"🏁 ALL CONCEPTS COMPLETED IN {total_time:.1f}s")
    for cid, ok in results.items():
        status = "✅ PASS (5/5)" if ok else "❌ FAIL"
        print(f"   {cid}: {status}")
    print("=" * 80)

if __name__ == "__main__":
    main()
