"""
NEET UG 2D Video Engine - Configuration & Constants
Derived from MASTER_BLUEPRINT.md v1.1
"""
__version__ = "2.0.0"
PIPELINE_MILESTONE = "Kinematics-Flagship"

import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
QUEUE_DIR = BASE_DIR / "queue"
ASSETS_DIR = BASE_DIR / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
RENDER_DIR = BASE_DIR / "render"
TEMPLATES_DIR = RENDER_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "output"

RAW_AUDIO_DIR = OUTPUT_DIR / "raw_audio"
RAW_VIDEO_DIR = OUTPUT_DIR / "raw_video"
FINAL_DIR = OUTPUT_DIR / "final"
PRONUNCIATION_RULES_PATH = QUEUE_DIR / "pronunciation_rules.json"

# Ensure essential directories exist
for directory in [QUEUE_DIR, ASSETS_DIR, FONTS_DIR, RENDER_DIR, TEMPLATES_DIR, RAW_AUDIO_DIR, RAW_VIDEO_DIR, FINAL_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Locales & Voices (edge-tts)
# Baseline voices with clear diction for educational NEET pedagogy
LOCALES = {
    "en": {
        "voice": "en-IN-NeerjaNeural",
        "name": "English",
        "lang_code": "eng",
        "font_family": "Arial"
    },
    "hi": {
        "voice": "hi-IN-MadhurNeural",
        "name": "Hindi",
        "lang_code": "hin",
        "font_family": "Nirmala UI"
    },
    "ta": {
        "voice": "ta-IN-ValluvarNeural",
        "name": "Tamil",
        "lang_code": "tam",
        "font_family": "Nirmala UI"
    }
}

DEFAULT_LOCALES = ["en", "hi", "ta"]

# Render Specifications (Section 8 & 3D Extension)
RENDER_SPECS = {
    "draft": {
        "resolution": (1920, 1080),
        "pixel_width": 1920,
        "pixel_height": 1080,
        "fps": 30,
        "crf": 23,
        "preset": "fast",
        "manim_quality": "-qh"
    },
    "master": {
        "resolution": (3840, 2160),
        "pixel_width": 3840,
        "pixel_height": 2160,
        "fps": 30,
        "crf": 18,
        "preset": "slow",
        "manim_quality": "-qk"
    }
}

# 3D Render Specifications (Declared for Phase 5)
RENDER_3D_MULTIPLIER = 3.5

RENDER_3D_DRAFT = {
    "resolution": (1920, 1080),
    "pixel_width": 1920,
    "pixel_height": 1080,
    "fps": 30,
    "crf": 23,
    "preset": "fast",
    "timeout_sec": 180,
    "renderer": "cairo",
    "manim_quality": "-qh"
}

RENDER_3D_MASTER = {
    "resolution": (3840, 2160),
    "pixel_width": 3840,
    "pixel_height": 2160,
    "fps": 30,
    "crf": 18,
    "preset": "slow",
    "timeout_sec": 600,
    "renderer": "cairo",
    "manim_quality": "-qk"
}

# Audio Specifications
AUDIO_TARGET_LUFS = -14.0
AUDIO_BITRATE = "192k"
AUDIO_SAMPLE_RATE = 48000
WORDS_PER_MINUTE = 130
POST_FORMULA_PAUSE_SEC = 0.500

# Beat Pacing Defaults (Section 4)
TIER_HOLD_TIMES = {
    "settle": 4.0,     # 3-6s
    "context": 1.0,    # standard flow
    "standard": 1.2,   # standard flow
    "critical": 3.0,   # deliberate, visual highlight
    "release": 5.0     # 5-8s
}

# Branding & Intellectual Property Watermark Configuration
# Single source of truth for broadcast corner bug and legal MP4 metadata.
BRAND_NAME = "NEET UG 26-27"
BRAND_COPYRIGHT = "© 2026-2027 NEET UG Masterclass. All Rights Reserved."
BRAND_WATERMARK_ENABLED = True
BRAND_WATERMARK_TYPE = "text"                # "text" or "image"
BRAND_WATERMARK_TEXT = "NEET UG 26-27"       # Update here when project name is finalized

BRAND_WATERMARK_OPACITY = 0.35               # 35% broadcast translucency
BRAND_WATERMARK_FONT_SIZE = 17
BRAND_WATERMARK_FONT_PATH = FONTS_DIR / "Inter-Bold.otf"
BRAND_WATERMARK_POSITION = "bottom_right"    # "bottom_right", "bottom_left", "top_right", "top_left"
BRAND_LOGO_DIR = ASSETS_DIR / "branding"
BRAND_LOGO_PATH = BRAND_LOGO_DIR / "logo.png"
BRAND_LOGO_DIR.mkdir(parents=True, exist_ok=True)

# Typography Design System Standards (Gemini / Modern UI Standard)
FONT_PRIMARY = "Inter"
FONT_MONO = "Consolas"
DEFAULT_THEME = "modern_edtech"  # "modern_edtech", "academic_masterclass", "3b1b", "cupertino"

