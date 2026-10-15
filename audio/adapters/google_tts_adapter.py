"""
Google Text-to-Speech Adapter
Supports Google Cloud Neural2 / Studio voices with automatic gTTS fallback.
"""

import os
from pathlib import Path
from typing import Optional
from gtts import gTTS

from audio.adapters.base_adapter import BaseTTSAdapter

DEFAULT_GOOGLE_VOICES = {
    "ta-IN": "ta-IN-Neural2-B",   # Tamil Male
    "ta-IN-female": "ta-IN-Neural2-A", # Tamil Female
    "hi-IN": "hi-IN-Neural2-B",   # Hindi Male
    "hi-IN-female": "hi-IN-Neural2-A", # Hindi Female
    "en-IN": "en-IN-Neural2-B",   # Indian English Male
    "en-IN-female": "en-IN-Neural2-A"
}

class GoogleTTSAdapter(BaseTTSAdapter):
    """Adapter for Google Cloud Text-to-Speech API with gTTS fallback."""

    def get_default_voice(self, language: str = "en-IN") -> str:
        lang_lower = language.lower()
        if "ta" in lang_lower:
            return DEFAULT_GOOGLE_VOICES["ta-IN"]
        if "hi" in lang_lower:
            return DEFAULT_GOOGLE_VOICES["hi-IN"]
        return DEFAULT_GOOGLE_VOICES.get(language, DEFAULT_GOOGLE_VOICES["en-IN"])

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
        
        # Check if google-cloud-texttospeech is configured
        creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if creds and Path(creds).exists():
            try:
                from google.cloud import texttospeech
                client = texttospeech.TextToSpeechClient()
                s_input = texttospeech.SynthesisInput(text=text)
                
                if "ta" in language.lower():
                    lang_code = "ta-IN"
                elif "hi" in language.lower():
                    lang_code = "hi-IN"
                else:
                    lang_code = "en-IN"
                voice = texttospeech.VoiceSelectionParams(
                    language_code=lang_code,
                    name=chosen_voice
                )
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.MP3
                )
                response = client.synthesize_speech(
                    input=s_input, voice=voice, audio_config=audio_config
                )
                with open(output_path, "wb") as out:
                    out.write(response.audio_content)
                return output_path
            except Exception as e:
                print(f"⚠️ Google Cloud API error ({e}), falling back to gTTS...")

        # Fallback to standard gTTS
        lang_lower = language.lower()
        if "ta" in lang_lower:
            lang_code = "ta"
        elif "hi" in lang_lower:
            lang_code = "hi"
        else:
            lang_code = "en"
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(str(output_path))
        return output_path
