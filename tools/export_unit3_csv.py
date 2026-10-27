import json
import csv
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
manifest_path = BASE_DIR / "apps" / "curriculum_manifest.json"
csv_path = BASE_DIR / "queue" / "curriculum" / "physics" / "unit_03_laws_of_motion.csv"

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

u3_concepts = [c for c in manifest["concepts"] if c.get("canonical_id", "").startswith("P11-C03")]
total_u3 = len(u3_concepts)

ARCHETYPE_SCENE_MAP = {
    "P11-C03-T01-V01": "FirstLawFbdScene",
    "P11-C03-T01-V02": "SecondLawElevatorScene",
    "P11-C03-T01-V03": "ThirdLawAtwoodScene",
    "P11-C03-T02-V04": "ImpulseFtCurveScene",
    "P11-C03-T02-V05": "RocketMomentumScene",
    "P11-C03-T02-V06": "LamiTheoremScene",
    "P11-C03-T03-V07": "FrictionGraphScene",
    "P11-C03-T03-V08": "RoughInclineReposeScene",
    "P11-C03-T03-V09": "TwoBlockFrictionScene",
    "P11-C03-T04-V10": "LevelCurveSkiddingScene",
    "P11-C03-T04-V11": "BankedRoadVerticalCircleScene"
}

rows = []
for idx, c in enumerate(u3_concepts, 1):
    cid = c["canonical_id"]
    next_c = u3_concepts[idx] if idx < total_u3 else None
    next_id = next_c["canonical_id"] if next_c else "P11-C04-T01-V01"
    next_title = next_c["title"] if next_c else "Work-Energy Theorem & Scalar Product"

    row = {
        "canonical_id": cid,
        "parent_macro_movie_id": "P11-C03-MOVIE",
        "subject": c.get("subject", "Physics"),
        "grade": c.get("grade", 11),
        "chapter_no": c.get("chapter_no", 3),
        "chapter_name": c.get("chapter_name", "Laws of Motion"),
        "topic_no": c.get("topic_no", 1),
        "topic_name": c.get("topic_name", "Newton's Laws"),
        "video_no": c.get("video_no", 1),
        "concept_title": c.get("title", ""),
        "template_name": ARCHETYPE_SCENE_MAP.get(cid, "ModularUnit3Scene"),
        "dimension": "2D",
        "storyboard_ui_archetype": "CardBasedScene",
        "chapter_seq": idx,
        "total_chapter_videos": total_u3,
        "subject_seq": 22 + idx,  # Unit 1: 8, Unit 2: 14 -> Unit 3 starts at 23
        "total_subject_videos": 100,
        "global_seq": 22 + idx,
        "total_global_videos": 665,
        "next_video_id": next_id,
        "next_video_title": next_title,
        "latex_formula": c.get("latex_formula", ""),
        "plain_formula": c.get("plain_formula", ""),
        "ncert_citation": c.get("ncert_citation", "NCERT Class 11 Chapter 4"),
        "ncert_core_rule": c.get("ncert_core_rule", ""),
        "author_book_nuance": c.get("author_book_nuance", ""),
        "neet_trap_point": c.get("neet_trap_point", ""),
        "pyq_years": c.get("pyq_years", "NEET Core"),
        "status": "APPROVED",
        "audio_provider": "edge_tts",
        "voice_id": "en-IN-NeerjaExpressiveNeural",
        "thumbnail_path": f"output/unit_03_laws_of_motion/{cid}_thumb.png",
        "reference_media_path": "",
        "reference_role": "",
        "neet_2026_unit": "Unit 3: Laws of Motion",
        "chapter_core_topics": "Newton's Laws, Momentum, Friction, Circular Dynamics"
    }
    rows.append(row)

csv_path.parent.mkdir(parents=True, exist_ok=True)
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Successfully generated {csv_path} with {len(rows)} concepts!")
