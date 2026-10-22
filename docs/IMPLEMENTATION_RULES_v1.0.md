# NEET 2D/3D Video Pipeline: Official Implementation Rules v1.0
*Codified System Standards for Automated Educational Content Generation*

---

## Pillar 1: Canonical Taxonomy & Video Coordinates
1. **Canonical ID Structure**:
   - **Micro Concept Drills**: `[PCB]xx-Cxx-Txx-Vxx` (e.g. `P11-C02-T03-V02`)
     - `P/C/B`: Subject (Physics, Chemistry, Biology)
     - `11/12`: Grade / Class
     - `C01-C61`: Sequential Chapter across syllabus
     - `T01-T05`: Topic grouping within chapter
     - `V01-V15`: Sequential Concept Drill video
   - **Tier 1 Macro Story Movies**: `[PCB]xx-Cxx-MOVIE` (e.g. `P11-C02-MOVIE`)
2. **Master Curriculum Registry**:
   - Single source of truth is `queue/curriculum_master_full_665.csv` and `queue/taxonomy_master.csv`.
   - No video may be rendered without a recognized Canonical ID and parent movie mapping.

---

## Pillar 2: Dual-Tier Architecture (Macro Movie vs Micro Drills)
1. **Tier 1: Chapter Master Story Movie (~8 to 12 Minutes)**:
   - Exactly 61 Master Movies in total (1 per chapter).
   - Cinematic 3D storytelling, 5-Act narrative arc, real-world physical mystery, visual intuition.
   - Features on-screen glowing **Exam Anchor Badges** marking key formulas without disrupting story flow.
2. **Tier 2: Micro Concept Capsules (~1 to 3 Minutes each)**:
   - Exactly 665 surgical concept drills across the syllabus.
   - High-contrast 2D Manim animations, zero-fluff formula derivations, NCERT line traps, and PYQ shortcuts.

---

## Pillar 3: Visual Identity & The "Visual Physics" Aesthetic
1. **Zero Environmental Distraction Rule**:
   - Strictly prohibit realistic CGI clutter (no realistic cars with shiny paint, no streetlamps, no trees, no asphalt roads, no pedestrian models).
   - Objects are rendered as abstract illuminated masses, glowing particles, and laser vectors.
   - Reference videos provide **narration pacing and physical sequence only**; our engine enforces the visual aesthetic.
2. **Backdrop & Color Tokens**:
   - **Backdrop**: `#000000` / `#020408` (Pure Obsidian Void; saves mobile OLED battery and eliminates eye fatigue).
   - **Velocity / Primary Flow**: `#38BDF8` (Sky Cyan)
   - **Acceleration / PYQ Badges**: `#F59E0B` (Amber Gold)
   - **Forces / Gravity**: `#F43F5E` (Crimson Coral)
   - **Energy / Chemistry / Biology**: `#10B981` (Mint Emerald)
   - **Reference Coordinate Grids**: `#1E293B` (Ultra-faint Slate 800)
3. **The 5 Standardized Storyboard UI Archetypes**:
   - `KINETIC_STAGE`: 3D Spatial Motion, Parabolic Arcs, Glowing Vectors, Live Telemetry HUD.
   - `ORTHOGONAL_SPLIT`: 50/50 Dual Pane (Physical Simulation Left + Synchronized Phase Graph Right).
   - `MOLECULAR_REACTOR`: Microscopic Chamber, Membrane Boundaries, Bioluminescent Particles.
   - `FORMULA_DECONSTRUCTION`: Hero Equation Card, Annotated Callout Brackets, Amber NEET Trap Banner.
   - `NEURAL_CONSTELLATION`: Holographic Chapter GPS Constellation (Act 1 Opening & Act 5 Finale).

---

## Pillar 4: Pluggable Multi-Provider Audio Narration
1. **Engine Flexibility**:
   - Narration is decoupled through `audio/adapters/base_adapter.py`.
   - Supported engines:
     - `edge_tts`: 100% Free public Microsoft Neural voices (Zero API keys needed).
     - `google`: Google Cloud Text-to-Speech (Neural2 / WaveNet - 1M free chars/month).
     - `elevenlabs`: ElevenLabs Multilingual v2 (Studio cinematic quality for Macro Movies).
2. **Voice Standards**:
   - **Tamil (`ta-IN`)**: `ta-IN-ValluvarNeural` (Male) / `ta-IN-PallaviNeural` (Female).
   - **Indian English (`en-IN`)**: `en-IN-NeerjaExpressiveNeural` (Female) / `en-IN-PrabhatNeural` (Male).
3. **Granular Control**:
   - Audio provider and voice can be set globally (`config.py`), by chapter (`taxonomy_master.csv`), or per individual video row (`curriculum_master_full_665.csv`).
4. **MD5 Audio Caching**:
   - All audio files are cached by MD5 hash of `(provider, voice, language, text, rate, pitch)` in `audio/cache/`.
   - Re-rendering visual graphics never re-synthesizes or charges for audio.

---

## Pillar 5: Multilingual Pronunciation Shield
1. **Mandatory Pre-Processing**:
   - Every script is automatically passed through `tools/pronunciation_dictionary.json` before hitting any TTS engine.
2. **Acronym & Symbol Expansion**:
   - Acronyms like `NEET` must never spell out letters; in Tamil it converts to `நீட்`, in English to `Neet`.
   - Formulas ($v_y, H_{\max}, \theta$) expand into natural spoken phonetics ($v\text{ y}$, $H\text{ max}$, theta).
3. **Continuous Expansion**:
   - New mispronunciations discovered during review are added on-the-go to the dictionary JSON.

---

## Pillar 6: Minimalist 1080p Thumbnails
1. **Format & Contrast**:
   - Standard 16:9 (`1920x1080`) high-contrast cards optimized for mobile feed readability.
2. **Mandatory Visual Elements**:
   - Top-Left: Subject & Grade Pill (e.g. `PHYSICS • CLASS 11`).
   - Top-Right: Order Tracking Pill `[ Chapter Seq / Total ]` + Canonical ID.
   - Center Hero Card: Glowing rounded rectangle displaying the primary equation or key principle.
   - Bottom-Left: Bold Title and Chapter/Topic breadcrumb.
   - Bottom-Right: Vector star polygon Gold Badge (`★ HIGH YIELD | PYQ: 2017, 2024`).
3. **Automated Linking**:
   - Every video's thumbnail is saved to `output/thumbnails/<canonical_id>_thumbnail.png` and linked in `curriculum_master_full_665.csv`.

---

## Pillar 7: Reference Ingestion & Common Pool
1. **Curriculum Tagging**:
   - External reference videos are tagged to Canonical Concept IDs (`by_concept/`), Chapter IDs (`by_chapter/`), or Macro Movies (`macro_stories/`).
2. **The Common Pool Holding Zone**:
   - General, unmatched, or future-syllabus videos are held in `media/references/common_pool/` with semantic keywords.
   - When new syllabus units are introduced, `tools/tag_references.py --refresh-pool` automatically migrates them into the active curriculum.

---

## Pillar 8: Broadcast Safe-Zone & Zero-Clipping Guarantee
1. **Mandatory 90% Screen Safe Zone**:
   - In 16:9 Manim camera ($16 \times 9$ units, origin $(0,0)$, bounding box $[-7.11, +7.11] \times [-4.0, +4.0]$), all visual elements (axes, labels, headers, formula cards, and trap warnings) must reside strictly within:
     - Horizontal bounds: $x \in [-6.2, +6.2]$
     - Vertical bounds: $y \in [-3.5, +3.5]$
   - A minimum margin of $0.9$ Manim units must be maintained from all 4 display edges at all times.
2. **Strict Text Wrapping & Auto-Fit Rule**:
   - **No Un-wrapped Long Strings**: Any text string exceeding 35 characters must be auto-wrapped using `textwrap.fill(text, width=N)` where $N \le 55$.
   - **Auto-Scale Constraint**: If any text or mobject group width exceeds $11.5$ units, it must automatically scale down via `mobject.scale_to_fit_width(max_width)`.
   - **No Horizontal Overflow in Cards**: Cards containing body paragraphs (such as NEET Trap warnings) must stack the title above the body text (`arrange(DOWN)`), never single-line horizontally (`arrange(RIGHT)`).
3. **Axis & Graph Safe Positioning**:
   - Coordinate axes must be shifted inward with `to_corner(DL, buff=1.2).shift(RIGHT * 0.8 + UP * 0.2)` to ensure origin and tick labels never clip the bottom-left corner.
   - Vertical axis labels ($y$-axis) must be positioned directly at the top arrow (`next_to(axes.y_axis.get_top(), UP)`), completely eliminating left edge truncation.
4. **Header Collision Prevention**:
   - The Canonical ID badge must display only the clean canonical ID (e.g. `P11-C02-T03-V02`). Language suffixes or internal tags must never be rendered on the student-facing header badge.
   - Concept titles in the header must be constrained to available width between sequence pill and PYQ badge, auto-scaling if they exceed safe bounds.

---

## Pillar 9: Selective 2D / 3D Dimensional Engine Routing
1. **Tri-Level Dimension Resolution**:
   - **CLI Override**: `--dimension {auto, 2d, 3d}`. When specified, overrides curriculum defaults.
   - **Curriculum Metadata**: Read from `queue/curriculum_master_full_665.csv` column `dimension` (`2d` or `3d`).
   - **Template Registry**: Defined in `render/templates/registry.yaml` per template name.
2. **First-Class 3D Engine (`NEETVideoScene3D`)**:
   - Spatially complex concepts (e.g. 3D Projectile Trajectory, Lorentz Force, Dipole Fields, Molecular Geometries) can be rendered in 3D.
   - Uses `ThreeDScene` with dynamic camera orientation (`phi`, `theta`) and camera sweep paths.
   - **HUD Layering**: All textual UI cards (Canonical Badge, Sequence Pill, 3D Badge, Formula Cards, NEET Trap Warning, Revision Capsule) MUST be pinned flat to the screen using `add_fixed_in_frame_mobjects` to prevent spatial distortion.
3. **Visual Cache Isolation**:
   - Visual hash incorporates `dimension` (`2d` vs `3d`).
   - 2D raw renders (`<id>_raw.mp4`) and 3D raw renders (`<id>_3d_raw.mp4`) are stored and cached independently with zero cross-contamination.

---

## Pillar 10: Explicit NEET Trap Solution & Layman Clarity Rule
1. **The Trap Must Deliver the Solution**:
   - Merely alerting the student about an exam trap is prohibited. The video MUST explicitly display the **transformed formula answer** on screen.
   - Example (Projectile Angle from Vertical):
     - Standard Horizontal Launch: $H_{\max} = \frac{v_0^2 \sin^2\theta}{2g}$
     - Vertical Trap Answer: $\mathbf{H_{\max} = \frac{v_0^2 \cos^2\theta}{2g}}$
2. **Layman Physical Intuition**:
   - The root cause must be explained in everyday terms: *"Height depends strictly on vertical velocity component $v_y$. Since $\theta$ with the vertical makes $v_y = v_0 \cos\theta$, the formula directly replaces $\sin^2\theta$ with $\cos^2\theta$."*
   - Any student, parent, or layman watching must experience an immediate "Aha!" moment.
3. **Dual Formula Revision in Beat 5**:
   - The 15-second Exam Revision Capsule must summarize both standard and trap equations side-by-side or stacked cleanly within safe boundaries.

---

## Pillar 11: The "Learn → Play → Solve" Product Triad & In-Browser Video Export
1. **The Unified Pedagogical Triad**:
   - Every curriculum concept is delivered as a 3-tab learning unit in the student software application:
     - **Tab 1: 🎬 LEARN**: 45–60s broadcast concept video (`.mp4`) delivering the mental model and trap exposure.
     - **Tab 2: 🧪 PLAY**: Pure HTML5/Canvas interactive lab (`.html`) with live formula decomposition and draggable sliders.
     - **Tab 3: 📝 SOLVE**: 5 high-yield NEET practice questions directly testing the formula relationships.
2. **In-Engine Dynamic Telemetry Ticking**:
   - In broadcast videos, numerical readouts ($v_y, y(t)$) must tick dynamically in lockstep with the physics trajectory via `ValueTracker` to deliver authentic simulation realism.
3. **Client-Side 60 FPS Video Exporter**:
   - Interactive simulation labs (`.html`) must incorporate native `canvas.captureStream(60)` and `MediaRecorder` export buttons, allowing educators and students to download broadcast-grade WebM/MP4 simulation clips directly from any browser without installing software.




---

## Pillar 12: Pre-Flight Gatekeeper & Primary PDF Verification Protocol
1. **Mandatory Pre-Flight Sign-Off (Zero Blind Renders)**:
   - Before any chapter video compilation is permitted, the Pre-Flight Gatekeeper (`pipeline/preflight_gatekeeper.py`) must generate 4-beat static proof frames (`beat_1` to `beat_4`) for every concept drill in the chapter.
   - Batch rendering engines (`render_unit1_batch.py`, `render_concept_video.py`) enforce a hard lock: if any concept is missing `"APPROVED"` in `queue/approval_manifest.json`, compilation throws `PermissionError` and immediately halts.
2. **Primary PDF Fact-Checking (NCERT & NTA PYQ)**:
   - Never rely on unverified or synthesized syllabus claims.
   - Every formula, citation, and PYQ tag must be cross-verified directly against primary PDF sources:
     - Official NCERT Textbook PDFs (`PHYSICS-1-11-NCERT.pdf`, etc.)
     - Official NTA NEET Exam Question Paper PDFs (`C:\Users\DELL\OneDrive\Desktop\NEET\*.pdf`)
   - Unverified placeholder tags must be corrected or explicitly validated against the question papers before approving the storyboard.
3. **The Three-Tier Typography System & Glyph Safety Protocol**:
   - Typography across all scenes follows a strict 3-tier harmony:
     - **Tier 1: Main Headers**: **`Verdana Bold`** for scene and topic titles.
     - **Tier 2: Card & HUD Headers**: **`Cascadia Mono Bold`** for container card titles, taxonomy banners, and HUD labels.
     - **Tier 3: Body & Formula Text**: **`Consolas`** for bullet points, explanations, formulas, numbers, and derivations (monospaced fixed width eliminates kerning gaps permanently).
   - For exponents and subscripts, standard font mobjects with sub-mobject positioning must be used. Never use obscure Unicode glyphs (such as Canadian Aboriginal Syllabics `U+146B`) which render as missing-glyph hex boxes in Pango.
4. **Interactive Markdown Storyboards with Proof Carousels**:
   - The Pre-Flight Gatekeeper compiles all proof screenshots into an interactive Markdown storyboard (`<unit>_preflight_storyboard.md`) with slide carousels for Beats 1–4, formula cards, and NCERT/PYQ audit logs.


---

## Pillar 13: Dynamic Audio-Visual Synchronization & Mobile-First Pedagogy
1. **Dynamic Beat Pacing (Zero Hardcoded Wait Timers)**:
   - Hardcoded wait timers (e.g. `self.wait(10)`) are strictly forbidden in Manim scenes.
   - Every visual beat dynamically synchronizes with discrete TTS narration tracks:
     $$\text{Slide Hold Time} = \text{Audio Beat Duration} - \text{FadeIn (0.8s)} + \text{Inter-beat Buffer (0.5s)}$$
   - Eliminates desynchronization where slide visuals transition before narration completes.
2. **NEET Trap Memory Consolidation Hold (3.0-Second Silent Freeze)**:
   - Beat 4 (NEET Trap Card) must enforce a mandatory **3.0-second silent hold** after narration concludes before any transition.
   - Gives mobile students dedicated screen time to absorb the trap logic, copy formulas, and reflect without distraction.
3. **Mobile-First Typography Scale & Ban on Vector Compression**:
   - Zero horizontal font squeezing: `scale_to_fit_width()` is banned on text mobjects; aspect ratio must remain 1:1.
   - Text wrapping strictly capped at $\le 55$ characters per line.
   - Minimum font floor of $\ge 10.5\text{pt}$ (Consolas/Cascadia Mono) ensures perfect clarity on 5.5"–6.5" Android smartphones.

4. **Per-Language Dynamic Visual Alignment (Zero Multilingual Desync)**:
   - Speaking velocity and syllable structures differ widely between English, Hindi, and Tamil. A slide that takes 25 seconds to explain in English may require 32 seconds in Tamil.
   - The engine strictly prohibits reusing an English visual video with other language audio overlays.
   - Every language video (`en-IN`, `hi-IN`, `ta-IN`) must independently synthesize beat-level audio, compute beat hold durations, and compile a dedicated Manim visual render to ensure 100% audio-visual synchronization across all languages.

5. **Mandatory 3-Phase Closing Sequence (Punchline, 3.0s Freeze, and End Card)**:
   - In all languages (`en-IN`, `hi-IN`, `ta-IN`), Beat 4 must conclude with the explicit closing formula:
     - English: *"Master this to secure full marks in NEET Physics."*
     - Hindi: *"नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।"*
     - Tamil: *"நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்."*
   - Followed by:
     - Exactly **3.0 seconds of audio silence** while holding the NEET Trap card on screen.
     - A 3.5-second **Beat 5 Next Video Title End Card** ("UP NEXT IN SEQUENCE: Concept (N+1)/Total: [Title]").
   - **Mux Truncation Guardrail**: FFmpeg muxing commands must never truncate via `-shortest` against subtitle streams.
