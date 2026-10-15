"""
Macro Chapter Movie Stitching Engine
Compiles individual micro-concept videos into a continuous 15-20 minute
Chapter Masterclass with cinematic intro bumper, seamless transitions,
and exportable chapter index (YouTube description + EdApp manifest).
"""

import argparse
import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from config import FINAL_DIR, RAW_VIDEO_DIR, OUTPUT_DIR
from tools.render_concept_video import load_concept_record, get_media_duration, render_concept_video

CURRICULUM_CSV = BASE_DIR / "queue" / "curriculum_master_full_665.csv"
MACRO_MOVIES_DIR = OUTPUT_DIR / "macro_movies"
MACRO_MOVIES_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR = BASE_DIR / "output" / "temp_stitch"
TEMP_DIR.mkdir(parents=True, exist_ok=True)


def get_chapter_concepts(parent_movie_id: str) -> List[Dict[str, Any]]:
    """Loads and sorts all concept rows for the given parent macro movie."""
    if not CURRICULUM_CSV.exists():
        raise FileNotFoundError(f"Curriculum master not found at {CURRICULUM_CSV}")

    concepts = []
    with open(CURRICULUM_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("parent_macro_movie_id") == parent_movie_id:
                concepts.append(row)

    # Sort by chapter_seq
    concepts.sort(key=lambda r: int(r.get("chapter_seq", 1)))
    return concepts


def generate_intro_bumper(
    movie_id: str,
    subject: str,
    grade: int,
    chapter_name: str,
    total_concepts: int,
    output_path: Path
) -> Path:
    """
    Generates a 5-second cinematic 1080p intro bumper using ffmpeg filter_complex.
    Clean obsidian slate with glowing subject accent text.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Accent color by subject
    color_map = {
        "Physics": "0x38bdf8",     # Cyan
        "Chemistry": "0x10b981",   # Emerald
        "Biology": "0xfb923c"      # Coral
    }
    accent_hex = color_map.get(subject, "0x38bdf8")

    title_text = f"{subject.upper()}  •  CLASS {grade}"
    chapter_title = f"{chapter_name.upper()} MASTERCLASS"
    sub_text = f"COMPLETE HIGH-YIELD CURRICULUM  |  {total_concepts} CONCEPTS"

    font_bold = "assets/fonts/segoeuib.ttf"
    font_reg = "assets/fonts/segoeui.ttf"

    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"color=c=0x0b0f19:s=1920x1080:d=4.5",
        "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=mono",
        "-filter_complex",
        (
            f"[0:v]drawtext=text='{title_text}':fontfile={font_bold}:fontcolor={accent_hex}:fontsize=34:x=(w-text_w)/2:y=380,"
            f"drawtext=text='{chapter_title}':fontfile={font_bold}:fontcolor=white:fontsize=64:x=(w-text_w)/2:y=450,"
            f"drawtext=text='{sub_text}':fontfile={font_reg}:fontcolor=0x94a3b8:fontsize=24:x=(w-text_w)/2:y=560,"
            f"drawbox=y=620:color={accent_hex}:height=3:width=600:x=(w-600)/2:t=fill,"
            f"fade=t=in:st=0:d=0.8,fade=t=out:st=3.8:d=0.7[v];"
            f"[1:a]atrim=0:4.5,afade=t=in:st=0:d=0.5,afade=t=out:st=3.8:d=0.7[a]"
        ),
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
        str(output_path)
    ]

    try:
        subprocess.run(cmd, cwd=str(BASE_DIR), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    except subprocess.CalledProcessError as e:
        # Fallback if drawtext filters have font resolution issues
        cmd_simple = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "color=c=0x0b0f19:s=1920x1080:d=4.5",
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
            "-shortest",
            str(output_path)
        ]
        subprocess.run(cmd_simple, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    return output_path


def format_timestamp(seconds: float) -> str:
    """Formats seconds into MM:SS or HH:MM:SS."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"


def stitch_chapter_movie(
    parent_movie_id: str = "P11-C02-MOVIE",
    lang: str = "en-IN",
    render_missing: bool = False,
    quality: str = "draft"
) -> Dict[str, Any]:
    """
    Stitches all sequential micro-concept videos of a chapter into a Macro Movie.
    Exports the MP4 video, YouTube chapter timestamps, and EdApp manifest.
    """
    t_start = time.time()
    concepts = get_chapter_concepts(parent_movie_id)
    if not concepts:
        raise ValueError(f"No concepts found for movie ID: {parent_movie_id}")

    sample = concepts[0]
    subject = sample.get("subject", "Physics")
    grade = int(sample.get("grade", 11))
    chapter_name = sample.get("chapter_name", "Chapter")

    print("=" * 80)
    print(f"🎬 MACRO CHAPTER MOVIE COMPILER: {parent_movie_id}")
    print(f"   Subject: {subject} | Grade {grade} | Chapter: '{chapter_name}'")
    print(f"   Total Concepts to Stitch: {len(concepts)}")
    print("=" * 80)

    # 1. Verify existence of constituent videos
    final_videos_dir = BASE_DIR / "output" / "final_videos"
    video_files = []
    missing_concepts = []

    for c in concepts:
        cid = c["canonical_id"]
        # Standard final video path: {cid}_{lang}.mp4
        expected_path = final_videos_dir / f"{cid}_{lang}.mp4"
        if not expected_path.exists():
            # Check without lang suffix
            alt_path = final_videos_dir / f"{cid}.mp4"
            if alt_path.exists():
                expected_path = alt_path
            else:
                missing_concepts.append(c)
                continue
        video_files.append((c, expected_path))

    if missing_concepts:
        print(f"\n⚠️ Notice: {len(missing_concepts)} constituent videos not yet rendered:")
        for mc in missing_concepts:
            print(f"   - {mc['canonical_id']}: {mc['concept_title']}")

        if render_missing:
            print(f"\n⚙️ Auto-Rendering {len(missing_concepts)} missing concepts now...")
            for mc in missing_concepts:
                render_concept_video(
                    canonical_id=mc["canonical_id"],
                    quality=quality,
                    lang=lang,
                    dimension="2d",
                    skip_cache=False
                )
                expected_path = final_videos_dir / f"{mc['canonical_id']}_{lang}.mp4"
                video_files.append((mc, expected_path))
            # Re-sort after rendering
            video_files.sort(key=lambda item: int(item[0].get("chapter_seq", 1)))
        else:
            print("   (Proceeding with available concepts. Use --render-missing to compile all.)")

    if not video_files:
        raise RuntimeError("No rendered videos available to stitch.")

    # 2. Generate Chapter Intro Bumper
    bumper_path = TEMP_DIR / f"{parent_movie_id}_intro_bumper.mp4"
    print(f"\n🎨 Generating Cinematic Chapter Intro Bumper...")
    generate_intro_bumper(
        movie_id=parent_movie_id,
        subject=subject,
        grade=grade,
        chapter_name=chapter_name,
        total_concepts=len(concepts),
        output_path=bumper_path
    )
    print(f"   Intro Bumper Created: {bumper_path.name}")

    # 3. Build Concat Protocol List & Chapter Index
    concat_list_path = TEMP_DIR / f"{parent_movie_id}_concat.txt"
    chapter_index = []
    current_time = 0.0

    # Add Bumper
    bumper_dur = get_media_duration(bumper_path)
    chapter_index.append({
        "timestamp": format_timestamp(current_time),
        "seconds": round(current_time, 2),
        "title": f"Chapter Intro: {chapter_name}",
        "canonical_id": "INTRO"
    })
    current_time += bumper_dur

    lines_to_concat = [f"file '{bumper_path.as_posix()}'"]

    # Normalize audio/video to exact specs before concat (1920x1080 30fps, 48kHz aac)
    normalized_videos = []
    print(f"\n🔄 Normalizing {len(video_files)} concepts for lossless concatenation...")
    for idx, (c, v_path) in enumerate(video_files):
        cid = c["canonical_id"]
        ch_num = c.get("chapter_no", 2)
        top_num = c.get("topic_no", 1)
        vid_num = c.get("video_no", 1)
        s_code = f"S.{ch_num}.{top_num}.{vid_num}"
        c_title = c.get("concept_title", "Concept")

        dur = get_media_duration(v_path)
        chapter_index.append({
            "timestamp": format_timestamp(current_time),
            "seconds": round(current_time, 2),
            "title": f"{s_code} - {c_title}",
            "canonical_id": cid,
            "duration": round(dur, 2)
        })
        current_time += dur

        # Normalize video segment
        norm_segment = TEMP_DIR / f"norm_{cid}.mp4"
        norm_cmd = [
            "ffmpeg", "-y", "-i", str(v_path),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            "-vf", "scale=1920:1080",
            "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "1",
            str(norm_segment)
        ]
        subprocess.run(norm_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        lines_to_concat.append(f"file '{norm_segment.as_posix()}'")
        normalized_videos.append(norm_segment)

    with open(concat_list_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines_to_concat))

    # 4. Lossless Fast Concat
    macro_movie_output = MACRO_MOVIES_DIR / f"{parent_movie_id}.mp4"
    print(f"\n📦 Stitching Macro Movie with ffmpeg concat demuxer...")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_path),
        "-c", "copy",
        str(macro_movie_output)
    ]
    subprocess.run(concat_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    final_dur = get_media_duration(macro_movie_output)
    file_size_mb = macro_movie_output.stat().st_size / (1024 * 1024)

    # 5. Export Chapter Markers & YouTube Description
    yt_chapters_path = MACRO_MOVIES_DIR / f"{parent_movie_id}_youtube_chapters.txt"
    with open(yt_chapters_path, "w", encoding="utf-8") as f:
        f.write(f"NEET UG — {subject.upper()} CLASS {grade}\n")
        f.write(f"Chapter: {chapter_name} Complete Masterclass\n\n")
        f.write("⏱️ CHAPTER TIMESTAMPS:\n")
        for ch in chapter_index:
            f.write(f"{ch['timestamp']} {ch['title']}\n")

    # 6. Export Chapter Manifest for EdApp
    manifest_path = MACRO_MOVIES_DIR / f"{parent_movie_id}_manifest.json"
    manifest_data = {
        "chapter_id": parent_movie_id,
        "subject": subject,
        "grade": grade,
        "chapter_name": chapter_name,
        "total_concepts": len(concepts),
        "total_stitched_concepts": len(video_files),
        "macro_movie_duration_seconds": round(final_dur, 2),
        "macro_movie_path": str(macro_movie_output),
        "chapters": chapter_index
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    elapsed = time.time() - t_start
    print("=" * 80)
    print(f"✨ COMPLETE SUCCESS: Macro Chapter Movie Assembled!")
    print(f"   Output File     : {macro_movie_output.name}")
    print(f"   Path            : {macro_movie_output}")
    print(f"   Total Duration  : {format_timestamp(final_dur)} ({final_dur:.1f}s)")
    print(f"   File Size       : {file_size_mb:.2f} MB")
    print(f"   YouTube Chapter : {yt_chapters_path.name}")
    print(f"   EdApp Manifest  : {manifest_path.name}")
    print(f"   Compilation Time: {elapsed:.1f}s")
    print("=" * 80)

    return manifest_data


def main():
    parser = argparse.ArgumentParser(description="Macro Chapter Movie Stitcher")
    parser.add_argument("--movie_id", type=str, default="P11-C02-MOVIE", help="Parent macro movie ID")
    parser.add_argument("--lang", type=str, default="en-IN", help="Audio language suffix")
    parser.add_argument("--render-missing", action="store_true", help="Auto-render missing micro-videos before stitching")
    parser.add_argument("--quality", type=str, default="draft", help="Manim render quality for missing concepts")
    args = parser.parse_args()

    stitch_chapter_movie(
        parent_movie_id=args.movie_id,
        lang=args.lang,
        render_missing=args.render_missing,
        quality=args.quality
    )


if __name__ == "__main__":
    main()
