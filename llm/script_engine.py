"""
Script Engine & Multilingual Phonetic Normalizer for NEET Video Pipeline
Derived from MASTER_BLUEPRINT.md v1.1 Section 14, 15, 16, 18
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from config import PRONUNCIATION_RULES_PATH

class ScriptEngine:
    _cached_rules: Optional[Dict[str, Any]] = None
    _cached_mtime: float = 0.0

    @classmethod
    def load_pronunciation_rules(cls) -> Dict[str, Any]:
        """
        Dynamically loads and merges:
        1. Pre-packaged STEM Master Lexicon (queue/stem_master_lexicon.json)
        2. User Pronunciation Overrides (queue/user_pronunciation_overrides.json)
        User overrides take precedence over standard lexicon.
        """
        from config import QUEUE_DIR
        base_lexicon_path = QUEUE_DIR / "stem_master_lexicon.json"
        overrides_path = QUEUE_DIR / "user_pronunciation_overrides.json"
        legacy_path = QUEUE_DIR / "pronunciation_rules.json"

        merged = {"global": [], "ta": [], "hi": [], "en": []}

        # 1. Load Base STEM Lexicon
        target_base = base_lexicon_path if base_lexicon_path.exists() else legacy_path
        if target_base.exists():
            try:
                with open(target_base, "r", encoding="utf-8") as f:
                    base_data = json.load(f)
                    for k in ["global", "ta", "hi", "en"]:
                        merged[k].extend(base_data.get(k, []))
            except Exception:
                pass

        # 2. Overlay User Overrides (takes highest priority)
        if overrides_path.exists():
            try:
                with open(overrides_path, "r", encoding="utf-8") as f:
                    user_data = json.load(f)
                    for k in ["global", "ta", "hi", "en"]:
                        user_rules = user_data.get(k, [])
                        # Put user rules first or replace existing
                        merged[k] = user_rules + merged[k]
            except Exception:
                pass

        return merged

    @classmethod
    def normalize_for_tts(cls, text: str, lang: str = "en") -> str:
        """
        Phonetic normalization to eliminate raw LaTeX symbols, fix mispronunciations,
        and pronounce acronyms naturally across English, Hindi, and Tamil.
        """
        if not text:
            return ""

        rules_dict = cls.load_pronunciation_rules()
        normalized = text

        # 1. Apply Global Rules (Math operators, fractions, Greek letters)
        for rule in rules_dict.get("global", []):
            pattern = rule.get("find", "")
            repl = rule.get("replace", "")
            if pattern:
                try:
                    normalized = re.sub(pattern, repl, normalized)
                except Exception:
                    pass

        # 2. Apply Language-Specific Phonetic Rules (ta, hi, en)
        lang_rules = rules_dict.get(lang, [])
        for rule in lang_rules:
            pattern = rule.get("find", "")
            repl = rule.get("replace", "")
            if pattern:
                try:
                    normalized = re.sub(pattern, repl, normalized)
                except Exception:
                    pass

        # 3. Clean up lingering LaTeX escape characters
        normalized = re.sub(r"[\$\\]", "", normalized)

        # 4. Catalog citation & abbreviation spoken sanitization:
        # Prevent TTS from speaking awkward catalog citations like "H C Verma C H 3"
        normalized = re.sub(r"\bHCV\s*(?:Ch(?:apter)?\.?\s*\d+)?\s*:\s*", "Key insight: ", normalized, flags=re.IGNORECASE)
        normalized = re.sub(r"\bNCERT\s*(?:Class\s*\d+.*?,)?\s*Page\s*\d+\s*:\s*", "NCERT emphasizes: ", normalized, flags=re.IGNORECASE)
        normalized = re.sub(r"\bCh\.?\s*(\d+)", r"Chapter \1", normalized, flags=re.IGNORECASE)
        normalized = re.sub(r"\bpg\.?\s*(\d+)", r"page \1", normalized, flags=re.IGNORECASE)
        normalized = re.sub(r"\bvol\.?\s*(\d+)", r"volume \1", normalized, flags=re.IGNORECASE)

        # 5. Mathematical operator spoken normalization:
        # Prevent TTS from ever reading '*' as 'asterisk' or '·' as 'middle dot'
        if lang == "ta":
            normalized = re.sub(r"\s*[\*·]\s*", " பெருக்கல் ", normalized)
        elif lang == "hi":
            normalized = re.sub(r"\s*[\*·]\s*", " गुणा ", normalized)
        else:
            normalized = re.sub(r"\s*[\*·]\s*", " multiplied by ", normalized)

        # 6. Collapse repeated whitespace
        normalized = re.sub(r"\s+", " ", normalized).strip()

        return normalized

    @classmethod
    def inject_pyq_badge(cls, concept: Dict[str, Any], pyq_years: list) -> Dict[str, Any]:
        """
        Inject PYQ hook and visual badge into concept parameters per Blueprint Section 16.
        """
        if not pyq_years:
            return concept
        years_str = ", ".join(str(y) for y in sorted(pyq_years))
        badge_text = f"High Yield | PYQ: {years_str}"
        concept["parameters"]["pyqBadge"] = badge_text
        return concept
