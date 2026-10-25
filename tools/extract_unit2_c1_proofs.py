import subprocess
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
BRAIN_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\brain\d9fc2045-37b2-4535-b18a-d8358d69714d\storyboards_unit2\P11-C02-T01-V01")
BRAIN_DIR.mkdir(parents=True, exist_ok=True)

video_path = BASE_DIR / "output" / "unit_02_kinematics" / "P11-C02-T01-V01_en-IN.mp4"

samples = [
    ("beat_1_intro.png", 4.0),
    ("beat_2_hero.png", 20.0),
    ("beat_3_scenarios.png", 45.0),
    ("beat_4_trap.png", 80.0),
    ("beat_5_teaser.png", 98.0)
]

for out_name, ts in samples:
    out_file = BRAIN_DIR / out_name
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(ts),
        "-i", str(video_path),
        "-vframes", "1",
        "-q:v", "2",
        str(out_file)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Extracted {out_name} at {ts}s -> {out_file.exists()}")

print("Proof extraction completed!")
