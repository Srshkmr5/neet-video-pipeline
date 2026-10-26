"""
Batch Multilingual Production Engine for Unit 2: Kinematics
Executes sequential production, AES-128 HLS packaging, and storyboard proof extraction
for all 14 concepts across English, Hindi, and Tamil.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
sys.path.insert(0, str(BASE_DIR))

from tools.render_multilingual_unit2 import render_concept_multilingual_unit2
from tools.secure_media_packager import package_all_videos

UNIT2_CONCEPTS = [
    # Gate 1: Straight Line Motion (Already Done)
    ("P11-C02-T01-V01", "Position-Time Graphs"),
    ("P11-C02-T03-V08", "Velocity-Time Graphs & Displacement"),
    # Gate 2: Vectors & Relative Motion (Already Done)
    ("P11-C02-T02-V01", "Resolution of Vectors"),
    ("P11-C02-T03-V09", "Relative Velocity & River-Boat Vectors"),
    # Gate 3: Projectile Motion (7 concepts)
    ("P11-C02-T03-V01", "Time of Flight"),
    ("P11-C02-T03-V02", "The Max Height Arc"),
    ("P11-C02-T03-V03", "Horizontal Range and Complementary Angles"),
    ("P11-C02-T03-V04", "Equation of Trajectory"),
    ("P11-C02-T04-V10", "Horizontal Projection from a Height"),
    ("P11-C02-T04-V11", "Projectile on an Inclined Plane"),
    ("P11-C02-T04-V12", "Radius of Curvature at Apex"),
    # Gate 4: Circular Motion (3 concepts)
    ("P11-C02-T04-V01", "Centripetal Acceleration"),
    ("P11-C02-T05-V13", "Angular Velocity & Linear Speed Relation"),
    ("P11-C02-T05-V14", "Non-Uniform Circular Motion Acceleration"),
]

def extract_proofs_for_concept(cid: str):
    brain_dir = Path(r"C:\Users\DELL\.gemini\antigravity\brain\d9fc2045-37b2-4535-b18a-d8358d69714d\storyboards_unit2") / cid
    brain_dir.mkdir(parents=True, exist_ok=True)
    video_path = BASE_DIR / "output" / "unit_02_kinematics" / f"{cid}_en-IN.mp4"
    if not video_path.exists():
        return

    # Probe duration
    import json
    cmd_p = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(video_path)]
    r = subprocess.run(cmd_p, capture_output=True, text=True)
    dur = float(json.loads(r.stdout)["format"]["duration"])

    # Sample 5 beats evenly
    samples = [
        ("beat_1_intro.png", min(4.0, dur * 0.08)),
        ("beat_2_hero.png", dur * 0.25),
        ("beat_3_scenarios.png", dur * 0.55),
        ("beat_4_trap.png", dur * 0.82),
        ("beat_5_teaser.png", dur - 1.5)
    ]

    for name, ts in samples:
        out_f = brain_dir / name
        if not out_f.exists() or out_f.stat().st_size == 0:
            cmd = ["ffmpeg", "-y", "-ss", f"{ts:.2f}", "-i", str(video_path), "-vframes", "1", "-q:v", "2", str(out_f)]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    total = len(UNIT2_CONCEPTS)
    print("=" * 80)
    print(f"🎬 MASTER BATCH PRODUCTION PIPELINE: UNIT 2 KINEMATICS ({total} CONCEPTS)")
    print("=" * 80)

    for idx, (cid, title) in enumerate(UNIT2_CONCEPTS, 1):
        print(f"\n[{idx}/{total}] >>> INITIATING PRODUCTION: {cid} ({title})")
        # Step 1: Render Multilingual Videos
        render_concept_multilingual_unit2(cid, ["en-IN", "hi-IN", "ta-IN"])

        # Step 2: Extract Storyboard Proofs
        extract_proofs_for_concept(cid)

        # Step 3: Package AES-128 HLS Streams
        u2_dir = BASE_DIR / "output" / "unit_02_kinematics"
        package_all_videos(force=False, input_dirs=[u2_dir])
        print(f"[{idx}/{total}] ✅ COMPLETED & PACKAGED: {cid}")

    print("\n" + "=" * 80)
    print("🎉 ALL 14 CONCEPTS OF UNIT 2: KINEMATICS SUCCESSFULLY PRODUCED AND PACKAGED!")
    print("=" * 80)

if __name__ == "__main__":
    main()
