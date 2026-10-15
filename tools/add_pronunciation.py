"""
Add Pronunciation Override CLI
Enables educators and creators to add pronunciation overrides on-the-go with one simple command.
Automatically updates queue/user_pronunciation_overrides.json and optionally generates a test audio clip.
"""

import argparse
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

from config import QUEUE_DIR
from tools.test_pronunciation import test_pronunciation

OVERRIDES_PATH = QUEUE_DIR / "user_pronunciation_overrides.json"

def add_override(find_word: str, replace_phonetic: str, lang: str = "ta", notes: str = "", test_audio: bool = True):
    if not OVERRIDES_PATH.exists():
        data = {"global": [], "ta": [], "hi": [], "en": []}
    else:
        try:
            with open(OVERRIDES_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {"global": [], "ta": [], "hi": [], "en": []}

    if lang not in data:
        data[lang] = []

    # Build regex pattern: if plain alphanumeric, wrap in \b word boundaries
    if re.match(r"^[A-Za-z0-9\s_-]+$", find_word):
        pattern = rf"\b{re.escape(find_word.strip())}\b"
    else:
        pattern = find_word.strip()

    # Check if rule already exists; update it if so
    found = False
    for r in data[lang]:
        if r.get("find") == pattern or r.get("find") == find_word:
            r["find"] = pattern
            r["replace"] = replace_phonetic.strip()
            if notes:
                r["notes"] = notes
            found = True
            break

    if not found:
        data[lang].append({
            "find": pattern,
            "replace": replace_phonetic.strip(),
            "notes": notes or f"Custom override for {find_word}"
        })

    with open(OVERRIDES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully added pronunciation override to [{lang.upper()}]:")
    print(f"   '{find_word}'  ──▶  '{replace_phonetic}'")
    print(f"   Saved to: {OVERRIDES_PATH}")

    # Immediately test with a sample sentence!
    if test_audio:
        sample_sentence = f"In today's lesson, observe the {find_word} carefully."
        if lang == "ta":
            sample_sentence = f"இன்றைய பாடத்தில் {find_word} பற்றி படிப்போம்."
        elif lang == "hi":
            sample_sentence = f"आज के पाठ में {find_word} को ध्यान से देखें।"

        print(f"\n🎧 Testing pronunciation with sample: \"{sample_sentence}\"")
        test_pronunciation(sample_sentence, lang=lang, make_audio=True)

def main():
    parser = argparse.ArgumentParser(description="Add Pronunciation Override On-The-Go")
    parser.add_argument("--find", type=str, required=True, help="Word or acronym to catch (e.g. 'Vernier Caliper')")
    parser.add_argument("--replace", type=str, required=True, help="Phonetic replacement (e.g. 'வெர்னியர் காலிப்பர்')")
    parser.add_argument("--lang", type=str, default="ta", choices=["ta", "hi", "en", "global"], help="Language (ta, hi, en, global)")
    parser.add_argument("--notes", type=str, default="", help="Optional note explaining the correction")
    parser.add_argument("--no-test", action="store_true", help="Skip synthesizing test audio sample")
    
    args = parser.parse_args()
    add_override(args.find, args.replace, lang=args.lang, notes=args.notes, test_audio=not args.no_test)

if __name__ == "__main__":
    main()
