# NEET UG 2D Video Engine — Master Blueprint v1.1

## 0. Purpose
Single source of truth for an autonomous, code-driven 2D video engine for NEET UG
(Physics, Chemistry, Biology), orchestrated inside Google Antigravity.

## 1. Core Philosophy
Duration is emergent. Pacing is prescribed.
The engine does not schedule seconds. It declares how important each beat is,
and the template decides how slow and how repetitive it must be.

## 2. Locked Decisions
- Primary render nodes: ~674 core concept videos
- 1 video = 1 concept. Concept = 1 formula + 1 trap. The rest fold into neighbors.
- MVP languages: en, hi, ta
- Physics: Manim CE
- Chemistry: RDKit/OpenBabel -> SVG -> Manim
- Biology: SVG + Manim
- MVP audio: edge-tts
- Subtitles: edge-tts + WhisperX forced alignment
- Final MP4: 1 video + 3 audio tracks + 3 soft mov_text subtitle tracks
- First target: P11-C04-T02-V03 "The Max Height Arc"
- MD5 visual cache; FFmpeg stream-copy mux
- Dimensions: "2d" (MVP Phase 1-4) & "3d" (extension points reserved, built in Phase 5)
- MVP cost target: Rs 0

## 3. Canonical ID
Format: [Subject][Grade]-C[Chapter]-T[Topic]-V[Video]
Example: P11-C04-T02-V03
Export: /renders/P11/C04/P11-C04-T02-V03_The_Max_Height_Arc.mp4

## 4. Pacing Contract (Replaces Fixed Timings)
Every beat declares a tier. Duration is computed, never authored.

Tiers:
- settle    : slow, low stimulation, no new info. Used once at start. 3-6s.
- context   : normal pace. Real-life hook. Optional.
- standard  : normal pace. Supporting explanation.
- critical  : slow, deliberate, repeated 1-3x. Must-memorize content.
- release   : slow, winding down, no new info. Used once at end. 5-8s.

Duration formula:
  beat_duration = narration_audio_duration + visual_hold + repetition_passes

Critical beat repetition:
  Narration says key line 2-3x with different framing (definition -> example -> restated).
  Visual: formula appears -> dims -> reappears highlighted.

Opening beat (settle):
  No new information. Title card, soft motion, one calm sentence.

Closing beat (release):
  After end-capsule. No new information. Countdown ring fading out.
  One sentence preparing the student for the next video.

Length badge (derived, not authored):
  Green  : < 3 min
  Orange : 3-8 min
  Red    : > 8 min

## 5. Video Beat Structure
1. settle       - Opening, orient
2. context      - Optional real-life hook
3. standard     - Supporting explanation(s)
4. critical     - Core formula, derivation, trap (repeated)
5. end_capsule  - 15s revision overlay: formula + trap + 3-node flow
6. release      - Breathing room, prepare for next

Not every video uses every beat. Structure is declared per template.

## 6. Multilingual
Supported: en, hi, ta, te, kn, ml
MVP: en, hi, ta
Visual canvas identical across languages.
Titles, trap points, subtitles load from localized string dictionaries.
Audio tracks decoupled from visual render.
Bilingual terminology: regional term + English in brackets, rendered as two Text objects.
Audio baseline: -14 LUFS, 130 WPM, 500ms pause after formula reveals.

## 7. Technical Stack
Agent / IDE      : Google Antigravity
Animation        : Manim Community Edition
Chemistry        : RDKit / OpenBabel -> SVG
Biology          : SVG + Manim
TTS MVP          : edge-tts
Alignment        : WhisperX (local, CPU)
Assembly         : FFmpeg
State            : queue/state.json
Storage MVP      : Local + Google Drive
Database (later) : Supabase Free Tier

## 8. Render Spec
Draft   : 1920x1080, H.264 CRF 23, preset fast
Master  : 3840x2160, H.264 CRF 18, preset slow
3D Draft : 1920x1080, H.264 CRF 23, ThreeDScene / Cairo, 180s timeout
3D Master: 3840x2160, H.264 CRF 18, ThreeDScene / Cairo, 600s timeout
FPS     : 30
Audio   : AAC, 192 kbps, 48 kHz, -14 LUFS
Container: MP4
Subtitles: mov_text (soft, not burned-in)

## 9. Fonts (assets/fonts/)
NotoSansDevanagari-Regular.ttf
NotoSansTamil-Regular.ttf
NotoSansTelugu-Regular.ttf
NotoSansKannada-Regular.ttf
NotoSansMalayalam-Regular.ttf
All non-English text uses Text(font=...), never MathTex.
Mixed-language lines = two separate Text objects.

## 10. Template Registry
File: render/templates/registry.yaml
Every template must be registered before it can be queued.
JSON referencing an unregistered template is rejected by validator.
Every entry declares:
  dimension: "2d" | "3d"
  render_time_multiplier: float (1.0 for 2D, 3.5 for 3D)
  params: [list of required parameter keys]
  beats:  [list of beat tiers used]
  max_seconds: hard ceiling

## 11. Repository Structure
neet-video-pipeline/
├── .antigravity/
│   ├── rules.md
│   └── subagents/
│       ├── manim_healer.md
│       ├── tts_healer.md
│       └── mux_healer.md
├── config.py
├── main.py
├── queue/
│   ├── concepts.json
│   └── state.json
├── llm/
│   └── script_engine.py
├── assets/
│   ├── fonts/
│   └── tts_engine.py
├── render/
│   ├── templates/
│   │   └── registry.yaml
│   ├── manim_compiler.py
│   └── stitching.py
└── output/
    ├── raw_audio/
    ├── raw_video/
    └── final/

## 12. JSON Contract
{
  "videoId": "P11-C04-T02-V03",
  "prompt_version": "v1",
  "serialTitle": "The Max Height Arc",
  "subject": "Physics",
  "grade": 11,
  "templateName": "FormulaWithGraph",
  "beats": [
    {"id": "settle",   "tier": "settle"},
    {"id": "hook",     "tier": "context"},
    {"id": "concept",  "tier": "critical", "repeat": 2},
    {"id": "trap",     "tier": "critical", "repeat": 1},
    {"id": "capsule",  "tier": "standard"},
    {"id": "release",  "tier": "release"}
  ],
  "parameters": {
    "latexFormula": "H_{\\max} = \\frac{v_0^2 \\sin^2\\theta}{2g}",
    "trapWarning": "Angle theta MUST be measured relative to horizontal.",
    "graphPlot": "3*x - 0.5*x**2",
    "xRange": [0, 6],
    "yRange": [0, 4.5]
  },
  "locales": {
    "en": {"narration": "...", "trapPoint": "..."},
    "hi": {"narration": "...", "trapPoint": "..."},
    "ta": {"narration": "...", "trapPoint": "..."}
  }
}

## 13. Pipeline Workflow
1. Load queue/concepts.json
2. Validate against schema and template registry
3. Compute MD5 of visual parameters
4. If cached visual exists -> skip render
5. Else render Manim / SVG / RDKit
6. Synthesize localized audio via edge-tts
7. Align with WhisperX -> SRT -> VTT
8. Mux with FFmpeg: 1 video + 3 audio + 3 mov_text
9. Write state.json entry
10. On failure: route to correct healer subagent, retry per taxonomy

## 14. Error Taxonomy
schema_validation  : no retry, log and skip
latex_compile      : 1 retry via manim_healer
python_syntax      : 1 retry via manim_healer
missing_asset      : no retry, log and skip
tts_rate_limit     : 3 retries with backoff, skip lang if persists
ffmpeg_mux         : 1 retry via mux_healer
disk_full          : halt batch

## 15. Subagent Contracts
manim_healer
  in : {videoId, template_name, stderr, parameters}
  out: {patched_parameters | null, reason}
  forbidden: editing template Python files

tts_healer
  in : {lang, text, error}
  out: {normalized_text | null}
  duty: phonetic normalization (\\pi -> "pie", theta -> "theta", etc.)

mux_healer
  in : {video_path, audio_paths, ffmpeg_stderr}
  out: {fixed_ffmpeg_args | null}

Subagents never create files. They only patch data.

## 16. PYQ Integration
1. OCR PYQ PDFs 2016-2026 -> pyq_raw.json
2. Auto-tag each question to canonical video ID
3. Aggregate frequency per concept node
4. Store as pyq_map.json
5. At render time, inject into template parameters:
   Visual badge: "High Yield | PYQ: 2017, 2019, 2024"
   Audio hook : "This concept appeared in NEET 2017, 2019, 2024..."

PYQ injection is post-generation. LLM writes neutral scripts.

## 17. NotebookLM Role
NotebookLM is a retrieval and citation engine ONLY.
Sources loaded: NCERT textbooks, Exemplars, NEET UG PYQs 2016-2026.

Permitted:
- Return exact NCERT definitions, formulas, page references
- Return PYQ questions with year and question number
- Flag when a claim is not in source material

Forbidden:
- Generating JSON schemas
- Writing code
- Planning architecture
- Suggesting tools or renderers
- Inventing content not in uploaded PDFs

Every answer must cite [Book, Chapter, Page] or [NEET Year, Q#].

Usage: one query per concept node. Output feeds Gemini script generator.

## 18. Antigravity Guardrails
1. Parametric template enforcement: LLM generates JSON, never raw Manim code during batch
2. Formula phonetic normalization before TTS
3. Soft subtitle multiplexing (mov_text, not burned-in)
4. MD5 visual caching
5. One video must succeed end-to-end before batch scaling
6. No new templates during batch runs

## 19. QA Rubric
A video passes if all 5:
- NCERT-accurate (verified against NotebookLM)
- Audio clean, no glitches
- Audio-video sync within 150ms
- Trap warning is correct and matches a real PYQ distractor
- End-capsule is readable at 1080p on phone

Manual review: first 20 videos. Then 1-in-20 spot check.

## 20. Monetization
Target: 5,000 paid students x Rs 7,500 = Rs 3.75 Cr gross.
B2B: 25 coaching institutes x 200 seats x Rs 5,000.
Distribution: YouTube Shorts / Reels from 15s end-capsules + B2B bulk licensing.

## 21. Open Questions (Do Not Block Phase 1)
1. Exact chapter count per subject from Master Google Sheet
2. Which 10 videos form the pilot batch after P11-C04-T02-V03
3. Female voice for Biology in MVP or Phase 2
4. Bunny.net pricing confirmed before Phase 6
5. Player UI spec (Phase 6)

## 22. Glossary
AGY    : Google Antigravity
Beat   : A temporal unit in a video with a declared tier
Tier   : Pacing profile (settle, context, standard, critical, release)
End-capsule: 15s revision overlay
Canonical ID: Deterministic video identifier
MD5 cache: Hash-based visual reuse
mov_text: Soft subtitle format in MP4

## 23. 3D Extension Architecture (Declared Now, Built in Phase 5)

### 23.1 Core Principles
- 2D is the MVP production standard (Phase 1–4).
- 3D extension points are declared across registry, base classes, render specs, and schema from day one without refactoring.
- Active 3D rendering activates in Phase 5.

### 23.2 Manim Base Hierarchy
- `NEETVideoScene`: 2D scene base extending `manim.Scene`.
- `NEETVideoScene3D`: 3D scene base extending `manim.ThreeDScene`.
- Both share the exact same beat structure, tier pacing, audio durations, and 15s end revision capsule.
- In `NEETVideoScene3D`, 2D UI elements (header badges, formula card, revision capsule) are pinned flat using `add_fixed_in_frame_mobjects(...)`.
- Baseline camera orientation: `phi = 75°`, `theta = -45°` with ambient rotation hooks.

### 23.3 Chemistry 3D Pipeline Contract
- Architecture:
  `SMILES -> RDKit 3D conformer -> .mol/.sdf -> Manim ThreeDScene loader -> animated 3D scene.`
  `Fallback: RDKit -> PyMOL headless -> PNG sequence -> Manim composite.`
- Registered template: `MoleculeConformer3D` (`dimension: "3d"`, `render_time_multiplier: 3.5`).

### 23.4 Biology 3D Pipeline Contract
- Architecture:
  `Default: SVG (2D).`
  `3D cases (DNA helix, protein folding): use Mol* or PyMOL renders embedded as image sequences.`
- Registered template: `DNAHelix3D` (`dimension: "3d"`, `render_time_multiplier: 3.5`).

### 23.5 Disk and Time Budget (674 Primary Concept Nodes)
Assumes **10% of videos (67 videos) are 3D** and **90% of videos (607 videos) are 2D**:
- **Render Time Multiplier**: 1.0x (2D) vs 3.5x (3D).
- **Draft Batch Render Time**:
  - 2D: 607 videos x 30s = 5.06 hrs
  - 3D: 67 videos x 105s = 1.95 hrs
  - **Total Draft Time**: ~7.0 hours
- **Master Batch Render Time**:
  - 2D: 607 videos x 90s = 15.18 hrs
  - 3D: 67 videos x 315s = 5.86 hrs
  - **Total Master Time**: ~21.0 hours
- **Disk Budget**:
  - 2D: ~35 MB / video x 607 = ~21.2 GB
  - 3D: ~80 MB / video x 67 = ~5.4 GB
  - **Total Disk Footprint**: ~26.6 GB (Reserve 35–40 GB with caching)

### 23.6 Phase Roadmap Update
- **Phase 1**: 2D Vertical Slice (`P11-C04-T02-V03`) — Complete & Verified
- **Phase 2**: Batch Audio & Script Automation
- **Phase 3**: Physics 2D Template Expansion
- **Phase 4**: Chemistry 2D (SVG/RDKit) & Biology 2D (SVG)
- **Phase 5**: Scale by Subject + 3D Template Build (`NEETVideoScene3D`, RDKit 3D conformers, Mol*/PyMOL image sequences)
- **Phase 6**: Player UI & Bulk Licensing