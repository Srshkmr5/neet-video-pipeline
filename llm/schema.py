"""
Pydantic Data Models and Validation for NEET Video Pipeline
Derived from MASTER_BLUEPRINT.md v1.1 Section 12
"""
from enum import Enum
from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field, field_validator
import re

class BeatTier(str, Enum):
    SETTLE = "settle"
    CONTEXT = "context"
    STANDARD = "standard"
    CRITICAL = "critical"
    RELEASE = "release"

class Beat(BaseModel):
    id: str
    tier: BeatTier
    repeat: int = Field(default=1, ge=1, le=5)

class LocaleText(BaseModel):
    title: Optional[str] = None
    narration: str
    trapPoint: str
    pyqBadge: Optional[str] = None

class ConceptNode(BaseModel):
    videoId: str = Field(..., description="Canonical ID: [Subject][Grade]-C[Chapter]-T[Topic]-V[Video]")
    prompt_version: str = "v1"
    serialTitle: str
    subject: str
    grade: int
    templateName: str
    dimension: Optional[str] = Field(default="2d", description="'2d' or '3d'")
    
    # 3-Tier Sequence Coordinates
    seq_chapter: int = Field(default=1, description="Local index in chapter (e.g. 3 of 14)")
    total_chapter_videos: int = Field(default=1, description="Total videos in this chapter")
    seq_subject: Optional[int] = Field(default=None, description="Running sequence in subject (e.g. 11 of 234)")
    total_subject_videos: Optional[int] = Field(default=None)
    seq_global: Optional[int] = Field(default=None, description="Global curriculum sequence (e.g. 11 of 665)")
    total_global_videos: Optional[int] = Field(default=None)

    # Prerequisite / Progression Chain
    prev_video_id: Optional[str] = None
    next_video_id: Optional[str] = None
    next_video_title: Optional[str] = None

    beats: List[Beat]
    parameters: Dict[str, Any]
    locales: Dict[str, LocaleText]

    @field_validator("dimension")
    @classmethod
    def validate_dimension(cls, v: Optional[str]) -> str:
        if v and v.lower() not in ("2d", "3d"):
            raise ValueError(f"Invalid dimension '{v}', must be '2d' or '3d'")
        return (v or "2d").lower()

    @field_validator("videoId")
    @classmethod
    def validate_canonical_id(cls, v: str) -> str:
        pattern = r"^[PCB]\d{2}-C\d{2}-T\d{2}-V\d{2}$"
        if not re.match(pattern, v):
            raise ValueError(f"videoId '{v}' does not match canonical format [Subject][Grade]-C[Chapter]-T[Topic]-V[Video]")
        return v

    @field_validator("beats")
    @classmethod
    def validate_beats(cls, beats: List[Beat]) -> List[Beat]:
        if not beats:
            raise ValueError("beats list cannot be empty")
        if beats[0].tier != BeatTier.SETTLE:
            raise ValueError("The first beat must be tier 'settle'")
        if beats[-1].tier != BeatTier.RELEASE:
            raise ValueError("The last beat must be tier 'release'")
        return beats

    @field_validator("locales")
    @classmethod
    def validate_locales(cls, locales: Dict[str, LocaleText]) -> Dict[str, LocaleText]:
        required = {"en", "hi", "ta"}
        missing = required - set(locales.keys())
        if missing:
            raise ValueError(f"Missing required MVP locales: {missing}")
        return locales

class ConceptQueue(BaseModel):
    concepts: List[ConceptNode]
