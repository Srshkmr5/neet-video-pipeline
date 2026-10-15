# Manim Healer Subagent Contract

## Purpose
Specialized healer for Manim scene generation and compilation failures (e.g. LaTeX compile errors, out-of-bound ranges, numerical singularities).

## Contract
- **Input**:
  ```json
  {
    "videoId": "P11-C04-T02-V03",
    "template_name": "FormulaWithGraph",
    "stderr": "Latex error / Python traceback...",
    "parameters": { ... }
  }
  ```
- **Output**:
  ```json
  {
    "patched_parameters": { ... } | null,
    "reason": "Corrected escaped LaTeX characters in formula string"
  }
  ```

## Boundaries & Constraints
- **Forbidden**: Editing template Python files.
- **Allowed**: Patching parameter dictionary (e.g. formula strings, axis ranges, colors).
- **Retry budget**: Exactly 1 retry per video before flagging as failed in state.json.
