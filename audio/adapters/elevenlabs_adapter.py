"""
ElevenLabs Adapter (Hyper-realistic Studio Cinematic Narration)
Uses ElevenLabs Multilingual v2 model for deep human warmth and emotional cadence.
Requires ELEVENLABS_API_KEY in environment or .env; falls back gracefully to EdgeTTS if absent.
"""

import os
from pathlib import Path
from typing import Optional
import requests

from audio.adapters.base_adapter import BaseTTSAdapter
from audio.adapters.edge_tts_adapter import EdgeTTSAdapter

# Popular ElevenLabs High-Quality Narrator Voice IDs
DEFAULT_ELEVEN_VOICES = {
    "Adam": "pNInz6obpgDQGcFmaJgB",      # Deep, authoritative documentary narration
    "Brian": "nPczCjzI2devNBz1zQrb",     # Warm, engaging educator voice
    "Rachel": "21m00Tcm4TlvDq8ikWAM",    # Calm, crystal clear female narration
    "default": "pNInz6obpgDQGcFmaJgB"
}

class ElevenLabsAdapter(BaseTTSAdapter):
    """Adapter for ElevenLabs Text-to-Speech API."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ELEVENLABS_API_KEY")

    def get_default_voice(self, language: str = "en-IN") -> str:
        return DEFAULT_ELEVEN_VOICES["Brian"]

    def synthesize(
        self,
        text: str,
        output_path: Path,
        voice_id: Optional[str] = None,
        language: str = "en-IN",
        rate: str = "+0%",
        pitch: str = "+0Hz"
    ) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        chosen_voice = voice_id or self.get_default_voice(language)
        
        # Check if voice is a named key in dictionary
        voice_code = DEFAULT_ELEVEN_VOICES.get(chosen_voice, chosen_voice)

        if not self.api_key:
            print("⚠️ ELEVENLABS_API_KEY not found in environment. Gracefully falling back to Edge-TTS neural engine...")
            edge_adapter = EdgeTTSAdapter()
            return edge_adapter.synthesize(text, output_path, None, language, rate, pitch)

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_code}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.3,
                "use_speaker_boost": True
            }
        }

        response = requests.post(url, json=data, headers=headers, timeout=60)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return output_path
        else:
            print(f"⚠️ ElevenLabs API returned HTTP {response.status_code} ({response.text}). Falling back to Edge-TTS...")
            edge_adapter = EdgeTTSAdapter()
            return edge_adapter.synthesize(text, output_path, None, language, rate, pitch)
