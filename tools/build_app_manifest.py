"""
Curriculum & Media Manifest Builder for NEET EdApp
Merges queue/curriculum_master_full_665.csv with verified secure streams into apps/curriculum_manifest.json.
"""

import os
import sys
import csv
import json
from pathlib import Path
from typing import Dict, Any, List

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "queue" / "curriculum_master_full_665.csv"
SECURE_STREAMS_DIR = BASE_DIR / "output" / "secure_streams"
MANIFEST_OUTPUT_PATH = BASE_DIR / "apps" / "curriculum_manifest.json"

def build_trap_quiz(row: Dict[str, str]) -> Dict[str, Any]:
    """
    Builds a NEET Trap PYQ question object based on formula, trap point, and nuances.
    """
    canonical_id = row.get("canonical_id", "")
    title = row.get("concept_title", "Concept")
    trap_point = row.get("neet_trap_point", "")
    plain_formula = row.get("plain_formula", "")
    pyq_years = row.get("pyq_years", "Recent NEET")
    
    # Custom tailored quiz for flagship concept S.2.3.2 (P11-C02-T03-V02)
    if canonical_id == "P11-C02-T03-V02":
        return {
            "title": "Swapping Sine and Cosine (Angle with Vertical Axis)",
            "warning": "The textbook formula H_max = (v0² sin²θ)/(2g) is valid ONLY when θ is measured from the horizontal! If measured from vertical, vertical speed is v0 cos θ, turning sin²θ into cos²θ.",
            "pyq_year": "NEET 2024",
            "question": "A projectile is launched with velocity v₀ = 50 m/s at an angle of 30° with the VERTICAL. What is the maximum vertical height reached? (Take g = 10 m/s²)",
            "options": [
                {"id": 0, "text": "A) 31.25 m", "trap": "Trap: Applied sin²(30°) blindly instead of vertical component!"},
                {"id": 1, "text": "B) 93.75 m", "trap": "Correct: Uses cos²(30°) = 0.75 for vertical motion.", "correct": True},
                {"id": 2, "text": "C) 125.0 m", "trap": "Incorrect: Assumed pure vertical projection."},
                {"id": 3, "text": "D) 62.5 m", "trap": "Incorrect: Arithmetic error in squaring velocity."}
            ],
            "correct_index": 1,
            "explanation": "Since angle is given with the vertical axis, the vertical velocity component is vy = v0·cos(30°) = 50·(√3/2) = 25√3 m/s. H_max = vy²/(2g) = (25√3)² / 20 = (625·3)/20 = 1875/20 = 93.75 m. Option A (31.25 m) is the exact trap distractor chosen by students who didn't read 'with vertical'!"
        }

    # Custom quiz for Time of Flight (P11-C02-T03-V01)
    if canonical_id == "P11-C02-T03-V01":
        return {
            "title": "Horizontal Acceleration Assumption Trap",
            "warning": "Students frequently try to incorporate horizontal speed vx into time of flight calculations.",
            "pyq_year": "NEET 2021",
            "question": "Two projectiles are launched from the same point with different launch angles and initial speeds, but both attain the exact same maximum height H. What is the ratio of their times of flight T₁ / T₂?",
            "options": [
                {"id": 0, "text": "A) 1 : 1", "trap": "Correct: Both reach same H_max => same initial vertical velocity vy0 => same time of flight T = 2vy0/g.", "correct": True},
                {"id": 1, "text": "B) 1 : 2", "trap": "Trap: Assumed time depends on range or horizontal speed."},
                {"id": 2, "text": "C) Dependent on launch angle θ", "trap": "Trap: Failed to realize H_max determines vy0 independently of θ."},
                {"id": 3, "text": "D) 2 : 1", "trap": "Incorrect ratio inversion."}
            ],
            "correct_index": 0,
            "explanation": "Since H_max = vy²/(2g), same H_max strictly means same vertical speed vy. Time of flight T = 2vy/g depends exclusively on vertical speed. Therefore T1/T2 = 1:1, regardless of their ranges or horizontal components!"
        }

    # Generic high-yield trap generation for other concepts
    warning_text = trap_point if trap_point else f"Common exam pitfall in applying {plain_formula or title}."
    return {
        "title": f"NEET Trap: {title}",
        "warning": warning_text,
        "pyq_year": f"NEET {pyq_years.split(',')[0].strip()}" if pyq_years else "NEET High-Yield",
        "question": f"In a standard NEET problem on '{title}', which of the following statements represents the critical condition to prevent sign or angle errors?",
        "options": [
            {"id": 0, "text": "A) Verify coordinate axes orientation and component reference angle before applying formula.", "trap": "Correct: Prevents sine/cosine and +/- direction inversion.", "correct": True},
            {"id": 1, "text": "B) The textbook scalar equation applies universally in all reference frames.", "trap": "Trap: Scalar equations fail when acceleration changes or frame is non-inertial."},
            {"id": 2, "text": "C) Gravitational acceleration g is always negative regardless of chosen axis.", "trap": "Trap: Sign of g depends strictly on positive axis definition."},
            {"id": 3, "text": "D) Horizontal velocity component alters vertical flight duration.", "trap": "Trap: Horizontal and vertical motions are strictly independent."}
        ],
        "correct_index": 0,
        "explanation": f"Key Rule: {row.get('ncert_core_rule', 'Always resolve components along chosen perpendicular axes.')} {row.get('author_book_nuance', '')}"
    }

def build_manifest() -> Dict[str, Any]:
    print("📖 Reading Curriculum Master CSV...")
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Missing {CSV_PATH}")

    concepts = []
    available_streams = set()
    if SECURE_STREAMS_DIR.exists():
        for d in SECURE_STREAMS_DIR.iterdir():
            if d.is_dir() and (d / "master.m3u8").exists():
                available_streams.add(d.name)

    print(f"📡 Found {len(available_streams)} encrypted stream packages.")

    with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = row.get("canonical_id", "").strip()
            if not cid:
                continue

            # Detect available streams for en, hi, ta and 2d/3d
            streams = {"2d": {}, "3d": {}}
            has_any_stream = False

            # Check 2D
            for lang in ["en", "hi", "ta"]:
                stem_2d = f"{cid}_{lang}-IN"
                if stem_2d in available_streams:
                    streams["2d"][lang] = f"/api/stream/{stem_2d}/master.m3u8"
                    has_any_stream = True

            # Check 3D
            for lang in ["en", "hi", "ta"]:
                stem_3d = f"{cid}_3d_{lang}-IN"
                if stem_3d in available_streams:
                    streams["3d"][lang] = f"/api/stream/{stem_3d}/master.m3u8"
                    has_any_stream = True

            # Check if simulation exists
            simulation_url = None
            if "Projectile" in row.get("topic_name", "") or "P11-C02-T03" in cid:
                simulation_url = "/simulations/projectile_3d_simulation.html"

            concept_node = {
                "canonical_id": cid,
                "subject": row.get("subject", "Physics"),
                "grade": int(row.get("grade", 11) or 11),
                "unit": row.get("neet_2026_unit", "").strip() or f"UNIT {row.get('chapter_no', 1)}: {row.get('chapter_name', '')}",
                "chapter_no": int(row.get("chapter_no", 1) or 1),
                "chapter_name": row.get("chapter_name", "").strip(),
                "topic_no": int(row.get("topic_no", 1) or 1),
                "topic_name": row.get("topic_name", "").strip(),
                "video_no": int(row.get("video_no", 1) or 1),
                "title": row.get("concept_title", ""),
                "dimension_support": "3d" if bool(streams["3d"]) else "2d",
                "latex_formula": row.get("latex_formula", ""),
                "plain_formula": row.get("plain_formula", ""),
                "ncert_citation": row.get("ncert_citation", ""),
                "ncert_core_rule": row.get("ncert_core_rule", ""),
                "author_book_nuance": row.get("author_book_nuance", ""),
                "neet_trap_point": row.get("neet_trap_point", ""),
                "pyq_years": row.get("pyq_years", ""),
                "has_secure_stream": has_any_stream,
                "streams": streams,
                "simulation": simulation_url,
                "trap_quiz": build_trap_quiz(row)
            }
            concepts.append(concept_node)

    manifest = {
        "version": "2.0.0",
        "app_title": "NEET UG Masterclass Triad Player",
        "total_concepts": len(concepts),
        "active_stream_concepts": sum(1 for c in concepts if c["has_secure_stream"]),
        "concepts": concepts
    }

    MANIFEST_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_OUTPUT_PATH, "w", encoding="utf-8") as out_f:
        json.dump(manifest, out_f, indent=2, ensure_ascii=False)

    print(f"🎉 Manifest compiled successfully: {MANIFEST_OUTPUT_PATH} ({len(concepts)} concepts, {manifest['active_stream_concepts']} active stream nodes)")
    return manifest

if __name__ == "__main__":
    build_manifest()
