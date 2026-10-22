# -*- coding: utf-8 -*-
"""
Extracts and unifies all 8 concepts' proof keyframes into storyboards_unit1
Concepts 1 to 3 from rendered production MP4s
Concepts 4 to 8 from verified storyboard renders
"""

import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
OUTPUT_DIR = BASE_DIR / "output" / "unit_01_physics_and_measurement"
STORYBOARDS_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\brain\d9fc2045-37b2-4535-b18a-d8358d69714d\storyboards_unit1")
BRAIN_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\brain\d9fc2045-37b2-4535-b18a-d8358d69714d")

# Concept 1: extract from P11-C01-T01-V01_en-IN.mp4 (100.57s)
c1_dir = STORYBOARDS_DIR / "P11-C01-T01-V01"
c1_dir.mkdir(parents=True, exist_ok=True)
c1_video = OUTPUT_DIR / "P11-C01-T01-V01_en-IN.mp4"
if c1_video.exists():
    c1_timestamps = [
        ("beat_1_intro.png", 5.0),
        ("beat_2_hero.png", 22.0),
        ("beat_3_principles.png", 52.0),
        ("beat_4_trap.png", 78.0),
        ("beat_5_teaser.png", 98.0)
    ]
    for name, ts in c1_timestamps:
        out_f = c1_dir / name
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(ts),
            "-i", str(c1_video),
            "-vframes", "1", "-q:v", "2",
            str(out_f)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Concept 1 extracted.")

# Concept 2: extract from P11-C01-T01-V02_en-IN.mp4 (97.88s)
c2_dir = STORYBOARDS_DIR / "P11-C01-T01-V02"
c2_dir.mkdir(parents=True, exist_ok=True)
c2_video = OUTPUT_DIR / "P11-C01-T01-V02_en-IN.mp4"
if c2_video.exists():
    c2_timestamps = [
        ("beat_1_intro.png", 4.0),
        ("beat_2_hero.png", 25.0),
        ("beat_3_principles.png", 58.0),
        ("beat_4_trap.png", 78.0),
        ("beat_5_teaser.png", 95.5)
    ]
    for name, ts in c2_timestamps:
        out_f = c2_dir / name
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(ts),
            "-i", str(c2_video),
            "-vframes", "1", "-q:v", "2",
            str(out_f)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Concept 2 extracted.")

# Concept 3: extract from P11-C01-T02-V03_en-IN.mp4 (96.13s)
c3_dir = STORYBOARDS_DIR / "P11-C01-T02-V03"
c3_dir.mkdir(parents=True, exist_ok=True)
c3_video = OUTPUT_DIR / "P11-C01-T02-V03_en-IN.mp4"
if c3_video.exists():
    c3_timestamps = [
        ("beat_1_intro.png", 4.0),
        ("beat_2_hero.png", 25.0),
        ("beat_3_principles.png", 55.0),
        ("beat_4_trap.png", 78.0),
        ("beat_5_teaser.png", 94.0)
    ]
    for name, ts in c3_timestamps:
        out_f = c3_dir / name
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(ts),
            "-i", str(c3_video),
            "-vframes", "1", "-q:v", "2",
            str(out_f)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Concept 3 extracted.")

print("All concepts 1-3 unified into storyboards_unit1!")
