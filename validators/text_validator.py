import json
from pathlib import Path


class ValidationError(Exception):
    """Raised when concept content fails validation."""


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_schema(concept):
    required = [
        "concept_id",
        "topic_name",
        "headline",
        "formula",
        "bullets",
        "trap",
        "language",
        "duration_seconds",
    ]
    missing = [key for key in required if key not in concept]
    if missing:
        raise ValidationError(f"Missing required keys: {missing}")

    if not concept["headline"] or len(concept["headline"]) > 80:
        raise ValidationError("headline length invalid")

    if not concept["formula"] or len(concept["formula"]) > 120:
        raise ValidationError("formula length invalid")

    if len(concept["bullets"]) < 1 or len(concept["bullets"]) > 4:
        raise ValidationError("bullets count invalid")

    for bullet in concept["bullets"]:
        if len(bullet) > 60:
            raise ValidationError(f"bullet too long: {bullet}")

    if len(concept["trap"]) > 120:
        raise ValidationError("trap text too long")

    if concept["language"] not in {"en", "hi", "bn"}:
        raise ValidationError("unsupported language")

    if not 5 <= float(concept["duration_seconds"]) <= 60:
        raise ValidationError("duration_seconds outside valid range")


def validate_text_geometry(concept):
    max_line_length = 32
    for section_name in ["headline", "formula", "trap"]:
        text = concept.get(section_name, "")
        if len(text) > max_line_length:
            raise ValidationError(f"{section_name} exceeds max line length of {max_line_length}")

    for bullet in concept.get("bullets", []):
        if len(bullet) > max_line_length:
            raise ValidationError(f"bullet exceeds max line length of {max_line_length}: {bullet}")


def validate_concept_file(path):
    concept = load_json(path)
    validate_schema(concept)
    validate_text_geometry(concept)
    return concept


if __name__ == "__main__":
    sample_path = Path("data/concepts/sample_concept.json")
    concept = validate_concept_file(sample_path)
    print(f"Validated concept: {concept['concept_id']}")
