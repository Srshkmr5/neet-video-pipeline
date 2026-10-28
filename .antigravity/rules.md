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

15. **Lossless Audio End-Padding (`apad`) for Zero Player Stalling**:
    - When packaging multi-lingual MP4s and AES-128 HLS streams, browser HTML5 `<video>` and Video.js decoders stall and pause playback if the audio track terminates even milliseconds before the visual stream, freezing the player before Beat 5 end cards finish.
    - **Enforcement**: Every packaging workflow must losslessly pad audio via FFmpeg `-af "apad"` with `-c:v copy -shortest` so that audio duration is guaranteed to equal or slightly exceed the video stream.

16. **Dynamic Native WebVTT Subtitle Pipeline & CC State**:
    - Every concept render in all languages (`en-IN`, `hi-IN`, `ta-IN`) must produce synchronized WebVTT (`.vtt`) files.
    - Triad EdApp Player must dynamically update native `<track kind="subtitles">` elements on concept selection, featuring high-contrast backdrop styling and an interactive CC toggle button (`CC ON / CC OFF`).

17. **Simulation Deep-Link Architecture & Lexical Initialization Order (TDZ Guard)**:
    - In interactive simulation hubs (e.g., `unit_02_kinematics_lab.html`, `unit_03_laws_of_motion_lab.html`), deep-link URL parsing and initial mode/concept dispatch (`applyConceptOrMode()`) MUST be located at the very bottom of the `<script>` tag.
    - Strictly prohibit executing preset switchers before DOM canvases (`gCanvas`, `vCanvas`, `pCanvas`, `cCanvas`) and physics engine functions are declared, eliminating fatal ES6 `ReferenceError` (Temporal Dead Zone) crashes on direct links.

18. **Iframe Visibility & Tab-Switch Dynamic Resizing (`ResizeObserver` & `postMessage`)**:
    - Simulation hubs embedded inside multi-tab interfaces (where tabs use `display: none` / `.hidden`) evaluate `getBoundingClientRect()` to $0 \times 0$ when initialized in the background.
    - **Enforcement**:
      1. Every simulation canvas must observe its parent container wrapper with a `ResizeObserver`, triggering an immediate redraw as soon as container dimensions become $> 0$.
      2. The parent player's tab switcher (`switchTab('lab')`) must dispatch `postMessage({ type: 'REDRAW_SIMULATION', concept: currentConcept.canonical_id })` to child iframes to guarantee instant, crisp rendering without black/blank canvases.

19. **Pure UTF-8 Encoding & Mathematical Notation Purity (Zero Mojibake)**:
    - Web simulations and UI components must maintain pure UTF-8 encoding. Double-encoded characters (e.g. `Â°`, `vâ‚€Â²`, `ðŸŽ¯`) are strictly prohibited.
    - Use standard HTML entities (`&deg;`, `&theta;`, `&mu;`, `&Delta;`, `&omega;`) or KaTeX notation for physics terms. Interactive labs must omit non-functional video export buttons or redundant controls that clutter mobile viewports.

20. **Unit 3 (Laws of Motion) Simulation Hub Architecture**:
    - Unit 3's interactive hub (`simulations/unit_03_laws_of_motion_lab.html`) will adopt the unified 4-engine architecture with direct deep-links for all concepts:
      * **Engine 1**: Newton's Laws & Free-Body Diagrams (FBDs) with resolved orthogonal forces ($N$, $mg$, tension $T$, applied force $F$).
      * **Engine 2**: Friction Lab (Static friction limit $f_s \le \mu_s N$, kinetic friction $f_k = \mu_k N$, Angle of Repose $\tan\theta = \mu_s$, block on variable incline).
      * **Engine 3**: Connected Bodies & Pulley Systems (Atwood machine, 2-body horizontal/inclined plane with string tension and acceleration $a$).
      * **Engine 4**: Circular Dynamics & Banking of Roads (Unbanked vs. Banked curve, optimum velocity $v_0 = \sqrt{rg \tan\theta}$, maximum safe speed with friction $v_{\max} = \sqrt{\frac{rg(\tan\theta + \mu)}{1 - \mu\tan\theta}}$).

21. **Interactive Physics Simulation Fidelity & Live Visual Parameter Coupling (Zero Decorative/Static Controls)**:
    - **Live Geometric & Vector Coupling**: Every slider, toggle, or numerical input in an interactive simulation MUST trigger an immediate, mathematically proportional visual transformation on the canvas. Prohibit "decorative" or static placeholder diagrams where controls merely update text readouts.
    - **Mass & Geometry Scaling**: All mass changes ($m, m_1, m_2$) must visibly scale mobject geometry ($W, H \propto \sqrt{m}$) and corresponding vector arrows (weight $W = mg$, normal reaction $N$, string tension $T$).
    - **Angle & Kinematic Transformation**: Changing tilt or launch angles ($\theta$) must physically rotate the drawn surface (inclined plane, banked road wedge, pull vectors) in exact degrees. Changing friction coefficients ($\mu_s, \mu_k$) must visibly alter physical states (e.g. static stick vs sliding downhill with acceleration trails when $\theta > \theta_R = \arctan\mu_s$; common motion vs relative slipping between stacked blocks).
    - **Mathematical Coupling & Formula Audit (Zero Parameter Cancellation)**: Ensure formulas do not mathematically cancel out slider variables (e.g., computing spring compression as $N_{\text{app}}/W$ cancels mass $m$; it must be computed as $N_{\text{app}} / k$ so greater mass compresses springs deeper). Every slider input in the DOM must be read and used directly inside the canvas drawing function.
    - **Bespoke Concept Renderers**: Every sub-concept mode (e.g. FBD vs Elevator vs Atwood; Impulse F-t vs Rocket Thrust vs Lami; Level Skidding vs Banked Road vs Vertical Loop) must execute its own dedicated, bespoke visual rendering routine. Sharing a generic or unresponsive canvas across distinct physical concepts is strictly prohibited.

22. **Pedagogical Simulation Layout & Dynamic Equilibrium Standard (The "Anti-Glitch" Rule)**:
    - **Mandatory Dual-Panel Separation (Physical Stage vs. Analytical Graphs)**:
      - Mathematical plots ($F\text{-}t$ impulse curves, $v\text{-}t$ kinematic plots, $P\text{-}V$ indicator diagrams, energy curves) must **NEVER** share an unbordered, ambiguous canvas space with physical objects (balls, cars, blocks). Non-expert students mistake abstract graphs for physical obstacles.
      - **Enforcement**: Simulations presenting both physical motion and analytical curves must enforce a split-panel layout:
        1. **Panel 1: Physical Experiment Stage**: Labeled stage with explicit physical boundaries (e.g., sensor wall on left, automated spring launcher on right). Physical objects must never reverse direction in empty mid-air without a visible physical rebounder or launcher.
        2. **Panel 2: Analytical Data Graph Panel**: Distinct, bordered dashboard panel with gridlines, labeled axes with units (e.g. $F(t)$ in N, $t$ in ms), and an explanatory subtitle clarifying that the curve is an abstract data plot recorded by sensors during the physical event.
      - **Live Synchronous Tracing**: Analytical curves must be dynamically synchronized with physical events. When a collision or cycle occurs, a glowing tracer dot and active curve pulse must trace in real time, visually linking the physical contact to the area under the curve.
    - **Dynamic Equilibrium Standard (Zero Static Freeze)**:
      - Physical systems in "static equilibrium" (e.g. Lami's concurrent forces $\Sigma \vec{F} = \vec{0}$, static friction grip, optimal banking speed) must **NEVER** appear as completely frozen, static graphics. Students assume a dead screen is a software crash.
      - **Enforcement**:
        1. **Ambient Suspension Float**: Systems suspended by cords, springs, or normal forces must incorporate subtle ambient harmonic breathing ($1\text{–}2\text{px}$) to demonstrate live tension.
        2. **Restoring Perturbation Physics**: Dragging sliders or clicking dedicated "Perturb / Nudge" action buttons must visibly displace the system off-center and animate damped restoring forces returning it to equilibrium, visually demonstrating *stable equilibrium*.
        3. **Active Motion Cues**: Vehicles traveling at constant or optimal velocity must display streaming road markings, rotating wheel spokes, or trail particles to clearly convey motion.
    - **Conservation of Energy & Kinetic Continuity**:
      - Kinetic loops must obey energy conservation: objects speeding up when descending and slowing down when climbing ($v = \sqrt{v_0^2 \pm 2gh}$).
      - Motion must never damp to zero and permanently lock at a clamp boundary; systems must smoothly oscillate or cycle continuously so user slider adjustments remain immediately visible.

23. **Strict Audio-Visual Semantic Synchronization & Spoken Formula On-Screen Presence**:
    - **Spoken Formula On-Screen Rule**: Every mathematical formula, equation, variable relation, or quantitative law spoken in the audio narration track MUST be simultaneously visible on the screen during that exact visual beat. Spoken audio must never reference, explain, or derive an equation while the visual slide displays unrelated or preceding content.
    - **Beat-by-Beat Semantic Alignment**:
      * **Beat 1 (NCERT Evergreen Intro)**: Spoken audio introduces the canonical topic and chapter sequence; visual slide displays the exact topic name, NCERT chapter/section citation, and canonical ID.
      * **Beat 2 (Hero Stage & Core Physical Law)**: Spoken audio introduces the primary physical law and fundamental equation; visual slide MUST display that exact primary formula prominently in the central formula box alongside the physical diagram and core principles.
      * **Beat 3 (Analytical Deep-Dive & Derivation)**: Spoken audio derives or analyzes specific cases (e.g. angle pull $N = mg - F\sin\theta$, elevator pseudo force $N = m(g \pm a)$, Atwood machine equations, rocket thrust $u(dm/dt)$, piecewise friction graph, two-block threshold $a_{\max} = \mu_s g$, banking/loop threshold); visual slide MUST display the exact derivations, case equations, and limiting cases being spoken.
      * **Beat 4 (NEET Trap Card & NCERT Rule)**: Spoken audio warns of the fatal trap and states the NCERT correction rule; visual card MUST display the fatal trap callout and the NCERT rule equation in the green resolution box (with zero hardcoded PYQ exam years).
      * **Beat 5 (Consolidation Hold & Next Video End Card)**: Beat 4 holds for a mandatory 3.0-second silent freeze after narration concludes, transitioning cleanly to a 3.5-second Beat 5 Next Video End Card directing students to the subsequent concept and interactive simulation lab.


