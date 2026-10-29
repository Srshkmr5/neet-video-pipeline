import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "canonical_id",
    "chapter_name",
    "concept_title",
    "template_name",
    "dimension",
    "latex_formula",
    "plain_formula",
    "ncert_citation",
    "ncert_core_rule",
    "author_book_nuance",
    "neet_trap_point",
    "pyq_years",
    "status",
    "audio_provider",
    "voice_id",
]

MAX_CHARS_PER_LINE = 32
MAX_LINES_PER_FIELD = 4
MIN_FONT_SIZE_PT = 16

def fail(msg):
    raise ValueError(msg)

def validate_field(name, value):
    if value is None:
        fail(f"Missing field: {name}")
    if not isinstance(value, str):
        fail(f"Field {name} must be a string")
    if len(value.strip()) == 0:
        fail(f"Field {name} is empty")

    lines = value.splitlines()
    for line in lines:
        if len(line.strip()) > MAX_CHARS_PER_LINE:
            fail(f"Field {name} exceeds max chars per line: {len(line.strip())} > {MAX_CHARS_PER_LINE}")
    if len(lines) > MAX_LINES_PER_FIELD:
        fail(f"Field {name} exceeds max lines: {len(lines)} > {MAX_LINES_PER_FIELD}")

def validate_payload(payload):
    for field in REQUIRED_FIELDS:
        if field not in payload:
            fail(f"Missing required field: {field}")
        validate_field(field, payload[field])

    if payload["dimension"] not in ["2d", "3d"]:
        fail("dimension must be '2d' or '3d'")

    if payload["status"] not in ["APPROVED", "DRAFT"]:
        fail("status must be APPROVED or DRAFT")

    if "W" not in payload["plain_formula"] and "work" not in payload["concept_title"].lower():
        pass

    if payload.get("latex_formula", "").__contains__("Consolas"):
        fail("Formula must not contain forbidden font names")

    # render-safe constraints
    if len(payload["latex_formula"]) > 120:
        fail("latex_formula too long for render-safe card")

    if len(payload["ncert_core_rule"]) > 240:
        fail("ncert_core_rule too long")

    if len(payload["neet_trap_point"]) > 200:
        fail("neet_trap_point too long")

    if MIN_FONT_SIZE_PT < 16:
        fail("Font floor misconfigured")

def validate_file(path):
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    validate_payload(data)
    print(f"VALID: {path.name}")
    return data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_concept.py queue/concepts/golden_c01.json")
        sys.exit(1)

    try:
        validate_file(sys.argv[1])
    except Exception as e:
        print(f"INVALID: {e}")
        sys.exit(2)
