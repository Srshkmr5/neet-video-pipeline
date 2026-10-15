"""
Base Audio TTS Adapter Interface
Defines the abstract interface for all audio narration providers.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, Optional

class BaseTTSAdapter(ABC):
    """Abstract Base Class for Text-to-Speech Providers."""
    
    @abstractmethod
    def synthesize(
        self,
        text: str,
        output_path: Path,
        voice_id: Optional[str] = None,
        language: str = "en-IN",
        rate: str = "+0%",
        pitch: str = "+0Hz"
    ) -> Path:
        """
        Synthesizes text into an audio file (.mp3 / .wav).
        
        Args:
            text: Preprocessed text script.
            output_path: Target destination path for synthesized audio.
            voice_id: Specific voice name or ID.
            language: Target language code (e.g. 'ta-IN', 'en-IN').
            rate: Speed modifier (e.g. '+0%', '-5%').
            pitch: Pitch modifier (e.g. '+0Hz').
            
        Returns:
            Path to the saved audio file.
        """
        pass

    @abstractmethod
    def get_default_voice(self, language: str = "en-IN") -> str:
        """Returns the recommended default voice for a given language."""
        pass
