"""
Edge-TTS Adapter (Microsoft Neural Public Engine)
100% Free, Zero API Key required.
Provides high-fidelity Tamil (Valluvar / Pallavi) and Indian English (Neerja / Prabhat) neural voices.
"""

import asyncio
from pathlib import Path
from typing import Optional
import edge_tts

from audio.adapters.base_adapter import BaseTTSAdapter

DEFAULT_VOICES = {
    "ta-IN": "ta-IN-ValluvarNeural",     # High-clarity native Tamil Male
    "ta-IN-female": "ta-IN-PallaviNeural", # Native Tamil Female
    "hi-IN": "hi-IN-MadhurNeural",       # Natural Hindi Male
    "hi-IN-female": "hi-IN-SwaraNeural", # Natural Hindi Female
    "en-IN": "en-IN-NeerjaExpressiveNeural", # Natural expressive Indian English Female
    "en-IN-male": "en-IN-PrabhatNeural",  # Authoritative Indian English Male
    "en-US": "en-US-GuyNeural"
}

class EdgeTTSAdapter(BaseTTSAdapter):
    """Adapter for Microsoft Edge-TTS public neural engine."""

    def get_default_voice(self, language: str = "en-IN") -> str:
        lang_lower = language.lower()
        if "ta" in lang_lower:
            return DEFAULT_VOICES["ta-IN"]
        if "hi" in lang_lower:
            return DEFAULT_VOICES["hi-IN"]
        return DEFAULT_VOICES.get(language, DEFAULT_VOICES["en-IN"])

    async def _async_synthesize(
        self,
        text: str,
        output_path: Path,
        voice: str,
        rate: str = "+0%",
        pitch: str = "+0Hz"
    ):
        output_path.parent.mkdir(parents=True, exist_ok=True)
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(str(output_path))

    def synthesize(
        self,
        text: str,
        output_path: Path,
        voice_id: Optional[str] = None,
        language: str = "en-IN",
        rate: str = "+0%",
        pitch: str = "+0Hz"
    ) -> Path:
        chosen_voice = voice_id or self.get_default_voice(language)
        
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Running inside existing loop
                import nest_asyncio
                nest_asyncio.apply()
                loop.run_until_complete(self._async_synthesize(text, output_path, chosen_voice, rate, pitch))
            else:
                loop.run_until_complete(self._async_synthesize(text, output_path, chosen_voice, rate, pitch))
        except RuntimeError:
            asyncio.run(self._async_synthesize(text, output_path, chosen_voice, rate, pitch))

        return output_path
