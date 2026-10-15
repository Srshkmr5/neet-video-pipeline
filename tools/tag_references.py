"""
Reference Tagging & Ingestion Tool
Tags reference videos to Canonical Concept IDs (e.g. P11-C02-T03-V02) or Chapter IDs (e.g. P11-C02).
Maintains queue/reference_registry.json as the persistent index for CBSE / NEET curriculum coverage.
"""

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional
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

REGISTRY_PATH = QUEUE_DIR / "reference_registry.json"
TAXONOMY_PATH = QUEUE_DIR / "taxonomy_master.json"
REFERENCES_DIR = BASE_DIR / "media" / "references"

def load_taxonomy() -> Dict[str, Any]:
    if not TAXONOMY_PATH.exists():
        return {}
    with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
        return json.load(f).get("chapters", {})

def load_registry() -> Dict[str, Any]:
    if REGISTRY_PATH.exists():
        try:
            with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                reg = json.load(f)
                if "common_pool" not in reg:
                    reg["common_pool"] = {}
                if "by_macro_story" not in reg:
                    reg["by_macro_story"] = {}
                return reg
        except Exception:
            pass
    return {
        "metadata": {
            "description": "Index of reference video assets mapped to CBSE / NEET Canonical Taxonomy",
            "total_tagged_concepts": 0,
            "total_tagged_chapters": 0,
            "total_tagged_macro_stories": 0,
            "total_common_pool_items": 0
        },
        "by_concept": {},
        "by_chapter": {},
        "by_macro_story": {},
        "common_pool": {}
    }

def save_registry(registry: Dict[str, Any]):
    registry["metadata"]["total_tagged_concepts"] = len(registry.get("by_concept", {}))
    registry["metadata"]["total_tagged_chapters"] = len(registry.get("by_chapter", {}))
    registry["metadata"]["total_tagged_macro_stories"] = len(registry.get("by_macro_story", {}))
    registry["metadata"]["total_common_pool_items"] = len(registry.get("common_pool", {}))
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def tag_reference_file(
    video_path: Path,
    target_id: str,
    role: str = "blueprint",
    notes: str = "",
    move_file: bool = True
) -> Dict[str, Any]:
    """
    Tags a video to a concept (P11-C02-T03-V02), chapter (P11-C02), or Macro Movie (P11-C02-MOVIE).
    """
    if not video_path.exists():
        raise FileNotFoundError(f"Reference video not found at: {video_path}")
        
    registry = load_registry()
    tax_chapters = load_taxonomy()
    
    # Concept Pattern: P11-C02-T03-V02
    concept_match = re.match(r"^([PCB]\d{2}-C\d{2})-T\d{2}-V\d{2}$", target_id)
    # Macro Story Pattern: P11-C02-MOVIE
    macro_match = re.match(r"^([PCB]\d{2}-C\d{2})-MOVIE$", target_id)
    # Chapter Pattern: P11-C02
    chapter_match = re.match(r"^[PCB]\d{2}-C\d{2}$", target_id)
    
    if concept_match:
        ch_id = concept_match.group(1)
        ch_meta = tax_chapters.get(ch_id, {})
        dest_dir = REFERENCES_DIR / "by_concept" / target_id
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / video_path.name
        
        if move_file and video_path.resolve() != dest_file.resolve():
            shutil.copy2(str(video_path), str(dest_file))
            stored_path = dest_file
        else:
            stored_path = video_path
            
        entry = {
            "canonical_id": target_id,
            "chapter_id": ch_id,
            "chapter_title": ch_meta.get("chapter_title", "Unknown"),
            "neet_2026_unit": ch_meta.get("neet_2026_unit", "Unknown"),
            "file_path": str(stored_path.relative_to(BASE_DIR) if stored_path.is_relative_to(BASE_DIR) else stored_path),
            "filename": video_path.name,
            "role": role,  # blueprint | hybrid_asset | aesthetic_style
            "notes": notes
        }
        registry["by_concept"][target_id] = entry
        print(f"✅ Tagged Concept [{target_id}] -> {video_path.name} (Role: {role.upper()})")

    elif macro_match:
        ch_id = macro_match.group(1)
        ch_meta = tax_chapters.get(ch_id, {})
        dest_dir = REFERENCES_DIR / "macro_stories" / target_id
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / video_path.name
        
        if move_file and video_path.resolve() != dest_file.resolve():
            shutil.copy2(str(video_path), str(dest_file))
            stored_path = dest_file
        else:
            stored_path = video_path
            
        entry = {
            "macro_movie_id": target_id,
            "chapter_id": ch_id,
            "chapter_title": ch_meta.get("chapter_title", "Unknown"),
            "neet_2026_unit": ch_meta.get("neet_2026_unit", "Unknown"),
            "file_path": str(stored_path.relative_to(BASE_DIR) if stored_path.is_relative_to(BASE_DIR) else stored_path),
            "filename": video_path.name,
            "role": role or "3d_cinematic_storyboard",
            "notes": notes
        }
        if "by_macro_story" not in registry:
            registry["by_macro_story"] = {}
        registry["by_macro_story"][target_id] = entry
        print(f"🎬 Tagged Tier 1 Macro Story [{target_id}] -> {video_path.name} (Role: {role.upper()})")
        
    elif chapter_match:
        ch_id = target_id
        ch_meta = tax_chapters.get(ch_id, {})
        dest_dir = REFERENCES_DIR / "by_chapter" / target_id
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / video_path.name
        
        if move_file and video_path.resolve() != dest_file.resolve():
            shutil.copy2(str(video_path), str(dest_file))
            stored_path = dest_file
        else:
            stored_path = video_path
            
        entry = {
            "chapter_id": ch_id,
            "chapter_title": ch_meta.get("chapter_title", "Unknown"),
            "neet_2026_unit": ch_meta.get("neet_2026_unit", "Unknown"),
            "file_path": str(stored_path.relative_to(BASE_DIR) if stored_path.is_relative_to(BASE_DIR) else stored_path),
            "filename": video_path.name,
            "role": role,
            "notes": notes
        }
        registry["by_chapter"][target_id] = entry
        print(f"✅ Tagged Chapter [{target_id}] -> {video_path.name} (Role: {role.upper()})")
    else:
        raise ValueError(f"Invalid target ID format: {target_id}. Expected [PCB]xx-Cxx-Txx-Vxx, [PCB]xx-Cxx-MOVIE, or [PCB]xx-Cxx")
        
    save_registry(registry)
    return entry

def scan_inbox_and_folders() -> int:
    """
    Scans media/references/inbox/ for files with Canonical IDs in their filenames,
    and also scans existing by_concept / by_chapter directories to sync the registry.
    """
    inbox_dir = REFERENCES_DIR / "inbox"
    concept_dir = REFERENCES_DIR / "by_concept"
    chapter_dir = REFERENCES_DIR / "by_chapter"
    
    tagged_count = 0
    
def tag_to_common_pool(
    video_path: Path,
    concept_tag: str,
    subject_hint: str = "",
    grade_hint: int = 0,
    keywords: Optional[List[str]] = None,
    role: str = "blueprint",
    notes: str = "",
    move_file: bool = True
) -> Dict[str, Any]:
    """
    Tags an unmatched / general / future-syllabus video to the Common Pool.
    """
    if not video_path.exists():
        raise FileNotFoundError(f"Reference video not found at: {video_path}")

    registry = load_registry()
    pool_dir = REFERENCES_DIR / "common_pool"
    pool_dir.mkdir(parents=True, exist_ok=True)
    dest_file = pool_dir / video_path.name

    if move_file and video_path.resolve() != dest_file.resolve():
        shutil.copy2(str(video_path), str(dest_file))
        stored_path = dest_file
    else:
        stored_path = video_path

    # Clean pool key
    pool_id = f"pool_{video_path.stem.lower()}"
    pool_id = re.sub(r"[^a-z0-9_]", "_", pool_id)

    kw_list = keywords or []
    if not kw_list and concept_tag:
        kw_list = [w.lower().strip() for w in re.split(r"[\s,;]+", concept_tag) if len(w) > 2]

    entry = {
        "pool_id": pool_id,
        "filename": video_path.name,
        "file_path": str(stored_path.relative_to(BASE_DIR) if stored_path.is_relative_to(BASE_DIR) else stored_path),
        "concept_tag": concept_tag,
        "subject_hint": subject_hint,
        "grade_hint": grade_hint,
        "keywords": kw_list,
        "role": role,
        "notes": notes,
        "status": "UNMATCHED_COMMON_POOL"
    }

    registry["common_pool"][pool_id] = entry
    save_registry(registry)
    print(f"📦 Stored in Common Pool [{pool_id}] -> {video_path.name}")
    print(f"   Tag: '{concept_tag}' | Subject: {subject_hint or 'General'} | Grade: {grade_hint or 'Any'}")
    return entry

def refresh_common_pool(threshold: float = 0.65) -> int:
    """
    Re-evaluates all items in media/references/common_pool against the latest taxonomy_master.json.
    Promotes and migrates matching videos into by_concept or by_chapter.
    """
    registry = load_registry()
    tax_chapters = load_taxonomy()
    pool = registry.get("common_pool", {})

    if not pool:
        print("ℹ️  Common Pool is empty. Nothing to refresh.")
        return 0

    print(f"🔄 Refreshing Common Pool ({len(pool)} unmapped item(s)) against {len(tax_chapters)} syllabus chapters...")
    promoted_count = 0

    for pool_id, item in list(pool.items()):
        concept_tag = item.get("concept_tag", "").lower()
        keywords = [k.lower() for k in item.get("keywords", [])]
        subj_hint = item.get("subject_hint", "").lower()
        grade_hint = int(item.get("grade_hint", 0))
        file_path = BASE_DIR / item.get("file_path", "")

        best_match_id = None
        best_match_type = None  # "concept" | "chapter"
        best_score = 0.0

        for ch_id, ch in tax_chapters.items():
            ch_subj = ch.get("subject", "").lower()
            ch_grade = int(ch.get("grade", 0))
            ch_title = ch.get("chapter_title", "").lower()
            ch_topics = ch.get("core_topics", "").lower()

            # Subject/Grade compatibility filter
            if subj_hint and subj_hint != ch_subj:
                continue
            if grade_hint > 0 and grade_hint != ch_grade:
                continue

            # Token matching
            combined_text = f"{ch_title} {ch_topics}"
            
            # Count keyword hits
            hits = sum(1 for kw in keywords if kw in combined_text)
            tag_hits = sum(1 for word in concept_tag.split() if len(word) > 2 and word in combined_text)
            
            total_checks = max(1, len(keywords) + len(concept_tag.split()))
            score = (hits * 1.5 + tag_hits) / total_checks

            # Exact title or topic mention boost
            if concept_tag in ch_title or concept_tag in ch_topics:
                score += 0.5
            for kw in keywords:
                if kw in ch_topics:
                    score += 0.2

            if score > best_score:
                best_score = score
                best_match_id = ch_id
                best_match_type = "chapter"

        if best_score >= threshold and best_match_id:
            print(f"\n🎉 MATCH FOUND for Pool Item [{pool_id}]!")
            print(f"   Item: '{item.get('concept_tag')}' (Score: {best_score:.2f})")
            print(f"   Matched Chapter: [{best_match_id}] {tax_chapters[best_match_id].get('chapter_title')}")
            
            # Promote to by_chapter or first concept
            if file_path.exists():
                tag_reference_file(
                    video_path=file_path,
                    target_id=best_match_id,
                    role=item.get("role", "blueprint"),
                    notes=f"Auto-promoted from Common Pool ({item.get('concept_tag')})",
                    move_file=True
                )
                # Remove original from common pool directory if different
                dest_file = REFERENCES_DIR / "by_chapter" / best_match_id / file_path.name
                if file_path.resolve() != dest_file.resolve() and file_path.exists():
                    try:
                        file_path.unlink()
                    except Exception:
                        pass

            # Remove from common pool registry
            del registry["common_pool"][pool_id]
            promoted_count += 1
        else:
            print(f"   • [{pool_id}] '{item.get('concept_tag')}' -> No confident match yet (Best score: {best_score:.2f}). Kept in Common Pool.")

    save_registry(registry)
    print(f"\n✅ Common Pool refresh complete. Promoted {promoted_count} video(s).")
    return promoted_count

def scan_inbox_and_folders() -> int:
    """
    Scans media/references/inbox/ for files with Canonical IDs in their filenames,
    and also scans existing by_concept / by_chapter directories to sync the registry.
    """
    inbox_dir = REFERENCES_DIR / "inbox"
    concept_dir = REFERENCES_DIR / "by_concept"
    chapter_dir = REFERENCES_DIR / "by_chapter"
    pool_dir = REFERENCES_DIR / "common_pool"
    
    tagged_count = 0
    
    # 1. Scan inbox for filename hints
    if inbox_dir.exists():
        for f in inbox_dir.glob("*.*"):
            if f.suffix.lower() not in [".mp4", ".mov", ".mkv", ".webm", ".png", ".jpg"]:
                continue
            m_concept = re.search(r"([PCB]\d{2}-C\d{2}-T\d{2}-V\d{2})", f.name)
            m_chapter = re.search(r"([PCB]\d{2}-C\d{2})", f.name)
            
            if m_concept:
                cid = m_concept.group(1)
                tag_reference_file(f, cid, role="blueprint", notes="Auto-tagged from inbox filename")
                tagged_count += 1
            elif m_chapter:
                chid = m_chapter.group(1)
                tag_reference_file(f, chid, role="aesthetic_style", notes="Auto-tagged from inbox filename")
                tagged_count += 1
            else:
                # If no syllabus ID found in filename, move to common pool!
                tag_to_common_pool(
                    video_path=f,
                    concept_tag=f.stem.replace("_", " "),
                    notes="Ingested from inbox into Common Pool"
                )
                tagged_count += 1

    # 2. Sync by_concept folder tree
    if concept_dir.exists():
        for c_folder in concept_dir.iterdir():
            if c_folder.is_dir() and re.match(r"^[PCB]\d{2}-C\d{2}-T\d{2}-V\d{2}$", c_folder.name):
                for f in c_folder.glob("*.*"):
                    if f.suffix.lower() in [".mp4", ".mov", ".mkv", ".webm", ".png", ".jpg"]:
                        tag_reference_file(f, c_folder.name, role="blueprint", notes="Synced from by_concept folder", move_file=False)
                        tagged_count += 1

    # 3. Sync by_chapter folder tree
    if chapter_dir.exists():
        for ch_folder in chapter_dir.iterdir():
            if ch_folder.is_dir() and re.match(r"^[PCB]\d{2}-C\d{2}$", ch_folder.name):
                for f in ch_folder.glob("*.*"):
                    if f.suffix.lower() in [".mp4", ".mov", ".mkv", ".webm", ".png", ".jpg"]:
                        tag_reference_file(f, ch_folder.name, role="aesthetic_style", notes="Synced from by_chapter folder", move_file=False)
                        tagged_count += 1

    # 4. Sync macro_stories folder tree
    macro_dir = REFERENCES_DIR / "macro_stories"
    if macro_dir.exists():
        for m_folder in macro_dir.iterdir():
            if m_folder.is_dir() and re.match(r"^[PCB]\d{2}-C\d{2}-MOVIE$", m_folder.name):
                for f in m_folder.glob("*.*"):
                    if f.suffix.lower() in [".mp4", ".mov", ".mkv", ".webm", ".png", ".jpg"]:
                        tag_reference_file(f, m_folder.name, role="3d_cinematic_storyboard", notes="Synced from macro_stories folder", move_file=False)
                        tagged_count += 1

    return tagged_count

def main():
    parser = argparse.ArgumentParser(description="Reference Video Curriculum Tagging Tool")
    parser.add_argument("--video", type=str, help="Path to reference video file")
    parser.add_argument("--target", type=str, help="Canonical Concept ID (e.g. P11-C02-T03-V02), Chapter ID (e.g. P11-C02), or Macro Movie ID (e.g. P11-C02-MOVIE)")
    parser.add_argument("--role", type=str, default="blueprint", choices=["blueprint", "hybrid_asset", "aesthetic_style", "3d_cinematic_storyboard", "visual_metaphor"], help="Role of the reference")
    parser.add_argument("--notes", type=str, default="", help="Optional notes on the reference")
    parser.add_argument("--scan", action="store_true", help="Scan media/references/inbox/ and sync existing folders")
    
    # Common Pool arguments
    parser.add_argument("--pool", action="store_true", help="Tag to Common Pool (unmatched / future syllabus holding zone)")
    parser.add_argument("--concept", type=str, default="", help="Descriptive concept name (for common pool)")
    parser.add_argument("--subject", type=str, default="", help="Subject hint (e.g. Mathematics, Physics, Chemistry)")
    parser.add_argument("--grade", type=int, default=0, help="Grade / Class hint (e.g. 10, 11, 12)")
    parser.add_argument("--keywords", type=str, default="", help="Comma-separated keywords (e.g. 'trigonometry,sin,cos,unit circle')")
    parser.add_argument("--refresh-pool", action="store_true", help="Refresh Common Pool against latest taxonomy_master.json")
    
    args = parser.parse_args()
    
    if args.refresh_pool:
        refresh_common_pool()
    elif args.scan:
        cnt = scan_inbox_and_folders()
        print(f"🔄 Inbox & folder scan complete. Synced {cnt} reference asset(s).")
    elif args.pool and args.video:
        kw_list = [k.strip() for k in args.keywords.split(",") if k.strip()]
        concept = args.concept or Path(args.video).stem.replace("_", " ")
        tag_to_common_pool(
            video_path=Path(args.video),
            concept_tag=concept,
            subject_hint=args.subject,
            grade_hint=args.grade,
            keywords=kw_list,
            role=args.role,
            notes=args.notes
        )
    elif args.video and args.target:
        tag_reference_file(Path(args.video), args.target, role=args.role, notes=args.notes)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

