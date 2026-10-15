"""
Reference Coverage Reporting Tool
Calculates and displays the curriculum reference coverage across all 61 CBSE / NEET chapters (665 videos).
Outputs high-visibility ASCII progress bars and saves output/reports/reference_coverage.md.
"""

import argparse
import json
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

def render_bar(percentage: float, width: int = 15) -> str:
    filled = int(round((percentage / 100.0) * width))
    empty = width - filled
    return "█" * filled + "░" * empty

def calculate_coverage():
    tax_path = QUEUE_DIR / "taxonomy_master.json"
    reg_path = QUEUE_DIR / "reference_registry.json"

    if not tax_path.exists():
        print("❌ taxonomy_master.json not found.")
        return

    with open(tax_path, "r", encoding="utf-8") as f:
        tax_data = json.load(f)

    reg_data = {"by_concept": {}, "by_chapter": {}}
    if reg_path.exists():
        with open(reg_path, "r", encoding="utf-8") as f:
            reg_data = json.load(f)

    chapters = tax_data.get("chapters", {})
    concepts_tagged = reg_data.get("by_concept", {})
    chapters_tagged = reg_data.get("by_chapter", {})

    # Subject aggregations
    subject_stats = {
        "Physics": {"total": 234, "tagged": 0, "chapters": []},
        "Chemistry": {"total": 221, "tagged": 0, "chapters": []},
        "Biology": {"total": 210, "tagged": 0, "chapters": []}
    }

    chapter_coverage_list = []
    
    for ch_id, ch in chapters.items():
        subj = ch.get("subject", "Physics")
        v_count = ch.get("video_count", 1)
        
        # Count tagged concepts in this chapter
        tagged_for_ch = sum(
            1 for cid, meta in concepts_tagged.items()
            if meta.get("chapter_id") == ch_id
        )
        has_ch_level_ref = ch_id in chapters_tagged

        subject_stats[subj]["tagged"] += tagged_for_ch

        pct = (tagged_for_ch / v_count) * 100.0 if v_count > 0 else 0.0

        item = {
            "chapter_id": ch_id,
            "subject": subj,
            "grade": ch.get("grade", 11),
            "chapter_title": ch.get("chapter_title", ""),
            "neet_2026_unit": ch.get("neet_2026_unit", ""),
            "target_videos": v_count,
            "tagged_videos": tagged_for_ch,
            "has_chapter_level_ref": has_ch_level_ref,
            "coverage_pct": pct
        }
        chapter_coverage_list.append(item)
        subject_stats[subj]["chapters"].append(item)

    total_global_videos = 665
    total_global_tagged = len(concepts_tagged)
    global_pct = (total_global_tagged / total_global_videos) * 100.0

    # Print Terminal Report
    print("=" * 78)
    print("      CBSE / NEET UG REFERENCE CURRICULUM COVERAGE REPORT")
    print("=" * 78)

    for subj, sdata in subject_stats.items():
        s_pct = (sdata["tagged"] / sdata["total"]) * 100.0
        bar = render_bar(s_pct, width=20)
        print(f"\n📘 Subject: {subj.upper()} | Tagged: {sdata['tagged']:3d} / {sdata['total']:3d} ({s_pct:5.1f}%) [{bar}]")
        print("-" * 78)
        
        for c in sdata["chapters"]:
            c_bar = render_bar(c["coverage_pct"], width=10)
            status_flag = "✓ FULL" if c["coverage_pct"] >= 100.0 else ("• PARTIAL" if c["tagged_videos"] > 0 else "  PENDING")
            ch_ref_flag = " [Ch-Style Tagged]" if c["has_chapter_level_ref"] else ""
            print(f"  [{c['chapter_id']}] {c['chapter_title'][:32]:<32} : {c['tagged_videos']:2d}/{c['target_videos']:2d} ({c['coverage_pct']:5.1f}%) [{c_bar}] {status_flag}{ch_ref_flag}")

    common_pool = reg_data.get("common_pool", {})

    print("\n" + "=" * 78)
    g_bar = render_bar(global_pct, width=25)
    print(f"🌟 TOTAL ACTIVE CURRICULUM COVERAGE : {total_global_tagged:3d} / {total_global_videos:3d} ({global_pct:5.1f}%) [{g_bar}]")
    print(f"   Chapter-Level Visual Themes      : {len(chapters_tagged)} / 61 Chapters Tagged")
    print(f"📦 COMMON REFERENCE POOL (Unmapped) : {len(common_pool)} item(s) awaiting syllabus matching")
    if common_pool:
        print("   " + "-" * 74)
        for pid, pitem in list(common_pool.items())[:10]:
            print(f"   • [{pid}] {pitem.get('concept_tag')[:34]:<34} | {pitem.get('subject_hint') or 'General':<11} | Gr:{pitem.get('grade_hint') or 'Any'}")
        if len(common_pool) > 10:
            print(f"   ... and {len(common_pool) - 10} more items.")
    print("=" * 78)

    # Save Markdown Report
    rep_dir = BASE_DIR / "output" / "reports"
    rep_dir.mkdir(parents=True, exist_ok=True)
    md_file = rep_dir / "reference_coverage.md"

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# CBSE / NEET UG Reference Video Coverage Report\n\n")
        f.write(f"**Total Progress**: {total_global_tagged} / {total_global_videos} concepts tagged ({global_pct:.1f}%)\n\n")
        f.write(f"**Common Reference Pool**: {len(common_pool)} unmapped / future syllabus assets stored\n\n")
        f.write("| Subject | Tagged Concepts | Total Concepts | Coverage % |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for subj, sdata in subject_stats.items():
            s_pct = (sdata["tagged"] / sdata["total"]) * 100.0
            f.write(f"| **{subj}** | {sdata['tagged']} | {sdata['total']} | {s_pct:.1f}% |\n")
            
        f.write("\n\n## Chapter Breakdown\n\n")
        f.write("| Canonical ID | Chapter Title | NEET 2026 Unit | Tagged | Total | Progress |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for c in chapter_coverage_list:
            f.write(f"| `{c['chapter_id']}` | {c['chapter_title']} | {c['neet_2026_unit']} | {c['tagged_videos']} | {c['target_videos']} | {c['coverage_pct']:.1f}% |\n")

        if common_pool:
            f.write("\n\n## Common Pool Inventory (Holding Zone)\n\n")
            f.write("| Pool ID | Concept Tag | Subject Hint | Grade Hint | Filename |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for pid, pitem in common_pool.items():
                f.write(f"| `{pid}` | {pitem.get('concept_tag')} | {pitem.get('subject_hint', 'General')} | {pitem.get('grade_hint', 'Any')} | {pitem.get('filename')} |\n")

    print(f"\n📄 Markdown report saved to: {md_file}")

if __name__ == "__main__":
    calculate_coverage()
