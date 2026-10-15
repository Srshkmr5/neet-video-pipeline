"""
Pronunciation Testing Tool
CLI to test phonetic normalization rules and synthesize instant 2-second audio samples
using Edge-TTS voices across English, Hindi, and Tamil.
"""

import argparse
import asyncio
import json
import re
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import edge_tts
from config import LOCALES, PRONUNCIATION_RULES_PATH
from llm.script_engine import ScriptEngine

async def synthesize_test_audio(text: str, voice: str, output_path: Path) -> float:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_path))
    from assets.tts_engine import TTSEngine
    return TTSEngine.get_audio_duration(output_path)

def test_pronunciation(text: str, lang: str = "ta", make_audio: bool = True):
    print("=" * 70)
    print(f"       PRONUNCIATION & PHONETIC NORMALIZATION TEST [{lang.upper()}]")
    print("=" * 70)

    locale_info = LOCALES.get(lang, LOCALES["en"])
    voice = locale_info["voice"]
    lang_name = locale_info["name"]

    print(f"🌐 Target Language : {lang_name} ({lang})")
    print(f"🎙️ Edge-TTS Voice  : {voice}")
    print(f"\n📝 Original Text:\n   \"{text}\"")

    normalized = ScriptEngine.normalize_for_tts(text, lang=lang)
    print(f"\n🗣️ Normalized Spoken Text:\n   \"{normalized}\"")

    # Detect triggered rules
    rules_dict = ScriptEngine.load_pronunciation_rules()
    triggered = []
    
    # Global checks
    for r in rules_dict.get("global", []):
        pat = r.get("find", "")
        if pat and re.search(pat, text):
            triggered.append(f"[GLOBAL] '{pat}' -> '{r.get('replace')}'")

    # Language checks
    for r in rules_dict.get(lang, []):
        pat = r.get("find", "")
        if pat and re.search(pat, text):
            note = f" ({r.get('notes')})" if r.get("notes") else ""
            triggered.append(f"[{lang.upper()}] '{pat}' -> '{r.get('replace')}'{note}")

    print("\n🔍 Rules Triggered:")
    if triggered:
        for t in triggered:
            print(f"   ✓ {t}")
    else:
        print("   (No specific rules triggered; text passed as-is)")

    if make_audio:
        out_dir = BASE_DIR / "output" / "previews"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"pronunciation_test_{lang}.mp3"

        print(f"\n⏳ Synthesizing test audio with {voice}...")
        try:
            duration = asyncio.run(synthesize_test_audio(normalized, voice, out_file))
            print(f"✅ Audio generated successfully! Duration: {duration:.2f}s")
            print(f"   Saved to: {out_file}")
        except Exception as e:
            print(f"❌ Error generating audio: {e}")

    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Multilingual Pronunciation Testing Tool for Edge-TTS")
    parser.add_argument("--text", type=str, required=True, help="Input text to test")
    parser.add_argument("--lang", type=str, default="ta", choices=["ta", "hi", "en"], help="Language code (ta, hi, en)")
    parser.add_argument("--no-audio", action="store_true", help="Only show normalized text, skip audio generation")
    args = parser.parse_args()

    test_pronunciation(args.text, lang=args.lang, make_audio=not args.no_audio)

if __name__ == "__main__":
    main()
