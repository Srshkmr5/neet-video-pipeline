import json
from pathlib import Path

from validators.text_validator import validate_concept_file


class PipelineOrchestrator:
    def __init__(self, concept_path):
        self.concept_path = Path(concept_path)

    def run(self):
        concept = validate_concept_file(self.concept_path)
        out_dir = Path("proof/output")
        out_dir.mkdir(parents=True, exist_ok=True)

        render_meta = {
            "concept_id": concept["concept_id"],
            "topic_name": concept["topic_name"],
            "status": "validated",
            "language": concept["language"],
            "duration_seconds": concept["duration_seconds"],
        }

        output_path = out_dir / f"{concept['concept_id']}_proof.json"
        output_path.write_text(json.dumps(render_meta, indent=2), encoding="utf-8")
        return output_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the proof generation pipeline for one concept.")
    parser.add_argument("--concept", required=True, help="Path to a concept JSON file")
    args = parser.parse_args()

    orchestrator = PipelineOrchestrator(args.concept)
    result = orchestrator.run()
    print(f"validated and exported: {result}")
