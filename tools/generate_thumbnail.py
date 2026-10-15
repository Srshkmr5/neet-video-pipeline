"""
Automated Minimalist Thumbnail Generator
Generates high-contrast, recognizable, traceable 1920x1080 thumbnails
with subject color coding, sequence pills, hero formula cards, and PYQ badges.
"""

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
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

from PIL import Image, ImageDraw, ImageFont
from config import QUEUE_DIR, OUTPUT_DIR
from render.templates.base import format_math_unicode

THUMBNAILS_DIR = OUTPUT_DIR / "thumbnails"
THUMBNAILS_DIR.mkdir(parents=True, exist_ok=True)

# Subject Color Coding Themes
THEMES = {
    "Physics": {
        "bg_base": (11, 15, 25),          # Deep Navy Slate #0B0F19
        "accent": (56, 189, 248),         # Sky Cyan #38BDF8
        "accent_dark": (2, 132, 199),     # Cobalt Blue #0284C7
        "hero_border": (56, 189, 248),
        "card_fill": (18, 24, 38),
        "pill_bg": (23, 37, 84),
        "glow": (14, 165, 233, 40)
    },
    "Chemistry": {
        "bg_base": (8, 20, 15),           # Deep Emerald Slate #08140F
        "accent": (16, 185, 129),         # Emerald Mint #10B981
        "accent_dark": (5, 150, 105),     # Deep Emerald #059669
        "hero_border": (16, 185, 129),
        "card_fill": (13, 31, 24),
        "pill_bg": (6, 78, 59),
        "glow": (16, 185, 129, 40)
    },
    "Biology": {
        "bg_base": (24, 13, 9),           # Deep Coral Slate #180D09
        "accent": (251, 146, 60),         # Sunset Coral #FB923C
        "accent_dark": (234, 88, 12),     # Rust Amber #EA580C
        "hero_border": (251, 146, 60),
        "card_fill": (38, 21, 15),
        "pill_bg": (124, 45, 18),
        "glow": (249, 115, 22, 40)
    }
}

GOLD_ACCENT = (245, 158, 11)   # #F59E0B
TEXT_WHITE = (255, 255, 255)
TEXT_MUTED = (148, 163, 184)   # Slate 400

def get_font(size: int, bold: bool = False):
    font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
    try:
        return ImageFont.truetype(font_name, size)
    except Exception:
        fallback = "arialbd.ttf" if bold else "arial.ttf"
        try:
            return ImageFont.truetype(fallback, size)
        except Exception:
            return ImageFont.load_default()

def draw_rounded_pill(draw: ImageDraw.ImageDraw, box, radius: int, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def draw_star(draw: ImageDraw.ImageDraw, cx: float, cy: float, r_outer: float, r_inner: float, fill: Tuple[int, int, int]):
    points = []
    for i in range(10):
        r = r_outer if i % 2 == 0 else r_inner
        angle = i * math.pi / 5 - math.pi / 2
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(points, fill=fill)

def generate_thumbnail_image(data: Dict[str, Any], output_path: Path) -> Path:
    width, height = 1920, 1080
    subject = data.get("subject", "Physics")
    grade = data.get("grade", 11)
    canonical_id = data.get("canonical_id", "P11-C02-T03-V02")
    concept_title = data.get("concept_title", "Concept Analysis").strip()
    chapter_name = data.get("chapter_name", "Curriculum Topic").strip()
    topic_name = data.get("topic_name", "").strip()
    plain_formula = data.get("plain_formula", "").strip() or data.get("latex_formula", "").strip()
    ch_seq = int(data.get("chapter_seq", 1))
    total_ch = int(data.get("total_chapter_videos", 14))
    pyq_years = str(data.get("pyq_years", "")).strip()

    theme = THEMES.get(subject, THEMES["Physics"])

    # 1. Base Image with Subtle Gradient
    img = Image.new("RGBA", (width, height), theme["bg_base"])
    draw = ImageDraw.Draw(img)

    # Subtle radial glow from center-top
    glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)
    center_x, center_y = width // 2, int(height * 0.45)
    for r in range(450, 50, -30):
        alpha = int(35 * (1.0 - (r / 450.0)))
        glow_color = theme["accent"] + (alpha,)
        glow_draw.ellipse([center_x - r * 1.6, center_y - r, center_x + r * 1.6, center_y + r], fill=glow_color)
    img = Image.alpha_composite(img, glow_layer)
    draw = ImageDraw.Draw(img)

    # 2. Header: Subject Badge (Top-Left)
    ch_num = data.get("chapter_no", data.get("chapter_seq", 2))
    top_num = data.get("topic_no", 3)
    vid_num = data.get("video_no", 2)
    neet_code = data.get("neet_code") or f"{ch_num}.{top_num}.{vid_num}"

    subj_font = get_font(26, bold=True)
    subj_label = f"{subject.upper()} • CLASS {grade}"
    bbox_subj = draw.textbbox((0, 0), subj_label, font=subj_font)
    subj_w = bbox_subj[2] - bbox_subj[0] + 44
    subj_box = [80, 70, 80 + subj_w, 70 + 52]
    draw_rounded_pill(draw, subj_box, radius=12, fill=theme["pill_bg"], outline=theme["accent"], width=2)
    draw.text((102, 78), subj_label, font=subj_font, fill=theme["accent"])

    # 2b. Header: Centered Syllabus Code & Topic Name for Uniformity & Quick Recognition
    s_label = f"S.{neet_code}   |   {topic_name.upper()}" if topic_name else f"S.{neet_code}"
    s_font = get_font(26, bold=True)
    bbox_s = draw.textbbox((0, 0), s_label, font=s_font)
    s_text_w = bbox_s[2] - bbox_s[0]
    s_w = s_text_w + 48
    s_box = [center_x - s_w // 2, 70, center_x + s_w // 2, 70 + 52]
    # Distinct Rose / Coral pill for syllabus coordinate
    draw_rounded_pill(draw, s_box, radius=12, fill=(59, 7, 22), outline=(244, 63, 94), width=2)
    draw.text((center_x - s_text_w // 2, 78), s_label, font=s_font, fill=(251, 113, 133))

    # 3. Header: Sequence Progress & Canonical ID (Top-Right)
    seq_font = get_font(28, bold=True)
    seq_str = f"[ {ch_seq:02d} / {total_ch:02d} ]"
    id_str = canonical_id
    full_right_str = f"{seq_str}   {id_str}"
    bbox_seq = draw.textbbox((0, 0), full_right_str, font=seq_font)
    seq_w = bbox_seq[2] - bbox_seq[0] + 48
    seq_box = [width - 80 - seq_w, 70, width - 80, 70 + 52]
    draw_rounded_pill(draw, seq_box, radius=12, fill=(15, 23, 42), outline=theme["accent_dark"], width=2)
    draw.text((width - 80 - seq_w + 24, 78), full_right_str, font=seq_font, fill=TEXT_WHITE)

    # 4. Center Hero Graphic / Formula Card
    card_w, card_h = 1320, 420
    card_x1 = (width - card_w) // 2
    card_y1 = int(height * 0.22)
    card_box = [card_x1, card_y1, card_x1 + card_w, card_y1 + card_h]

    # Double-border card with glowing stroke
    draw_rounded_pill(draw, card_box, radius=24, fill=theme["card_fill"], outline=theme["hero_border"], width=3)

    # Formula inside Hero Card
    is_fraction = False
    if plain_formula and "=" in plain_formula and "/" in plain_formula:
        parts_eq = plain_formula.split("=")
        lhs = parts_eq[0].strip() + " ="
        rhs = parts_eq[1].strip()
        if "/" in rhs and rhs.count("/") == 1:
            is_fraction = True
            parts_frac = rhs.split("/")
            num_raw = parts_frac[0].strip()
            den_raw = parts_frac[1].strip()

            def clean_math(s: str) -> str:
                res = s.strip()
                if res.startswith("(") and res.endswith(")"):
                    res = res[1:-1].strip()
                return format_math_unicode(res)

            clean_num = clean_math(num_raw)
            clean_den = clean_math(den_raw)

            f_font_size = 56
            lhs_font = get_font(f_font_size, bold=True)
            num_font = get_font(f_font_size - 4, bold=True)
            den_font = get_font(f_font_size - 4, bold=True)

            bbox_lhs = draw.textbbox((0, 0), lhs, font=lhs_font)
            bbox_num = draw.textbbox((0, 0), clean_num, font=num_font)
            bbox_den = draw.textbbox((0, 0), clean_den, font=den_font)

            w_lhs = bbox_lhs[2] - bbox_lhs[0]
            h_lhs = bbox_lhs[3] - bbox_lhs[1]
            w_num = bbox_num[2] - bbox_num[0]
            h_num = bbox_num[3] - bbox_num[1]
            w_den = bbox_den[2] - bbox_den[0]
            h_den = bbox_den[3] - bbox_den[1]

            frac_w = max(w_num, w_den) + 50
            total_formula_w = w_lhs + 35 + frac_w

            start_x = card_x1 + (card_w - total_formula_w) // 2
            center_y = card_y1 + (card_h // 2) - 15

            # LHS position
            draw.text((start_x, center_y - (h_lhs // 2)), lhs, font=lhs_font, fill=TEXT_WHITE)

            # Fraction bar
            bar_x1 = start_x + w_lhs + 35
            bar_x2 = bar_x1 + frac_w
            bar_y = center_y + 4
            draw.line([(bar_x1, bar_y), (bar_x2, bar_y)], fill=GOLD_ACCENT, width=4)

            # Numerator position (centered over bar)
            num_x = bar_x1 + (frac_w - w_num) // 2
            num_y = bar_y - h_num - 20
            draw.text((num_x, num_y), clean_num, font=num_font, fill=GOLD_ACCENT)

            # Denominator position (centered under bar)
            den_x = bar_x1 + (frac_w - w_den) // 2
            den_y = bar_y + 16
            draw.text((den_x, den_y), clean_den, font=den_font, fill=GOLD_ACCENT)

    if not is_fraction and plain_formula:
        plain_formula = format_math_unicode(plain_formula)
        # Scale font to fit card
        formula_font_size = 56 if len(plain_formula) < 35 else (44 if len(plain_formula) < 55 else 36)
        formula_font = get_font(formula_font_size, bold=True)
        bbox_f = draw.textbbox((0, 0), plain_formula, font=formula_font)
        fw, fh = bbox_f[2] - bbox_f[0], bbox_f[3] - bbox_f[1]
        fx = card_x1 + (card_w - fw) // 2
        fy = card_y1 + (card_h - fh) // 2 - 15
        draw.text((fx, fy), plain_formula, font=formula_font, fill=TEXT_WHITE)
    elif not is_fraction and not plain_formula:
        # Fallback Graphic Label
        hero_label = f"KEY CONCEPT: {concept_title.upper()}"
        formula_font = get_font(48, bold=True)
        bbox_f = draw.textbbox((0, 0), hero_label, font=formula_font)
        fw = bbox_f[2] - bbox_f[0]
        fx = card_x1 + (card_w - fw) // 2
        fy = card_y1 + (card_h - 60) // 2
        draw.text((fx, fy), hero_label, font=formula_font, fill=theme["accent"])

    # Hero card bottom watermark tag
    card_tag = f"CORE FORMULA & PRINCIPLE"
    tag_font = get_font(20, bold=True)
    bbox_tag = draw.textbbox((0, 0), card_tag, font=tag_font)
    draw.text((card_x1 + (card_w - (bbox_tag[2] - bbox_tag[0])) // 2, card_y1 + card_h - 45), card_tag, font=tag_font, fill=theme["accent_dark"])

    # 5. Bottom Section: Bold Title & Chapter Path (Bottom-Left)
    title_font = get_font(54, bold=True)
    # Truncate title if extremely long
    display_title = concept_title.upper() if len(concept_title) < 42 else (concept_title[:40].upper() + "...")
    draw.text((80, height - 240), display_title, font=title_font, fill=TEXT_WHITE)

    subtitle_font = get_font(30, bold=False)
    sub_path = f"Chapter: {chapter_name}" if chapter_name else ""
    draw.text((82, height - 165), sub_path, font=subtitle_font, fill=TEXT_MUTED)

    # 6. Bottom Section: High-Yield / PYQ Badge (Bottom-Right)
    if pyq_years and pyq_years.lower() != "nan":
        badge_str = f"HIGH YIELD | PYQ: {pyq_years}"
    else:
        badge_str = "NEET HIGH YIELD CORE"

    badge_font = get_font(28, bold=True)
    bbox_b = draw.textbbox((0, 0), badge_str, font=badge_font)
    text_w = bbox_b[2] - bbox_b[0]
    star_spacing = 38
    badge_w = text_w + star_spacing + 54
    badge_box = [width - 80 - badge_w, height - 195, width - 80, height - 135]
    draw_rounded_pill(draw, badge_box, radius=14, fill=(30, 20, 5), outline=GOLD_ACCENT, width=2)
    
    # Draw vector gold star
    star_cx = width - 80 - badge_w + 30
    star_cy = height - 165
    draw_star(draw, star_cx, star_cy, r_outer=13, r_inner=6, fill=GOLD_ACCENT)
    
    draw.text((width - 80 - badge_w + 50, height - 180), badge_str, font=badge_font, fill=GOLD_ACCENT)

    # Save Thumbnail
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img = img.convert("RGB")
    img.save(str(output_path), "PNG", quality=95)
    return output_path

def generate_demo_thumbnails() -> Dict[str, Path]:
    demos = [
        {
            "canonical_id": "P11-C02-T03-V02",
            "subject": "Physics",
            "grade": 11,
            "chapter_no": 2,
            "topic_no": 3,
            "video_no": 2,
            "neet_code": "2.3.2",
            "chapter_name": "Kinematics",
            "topic_name": "Projectile Motion",
            "concept_title": "The Max Height Arc",
            "plain_formula": "H_max = (v0^2 * sin^2 θ) / 2g",
            "chapter_seq": 4,
            "total_chapter_videos": 14,
            "pyq_years": "2017, 2019, 2024"
        },
        {
            "canonical_id": "C12-C01-T02-V01",
            "subject": "Chemistry",
            "grade": 12,
            "chapter_no": 1,
            "topic_no": 2,
            "video_no": 1,
            "neet_code": "1.2.1",
            "chapter_name": "Solutions",
            "topic_name": "Colligative Properties",
            "concept_title": "Osmotic Pressure & Van't Hoff",
            "plain_formula": "π = i * C * R * T",
            "chapter_seq": 3,
            "total_chapter_videos": 10,
            "pyq_years": "2018, 2021, 2023"
        },
        {
            "canonical_id": "B12-C05-T02-V01",
            "subject": "Biology",
            "grade": 12,
            "chapter_no": 5,
            "topic_no": 2,
            "video_no": 1,
            "neet_code": "5.2.1",
            "chapter_name": "Molecular Basis of Inheritance",
            "topic_name": "Replication Fork",
            "concept_title": "DNA Replication Mechanics",
            "plain_formula": "5' -> 3' Leading & Lagging Strands",
            "chapter_seq": 2,
            "total_chapter_videos": 15,
            "pyq_years": "2016, 2020, 2024"
        }
    ]

    out_paths = {}
    for demo in demos:
        cid = demo["canonical_id"]
        out_p = THUMBNAILS_DIR / f"{cid}_thumbnail.png"
        generate_thumbnail_image(demo, out_p)
        out_paths[cid] = out_p
        print(f"✅ Generated {demo['subject']} Demo Thumbnail: {out_p}")

    return out_paths

def generate_from_csv(canonical_id: Optional[str] = None, batch_all: bool = False):
    csv_path = QUEUE_DIR / "curriculum_master_full_665.csv"
    if not csv_path.exists():
        print(f"❌ {csv_path} not found.")
        return

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    count = 0
    for r in rows:
        cid = r.get("canonical_id", "")
        if not cid:
            continue

        if not batch_all and canonical_id and cid != canonical_id:
            continue

        out_p = THUMBNAILS_DIR / f"{cid}_thumbnail.png"
        generate_thumbnail_image(r, out_p)
        count += 1
        if not batch_all:
            print(f"✅ Generated Thumbnail for [{cid}]: {out_p}")
            break

    if batch_all:
        print(f"\n🎉 Successfully batch generated {count} thumbnails in {THUMBNAILS_DIR}!")

def main():
    parser = argparse.ArgumentParser(description="Automated Minimalist Thumbnail Generator")
    parser.add_argument("--id", type=str, help="Generate thumbnail for a specific Canonical ID")
    parser.add_argument("--all", action="store_true", help="Batch generate thumbnails for all videos in curriculum")
    parser.add_argument("--demo", action="store_true", help="Generate 3 demo thumbnails for Physics, Chemistry, and Biology")
    args = parser.parse_args()

    if args.demo:
        generate_demo_thumbnails()
    elif args.id:
        generate_from_csv(canonical_id=args.id)
    elif args.all:
        generate_from_csv(batch_all=True)
    else:
        # Default run demo
        generate_demo_thumbnails()

if __name__ == "__main__":
    main()
