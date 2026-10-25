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

9. **Dynamic Audio-Visual Beat Synchronization (Zero Hardcoded Timers)**:
   - Hardcoded slide hold times (e.g. `self.wait(10)`) are strictly prohibited.
   - Each visual beat's duration must dynamically bind to its corresponding discrete TTS audio track duration:
     $$\text{Slide Hold Time} = \text{Audio Beat Duration} - \text{FadeIn (0.8s)} + \text{Inter-beat Buffer (0.5s)}$$
   - Slide transitions must never occur while narration for the current beat is still playing (eliminating desync issues such as topic slides switching early while prior audio continues).

10. **NEET Trap Memory Consolidation Hold (3.0-Second Silent Freeze)**:
    - Beat 4 (NEET Trap Card) must enforce a mandatory **3.0-second silent hold** after narration concludes before transitioning to Beat 5 or ending.
    - This dedicated screen freeze allows mobile students to take screenshots, absorb the trap logic and formula transformations, and reflect without cognitive overload.

11. **Mobile-First High-DPI Typography Scale & Vector Integrity**:
    - **Strict Ban on `scale_to_fit_width()`**: Horizontal vector squeezing is prohibited on textual mobjects. Preserving a 1:1 font aspect ratio prevents unreadable barcode-like text distortion.
    - **Text Line Wrapping**: Enforce natural two-line wrapping with a strict limit of $\le 55$ characters per line.
    - **Minimum Font Floor**: All body text, data rows, and formulas must maintain a minimum font size of $\ge 10.5\text{pt}$ (Consolas/Cascadia Mono) so content remains crisp and legible on 5.5"–6.5" Android smartphones in both landscape and portrait orientations.

12. **Per-Language Dynamic Visual Alignment (Zero Language Drift)**:
    - Narration speaking rates and syllable lengths vary significantly across languages (e.g., Hindi and Tamil narration often require 15%–30% different timing per beat compared to English).
    - It is strictly prohibited to stretch, compress, or reuse an English visual render for Hindi or Tamil audio tracks.
    - Every language edition (`en-IN`, `hi-IN`, `ta-IN`) MUST synthesize beat-discrete audio first, measure the exact beat durations in that language, and render a custom visual timeline where slide transitions and the 3.0s NEET trap freeze align precisely with that language's narration.

13. **Mandatory 3-Phase Closing Sequence (Punchline -> 3.0s Silent Hold -> Next Video End Card)**:
    - Every concept video in ALL languages (`en-IN`, `hi-IN`, `ta-IN`) must strictly include the three-phase closing sequence:
      1. **Pedagogical Punchline**: Beat 4 narration MUST conclude with the exam anchor sentence:
         - English: *"Master this to secure full marks in NEET Physics."*
         - Hindi: *"नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।"*
         - Tamil: *"நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்."*
      2. **3.0-Second Silent Trap Freeze**: The visual NEET Trap card must remain completely static on screen for exactly 3.0 seconds in total audio silence after narration ends.
      3. **Beat 5 Next Video End Card**: A 3.5-second sequence card displaying `"UP NEXT IN SEQUENCE: Concept (N+1)/Total - Next Title"`, `"Canonical ID"`, and `"INTERACTIVE LAB AVAILABLE IN APP TAB 2"`.
    - **Zero Mux Truncation**: Never pass `-shortest` with subtitle streams in FFmpeg muxing, as subtitle stream completion prematurely terminates the video and cuts off the silent freeze and end card.

14. **Pure Triad Dynamic Binding & Schema Integrity (Zero Cross-Unit Bleed)**:
    - **No Hardcoded Static Fallbacks**: Client UI templates (such as `apps/edapp_player.html`) must NEVER contain hardcoded formulas, warnings, or questions tied to a specific unit (e.g. projectile motion equations appearing in measurement units). Initial static HTML templates must either match the syllabus root (Unit 1.1.1) or render a clean generic skeleton until populated dynamically by `selectConcept()`.
    - **Dynamic Lab/Cards Binding (Tab 2)**: Both `selectConcept()` and `switchTab('lab')` must dynamically bind `simIframe.src` to `currentConcept.simulation`. Hardcoded simulation defaults or cross-unit fallbacks (e.g. defaulting to Unit 2's 3D projectile lab inside Unit 1) are strictly prohibited. Tab 2 labels must dynamically adapt between `2 • CONCEPT LAB (CARDS)` (2D concepts) and `2 • 3D SPATIAL LAB` (3D concepts).
    - **Mandatory NEET Trap Formula Card Schema (Tab 3)**:
      - Every concept entry in `curriculum_manifest.json` MUST provide a structured `trap_quiz.formula_card`:
        ```json
        "formula_card": {
          "incorrect": "Common Student Misconception / Trap Formula",
          "correct": "Authentic NCERT / Exam Correction"
        }
        ```
      - `loadTrapQuiz()` must dynamically render this card on every concept change or cleanly hide the container element if no formula is applicable, eliminating persistent stale formulas.
    - **Zero Filter Bias in Curriculum Navigation**: Filter dropdown functions (`populateUnits()`, `populateTopics()`) must initialize dynamically from the curriculum manifest without hardcoded unit/topic overrides (e.g. forcing `KINEMATICS` or `Projectile`), ensuring the syllabus always opens sequentially from the user's active unit.

