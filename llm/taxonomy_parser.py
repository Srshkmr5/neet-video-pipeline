"""
Taxonomy Parser: Extracts and locks Canonical ID.docx into queue/taxonomy_master.json
Maps all 64 chapters across Physics, Chemistry, and Biology to running sequence coordinates
and cross-references with official 2026 NEET UG Syllabus Units.
"""
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from config import QUEUE_DIR

# NEET 2026 Syllabus Unit Cross-Reference Mappings
NEET_2026_UNIT_MAP = {
    # Physics 11
    "P11-C01": "UNIT 1: PHYSICS AND MEASUREMENT",
    "P11-C02": "UNIT 2: KINEMATICS",
    "P11-C03": "UNIT 3: LAWS OF MOTION",
    "P11-C04": "UNIT 4: WORK, ENERGY, AND POWER",
    "P11-C05": "UNIT 5: ROTATIONAL MOTION",
    "P11-C06": "UNIT 6: GRAVITATION",
    "P11-C07": "UNIT 7: PROPERTIES OF SOLIDS AND LIQUIDS",
    "P11-C08": "UNIT 8: THERMODYNAMICS",
    "P11-C09": "UNIT 9: KINETIC THEORY OF GASES",
    "P11-C10": "UNIT 10: OSCILLATIONS AND WAVES",
    # Physics 12
    "P12-C01": "UNIT 11: ELECTROSTATICS",
    "P12-C02": "UNIT 12: CURRENT ELECTRICITY",
    "P12-C03": "UNIT 13: MAGNETIC EFFECTS OF CURRENT AND MAGNETISM",
    "P12-C04": "UNIT 14: ELECTROMAGNETIC INDUCTION AND ALTERNATING CURRENTS",
    "P12-C05": "UNIT 15: ELECTROMAGNETIC WAVES",
    "P12-C06": "UNIT 16: OPTICS",
    "P12-C07": "UNIT 17: DUAL NATURE OF MATTER AND RADIATION",
    "P12-C08": "UNIT 18: ATOMS AND NUCLEI",
    "P12-C09": "UNIT 19: ELECTRONIC DEVICES",
    "P12-C10": "UNIT 20: EXPERIMENTAL SKILLS",
    # Chemistry 11
    "C11-C01": "UNIT 1: SOME BASIC CONCEPTS IN CHEMISTRY",
    "C11-C02": "UNIT 2: ATOMIC STRUCTURE",
    "C11-C03": "UNIT 3: CHEMICAL BONDING AND MOLECULAR STRUCTURE",
    "C11-C04": "UNIT 4: CHEMICAL THERMODYNAMICS",
    "C11-C05": "UNIT 6: EQUILIBRIUM",
    "C11-C06": "UNIT 9: CLASSIFICATION OF ELEMENTS AND PERIODICITY IN PROPERTIES",
    "C11-C07": "UNIT 13: PURIFICATION AND CHARACTERISATION OF ORGANIC COMPOUNDS",
    "C11-C08": "UNIT 14: SOME BASIC PRINCIPLES OF ORGANIC CHEMISTRY",
    "C11-C09": "UNIT 15: HYDROCARBONS",
    # Chemistry 12
    "C12-C01": "UNIT 5: SOLUTIONS",
    "C12-C02": "UNIT 7: REDOX REACTIONS AND ELECTROCHEMISTRY",
    "C12-C03": "UNIT 8: CHEMICAL KINETICS",
    "C12-C04": "UNIT 10: P-BLOCK ELEMENTS",
    "C12-C05": "UNIT 11: D- AND F-BLOCK ELEMENTS",
    "C12-C06": "UNIT 12: COORDINATION COMPOUNDS",
    "C12-C07": "UNIT 16: ORGANIC COMPOUNDS CONTAINING HALOGENS",
    "C12-C08": "UNIT 17: ORGANIC COMPOUNDS CONTAINING OXYGEN",
    "C12-C09": "UNIT 18: ORGANIC COMPOUNDS CONTAINING NITROGEN",
    "C12-C10": "UNIT 19: BIOMOLECULES",
    "C12-C11": "UNIT 20: PRINCIPLES RELATED TO PRACTICAL CHEMISTRY",
    # Biology 11
    "B11-C01": "UNIT 1: DIVERSITY IN LIVING WORLD",
    "B11-C02": "UNIT 2: STRUCTURAL ORGANISATION IN ANIMALS AND PLANTS",
    "B11-C03": "UNIT 3: CELL STRUCTURE AND FUNCTION",
    "B11-C04": "UNIT 4: PLANT PHYSIOLOGY",
    "B11-C05": "UNIT 5: HUMAN PHYSIOLOGY (Breathing)",
    "B11-C06": "UNIT 5: HUMAN PHYSIOLOGY (Circulation)",
    "B11-C07": "UNIT 5: HUMAN PHYSIOLOGY (Excretion)",
    "B11-C08": "UNIT 5: HUMAN PHYSIOLOGY (Locomotion & Movement)",
    "B11-C09": "UNIT 5: HUMAN PHYSIOLOGY (Neural Control & Coordination)",
    "B11-C10": "UNIT 5: HUMAN PHYSIOLOGY (Chemical Coordination & Integration)",
    # Biology 12
    "B12-C01": "UNIT 6: REPRODUCTION (Plant)",
    "B12-C02": "UNIT 6: REPRODUCTION (Human)",
    "B12-C03": "UNIT 6: REPRODUCTION (Reproductive Health)",
    "B12-C04": "UNIT 7: GENETICS AND EVOLUTION (Heredity and Variation)",
    "B12-C05": "UNIT 7: GENETICS AND EVOLUTION (Molecular Basis of Inheritance)",
    "B12-C06": "UNIT 7: GENETICS AND EVOLUTION (Evolution)",
    "B12-C07": "UNIT 8: BIOLOGY AND HUMAN WELFARE (Health & Disease)",
    "B12-C08": "UNIT 8: BIOLOGY AND HUMAN WELFARE (Microbes in Human Welfare)",
    "B12-C09": "UNIT 9: BIOTECHNOLOGY AND ITS APPLICATIONS",
    "B12-C10": "UNIT 10: ECOLOGY AND ENVIRONMENT (Organisms & Populations)",
    "B12-C11": "UNIT 10: ECOLOGY AND ENVIRONMENT (Ecosystem & Biodiversity)"
}

def parse_docx_table(docx_path: Path):
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read("word/document.xml"))
        lines = [''.join(p.itertext()).strip() for p in tree.iter() if p.tag.endswith('p') and ''.join(p.itertext()).strip()]

    rows = []
    # Pattern: ID, Title, Core Topics, Videos
    # Example: P11-C01,Physics and Measurement,"Units, SI Units, Errors, Dimensions & Applications",8
    pattern = re.compile(r"^([PCB]\d{2}-C\d{2})\s*,\s*\"?([^\",]+(?:,[^\",]+)*?)\"?\s*,\s*\"?([^\"]+)\"?\s*,\s*(\d+)$")

    for line in lines:
        if line.startswith("Canonical ID"):
            continue
        # Clean non-breaking spaces or zero-width spaces
        clean_line = line.replace('\u200b', '').replace('\xa0', ' ').strip()
        
        # Try direct regex or split
        m = pattern.match(clean_line)
        if m:
            cid, title, topics, v_count = m.groups()
            rows.append({
                "canonical_chapter_id": cid.strip(),
                "chapter_title": title.strip(),
                "core_topics": topics.strip(),
                "video_count": int(v_count.strip())
            })
        else:
            # Fallback csv-style parse
            parts = [p.strip().strip('"') for p in clean_line.rsplit(",", 3)]
            if len(parts) >= 4 and re.match(r"^[PCB]\d{2}-C\d{2}$", parts[0]):
                try:
                    v_count = int(parts[-1])
                    rows.append({
                        "canonical_chapter_id": parts[0],
                        "chapter_title": parts[1],
                        "core_topics": parts[2],
                        "video_count": v_count
                    })
                except ValueError:
                    pass

    return rows

def build_taxonomy_master(docx_path: Path = BASE_DIR / "syllabus" / "Canonical ID.docx"):
    rows = parse_docx_table(docx_path)
    print(f"Parsed {len(rows)} chapters from {docx_path.name}")

    subject_totals = {"Physics": 0, "Chemistry": 0, "Biology": 0}
    subject_trackers = {"Physics": 0, "Chemistry": 0, "Biology": 0}
    global_tracker = 0

    # Calculate subject totals
    for r in rows:
        subj_char = r["canonical_chapter_id"][0]
        subj = "Physics" if subj_char == "P" else ("Chemistry" if subj_char == "C" else "Biology")
        r["subject"] = subj
        r["grade"] = int(r["canonical_chapter_id"][1:3])
        subject_totals[subj] += r["video_count"]

    total_global_videos = sum(subject_totals.values())

    enriched_chapters = []
    for r in rows:
        subj = r["subject"]
        cid = r["canonical_chapter_id"]
        v_count = r["video_count"]

        # Subject running sequence
        s_start = subject_trackers[subj] + 1
        s_end = subject_trackers[subj] + v_count
        subject_trackers[subj] = s_end

        # Global running sequence
        g_start = global_tracker + 1
        g_end = global_tracker + v_count
        global_tracker = g_end

        r["subject_video_start_seq"] = s_start
        r["subject_video_end_seq"] = s_end
        r["total_subject_videos"] = subject_totals[subj]

        r["global_video_start_seq"] = g_start
        r["global_video_end_seq"] = g_end
        r["total_global_videos"] = total_global_videos

        r["neet_2026_unit"] = NEET_2026_UNIT_MAP.get(cid, "NEET SYLLABUS MAPPED")

        # Tier 1 Macro Story Movie Metadata (10-minute 3D cinematic overview)
        r["macro_movie_id"] = f"{cid}-MOVIE"
        r["macro_movie_title"] = f"{r['chapter_title']}: The Master Story"
        r["macro_movie_duration_mins"] = 10
        r["macro_movie_format"] = "3D Cinematic / 5-Act Narrative Arc"

        enriched_chapters.append(r)

    master = {
        "metadata": {
            "source_document": str(docx_path),
            "total_chapters": len(enriched_chapters),
            "total_videos": total_global_videos,
            "subject_breakdown": subject_totals
        },
        "chapters": {c["canonical_chapter_id"]: c for c in enriched_chapters}
    }

    out_file = QUEUE_DIR / "taxonomy_master.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2, ensure_ascii=False)

    print(f"Locked {len(enriched_chapters)} chapters into {out_file}")
    print(f"Total Videos: {total_global_videos} (Physics: {subject_totals['Physics']}, Chemistry: {subject_totals['Chemistry']}, Biology: {subject_totals['Biology']})")
    return master

if __name__ == "__main__":
    build_taxonomy_master()
