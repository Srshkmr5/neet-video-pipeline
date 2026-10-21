"""
Secure Media Packager for NEET EdApp
Transcodes raw concept videos into AES-128 encrypted HLS streams.
Derived from Master Blueprint Security Layer v2.0
"""

import os
import sys
import secrets
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# Set utf-8 stdout wrapper for Windows terminals
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


BASE_DIR = Path(__file__).resolve().parent.parent
FINAL_VIDEOS_DIR = BASE_DIR / "output" / "final_videos"
SECURE_STREAMS_DIR = BASE_DIR / "output" / "secure_streams"
SERVER_KEYS_DIR = BASE_DIR / "server" / "security" / "keys"

def ensure_directories():
    SECURE_STREAMS_DIR.mkdir(parents=True, exist_ok=True)
    SERVER_KEYS_DIR.mkdir(parents=True, exist_ok=True)

def package_video_aes128(video_path: Path, force: bool = False) -> bool:
    """
    Encrypts and segments a single MP4 video into AES-128 HLS package.
    """
    video_stem = video_path.stem  # e.g., P11-C02-T03-V02_en-IN
    target_dir = SECURE_STREAMS_DIR / video_stem
    master_playlist = target_dir / "master.m3u8"

    if master_playlist.exists() and not force:
        # Already packaged
        return True

    target_dir.mkdir(parents=True, exist_ok=True)

    # 1. Generate or load 16-byte cryptographic key
    key_file = SERVER_KEYS_DIR / f"{video_stem}.key"
    if not key_file.exists():
        key_bytes = secrets.token_bytes(16)
        with open(key_file, "wb") as kf:
            kf.write(key_bytes)

    # 2. Generate key_info file for FFmpeg
    # Format:
    # Line 1: URI in m3u8 playlist where client requests key
    # Line 2: Path to key file for ffmpeg to read during encryption
    key_info_file = target_dir / "key_info.txt"
    key_uri = f"/api/stream/key/{video_stem}"
    key_abs_path = str(key_file.resolve()).replace("\\", "/")

    with open(key_info_file, "w", encoding="utf-8") as kif:
        kif.write(f"{key_uri}\n")
        kif.write(f"{key_abs_path}\n")

    # 3. Execute FFmpeg stream packaging (stream copy, ultra fast)
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path.resolve()),
        "-c", "copy",
        "-hls_time", "4",
        "-hls_playlist_type", "vod",
        "-hls_key_info_file", str(key_info_file.resolve()),
        "-hls_segment_filename", str((target_dir / "segment_%03d.ts").resolve()),
        str(master_playlist.resolve())
    ]

    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        # Clean up temporary key_info file from public output directory
        if key_info_file.exists():
            key_info_file.unlink()
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to package {video_stem}: {e.stderr.decode('utf-8', errors='ignore')[:300]}")
        return False

def package_all_videos(force: bool = False) -> Dict[str, int]:
    ensure_directories()
    mp4_files = list(FINAL_VIDEOS_DIR.glob("*.mp4"))
    
    total = len(mp4_files)
    succeeded = 0
    skipped = 0
    failed = 0

    print(f"🔒 Initiating AES-128 HLS Secure Packaging for {total} video(s)...")

    for idx, video_path in enumerate(mp4_files, 1):
        target_dir = SECURE_STREAMS_DIR / video_path.stem
        if (target_dir / "master.m3u8").exists() and not force:
            skipped += 1
            continue

        ok = package_video_aes128(video_path, force=force)
        if ok:
            succeeded += 1
            print(f"  [{idx}/{total}] ✅ Encrypted & Segmented: {video_path.name}")
        else:
            failed += 1

    print(f"\n✨ Secure Packaging Complete! Encrypted: {succeeded}, Already Cached: {skipped}, Failed: {failed}")
    return {"total": total, "encrypted": succeeded, "skipped": skipped, "failed": failed}

if __name__ == "__main__":
    package_all_videos(force=False)
