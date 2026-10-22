# -*- coding: utf-8 -*-
"""
High-Performance Visual Storyboard Frame Generator for Unit 1 Concepts (Concepts 4 to 8)
Uses Manim's -a (render all scenes) and -s (save frame) in a single unified invocation per concept.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

import os
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STORYBOARDS_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\brain\d9fc2045-37b2-4535-b18a-d8358d69714d\storyboards_unit1")
STORYBOARDS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR = BASE_DIR / "output" / "storyboard_temp"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

CONCEPTS = [
    {
        "id": "P11-C01-T02-V04",
        "title": "Principle of Homogeneity of Dimensions",
        "scene_class": "HomogeneityVanDerWaalsScene",
        "seq": 4,
        "total": 8,
        "next_id": "P11-C01-T03-V05",
        "next_title": "Classification of Errors & Mean Absolute Error"
    },
    {
        "id": "P11-C01-T03-V05",
        "title": "Classification of Errors & Mean Absolute Error",
        "scene_class": "MeasurementErrorDistributionScene",
        "seq": 5,
        "total": 8,
        "next_id": "P11-C01-T03-V06",
        "next_title": "Combination & Propagation of Errors (Power Rule)"
    },
    {
        "id": "P11-C01-T03-V06",
        "title": "Combination & Propagation of Errors (Power Rule)",
        "scene_class": "PowerRuleCalculationTreeScene",
        "seq": 6,
        "total": 8,
        "next_id": "P11-C01-T04-V07",
        "next_title": "Measuring Instruments: Vernier Callipers & Screw Gauge"
    },
    {
        "id": "P11-C01-T04-V07",
        "title": "Measuring Instruments: Vernier Callipers & Screw Gauge",
        "scene_class": "VernierDualScaleVisualizerScene",
        "seq": 7,
        "total": 8,
        "next_id": "P11-C01-T04-V08",
        "next_title": "Significant Figures & Arithmetic Rounding Rules"
    },
    {
        "id": "P11-C01-T04-V08",
        "title": "Significant Figures & Arithmetic Rounding Rules",
        "scene_class": "SignificantFiguresRulesBoxScene",
        "seq": 8,
        "total": 8,
        "next_id": "",
        "next_title": "Chapter 1 Complete • Ready for Unit 2: Kinematics"
    }
]

def generate_storyboard_for_concept(concept: dict):
    cid = concept["id"]
    cls_name = concept["scene_class"]
    print(f"\n=======================================================")
    print(f"🎨 Generating Storyboard Frames for Concept {concept['seq']}/8: {cid}")
    print(f"   Title: {concept['title']}")
    print(f"   Archetype: {cls_name}")
    print(f"=======================================================")

    out_concept_dir = STORYBOARDS_DIR / cid
    out_concept_dir.mkdir(parents=True, exist_ok=True)

    expected = ["beat_1_intro.png", "beat_2_hero.png", "beat_3_principles.png", "beat_4_trap.png", "beat_5_teaser.png"]
    if all((out_concept_dir / f).exists() for f in expected):
        print(f"   [+] All 5 storyboard frames already exist for {cid}. Skipping.")
        return True

    concept_temp = TEMP_DIR / cid
    concept_temp.mkdir(parents=True, exist_ok=True)

    runner_py = concept_temp / f"runner_{cid}.py"
    code = f'''# -*- coding: utf-8 -*-
import sys
from pathlib import Path
BASE_DIR = Path(r"{str(BASE_DIR)}")
sys.path.insert(0, str(BASE_DIR))

from manim import *
import manimpango
from config import FONTS_DIR
import render.templates.unit_01_archetypes as u1

for font_file in FONTS_DIR.glob("*.[tT][tT][fF]"):
    manimpango.register_font(str(font_file.resolve()))

NODE_DATA = {{
    "videoId": "{cid}",
    "canonical_id": "{cid}",
    "serialTitle": "{concept['title']}",
    "subject": "Physics",
    "grade": 11,
    "chapter_no": 1,
    "topic_no": 2,
    "video_no": {concept['seq']},
    "seq_chapter": {concept['seq']},
    "total_chapter_videos": {concept['total']},
    "next_video_id": "{concept['next_id']}",
    "next_video_title": "{concept['next_title']}",
    "parameters": {{}}
}}

class Beat1(u1.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_1())

class Beat2(u1.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_2())

class Beat3(u1.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_3())

class Beat4(u1.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_beat_4())

class Beat5(u1.{cls_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.add(self.build_release_teaser())
'''
    runner_py.write_text(code, encoding="utf-8")

    media_dir = concept_temp / "media_batch"
    cmd = [
        "manim", "render",
        "-a", "-s",
        "-r", "1920,1080",
        "--media_dir", str(media_dir),
        str(runner_py)
    ]
    print(f"   [+] Executing batch single-process render of all 5 beats...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"   [!] Error during batch render:\n{res.stderr[-400:]}")
        return False

    beat_mapping = {
        "Beat1": "beat_1_intro.png",
        "Beat2": "beat_2_hero.png",
        "Beat3": "beat_3_principles.png",
        "Beat4": "beat_4_trap.png",
        "Beat5": "beat_5_teaser.png"
    }

    found_images = list(media_dir.rglob("*.png"))
    for f in found_images:
        for prefix, target_name in beat_mapping.items():
            if f.name.startswith(prefix):
                dst = out_concept_dir / target_name
                shutil.copy2(f, dst)
                print(f"       ✅ Saved: {target_name} ({dst.stat().st_size // 1024} KB)")

    return True

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    for c in CONCEPTS:
        if target and c["id"] != target:
            continue
        generate_storyboard_for_concept(c)
    print("\n🎉 STORYBOARDS EXECUTION COMPLETE!")

if __name__ == "__main__":
    main()
