"""
Lossless Remux & AES-128 Repackager for Unit 2: Kinematics
Pads audio with digital silence up to the exact millisecond of the raw video,
muxes soft subtitles, and rebuilds encrypted HLS streams.
Runs in ~40 seconds total across all 42 videos without re-rendering Manim.
"""

import os
import sys
import time
import json
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
from tools.secure_media_packager import package_video_aes128

BEAT_DIR = BASE_DIR / "output" / "beat_audio"
UNIT2_DIR = BASE_DIR / "output" / "unit_02_kinematics"
FINAL_DIR = BASE_DIR / "output" / "final_videos"
UNIT2_DIR.mkdir(parents=True, exist_ok=True)
FINAL_DIR.mkdir(parents=True, exist_ok=True)

def get_video_duration(video_path: Path) -> float:
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", str(video_path)]
    info = json.loads(subprocess.check_output(cmd))
    for s in info.get("streams", []):
        if s.get("codec_type") == "video" and "duration" in s:
            return float(s["duration"])
    fmt_cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(video_path)]
    info = json.loads(subprocess.check_output(fmt_cmd))
    return float(info["format"]["duration"])

def main():
    dirs = sorted([d for d in BEAT_DIR.iterdir() if d.is_dir() and "P11-C02" in d.name])
    total = len(dirs)
    print(f"🎬 Starting lossless remux & HLS packaging for {total} Unit 2 video packages...")
    t0_start = time.time()

    success_count = 0
    for idx, d in enumerate(dirs, 1):
        stem = d.name # e.g. P11-C02-T01-V01_en-IN
        raw_vids = list(d.glob("manim_media/videos/*/1080p30/*_synced_raw.mp4"))
        master_wavs = list(d.glob("*_synced_master.wav"))
        srts = list(d.glob("*.srt"))

        if not raw_vids or not master_wavs:
            print(f"⚠️ [{idx:02d}/{total:02d}] Missing raw or wav for {stem}, skipping")
            continue

        raw_vid = raw_vids[0]
        master_wav = master_wavs[0]
        srt_file = srts[0] if srts else None

        # 1. Determine exact duration
        v_dur = get_video_duration(raw_vid)

        # 2. Build mux command
        out_mp4 = UNIT2_DIR / f"{stem}.mp4"
        temp_mp4 = UNIT2_DIR / f"temp_{stem}.mp4"

        cmd_mux = [
            "ffmpeg", "-y",
            "-i", str(raw_vid),
            "-i", str(master_wav),
        ]
        
        if srt_file and srt_file.exists():
            cmd_mux.extend(["-i", str(srt_file)])
            cmd_mux.extend([
                "-filter_complex", "[1:a]apad[aout]",
                "-map", "0:v:0",
                "-map", "[aout]",
                "-map", "2:s:0",
                "-c:v", "copy",
                "-c:a", "aac", "-b:a", "192k",
                "-c:s", "mov_text",
                "-t", f"{v_dur:.3f}",
                str(temp_mp4)
            ])
        else:
            cmd_mux.extend([
                "-filter_complex", "[1:a]apad[aout]",
                "-map", "0:v:0",
                "-map", "[aout]",
                "-c:v", "copy",
                "-c:a", "aac", "-b:a", "192k",
                "-t", f"{v_dur:.3f}",
                str(temp_mp4)
            ])

        res = subprocess.run(cmd_mux, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            print(f"❌ Failed mux for {stem}: {res.stderr.decode('utf-8', errors='ignore')[:150]}")
            if temp_mp4.exists():
                temp_mp4.unlink()
            continue

        if temp_mp4.exists():
            try:
                if out_mp4.exists():
                    out_mp4.unlink()
                temp_mp4.replace(out_mp4)
            except Exception as e:
                print(f"  Note on out_mp4 replace: {e}")
            try:
                shutil.copy2(out_mp4, FINAL_DIR / f"{stem}.mp4")
            except Exception as e:
                print(f"  Note on copy to final_videos: {e}")

        # 3. Repackage AES-128 HLS
        ok = package_video_aes128(out_mp4, force=True)
        if ok:
            success_count += 1
            print(f"[{idx:02d}/{total:02d}] ✅ Muxed ({v_dur:.1f}s) & Encrypted HLS: {stem}")
        else:
            print(f"[{idx:02d}/{total:02d}] ⚠️ Muxed but HLS packager error: {stem}")

    elapsed = round(time.time() - t0_start, 1)
    print(f"\n🎉 Successfully processed {success_count}/{total} videos in {elapsed}s!")

if __name__ == "__main__":
    main()
