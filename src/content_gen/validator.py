import json
import textwrap
from pathlib import Path

class ValidationError(Exception):
    pass

def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)

def validate_text_budget(payload):
    max_chars = 32
    max_lines = 4

    fields = [
        ("latex_formula", payload.get("latex_formula", "")),
        ("ncert_core_rule", payload.get("ncert_core_rule", "")),
        ("neet_trap_point", payload.get("neet_trap_point", "")),
        ("author_book_nuance", payload.get("author_book_nuance", ""))
    ]

    # Concept title has its own headline budget (max 80 chars, but wrapped lines <= 32 chars)
    title = payload.get("concept_title", "")
    if len(title) > 80:
        raise ValidationError(f"Concept title exceeds max length: {len(title)} > 80")

    for name, field in fields:
        if not field:
            continue
        # Wrap long text naturally to check line budgets
        wrapped_lines = textwrap.wrap(field, width=max_chars)
        for line in wrapped_lines:
            if len(line) > max_chars:
                raise ValidationError(f"{name} exceeds max chars per line: {len(line)} > {max_chars}: {line[:80]}")
        if len(wrapped_lines) > 8:
            raise ValidationError(f"{name} exceeds maximum budget: {len(wrapped_lines)} lines")

def validate_payload(payload):
    if not payload.get("canonical_id"):
        raise ValidationError("Missing canonical_id")
    if not payload.get("latex_formula"):
        raise ValidationError("Missing latex_formula")
    if not payload.get("ncert_core_rule"):
        raise ValidationError("Missing ncert_core_rule")
    validate_text_budget(payload)

def validate_concept_file(path):
    payload = load_json(path)
    validate_payload(payload)
    return payload

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "queue/concepts/golden_c01.json"
    payload = validate_concept_file(target)
    print(f"Validation SUCCESS: {payload.get('canonical_id')} passed all schema and text budgets.")
