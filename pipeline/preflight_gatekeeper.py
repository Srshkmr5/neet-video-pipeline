"""
Pre-Flight Visual Verification Gatekeeper Pipeline
NEET UG Video Engine

Mandatory Quality Gate:
No video may be rendered without generating and approving 4-beat static proof screenshots.
"""

import os
import sys
import csv
import json
import time
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# UTF-8 stdout on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

PROOF_DIR = BASE_DIR / "output" / "preflight_proofs"
MANIFEST_PATH = BASE_DIR / "queue" / "approval_manifest.json"
BRAIN_ARTIFACT_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\brain\d9fc2045-37b2-4535-b18a-d8358d69714d")

# Registered Unit 1 archetypes
REGISTERED_ARCHETYPES = {
    "BaseQuantitiesTable7": "BaseQuantitiesTable7Scene",
    "DerivedUnitsAlgebraicLadder": "DerivedUnitsAlgebraicLadderScene",
    "DimensionEquivalenceMatrix": "DimensionEquivalenceMatrixScene",
    "HomogeneityVanDerWaals": "HomogeneityVanDerWaalsScene",
    "MeasurementErrorDistribution": "MeasurementErrorDistributionScene",
    "PowerRuleCalculationTree": "PowerRuleCalculationTreeScene",
    "VernierDualScaleVisualizer": "VernierDualScaleVisualizerScene",
    "SignificantFiguresRulesBox": "SignificantFiguresRulesBoxScene"
}

def clean_corrupted_svg_cache():
    """Defensive sanitation: Purge 0-byte SVG files that cause Pango XML ParseError crashes."""
    count = 0
    for svg in BASE_DIR.glob("**/*.svg"):
        try:
            if svg.is_file() and svg.stat().st_size == 0:
                svg.unlink()
                count += 1
        except Exception:
            pass
    if count > 0:
        print(f"🧹 Cleaned {count} corrupted 0-byte SVG cache files.")

def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_manifest(manifest: dict):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

def audit_typography(row: dict) -> list:
    """Verifies that no raw caret notation or untranslated placeholders leak into strings."""
    warnings = []
    text_fields = ["concept_title", "plain_formula", "author_book_nuance", "neet_trap_point"]
    for field in text_fields:
        val = str(row.get(field, ""))
        if "^" in val:
            warnings.append(f"Field '{field}' contains raw keyboard caret '^': {val}")
        if "?" in val and "sin(" not in val:
            warnings.append(f"Field '{field}' contains untranslated question mark '?': {val}")
    return warnings

def generate_concept_proofs(row: dict, output_concept_dir: Path) -> dict:
    """Renders all 4 static proof beats (PNG) for a given curriculum row using Manim."""
    canonical_id = row["canonical_id"]
    template_name = row["template_name"]
    concept_title = row["concept_title"]

    if template_name not in REGISTERED_ARCHETYPES:
        raise ValueError(f"Unregistered template archetype '{template_name}' for {canonical_id}!")

    class_name = REGISTERED_ARCHETYPES[template_name]
    output_concept_dir.mkdir(parents=True, exist_ok=True)

    # Node data payload matching engine schema
    node_data = {
        "videoId": canonical_id,
        "canonical_id": canonical_id,
        "serialTitle": concept_title,
        "chapter_no": int(row.get("chapter_no", 1)),
        "topic_no": int(row.get("topic_no", 1)),
        "video_no": int(row.get("video_no", 1)),
        "seq_chapter": int(row.get("chapter_seq", 1)),
        "total_chapter_videos": int(row.get("total_chapter_videos", 8)),
        "next_video_id": row.get("next_video_id", ""),
        "next_video_title": row.get("next_video_title", ""),
        "parameters": {
            "conceptTitle": concept_title,
            "pyqBadge": f"NEET PYQ: {row.get('pyq_years')}" if row.get("pyq_years") else "HIGH YIELD",
            "latexFormula": row.get("latex_formula", ""),
            "plainFormula": row.get("plain_formula", ""),
            "trapWarning": row.get("neet_trap_point", ""),
            "ncertRule": row.get("ncert_core_rule", ""),
            "authorNuance": row.get("author_book_nuance", ""),
            "ncertCitation": row.get("ncert_citation", "")
        }
    }

    # Generate a standalone runner script with 4 static beat scene classes
    runner_script = output_concept_dir / f"runner_{canonical_id}.py"
    
    code = f'''import sys
from pathlib import Path
BASE_DIR = Path({repr(str(BASE_DIR))})
sys.path.insert(0, str(BASE_DIR))

from manim import *
FONT_HEADER = "Verdana"
FONT_CARD = "Cascadia Mono"
FONT_BODY = "Consolas"
Text.set_default(font=FONT_BODY)
_orig_t_init = Text.__init__
def _safe_runner_text_init(self, *args, **kwargs):
    if not kwargs.get("font"):
        kwargs["font"] = FONT_BODY
    return _orig_t_init(self, *args, **kwargs)
Text.__init__ = _safe_runner_text_init
import render.templates.unit_01_archetypes as u1

NODE_DATA = {json.dumps(node_data, ensure_ascii=False)}

class Beat1Proof(u1.{class_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.camera.background_color = self.bg_color
        self.setup_header()
        self.add(self.build_beat_1())

class Beat2Proof(u1.{class_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.camera.background_color = self.bg_color
        self.setup_header()
        self.add(self.build_beat_2())

class Beat3Proof(u1.{class_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.camera.background_color = self.bg_color
        self.setup_header()
        self.add(self.build_beat_3())

class Beat4Proof(u1.{class_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.camera.background_color = self.bg_color
        self.setup_header()
        self.add(self.build_beat_4())

class Beat5Proof(u1.{class_name}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)
    def construct(self):
        self.camera.background_color = self.bg_color
        self.add(self.build_release_teaser())
'''
    with open(runner_script, "w", encoding="utf-8") as f:
        f.write(code)

    proof_paths = {}
    media_dir = output_concept_dir / "media"

    beats = [
        ("beat_1", "Beat1Proof", "1. Syllabus Header"),
        ("beat_2", "Beat2Proof", "2. Hero Visual"),
        ("beat_3", "Beat3Proof", "3. Core Principle & Formula"),
        ("beat_4", "Beat4Proof", "4. NEET Trap Card"),
        ("beat_5", "Beat5Proof", "5. Up Next Teaser Tile")
    ]

    for b_key, scene_name, b_desc in beats:
        clean_corrupted_svg_cache()
        cmd = ["manim", "-s", "-qh", "--media_dir", str(media_dir), str(runner_script), scene_name]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
        
        if res.returncode != 0:
            print(f"   ❌ Error rendering {b_desc}: {res.stderr[-300:]}")
            continue

        pngs = list(media_dir.glob(f"**/{scene_name}*.png"))
        if pngs:
            pngs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
            dest_png = output_concept_dir / f"{canonical_id}_{b_key}.png"
            shutil.copyfile(pngs[0], dest_png)
            proof_paths[b_key] = str(dest_png)
            
            # Copy to brain artifact directory
            brain_dest = BRAIN_ARTIFACT_DIR / f"proof_{canonical_id}_{b_key}.png"
            shutil.copyfile(pngs[0], brain_dest)
            proof_paths[f"{b_key}_brain"] = str(brain_dest)
            print(f"      ✓ {b_desc}: {dest_png.name}")

    return proof_paths

def process_unit(csv_path: str, auto_approve: bool = False):
    clean_corrupted_svg_cache()
    csv_file = Path(csv_path)
    if not csv_file.exists():
        print(f"❌ Error: CSV file '{csv_path}' does not exist.")
        return

    print("=" * 80)
    print(f"🛡️ PRE-FLIGHT VERIFICATION GATEKEEPER: {csv_file.name}")
    print("=" * 80)

    with open(csv_file, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    unit_name = csv_file.stem
    unit_proof_dir = PROOF_DIR / unit_name
    unit_proof_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    total_concepts = len(rows)

    print(f"📋 Loaded {total_concepts} concepts for verification.")
    
    storyboard_lines = [
        f"# Pre-Flight Visual Verification Storyboard: {unit_name.replace('_', ' ').title()}",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Source Curriculum:** [`{csv_file.name}`](file:///{str(csv_file).replace(chr(92), '/')})",
        "",
        "> [!IMPORTANT]",
        "> **Human-in-the-Loop Proof Gate:** Every concept below has 5 static proof screenshots (Header, Hero Visual, Formula, NEET Trap, Up Next Teaser).",
        "> Confirm the pedagogical accuracy and typography before releasing to video render.",
        "",
        "---",
        ""
    ]

    for idx, row in enumerate(rows):
        cid = row["canonical_id"]
        title = row["concept_title"]
        tpl = row["template_name"]
        ncert = row.get("ncert_citation", "NCERT Class 11 Part 1")
        trap = row.get("neet_trap_point", "")
        pyq = row.get("pyq_years", "N/A")

        print(f"\n[{idx+1}/{total_concepts}] Verifying {cid}: {title} ({tpl})...")

        # Stage 1: Typography Audit
        typo_warnings = audit_typography(row)
        if typo_warnings:
            print(f"   ⚠️ Typography Warning:")
            for tw in typo_warnings:
                print(f"      - {tw}")

        # Stage 2: Proof Generation
        concept_dir = unit_proof_dir / cid
        proof_data = generate_concept_proofs(row, concept_dir)

        # Update Manifest
        current_status = manifest.get(cid, {}).get("status", "PENDING_REVIEW")
        if auto_approve:
            current_status = "APPROVED"

        manifest[cid] = {
            "canonical_id": cid,
            "concept_title": title,
            "template_name": tpl,
            "status": current_status,
            "last_verified_at": datetime.now().isoformat(),
            "proofs": proof_data,
            "ncert_citation": ncert,
            "typo_warnings_count": len(typo_warnings)
        }

        # Add to Storyboard
        badge = "🟢 APPROVED" if current_status == "APPROVED" else "🟡 PENDING REVIEW"
        
        b1_img = proof_data.get("beat_1_brain", "").replace("\\", "/")
        b2_img = proof_data.get("beat_2_brain", "").replace("\\", "/")
        b3_img = proof_data.get("beat_3_brain", "").replace("\\", "/")
        b4_img = proof_data.get("beat_4_brain", "").replace("\\", "/")
        b5_img = proof_data.get("beat_5_brain", "").replace("\\", "/")

        storyboard_lines.extend([
            f"## Concept {idx+1}: {cid} — {title}",
            f"**Status:** {badge} | **Template:** `{tpl}` | **PYQ:** `{pyq}`",
            f"**NCERT Citation:** *{ncert}*",
            "",
            "````carousel",
            f"![Beat 1: Header Settle](/{b1_img})" if b1_img else "![Beat 1 Pending]()",
            "<!-- slide -->",
            f"![Beat 2: Hero Visual](/{b2_img})" if b2_img else "![Beat 2 Pending]()",
            "<!-- slide -->",
            f"![Beat 3: Core Principle & Formula](/{b3_img})" if b3_img else "![Beat 3 Pending]()",
            "<!-- slide -->",
            f"![Beat 4: NEET Distractor Trap](/{b4_img})" if b4_img else "![Beat 4 Pending]()",
            "<!-- slide -->",
            f"![Beat 5: Up Next Teaser Tile](/{b5_img})" if b5_img else "![Beat 5 Pending]()",
            "````",
            "",
            f"**NEET Distractor Trap:**",
            f"> [!CAUTION]",
            f"> {trap}",
            "",
            "---",
            ""
        ])

    save_manifest(manifest)

    # Write Storyboard Artifact
    storyboard_path = unit_proof_dir / "storyboard.md"
    with open(storyboard_path, "w", encoding="utf-8") as f:
        f.write("\n".join(storyboard_lines))

    # Also write to Brain Artifact directory
    brain_storyboard = BRAIN_ARTIFACT_DIR / f"{unit_name}_preflight_storyboard.md"
    with open(brain_storyboard, "w", encoding="utf-8") as f:
        f.write("\n".join(storyboard_lines))

    print("\n" + "=" * 80)
    print(f"✅ PRE-FLIGHT VERIFICATION COMPLETE!")
    print(f"   Manifest: {MANIFEST_PATH}")
    print(f"   Storyboard: {storyboard_path}")
    print(f"   Brain Artifact: {brain_storyboard}")
    print("=" * 80)

def approve_concept(canonical_id: str, status: str = "APPROVED"):
    manifest = load_manifest()
    if canonical_id == "ALL":
        for k in manifest:
            manifest[k]["status"] = status
            manifest[k]["approved_at"] = datetime.now().isoformat()
        print(f"✓ All concepts marked as {status}!")
    elif canonical_id in manifest:
        manifest[canonical_id]["status"] = status
        manifest[canonical_id]["approved_at"] = datetime.now().isoformat()
        print(f"✓ Concept {canonical_id} marked as {status}!")
    else:
        print(f"❌ Error: Concept {canonical_id} not found in manifest.")
    save_manifest(manifest)

def show_status():
    manifest = load_manifest()
    if not manifest:
        print("Manifest is empty. Run preflight verification first.")
        return

    print("=" * 80)
    print(f"{'Canonical ID':<18} | {'Status':<16} | {'Template':<28} | Concept Title")
    print("-" * 80)
    for cid, data in manifest.items():
        st = data.get("status", "UNVERIFIED")
        tpl = data.get("template_name", "N/A")
        title = data.get("concept_title", "")
        print(f"{cid:<18} | {st:<16} | {tpl:<28} | {title}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pre-Flight Visual Verification Gatekeeper")
    parser.add_argument("--unit", type=str, help="Path to unit curriculum CSV")
    parser.add_argument("--approve", type=str, help="Canonical ID to approve (or 'ALL')")
    parser.add_argument("--reject", type=str, help="Canonical ID to reject")
    parser.add_argument("--status", action="store_true", help="Display current approval status of all concepts")
    args = parser.parse_args()

    if args.approve:
        approve_concept(args.approve, status="APPROVED")
    elif args.reject:
        approve_concept(args.reject, status="REJECTED")
    elif args.status:
        show_status()
    elif args.unit:
        process_unit(args.unit)
    else:
        parser.print_help()
