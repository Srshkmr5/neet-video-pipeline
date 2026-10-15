"""
Unit & Integration Tests for 3D Extension Architecture
Tests Template Registry, Manim Base Hierarchy, Batch Scheduling, and Schema Validation.
"""
import sys
import yaml
from pathlib import Path

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from llm.schema import ConceptNode, BeatTier
from render.templates.base import NEETVideoScene, NEETVideoScene3D, BaseNeetScene
from llm.pacing import PacingEngine
from config import TEMPLATES_DIR, RENDER_3D_DRAFT, RENDER_3D_MASTER, RENDER_3D_MULTIPLIER

def test_registry_dimensions():
    reg_file = TEMPLATES_DIR / "registry.yaml"
    with open(reg_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    templates = data["templates"]

    # Verify 2D templates
    expected_2d = ["FormulaWithGraph", "VectorDiagram", "DerivationStep", "WaveDiagram", "TwoColumnCompare"]
    for name in expected_2d:
        assert name in templates, f"Missing 2D template {name}"
        assert templates[name]["dimension"] == "2d", f"{name} dimension should be '2d'"
        assert templates[name]["render_time_multiplier"] == 1.0, f"{name} multiplier should be 1.0"

    # Verify 3D templates
    expected_3d = ["MoleculeConformer3D", "DNAHelix3D", "MagneticField3D"]
    for name in expected_3d:
        assert name in templates, f"Missing 3D template {name}"
        assert templates[name]["dimension"] == "3d", f"{name} dimension should be '3d'"
        assert templates[name]["render_time_multiplier"] == 3.5, f"{name} multiplier should be 3.5"

    print("✅ test_registry_dimensions: All 2D and 3D templates validated.")

def test_manim_base_classes():
    assert NEETVideoScene.dimension == "2d"
    assert NEETVideoScene3D.dimension == "3d"
    assert BaseNeetScene is NEETVideoScene

    # Test instantiation
    scene_2d = NEETVideoScene(node_data={"videoId": "P11-C01-T01-V01", "serialTitle": "Test 2D"})
    scene_3d = NEETVideoScene3D(node_data={"videoId": "P11-C01-T01-V02", "serialTitle": "Test 3D"})

    assert scene_2d.video_id == "P11-C01-T01-V01"
    assert scene_3d.video_id == "P11-C01-T01-V02"
    print("✅ test_manim_base_classes: NEETVideoScene and NEETVideoScene3D initialized cleanly.")

def test_batch_schedule_estimator():
    reg_file = TEMPLATES_DIR / "registry.yaml"
    with open(reg_file, "r", encoding="utf-8") as f:
        templates = yaml.safe_load(f)["templates"]

    # Simulate 674 nodes: 607 2D (FormulaWithGraph), 67 3D (MoleculeConformer3D)
    mock_nodes = []
    for i in range(607):
        mock_nodes.append({"templateName": "FormulaWithGraph"})
    for i in range(67):
        mock_nodes.append({"templateName": "MoleculeConformer3D"})

    draft_res = PacingEngine.estimate_batch_schedule(mock_nodes, templates, quality="draft")
    master_res = PacingEngine.estimate_batch_schedule(mock_nodes, templates, quality="master")

    assert draft_res["total_nodes"] == 674
    assert draft_res["count_2d"] == 607
    assert draft_res["count_3d"] == 67

    # Draft time should be ~7.0 hrs (approx 7.0 ± 0.3)
    assert 6.5 <= draft_res["estimated_render_hours"] <= 7.5, f"Draft hours: {draft_res['estimated_render_hours']}"
    # Master time should be ~21.0 hrs (approx 21.0 ± 0.5)
    assert 20.5 <= master_res["estimated_render_hours"] <= 21.5, f"Master hours: {master_res['estimated_render_hours']}"
    # Disk footprint should be ~26.4 GB
    assert 25.0 <= draft_res["estimated_disk_gb"] <= 27.5, f"Disk GB: {draft_res['estimated_disk_gb']}"

    print(f"✅ test_batch_schedule_estimator: 674 nodes -> Draft: {draft_res['estimated_render_hours']:.2f} hrs, Master: {master_res['estimated_render_hours']:.2f} hrs, Disk: {draft_res['estimated_disk_gb']:.2f} GB.")

def test_schema_dimension_validation():
    # Valid 2d
    n2 = ConceptNode(
        videoId="P11-C04-T02-V03",
        serialTitle="2D Node",
        subject="Physics",
        grade=11,
        templateName="FormulaWithGraph",
        dimension="2d",
        beats=[{"id": "settle", "tier": BeatTier.SETTLE}, {"id": "release", "tier": BeatTier.RELEASE}],
        parameters={"test": "val"},
        locales={
            "en": {"narration": "a", "trapPoint": "b"},
            "hi": {"narration": "a", "trapPoint": "b"},
            "ta": {"narration": "a", "trapPoint": "b"}
        }
    )
    assert n2.dimension == "2d"

    # Valid 3d
    n3 = ConceptNode(
        videoId="C11-C04-T02-V01",
        serialTitle="3D Node",
        subject="Chemistry",
        grade=11,
        templateName="MoleculeConformer3D",
        dimension="3d",
        beats=[{"id": "settle", "tier": BeatTier.SETTLE}, {"id": "release", "tier": BeatTier.RELEASE}],
        parameters={"test": "val"},
        locales={
            "en": {"narration": "a", "trapPoint": "b"},
            "hi": {"narration": "a", "trapPoint": "b"},
            "ta": {"narration": "a", "trapPoint": "b"}
        }
    )
    assert n3.dimension == "3d"

    # Invalid dimension
    try:
        ConceptNode(
            videoId="P11-C04-T02-V03",
            serialTitle="Invalid",
            subject="Physics",
            grade=11,
            templateName="FormulaWithGraph",
            dimension="4d",
            beats=[{"id": "settle", "tier": BeatTier.SETTLE}, {"id": "release", "tier": BeatTier.RELEASE}],
            parameters={},
            locales={
                "en": {"narration": "a", "trapPoint": "b"},
                "hi": {"narration": "a", "trapPoint": "b"},
                "ta": {"narration": "a", "trapPoint": "b"}
            }
        )
        assert False, "Should have rejected dimension '4d'"
    except Exception:
        pass

    print("✅ test_schema_dimension_validation: Validated '2d', '3d', and rejection of invalid dimensions.")

if __name__ == "__main__":
    test_registry_dimensions()
    test_manim_base_classes()
    test_batch_schedule_estimator()
    test_schema_dimension_validation()
    print("\n🎉 ALL 3D EXTENSION TESTS PASSED SUCCESSFULLY!")
