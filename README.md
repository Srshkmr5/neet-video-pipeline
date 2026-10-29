# NEET Video Pipeline

A clean, modular pipeline for generating educational STEM video content through structured schema validation, layout-safe rendering, and proof-based QA.

## Goal

Build a reliable system that converts curriculum concepts into storyboard-ready educational content, validates constraints before rendering, and scales from one concept to hundreds of videos.

## Architecture

The project follows a micro-stage pipeline:

1. Curriculum ingestion
2. Content generation to strict JSON
3. Schema & layout validation
4. Layout-safe scene render
5. Proof generation
6. QA / smoke checks
7. Voiceover and final assembly

## Key principles

- LLM generates content, not layout decisions.
- Rendering engine enforces geometry and typography constraints.
- Text is validated before render.
- Proof images are required before full video output.
- One concept must be stable before scaling to many videos.

## Project structure

- `data/` - curriculum and generated concept data
- `schema/` - strict content schemas
- `validators/` - validation logic
- `render/` - scene and layout code
- `pipeline/` - orchestration and batch logic
- `tests/` - smoke and validation tests
- `proof/` - render output and QA artifacts

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python pipeline/orchestrator.py --concept data/concepts/sample_concept.json
```

## Current milestone

This repository is intentionally scaffolded as a clean baseline. The first milestone is:

- one concept in strict JSON
- validation before render
- one proof frame rendered successfully
- no auto-shrinking text
- no hidden layout overflow

## Next steps

1. Add curriculum inputs for one subject concept.
2. Extend the validator for formula and typography checks.
3. Build one working scene archetype.
4. Add proof generation and smoke QA.
5. Add TTS/audio only after the proof render is stable.

## Notes

This repository is intentionally designed to avoid the monolithic anti-pattern of mixing prompt logic, layout, and rendering in a single file.
