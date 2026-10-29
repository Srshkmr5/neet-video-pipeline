from validators.text_validator import validate_concept_file


def test_sample_concept_is_valid():
    concept = validate_concept_file("data/concepts/sample_concept.json")
    assert concept["concept_id"] == "sample_concept_01"
    assert len(concept["bullets"]) >= 1


if __name__ == "__main__":
    test_sample_concept_is_valid()
    print("sample concept validation passed")
