"""
Unified Audio Narration Engine & Dispatcher
Dispatches synthesis requests to pluggable TTS providers (Edge-TTS, Google Cloud, ElevenLabs).
Applies multilingual pronunciation corrections and transparently manages an audio cache.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
from typing import Dict, Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from audio.adapters.base_adapter import BaseTTSAdapter
from audio.adapters.edge_tts_adapter import EdgeTTSAdapter
from audio.adapters.google_tts_adapter import GoogleTTSAdapter
from audio.adapters.elevenlabs_adapter import ElevenLabsAdapter

CACHE_DIR = BASE_DIR / "audio" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

DICTIONARY_PATH = BASE_DIR / "tools" / "pronunciation_dictionary.json"

class AudioEngine:
    """Master Audio Narration Controller."""

    def __init__(self, default_provider: str = "edge_tts"):
        self.default_provider = default_provider
        self.adapters: Dict[str, BaseTTSAdapter] = {
            "edge_tts": EdgeTTSAdapter(),
            "microsoft": EdgeTTSAdapter(),
            "google": GoogleTTSAdapter(),
            "google_cloud": GoogleTTSAdapter(),
            "elevenlabs": ElevenLabsAdapter(),
            "eleven_labs": ElevenLabsAdapter()
        }
        self.pronunciation_rules = self._load_pronunciation_rules()

    def _load_pronunciation_rules(self) -> Dict[str, Any]:
        if DICTIONARY_PATH.exists():
            try:
                with open(DICTIONARY_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def preprocess_text(self, text: str, language: str = "en-IN") -> str:
        """
        Applies pronunciation replacements (e.g. 'NEET' -> 'நீட்' in Tamil).
        """
        processed = text
        lang_key = "tamil" if "ta" in language.lower() else "english"
        
        # Replace global acronyms
        acronyms = self.pronunciation_rules.get("acronyms", {})
        for word, rule in acronyms.items():
            replacement = rule.get(lang_key) or rule.get("english")
            if replacement:
                pattern = r"\b" + re.escape(word) + r"\b"
                processed = re.sub(pattern, replacement, processed, flags=re.IGNORECASE)

        # Replace formulas and symbols
        formulas = self.pronunciation_rules.get("formulas_and_symbols", {})
        for sym, rule in formulas.items():
            replacement = rule.get(lang_key) or rule.get("spoken_english")
            if replacement:
                processed = processed.replace(sym, replacement)

        return processed

    def _compute_cache_key(
        self,
        provider: str,
        voice_id: str,
        language: str,
        text: str,
        rate: str,
        pitch: str
    ) -> str:
        raw_key = f"{provider}::{voice_id}::{language}::{rate}::{pitch}::{text}"
        return hashlib.md5(raw_key.encode("utf-8")).hexdigest()

    def generate_narration(
        self,
        text: str,
        output_path: Path,
        provider: Optional[str] = None,
        voice_id: Optional[str] = None,
        language: str = "en-IN",
        rate: str = "+0%",
        pitch: str = "+0Hz",
        use_cache: bool = True
    ) -> Path:
        """
        Generates audio narration using the specified or default provider.
        """
        chosen_provider = (provider or self.default_provider).lower()
        adapter = self.adapters.get(chosen_provider, self.adapters["edge_tts"])
        
        # 1. Preprocess text with pronunciation rules
        clean_text = self.preprocess_text(text, language)

        # 2. Check cache
        effective_voice = voice_id or adapter.get_default_voice(language)
        cache_key = self._compute_cache_key(chosen_provider, effective_voice, language, clean_text, rate, pitch)
        cached_file = CACHE_DIR / f"{cache_key}.mp3"

        if use_cache and cached_file.exists() and cached_file.stat().st_size > 0:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(cached_file), str(output_path))
            return output_path

        # 3. Synthesize via Adapter
        result_path = adapter.synthesize(
            text=clean_text,
            output_path=cached_file,
            voice_id=effective_voice,
            language=language,
            rate=rate,
            pitch=pitch
        )

        # 4. Copy to target destination
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(result_path), str(output_path))
        return output_path

def main():
    parser = argparse.ArgumentParser(description="Unified Audio Narration Engine")
    parser.add_argument("--text", type=str, required=True, help="Text to synthesize")
    parser.add_argument("--out", type=str, required=True, help="Output audio file path (.mp3)")
    parser.add_argument("--provider", type=str, default="edge_tts", choices=["edge_tts", "google", "elevenlabs"], help="TTS Provider")
    parser.add_argument("--voice", type=str, default="", help="Specific Voice Name/ID")
    parser.add_argument("--lang", type=str, default="en-IN", help="Language code (e.g. 'ta-IN', 'en-IN')")
    parser.add_argument("--rate", type=str, default="+0%", help="Speed modifier (e.g. '+0%', '-5%')")
    parser.add_argument("--pitch", type=str, default="+0Hz", help="Pitch modifier")

    args = parser.parse_args()
    engine = AudioEngine(default_provider=args.provider)
    out_p = engine.generate_narration(
        text=args.text,
        output_path=Path(args.out),
        provider=args.provider,
        voice_id=args.voice or None,
        language=args.lang,
        rate=args.rate,
        pitch=args.pitch
    )
    print(f"✅ Generated Audio Narration: {out_p}")

if __name__ == "__main__":
    main()
