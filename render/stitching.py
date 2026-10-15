"""
FFmpeg Multi-Track Muxer and Assembly Subsystem
Derived from MASTER_BLUEPRINT.md v1.1 Section 2, 3, 8, 13
"""
import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List

from config import FINAL_DIR, LOCALES

class FFmpegMuxer:
    @staticmethod
    def sanitize_title(title: str) -> str:
        return re.sub(r"[^\w\-]", "_", title).strip("_")

    @classmethod
    def get_canonical_export_path(cls, video_id: str, title: str) -> Path:
        """
        Export: /renders/[Subject][Grade]/C[Chapter]/[VideoId]_[SanitizedTitle].mp4
        In repository output: output/final/[VideoId]_[SanitizedTitle].mp4
        """
        clean_title = cls.sanitize_title(title)
        filename = f"{video_id}_{clean_title}.mp4"
        return FINAL_DIR / filename

    @classmethod
    def mux_multitrack_mp4(
        cls,
        video_path: Path,
        audio_tracks: Dict[str, Path],
        subtitle_tracks: Dict[str, Path],
        output_path: Path
    ) -> Path:
        """
        Muxes 1 video + 3 audio tracks + 3 soft mov_text subtitle tracks into a single MP4 container.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)

        ordered_langs = ["en", "hi", "ta"]
        cmd = ["ffmpeg", "-y", "-i", str(video_path)]

        # Add audio inputs
        for lang in ordered_langs:
            if lang in audio_tracks and Path(audio_tracks[lang]).exists():
                cmd.extend(["-i", str(audio_tracks[lang])])
            else:
                raise FileNotFoundError(f"Missing required audio track for locale '{lang}'")

        # Add subtitle inputs
        for lang in ordered_langs:
            if lang in subtitle_tracks and Path(subtitle_tracks[lang]).exists():
                cmd.extend(["-i", str(subtitle_tracks[lang])])
            else:
                raise FileNotFoundError(f"Missing required subtitle track for locale '{lang}'")

        # Mapping: 0:v (video), 1..3:a (audio), 4..6:s (subtitles)
        cmd.extend(["-map", "0:v:0"])
        for i in range(1, 4):
            cmd.extend(["-map", f"{i}:a:0"])
        for i in range(4, 7):
            cmd.extend(["-map", f"{i}:s:0"])

        # Codecs
        cmd.extend([
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-c:s", "mov_text"
        ])

        # Metadata for audio streams
        for idx, lang in enumerate(ordered_langs):
            meta = LOCALES.get(lang, {})
            lang_code = meta.get("lang_code", lang)
            lang_name = meta.get("name", lang.upper())
            cmd.extend([
                f"-metadata:s:a:{idx}", f"language={lang_code}",
                f"-metadata:s:a:{idx}", f"title={lang_name} Audio"
            ])

        # Metadata for subtitle streams
        for idx, lang in enumerate(ordered_langs):
            meta = LOCALES.get(lang, {})
            lang_code = meta.get("lang_code", lang)
            lang_name = meta.get("name", lang.upper())
            cmd.extend([
                f"-metadata:s:s:{idx}", f"language={lang_code}",
                f"-metadata:s:s:{idx}", f"title={lang_name} Subtitles"
            ])

        cmd.append(str(output_path))

        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        except subprocess.CalledProcessError as err:
            raise RuntimeError(f"FFmpeg muxing failed: {err.stderr}")

        return output_path

    @classmethod
    def probe_media(cls, file_path: Path) -> Dict[str, Any]:
        """Runs ffprobe on final container to inspect streams and metadata"""
        cmd = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            str(file_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return json.loads(res.stdout) if "json" in globals() else eval(res.stdout.replace("true", "True").replace("false", "False").replace("null", "None"))
