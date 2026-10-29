# NEET Video Pipeline

An automated, curriculum-driven educational video synthesis pipeline translating NCERT/NEET/JEE syllabus specifications into synchronized 1080p60 2D animated videos (Manim Community Edition) and interactive browser simulation sandboxes.

## Architecture & Directory Structure

```text
neet-video-pipeline/
├── config/
│   ├── text_budget.json              # Strict line & character limits per visual card
│   └── branding.py                   # Canonical color palette and coordinate bounds
├── queue/
│   ├── curriculum/
│   │   └── physics/
│   │       └── unit_04_work_energy_power.csv   # Ground truth curriculum dataset
│   └── concepts/
│       └── golden_c01.json           # Validated single-concept JSON payload
├── schemas/
│   └── concept_payload.schema.json   # JSON schema for concept metadata
├── src/
│   ├── content_gen/
│   │   ├── __init__.py
│   │   └── validate_concept.py       # Pre-render text budget & schema validator
│   ├── render/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── base_scene.py         # Modular base scene contract
│   │   │   └── typography.py         # Proportional typography rules & auto-wrapping
│   │   └── units/
│   │       └── unit_04/
│   │           ├── __init__.py
│   │           ├── c01_dot_product.py     # Independent Manim scene for Concept 1
│   │           └── c02_variable_force.py   # Independent Manim scene for Concept 2
│   └── simulations/
│       ├── shell.html                # Responsive web simulation container
│       └── units/
│           └── unit_04/
│               └── v01_dot_product.js # Isolated micro-simulation JavaScript module
├── tools/
│   └── test_smoke_pipeline.js        # Automated smoke test suite
└── output/
    ├── proofs/                       # 1080p static proof frames
    └── final_videos/                 # Final assembled multi-language MP4s
```

## Key Principles & Guardrails

1. **Pre-Render Validation**: All concept payloads pass `validate_concept.py` before touching Manim.
2. **Proportional Typography Only**: `Arial` and `Segoe UI` are used exclusively; fixed-width `Consolas` is prohibited for dense prose.
3. **Zero Downscaling**: Text sizing is fixed at $\ge 13\text{pt}$ (up to $30\text{pt}$ for titles) without `scale_to_fit_width` compression.
4. **Decoupled Architecture**: Each concept is isolated in its own rendering script and simulation micro-module, eliminating monolithic state corruption.

## Quickstart Commands

```powershell
# 1. Validate Golden Concept Payload
python src/content_gen/validate_concept.py queue/concepts/golden_c01.json

# 2. Render Concept 1 Static Proof
python -m manim -s -qm --disable_caching src/render/units/unit_04/c01_dot_product.py C01DotProductScene

# 3. Render Concept 2 Static Proof
python -m manim -s -qm --disable_caching src/render/units/unit_04/c02_variable_force.py C02VariableForceScene

# 4. Run Automated Smoke Test
node tools/test_smoke_pipeline.js
```
