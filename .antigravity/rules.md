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
