"""
TTS & Subtitle Engine using edge-tts and FFmpeg loudness normalization
Derived from MASTER_BLUEPRINT.md v1.1 Section 6, 7, 8
"""
import asyncio
import os
import subprocess
import json
from pathlib import Path
from typing import Dict, Any, Tuple
import edge_tts

from config import (
    LOCALES,
    AUDIO_TARGET_LUFS,
    RAW_AUDIO_DIR,
    WORDS_PER_MINUTE
)
from llm.script_engine import ScriptEngine

class TTSEngine:
    @staticmethod
    def get_audio_duration(file_path: Path) -> float:
        """Get exact duration in seconds using ffprobe"""
        cmd = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(file_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())

    @staticmethod
    def normalize_loudness(input_audio: Path, output_audio: Path, target_lufs: float = AUDIO_TARGET_LUFS) -> None:
        """
        Normalize audio loudness to target LUFS (-14 LUFS) using FFmpeg loudnorm filter.
        """
        cmd = [
            "ffmpeg",
            "-y",
            "-i", str(input_audio),
            "-af", f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11",
            "-ar", "48000",
            "-b:a", "192k",
            str(output_audio)
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    @classmethod
    async def synthesize_locale(cls, text: str, lang: str, video_id: str) -> Dict[str, Any]:
        """
        Synthesizes speech and subtitles for a specific locale.
        Returns dict with audio_path, subtitle_path, and duration.
        """
        locale_cfg = LOCALES.get(lang, LOCALES["en"])
        voice = locale_cfg["voice"]

        clean_text = ScriptEngine.normalize_for_tts(text, lang=lang)

        # Output paths
        lang_audio_dir = RAW_AUDIO_DIR / video_id
        lang_audio_dir.mkdir(parents=True, exist_ok=True)

        raw_audio_path = lang_audio_dir / f"{video_id}_{lang}_raw.mp3"
        norm_audio_path = lang_audio_dir / f"{video_id}_{lang}.mp3"
        vtt_sub_path = lang_audio_dir / f"{video_id}_{lang}.vtt"
        srt_sub_path = lang_audio_dir / f"{video_id}_{lang}.srt"

        # Edge TTS Communicate
        communicate = edge_tts.Communicate(
            text=clean_text,
            voice=voice,
            rate="+0%",
            volume="+0%"
        )

        # Write audio and subtitles
        sub_maker = edge_tts.SubMaker()
        with open(raw_audio_path, "wb") as audio_file:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_file.write(chunk["data"])
                elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                    sub_maker.feed(chunk)

        # Normalize audio to -14 LUFS first
        cls.normalize_loudness(raw_audio_path, norm_audio_path)
        duration = cls.get_audio_duration(norm_audio_path)

        # Write subtitle files (SRT and VTT)
        srt_content = sub_maker.get_srt()
        if not srt_content.strip():
            # Fallback single cue if edge-tts didn't emit boundary markers
            dur_ms = int(duration * 1000)
            hours, remainder = divmod(dur_ms // 1000, 3600)
            minutes, seconds = divmod(remainder, 60)
            millis = dur_ms % 1000
            end_time = f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"
            srt_content = f"1\n00:00:00,000 --> {end_time}\n{clean_text}\n"

        with open(srt_sub_path, "w", encoding="utf-8") as f:
            f.write(srt_content)

        # Convert SRT to VTT
        vtt_lines = ["WEBVTT\n\n"]
        for line in srt_content.strip().split("\n"):
            # replace comma with period in timestamp line
            if "-->" in line:
                vtt_lines.append(line.replace(",", ".") + "\n")
            else:
                vtt_lines.append(line + "\n")
        with open(vtt_sub_path, "w", encoding="utf-8") as f:
            f.writelines(vtt_lines)

        return {
            "lang": lang,
            "voice": voice,
            "raw_audio": str(raw_audio_path),
            "audio_path": str(norm_audio_path),
            "subtitle_vtt": str(vtt_sub_path),
            "subtitle_srt": str(srt_sub_path),
            "duration": duration
        }

    @classmethod
    async def synthesize_all_locales(cls, locales_dict: Dict[str, Any], video_id: str) -> Dict[str, Dict[str, Any]]:
        results = {}
        for lang, locale_obj in locales_dict.items():
            narration = locale_obj.narration if hasattr(locale_obj, "narration") else locale_obj["narration"]
            res = await cls.synthesize_locale(narration, lang, video_id)
            results[lang] = res
        return results
