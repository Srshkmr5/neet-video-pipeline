"""
Generate Master CSVs for Excel:
1. queue/taxonomy_master.csv - All 61 Chapters with NEET 2026 Units, Topics, Video Counts, and pre-formatted NotebookLM prompt snippets.
2. queue/curriculum_master_full_665.csv - All 665 video rows pre-sequenced, with completed Kinematics rows and placeholders for NotebookLM extraction.
"""

import csv
import json
import re
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from config import QUEUE_DIR

def get_storyboard_ui_archetype(subj: str, ch_title: str, t_name: str, c_title: str, v_idx: int, v_count: int) -> str:
    # Final video of chapter is often chapter review / GPS
    if v_idx == v_count:
        return "NEURAL_CONSTELLATION"
    
    c_lower = (c_title + " " + t_name + " " + ch_title).lower()
    
    if subj in ["Chemistry", "Biology"]:
        return "MOLECULAR_REACTOR"
    
    # Physics heuristics
    if any(k in c_lower for k in ["graph", "slope", "area", "v-t", "s-t", "shm", "wave", "alternating current", "integral"]):
        return "ORTHOGONAL_SPLIT"
    elif any(k in c_lower for k in ["formula", "equation", "derivation", "trap", "pyq", "law"]):
        return "FORMULA_DECONSTRUCTION"
    else:
        return "KINETIC_STAGE"

def generate_csvs():
    tax_json_path = QUEUE_DIR / "taxonomy_master.json"
    with open(tax_json_path, "r", encoding="utf-8") as f:
        tax_data = json.load(f)

    chapters = list(tax_data["chapters"].values())

    # 1. GENERATE taxonomy_master.csv (61 Chapter Rows)
    tax_csv_path = QUEUE_DIR / "taxonomy_master.csv"
    with open(tax_csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Canonical Chapter ID",
            "Subject",
            "Grade",
            "Chapter Title",
            "Tier 1 Macro Movie ID",
            "Tier 1 Macro Movie Title",
            "Tier 1 Duration",
            "NEET 2026 Syllabus Unit",
            "Target Videos",
            "Core Topics Covered",
            "Subject Video Range",
            "Course Global Range",
            "Status",
            "NotebookLM Prompt Parameter"
        ])

        for c in chapters:
            cid = c["canonical_chapter_id"]
            subj = c["subject"]
            grade = c["grade"]
            title = c["chapter_title"]
            unit = c["neet_2026_unit"]
            v_count = c["video_count"]
            topics = c["core_topics"]
            s_range = f"#{c['subject_video_start_seq']:03d} to #{c['subject_video_end_seq']:03d} (of {c['total_subject_videos']})"
            g_range = f"#{c['global_video_start_seq']:03d} to #{c['global_video_end_seq']:03d} (of {c['total_global_videos']})"
            
            # Status: Kinematics has ready concepts, others pending
            status = "READY (SAMPLE VALIDATED)" if cid == "P11-C02" else "PENDING_EXTRACTION"

            # Pre-formatted prompt parameter for user to copy into NotebookLM
            prompt_helper = (
                f"Subject: {subj} (Class {grade}) | Chapter: {cid} - {title} | "
                f"NEET Unit: {unit} | Core Topics: {topics} | Extract Exactly: {v_count} Videos"
            )

            writer.writerow([
                cid,
                subj,
                grade,
                title,
                c.get("macro_movie_id", f"{cid}-MOVIE"),
                c.get("macro_movie_title", f"{title}: The Master Story"),
                f"{c.get('macro_movie_duration_mins', 10)} Mins (3D Cinematic)",
                unit,
                v_count,
                topics,
                s_range,
                g_range,
                status,
                prompt_helper
            ])

    print(f"✅ Generated {tax_csv_path} ({len(chapters)} chapters)")

    # 2. LOAD EXISTING 7 KINEMATICS ROWS FROM curriculum_master_template.csv
    existing_template = QUEUE_DIR / "curriculum_master_template.csv"
    existing_concepts = {}
    if existing_template.exists():
        with open(existing_template, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_concepts[row["canonical_id"]] = row

    # 3. GENERATE curriculum_master_full_665.csv (All 665 Video Rows)
    full_csv_path = QUEUE_DIR / "curriculum_master_full_665.csv"
    
    headers = [
        "canonical_id",
        "parent_macro_movie_id",
        "subject",
        "grade",
        "chapter_no",
        "chapter_name",
        "topic_no",
        "topic_name",
        "video_no",
        "concept_title",
        "template_name",
        "dimension",
        "storyboard_ui_archetype",
        "chapter_seq",
        "total_chapter_videos",
        "subject_seq",
        "total_subject_videos",
        "global_seq",
        "total_global_videos",
        "next_video_id",
        "next_video_title",
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
        "thumbnail_path",
        "reference_media_path",
        "reference_role",
        "neet_2026_unit",
        "chapter_core_topics"
    ]

    total_rows = 0
    all_rows = []

    # Load reference registry
    reg_path = QUEUE_DIR / "reference_registry.json"
    reg_concepts = {}
    if reg_path.exists():
        try:
            with open(reg_path, "r", encoding="utf-8") as f:
                reg_concepts = json.load(f).get("by_concept", {})
        except Exception:
            pass

    for c in chapters:
        cid = c["canonical_chapter_id"]
        subj = c["subject"]
        grade = c["grade"]
        ch_title = c["chapter_title"]
        ch_no = int(cid.split("-C")[1])
        v_count = c["video_count"]
        unit = c["neet_2026_unit"]
        core_topics = c["core_topics"]
        
        # Split core topics roughly into chunks for topics
        topic_list = [t.strip() for t in core_topics.split(",") if t.strip()]
        if not topic_list:
            topic_list = [ch_title]

        for v_idx in range(1, v_count + 1):
            total_rows += 1
            s_seq = c["subject_video_start_seq"] + v_idx - 1
            g_seq = c["global_video_start_seq"] + v_idx - 1
            
            t_num = min(len(topic_list), max(1, ((v_idx - 1) * len(topic_list)) // v_count + 1))
            t_name = topic_list[t_num - 1]
            
            vid_id = f"{cid}-T{t_num:02d}-V{v_idx:02d}"

            next_id = ""
            next_title = ""
            if v_idx < v_count:
                next_t_num = min(len(topic_list), max(1, (v_idx * len(topic_list)) // v_count + 1))
                next_id = f"{cid}-T{next_t_num:02d}-V{v_idx + 1:02d}"
                next_title = f"Concept {v_idx + 1} of {ch_title}"
            
            matched = None
            if cid == "P11-C02":
                for ex_id, ex_row in existing_concepts.items():
                    if int(ex_row.get("chapter_seq", 0)) == v_idx:
                        matched = ex_row
                        vid_id = ex_id
                        break

            # Check if reference is tagged for this video
            ref_entry = reg_concepts.get(vid_id, {})
            ref_path_str = ref_entry.get("file_path", "")
            ref_role_str = ref_entry.get("role", "")

            # Determine Storyboard UI Archetype
            arch_title = matched.get("concept_title", f"[{ch_title}] Concept {v_idx}") if matched else f"[{ch_title}] Concept {v_idx}"
            archetype_name = get_storyboard_ui_archetype(subj, ch_title, t_name, arch_title, v_idx, v_count)

            if matched:
                all_rows.append({
                    "canonical_id": vid_id,
                    "parent_macro_movie_id": f"{cid}-MOVIE",
                    "subject": matched.get("subject", subj),
                    "grade": grade,
                    "chapter_no": ch_no,
                    "chapter_name": ch_title,
                    "topic_no": matched.get("topic_no", t_num),
                    "topic_name": matched.get("topic_name", t_name),
                    "video_no": matched.get("video_no", v_idx),
                    "concept_title": matched.get("concept_title", ""),
                    "template_name": matched.get("template_name", "FormulaWithGraph"),
                    "dimension": matched.get("dimension", "2d"),
                    "storyboard_ui_archetype": archetype_name,
                    "chapter_seq": v_idx,
                    "total_chapter_videos": v_count,
                    "subject_seq": s_seq,
                    "total_subject_videos": c["total_subject_videos"],
                    "global_seq": g_seq,
                    "total_global_videos": c["total_global_videos"],
                    "next_video_id": matched.get("next_video_id", next_id),
                    "next_video_title": matched.get("next_video_title", next_title),
                    "latex_formula": matched.get("latex_formula", ""),
                    "plain_formula": matched.get("plain_formula", ""),
                    "ncert_citation": matched.get("ncert_citation", ""),
                    "ncert_core_rule": matched.get("ncert_core_rule", ""),
                    "author_book_nuance": matched.get("author_book_nuance", ""),
                    "neet_trap_point": matched.get("neet_trap_point", ""),
                    "pyq_years": matched.get("pyq_years", ""),
                    "status": matched.get("status", "READY"),
                    "audio_provider": matched.get("audio_provider", "edge_tts"),
                    "voice_id": matched.get("voice_id", "en-IN-NeerjaExpressiveNeural"),
                    "thumbnail_path": f"output/thumbnails/{vid_id}_thumbnail.png",
                    "reference_media_path": matched.get("reference_media_path", ref_path_str),
                    "reference_role": matched.get("reference_role", ref_role_str),
                    "neet_2026_unit": unit,
                    "chapter_core_topics": core_topics
                })
            else:
                all_rows.append({
                    "canonical_id": vid_id,
                    "parent_macro_movie_id": f"{cid}-MOVIE",
                    "subject": subj,
                    "grade": grade,
                    "chapter_no": ch_no,
                    "chapter_name": ch_title,
                    "topic_no": t_num,
                    "topic_name": t_name,
                    "video_no": v_idx,
                    "concept_title": f"[{ch_title}] Concept {v_idx}",
                    "template_name": "FormulaWithGraph",
                    "dimension": "2d",
                    "storyboard_ui_archetype": archetype_name,
                    "chapter_seq": v_idx,
                    "total_chapter_videos": v_count,
                    "subject_seq": s_seq,
                    "total_subject_videos": c["total_subject_videos"],
                    "global_seq": g_seq,
                    "total_global_videos": c["total_global_videos"],
                    "next_video_id": next_id,
                    "next_video_title": next_title,
                    "latex_formula": "",
                    "plain_formula": "",
                    "ncert_citation": "",
                    "ncert_core_rule": "",
                    "author_book_nuance": "",
                    "neet_trap_point": "",
                    "pyq_years": "",
                    "status": "PENDING_NOTEBOOKLM",
                    "audio_provider": "edge_tts",
                    "voice_id": "en-IN-NeerjaExpressiveNeural",
                    "thumbnail_path": f"output/thumbnails/{vid_id}_thumbnail.png",
                    "reference_media_path": ref_path_str,
                    "reference_role": ref_role_str,
                    "neet_2026_unit": unit,
                    "chapter_core_topics": core_topics
                })

    with open(full_csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"✅ Generated {full_csv_path} ({len(all_rows)} total video rows)")

if __name__ == "__main__":
    generate_csvs()
