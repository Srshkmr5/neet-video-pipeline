"""
Curriculum Importer: Converts Master Curriculum CSV into Validated Concept Queue
Bridges NotebookLM / Google Sheets to One-Command Render Engine.
Derived from MASTER_BLUEPRINT.md v1.1
"""
import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Any, List
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
from llm.schema import ConceptNode, BeatTier, Beat, LocaleText
from llm.script_engine import ScriptEngine

class CurriculumImporter:
    @staticmethod
    def load_taxonomy_master() -> Dict[str, Any]:
        tax_path = QUEUE_DIR / "taxonomy_master.json"
        if tax_path.exists():
            with open(tax_path, "r", encoding="utf-8") as f:
                return json.load(f).get("chapters", {})
        return {}

    @classmethod
    def generate_multilingual_scripts(cls, row: Dict[str, str]) -> Dict[str, LocaleText]:
        title = row.get("concept_title", "").strip()
        topic = row.get("topic_name", "").strip()
        formula = row.get("plain_formula", "").strip()
        ncert_rule = row.get("ncert_core_rule", "").strip()
        author_nuance = row.get("author_book_nuance", "").strip()
        trap = row.get("neet_trap_point", "").strip()
        pyq_years = row.get("pyq_years", "").strip()

        ch_seq = row.get("chapter_seq", "").strip()
        total_ch = row.get("total_chapter_videos", "").strip()
        next_title = row.get("next_video_title", "").strip()

        teaser_en = f" Up next in video {int(ch_seq)+1 if ch_seq.isdigit() else ''}: {next_title}." if next_title else ""
        teaser_hi = f" अगला वीडियो: {next_title}।" if next_title else ""
        teaser_ta = f" அடுத்த காணொளி: {next_title}." if next_title else ""

        pyq_badge_en = f"High Yield | PYQ: {pyq_years}" if pyq_years else "Core Concept"
        pyq_badge_hi = f"उच्च अंक | विगत वर्ष: {pyq_years}" if pyq_years else "मूल सिद्धांत"
        pyq_badge_ta = f"முக்கிய வினா | PYQ: {pyq_years}" if pyq_years else "அடிப்படை கருத்து"

        # English Script
        narration_en = (
            f"Welcome to {topic}. Today we master {title}. "
            f"According to NCERT: {ncert_rule} "
            f"The primary formula is: {formula}. "
            f"Notice this crucial insight: {author_nuance} "
            f"Pay special attention to this NEET trap point: {trap} "
            f"Keep this core relationship firmly in mind to secure top marks in NEET.{teaser_en}"
        )

        # Hindi Script
        narration_hi = (
            f"{topic} में आपका स्वागत है। आज हम समझेंगे: {title}। "
            f"एनसीईआरटी के अनुसार: {ncert_rule} "
            f"इसका मुख्य सूत्र है: {formula}। "
            f"विशेष ध्यान देने योग्य बात: {author_nuance} "
            f"नीट परीक्षा की मुख्य भूल या ट्रैप पॉइंट: {trap} "
            f"इस महत्वपूर्ण संबंध को हमेशा याद रखें।{teaser_hi}"
        )

        # Tamil Script
        narration_ta = (
            f"{topic} பகுதிக்கு உங்களை வரவேற்கிறோம். இன்று நாம் {title} பற்றிய அடிப்படைக் கருத்தைக் காண்போம். "
            f"என்சிஇஆர்டி விதிப்படி: {ncert_rule} "
            f"இதன் முதன்மைச் சூத்திரம்: {formula}. "
            f"முக்கியமாக கவனிக்க வேண்டிய குறிப்பு: {author_nuance} "
            f"நீட் தேர்வில் மாணவர்கள் செய்யும் பொதுவான தவறு அல்லது பொறி: {trap} "
            f"இந்த முக்கிய சமன்பாட்டை மனதில் உறுதிப்படுத்திக் கொள்ளுங்கள்.{teaser_ta}"
        )

        return {
            "en": LocaleText(
                title=title,
                narration=ScriptEngine.normalize_for_tts(narration_en, "en"),
                trapPoint=trap,
                pyqBadge=pyq_badge_en
            ),
            "hi": LocaleText(
                title=title,
                narration=narration_hi,
                trapPoint=trap,
                pyqBadge=pyq_badge_hi
            ),
            "ta": LocaleText(
                title=title,
                narration=narration_ta,
                trapPoint=trap,
                pyqBadge=pyq_badge_ta
            )
        }

    @classmethod
    def parse_csv_row_to_node(cls, row: Dict[str, str], taxonomy_chapters: Dict[str, Any] = None) -> ConceptNode:
        taxonomy_chapters = taxonomy_chapters or cls.load_taxonomy_master()
        video_id = row.get("canonical_id", "").strip()
        title = row.get("concept_title", "").strip()
        subject = row.get("subject", "Physics").strip()
        grade = int(row.get("grade", 11))
        template_name = row.get("template_name", "FormulaWithGraph").strip()
        dimension = row.get("dimension", "2d").strip().lower()

        chapter_cid = "-".join(video_id.split("-")[:2]) if "-" in video_id else f"{subject[0]}{grade}-C01"
        ch_meta = taxonomy_chapters.get(chapter_cid, {})

        ch_seq = int(row.get("chapter_seq", 1))
        total_ch = int(row.get("total_chapter_videos", ch_meta.get("video_count", 14)))

        # Running sequence coordinates
        s_start = ch_meta.get("subject_video_start_seq", 1)
        g_start = ch_meta.get("global_video_start_seq", 1)
        seq_subj = s_start + ch_seq - 1
        seq_glob = g_start + ch_seq - 1
        tot_subj = ch_meta.get("total_subject_videos", 234)
        tot_glob = ch_meta.get("total_global_videos", 665)

        next_id = row.get("next_video_id", "").strip() or None
        next_title = row.get("next_video_title", "").strip() or None

        beats = [
            Beat(id="settle", tier=BeatTier.SETTLE, repeat=1),
            Beat(id="hook", tier=BeatTier.CONTEXT, repeat=1),
            Beat(id="concept", tier=BeatTier.CRITICAL, repeat=2),
            Beat(id="trap", tier=BeatTier.CRITICAL, repeat=1),
            Beat(id="capsule", tier=BeatTier.STANDARD, repeat=1),
            Beat(id="release", tier=BeatTier.RELEASE, repeat=1)
        ]

        parameters = {
            "latexFormula": row.get("latex_formula", "").strip(),
            "plainFormula": row.get("plain_formula", "").strip(),
            "trapWarning": row.get("neet_trap_point", "").strip(),
            "graphPlot": "3*x - 0.5*x**2",
            "xRange": [0, 6],
            "yRange": [0, 5],
            "ncertCitation": row.get("ncert_citation", "").strip(),
            "ncertRule": row.get("ncert_core_rule", "").strip(),
            "authorNuance": row.get("author_book_nuance", "").strip(),
            "pyqBadge": f"High Yield | PYQ: {row.get('pyq_years', '').strip()}" if row.get('pyq_years') else None,
            "neetUnit": ch_meta.get("neet_2026_unit", "NEET SYLLABUS MAPPED"),
            "seqChapterStr": f"Video {ch_seq} of {total_ch} in {row.get('chapter_name', 'Kinematics')}"
        }

        if template_name == "VectorDiagram":
            parameters["vectorMagnitudes"] = [5, 4, 3]
            parameters["vectorAngles"] = [0, 90, 45]

        locales = cls.generate_multilingual_scripts(row)

        return ConceptNode(
            videoId=video_id,
            prompt_version="v1",
            serialTitle=title,
            subject=subject,
            grade=grade,
            templateName=template_name,
            dimension=dimension,
            seq_chapter=ch_seq,
            total_chapter_videos=total_ch,
            seq_subject=seq_subj,
            total_subject_videos=tot_subj,
            seq_global=seq_glob,
            total_global_videos=tot_glob,
            next_video_id=next_id,
            next_video_title=next_title,
            beats=beats,
            parameters=parameters,
            locales=locales
        )

    @classmethod
    def import_csv_to_queue(
        cls,
        csv_path: Path,
        output_json_path: Path = QUEUE_DIR / "concepts.json",
        dry_run: bool = False
    ) -> List[ConceptNode]:
        if not csv_path.exists():
            raise FileNotFoundError(f"Curriculum CSV not found at: {csv_path}")

        print(f"📖 Reading Master Curriculum: {csv_path}")
        imported_nodes = []
        skipped_pending = 0
        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row_idx, row in enumerate(reader, start=1):
                cid = row.get("canonical_id", "").strip()
                if not cid:
                    continue
                status = row.get("status", "READY").strip().upper()
                if status == "PENDING_NOTEBOOKLM":
                    skipped_pending += 1
                    continue
                node = cls.parse_csv_row_to_node(row)
                imported_nodes.append(node)
                print(f"   ✓ Parsed [{node.videoId}] {node.serialTitle} ({node.templateName}, {node.dimension.upper()})")

        print(f"✅ Successfully converted {len(imported_nodes)} READY curriculum concept(s).")
        if skipped_pending > 0:
            print(f"ℹ️  Skipped {skipped_pending} row(s) marked 'PENDING_NOTEBOOKLM'.")

        if dry_run:
            print("🔍 Dry-run complete. No files modified.")
            return imported_nodes

        # Load existing queue or create new
        existing_nodes_map = {}
        if output_json_path.exists():
            with open(output_json_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for raw in data.get("concepts", []):
                        existing_nodes_map[raw["videoId"]] = raw
                except Exception:
                    pass

        # Upsert imported nodes
        for node in imported_nodes:
            existing_nodes_map[node.videoId] = node.model_dump()

        final_queue = {
            "concepts": list(existing_nodes_map.values())
        }

        output_json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(final_queue, f, indent=2, ensure_ascii=False)

        print(f"💾 Updated Concept Queue saved to: {output_json_path} (Total concepts: {len(final_queue['concepts'])})")
        return imported_nodes

def main():
    parser = argparse.ArgumentParser(description="Master Curriculum CSV to Antigravity Concept Queue Importer")
    parser.add_argument("--csv", type=str, default=str(QUEUE_DIR / "curriculum_master_template.csv"), help="Path to curriculum CSV")
    parser.add_argument("--output", type=str, default=str(QUEUE_DIR / "concepts.json"), help="Path to destination concepts.json")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing to queue")

    args = parser.parse_args()
    CurriculumImporter.import_csv_to_queue(
        csv_path=Path(args.csv),
        output_json_path=Path(args.output),
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()
