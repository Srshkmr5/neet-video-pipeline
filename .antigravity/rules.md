# Antigravity Pipeline Rules & Guardrails
Derived from MASTER_BLUEPRINT.md v1.1

## Core Guardrails
1. **Parametric Template Enforcement**:
   - The LLM and batch orchestrator generate and validate JSON concept nodes.
   - The LLM never writes raw Manim Python scenes during batch runs; all animations flow through registered parametric templates.
2. **Formula Phonetic Normalization**:
   - Math equations and LaTeX must be normalized to phonetic speech before passing to TTS engines (e.g. `\theta` -> "theta", `\pi` -> "pie", `v_0` -> "v naught").
3. **Soft Subtitle Multiplexing**:
   - Subtitles must be muxed as soft tracks (`mov_text` for MP4), never burned into the visual render.
4. **MD5 Visual Caching**:
   - Visual parameters must be hashed before rendering. If the raw visual MP4 with matching MD5 already exists, Manim compilation is bypassed and existing visual assets are reused.
5. **Deterministic Canonical ID**:
   - All files adhere to `[Subject][Grade]-C[Chapter]-T[Topic]-V[Video]` (e.g. `P11-C04-T02-V03`).
6. **Healer Boundaries**:
   - Healer subagents NEVER edit template code files or system architecture.
   - They strictly patch input parameters, phonetic strings, or FFmpeg CLI arguments.
7. **Autonomous Execution & Permissions**:
   - The user has granted full permissions for this project.
   - Proactively execute builds, renders, audio syntheses, repairs, and verification commands without pausing for intermediate approvals.

8. **Mandatory Pre-Flight Visual Verification & PDF Cross-Check (The Zero-Mistake Gatekeeper)**:
   - **Never render a chapter video blind**: No final video synthesis (`render_concept_video.py` or batch stitching) is permitted until a unit passes the Pre-Flight Gatekeeper.
   - **Hard Render Lock**: The render engine throws a hard `PermissionError` unless every concept canonical ID is explicitly marked `"APPROVED"` in `queue/approval_manifest.json`.
   - **Primary PDF Fact Verification**: All formulas, NCERT rules, trap points, and PYQ tags MUST be cross-verified directly against primary PDF sources (NCERT textbook PDFs and official NEET question paper PDFs in `C:\Users\DELL\OneDrive\Desktop\NEET\`), eliminating synthetic or hallucinated exam claims.
   - **Three-Tier Typography System & Glyph Purity**: The pipeline permanently enforces a 3-tier hierarchy:
     - `FONT_HEADER = "Verdana"` (Prominent, clean, high-impact topic and main scene titles)
     - `FONT_CARD = "Cascadia Mono"` (Modern technical container card headers, telemetry badges, and table headers)
     - `FONT_BODY = "Consolas"` (Body bullets, derivation steps, formulas, and values — guarantees 100% constant character width, razor-sharp LCD contrast, and zero kerning gaps)
     - Never use fake Unicode substitutions (such as Canadian Aboriginal Syllabics `146B`); all exponents/subscripts must use native sub-mobject positioning.
   - **Interactive Storyboard Proof**: The pipeline automatically compiles all 4-beat static proof screenshots (`beat_1` to `beat_4`) into an interactive Markdown storyboard carousel for visual review and sign-off before production rendering.
