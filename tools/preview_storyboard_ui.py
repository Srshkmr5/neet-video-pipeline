"""
Storyboard UI Archetype Generator & Visualizer
Renders 1080p preview stills for the 5 Standardized Obsidian-Neon Storyboard UI Archetypes,
adhering to the distraction-free "Visual Physics" aesthetic.
"""

import math
from pathlib import Path
from typing import Tuple, List, Dict, Any
from PIL import Image, ImageDraw, ImageFont
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

OUTPUT_DIR = BASE_DIR / "output" / "storyboards"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Standard Color Tokens (Obsidian-Neon System)
COLOR_BG = (2, 4, 8)                # Pure Obsidian Void #020408
COLOR_CARD_BG = (10, 15, 26)        # Dark Slate Card #0A0F1A
COLOR_BORDER_SLATE = (30, 41, 59)   # Slate 800 #1E293B
COLOR_GRID = (15, 23, 42)           # Subtle Grid #0F172A

COLOR_CYAN = (56, 189, 248)         # Velocity / Primary Flow #38BDF8
COLOR_AMBER = (245, 158, 11)        # Acceleration / Traps #F59E0B
COLOR_CORAL = (244, 63, 94)         # Force / Gravity #F43F5E
COLOR_EMERALD = (16, 185, 129)      # Energy / Chemistry #10B981
COLOR_WHITE = (255, 255, 255)
COLOR_MUTED = (148, 163, 184)       # Slate 400

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

def draw_star(draw: ImageDraw.ImageDraw, cx: float, cy: float, r_outer: float, r_inner: float, fill: Tuple[int, int, int]):
    points = []
    for i in range(10):
        r = r_outer if i % 2 == 0 else r_inner
        angle = i * math.pi / 5 - math.pi / 2
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(points, fill=fill)

def draw_header_and_footer(draw: ImageDraw.ImageDraw, width: int, height: int, subject: str, code: str, title: str, subtitle: str, badge_text: str = "★ HIGH YIELD"):
    # Top-Left Subject Pill
    f_pill = get_font(24, bold=True)
    draw.rounded_rectangle([70, 50, 360, 100], radius=10, fill=(15, 23, 42), outline=COLOR_CYAN, width=2)
    draw.text((95, 62), f"{subject.upper()} • NEET 2026", font=f_pill, fill=COLOR_CYAN)

    # Top-Right Canonical Code Pill
    bbox_code = draw.textbbox((0, 0), code, font=f_pill)
    code_w = bbox_code[2] - bbox_code[0] + 50
    code_x1 = width - 70 - code_w
    draw.rounded_rectangle([code_x1, 50, width - 70, 100], radius=10, fill=(15, 23, 42), outline=COLOR_BORDER_SLATE, width=2)
    draw.text((code_x1 + 25, 62), code, font=f_pill, fill=COLOR_WHITE)

    # Bottom-Left Title & Subtitle
    f_title = get_font(46, bold=True)
    f_sub = get_font(26, bold=False)
    draw.text((70, height - 165), title.upper(), font=f_title, fill=COLOR_WHITE)
    draw.text((72, height - 105), subtitle, font=f_sub, fill=COLOR_MUTED)

    # Bottom-Right PYQ Badge
    if badge_text:
        f_b = get_font(26, bold=True)
        bbox = draw.textbbox((0, 0), badge_text, font=f_b)
        bw = bbox[2] - bbox[0] + 65
        bx1 = width - 70 - bw
        draw.rounded_rectangle([bx1, height - 150, width - 70, height - 95], radius=12, fill=(30, 20, 5), outline=COLOR_AMBER, width=2)
        draw_star(draw, bx1 + 30, height - 123, 11, 5, fill=COLOR_AMBER)
        draw.text((bx1 + 50, height - 138), badge_text, font=f_b, fill=COLOR_AMBER)

# -------------------------------------------------------------
# ARCHETYPE 1: THE KINETIC VECTOR STAGE
# -------------------------------------------------------------
def render_archetype_1() -> Path:
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Faint Isometric Grid Floor
    ground_y = 780
    for x in range(100, w - 100, 120):
        draw.line([(x, ground_y), (x + 80, ground_y + 120)], fill=(20, 30, 48), width=1)
    draw.line([(80, ground_y), (w - 80, ground_y)], fill=(35, 50, 75), width=2)

    # Parabolic Trajectory Arc (Dotted Glowing Sky Cyan)
    start_x, start_y = 250, ground_y
    apex_x, apex_y = 960, 340
    end_x, end_y = 1670, ground_y
    
    # Calculate parabola: y = a*(x - apex_x)^2 + apex_y
    a = (ground_y - apex_y) / ((start_x - apex_x) ** 2)
    pts = []
    for px in range(start_x, end_x + 1, 6):
        py = a * ((px - apex_x) ** 2) + apex_y
        pts.append((px, py))

    for i in range(len(pts) - 1):
        if (i // 2) % 2 == 0:  # dashed neon trail
            draw.line([pts[i], pts[i + 1]], fill=COLOR_CYAN, width=3)

    # Apex Vertical Drop Line
    draw.line([(apex_x, apex_y), (apex_x, ground_y)], fill=(50, 70, 100), width=2)
    f_drop = get_font(24, bold=True)
    draw.text((apex_x + 15, (apex_y + ground_y) // 2), "H_max = 10.2 m", font=f_drop, fill=COLOR_AMBER)

    # Particle at Apex (Glowing Sphere)
    pr = 24
    draw.ellipse([apex_x - pr - 8, apex_y - pr - 8, apex_x + pr + 8, apex_y + pr + 8], fill=(56, 189, 248, 50))
    draw.ellipse([apex_x - pr, apex_y - pr, apex_x + pr, apex_y + pr], fill=COLOR_WHITE)

    # Vector 1: Velocity vx (Cyan Arrow Right)
    vx_len = 220
    draw.line([(apex_x + pr, apex_y), (apex_x + pr + vx_len, apex_y)], fill=COLOR_CYAN, width=6)
    draw.polygon([(apex_x + pr + vx_len, apex_y - 12), (apex_x + pr + vx_len + 25, apex_y), (apex_x + pr + vx_len, apex_y + 12)], fill=COLOR_CYAN)
    f_vec = get_font(28, bold=True)
    draw.text((apex_x + pr + vx_len + 35, apex_y - 16), "v_x = v₀ cos θ (CONST)", font=f_vec, fill=COLOR_CYAN)

    # Vector 2: Acceleration ay / g (Amber Arrow Down)
    g_len = 160
    draw.line([(apex_x, apex_y + pr), (apex_x, apex_y + pr + g_len)], fill=COLOR_AMBER, width=6)
    draw.polygon([(apex_x - 12, apex_y + pr + g_len), (apex_x, apex_y + pr + g_len + 25), (apex_x + 12, apex_y + pr + g_len)], fill=COLOR_AMBER)
    draw.text((apex_x - 180, apex_y + pr + g_len - 30), "a_y = - g", font=f_vec, fill=COLOR_AMBER)

    # Apex State Flag Pill
    draw.rounded_rectangle([apex_x - 160, apex_y - 95, apex_x + 160, apex_y - 45], radius=10, fill=(30, 20, 5), outline=COLOR_AMBER, width=2)
    f_flag = get_font(24, bold=True)
    draw.text((apex_x - 138, apex_y - 83), "APEX: v_y = 0 m/s", font=f_flag, fill=COLOR_AMBER)

    # Telemetry HUD Card (Top-Left)
    hud_box = [80, 150, 480, 410]
    draw.rounded_rectangle(hud_box, radius=14, fill=COLOR_CARD_BG, outline=COLOR_BORDER_SLATE, width=2)
    draw.rounded_rectangle([hud_box[0], hud_box[1], hud_box[2], hud_box[1] + 45], radius=14, fill=(15, 23, 42))
    f_hud_h = get_font(20, bold=True)
    draw.text((105, 162), "LIVE TELEMETRY HUD • P11-C02", font=f_hud_h, fill=COLOR_CYAN)

    f_hud_d = get_font(24, bold=False)
    f_hud_db = get_font(24, bold=True)
    rows = [
        ("Time Elapsed (t):", "1.84 s"),
        ("Horizontal (vx):", "14.1 m/s"),
        ("Vertical (vy):", "0.0 m/s [ZERO]"),
        ("Altitude (y):", "10.20 m"),
        ("Launch Angle (θ):", "45.0°")
    ]
    for idx, (lbl, val) in enumerate(rows):
        yy = 215 + idx * 36
        draw.text((105, yy), lbl, font=f_hud_d, fill=COLOR_MUTED)
        draw.text((320, yy), val, font=f_hud_db, fill=COLOR_WHITE if "ZERO" not in val else COLOR_AMBER)

    draw_header_and_footer(
        draw, w, h,
        subject="Physics",
        code="ARCHETYPE 01 • KINETIC STAGE",
        title="Projectile Apex Mechanics",
        subtitle="Kinematics • 3D Vector Stage with Live Telemetry HUD",
        badge_text="HIGH YIELD | PYQ: 2017, 2024"
    )

    out_p = OUTPUT_DIR / "archetype_1_kinetic_stage.png"
    img.convert("RGB").save(str(out_p), "PNG", quality=95)
    return out_p

# -------------------------------------------------------------
# ARCHETYPE 2: DUAL-PANE ORTHOGONAL SPLIT (SIM + LIVE GRAPH)
# -------------------------------------------------------------
def render_archetype_2() -> Path:
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), COLOR_BG)
    draw = ImageDraw.Draw(img)

    mid_x = w // 2
    # Vertical Split Divider
    draw.line([(mid_x, 140), (mid_x, h - 180)], fill=COLOR_BORDER_SLATE, width=2)

    # 1. Left Pane: Physical Simulation (50%)
    f_tag = get_font(22, bold=True)
    b_tag1 = draw.textbbox((0, 0), "SIMULATION PANE: 1D KINETIC MOTION", font=f_tag)
    w_tag1 = b_tag1[2] - b_tag1[0] + 44
    draw.rounded_rectangle([80, 140, 80 + w_tag1, 185], radius=8, fill=(15, 23, 42), outline=COLOR_CYAN, width=1)
    draw.text((102, 150), "SIMULATION PANE: 1D KINETIC MOTION", font=f_tag, fill=COLOR_CYAN)

    track_y = 520
    # Frictionless Track
    draw.line([(100, track_y + 60), (mid_x - 80, track_y + 60)], fill=(35, 50, 75), width=4)
    for tx in range(120, mid_x - 80, 80):
        draw.line([(tx, track_y + 60), (tx - 20, track_y + 85)], fill=(20, 30, 48), width=2)

    # Mass Block
    bx, by, bw, bh = 420, track_y - 70, 180, 130
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(20, 35, 60), outline=COLOR_CYAN, width=3)
    f_block = get_font(36, bold=True)
    draw.text((bx + 40, by + 40), "m = 2kg", font=f_block, fill=COLOR_WHITE)

    # Velocity Vector on Block
    draw.line([(bx + bw, by + bh // 2), (bx + bw + 180, by + bh // 2)], fill=COLOR_CYAN, width=6)
    draw.polygon([(bx + bw + 180, by + bh // 2 - 12), (bx + bw + 205, by + bh // 2), (bx + bw + 180, by + bh // 2 + 12)], fill=COLOR_CYAN)
    f_v = get_font(28, bold=True)
    draw.text((bx + bw + 40, by + bh // 2 - 45), "v = 20 m/s", font=f_v, fill=COLOR_CYAN)

    f_sub_lbl = get_font(24, bold=False)
    draw.text((100, 680), "• Motion is along a frictionless horizontal axis (+x)", font=f_sub_lbl, fill=COLOR_MUTED)
    draw.text((100, 720), "• Velocity is uniform; net acceleration a = 0", font=f_sub_lbl, fill=COLOR_MUTED)

    # 2. Right Pane: Synchronized v-t Graph (50%)
    b_tag2 = draw.textbbox((0, 0), "SYNCHRONIZED PHASE GRAPH: v-t CURVE", font=f_tag)
    w_tag2 = b_tag2[2] - b_tag2[0] + 44
    draw.rounded_rectangle([mid_x + 80, 140, mid_x + 80 + w_tag2, 185], radius=8, fill=(15, 23, 42), outline=COLOR_EMERALD, width=1)
    draw.text((mid_x + 102, 150), "SYNCHRONIZED PHASE GRAPH: v-t CURVE", font=f_tag, fill=COLOR_EMERALD)

    gx0, gy0 = mid_x + 120, 680
    gw, gh = 660, 380
    
    # Graph Axes
    draw.line([(gx0, gy0), (gx0 + gw, gy0)], fill=COLOR_WHITE, width=2)        # t-axis
    draw.line([(gx0, gy0), (gx0, gy0 - gh)], fill=COLOR_WHITE, width=2)        # v-axis
    f_axis = get_font(24, bold=True)
    draw.text((gx0 + gw + 15, gy0 - 15), "t (s)", font=f_axis, fill=COLOR_WHITE)
    draw.text((gx0 - 15, gy0 - gh - 35), "v (m/s)", font=f_axis, fill=COLOR_WHITE)

    # Graph Area (Integral = Displacement)
    t_end_x = gx0 + 440
    v_level_y = gy0 - 240
    draw.rectangle([gx0 + 2, v_level_y, t_end_x, gy0 - 2], fill=(16, 185, 129, 45))
    draw.line([(gx0, v_level_y), (t_end_x, v_level_y)], fill=COLOR_EMERALD, width=4)
    draw.line([(t_end_x, v_level_y), (t_end_x, gy0)], fill=(16, 185, 129, 140), width=2)

    # Active Plotting Cursor
    draw.ellipse([t_end_x - 12, v_level_y - 12, t_end_x + 12, v_level_y + 12], fill=COLOR_WHITE, outline=COLOR_EMERALD, width=3)
    f_area = get_font(30, bold=True)
    draw.text((gx0 + 110, v_level_y + 90), "SHADED AREA = Δx", font=f_area, fill=COLOR_EMERALD)
    draw.text((gx0 + 130, v_level_y + 135), "Δx = 20 m/s × 4s = 80 m", font=get_font(24, bold=False), fill=COLOR_WHITE)

    draw_header_and_footer(
        draw, w, h,
        subject="Physics",
        code="ARCHETYPE 02 • ORTHOGONAL SPLIT",
        title="Velocity-Time Integral & Displacement",
        subtitle="Sim-to-Graph Dual Synchronized Architecture (50/50 Split)",
        badge_text="HIGH YIELD | GRAPH RULE"
    )

    out_p = OUTPUT_DIR / "archetype_2_orthogonal_split.png"
    img.convert("RGB").save(str(out_p), "PNG", quality=95)
    return out_p

# -------------------------------------------------------------
# ARCHETYPE 3: MOLECULAR MICRO-REACTOR (ATOMIC / BIO CHAMBER)
# -------------------------------------------------------------
def render_archetype_3() -> Path:
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), (4, 10, 8))
    draw = ImageDraw.Draw(img)

    chamber_box = [120, 160, w - 120, h - 220]
    draw.rounded_rectangle(chamber_box, radius=20, fill=(6, 18, 14), outline=COLOR_EMERALD, width=2)

    # Semi-Permeable Membrane (Center Vertical Line)
    mem_x = w // 2
    for my in range(chamber_box[1] + 20, chamber_box[3] - 20, 30):
        draw.line([(mem_x, my), (mem_x, my + 16)], fill=COLOR_EMERALD, width=4)
        draw.ellipse([mem_x - 3, my + 18, mem_x + 3, my + 24], fill=(4, 10, 8)) # pore

    f_mem = get_font(20, bold=True)
    draw.text((mem_x - 140, chamber_box[1] + 18), "SEMI-PERMEABLE MEMBRANE", font=f_mem, fill=COLOR_EMERALD)

    # Left Side: Pure Solvent (Cyan Small Spheres)
    f_side = get_font(24, bold=True)
    draw.text((chamber_box[0] + 40, chamber_box[1] + 55), "PURE SOLVENT (High Potential)", font=f_side, fill=COLOR_CYAN)
    solvent_coords = [
        (250, 300), (320, 420), (220, 520), (380, 600), (460, 340), (560, 480), (680, 360), (740, 540), (820, 420)
    ]
    for sx, sy in solvent_coords:
        draw.ellipse([sx - 12, sy - 12, sx + 12, sy + 12], fill=COLOR_CYAN)
        draw.line([(sx - 18, sy + 10), (sx - 35, sy + 20)], fill=(56, 189, 248, 80), width=2) # motion streak

    # Right Side: Concentrated Solution (Large Amber Solute + Solvent)
    draw.text((w - 160 - 480, chamber_box[1] + 55), "CONCENTRATED SOLUTION (Low Potential)", font=f_side, fill=COLOR_AMBER)
    solute_coords = [
        (1100, 340), (1280, 460), (1450, 350), (1180, 600), (1380, 580), (1600, 480)
    ]
    for lx, ly in solute_coords:
        # Solute ion (large amber)
        draw.ellipse([lx - 26, ly - 26, lx + 26, ly + 26], fill=COLOR_AMBER)
        draw.ellipse([lx - 16, ly - 16, lx + 16, ly + 16], fill=(255, 230, 150))
        f_ion = get_font(18, bold=True)
        draw.text((lx - 12, ly - 12), "Na⁺", font=f_ion, fill=(15, 23, 42))

    # Net Flow Arrow Across Membrane
    draw.line([(mem_x - 120, 500), (mem_x + 120, 500)], fill=COLOR_WHITE, width=6)
    draw.polygon([(mem_x + 120, 485), (mem_x + 155, 500), (mem_x + 120, 515)], fill=COLOR_WHITE)
    f_flow = get_font(24, bold=True)
    draw.text((mem_x - 140, 455), "NET OSMOTIC WATER FLOW", font=f_flow, fill=COLOR_WHITE)

    # Telemetry HUD Card (Bottom-Right Inside Chamber)
    hud_y1 = chamber_box[3] - 185
    draw.rounded_rectangle([w - 480, hud_y1, w - 150, chamber_box[3] - 20], radius=12, fill=(10, 25, 20), outline=COLOR_EMERALD, width=2)
    f_rhud = get_font(20, bold=False)
    f_rhud_b = get_font(20, bold=True)
    draw.text((w - 460, hud_y1 + 15), "CHAMBER CONDITIONS", font=get_font(18, bold=True), fill=COLOR_EMERALD)
    draw.text((w - 460, hud_y1 + 48), "Temperature (T):", font=f_rhud, fill=COLOR_MUTED)
    draw.text((w - 270, hud_y1 + 48), "298 K", font=f_rhud_b, fill=COLOR_WHITE)
    draw.text((w - 460, hud_y1 + 80), "Van't Hoff (i):", font=f_rhud, fill=COLOR_MUTED)
    draw.text((w - 270, hud_y1 + 80), "2.0 (NaCl)", font=f_rhud_b, fill=COLOR_AMBER)
    draw.text((w - 460, hud_y1 + 112), "Osmotic Pres (π):", font=f_rhud, fill=COLOR_MUTED)
    draw.text((w - 270, hud_y1 + 112), "4.88 atm", font=f_rhud_b, fill=COLOR_EMERALD)

    draw_header_and_footer(
        draw, w, h,
        subject="Chemistry",
        code="ARCHETYPE 03 • MOLECULAR REACTOR",
        title="Osmotic Pressure & Van't Hoff Mechanics",
        subtitle="Solutions • Microscopic Particle Chamber Simulation",
        badge_text="HIGH YIELD | PYQ: 2018, 2023"
    )

    out_p = OUTPUT_DIR / "archetype_3_molecular_reactor.png"
    img.convert("RGB").save(str(out_p), "PNG", quality=95)
    return out_p

# -------------------------------------------------------------
# ARCHETYPE 4: FORMULA DECONSTRUCTION HUD (EXAM SURGERY)
# -------------------------------------------------------------
def render_archetype_4() -> Path:
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # 1. Central Hero Equation Card
    card_w, card_h = 1360, 280
    cx1 = (w - card_w) // 2
    cy1 = 200
    draw.rounded_rectangle([cx1, cy1, cx1 + card_w, cy1 + card_h], radius=24, fill=(12, 18, 32), outline=COLOR_CYAN, width=3)

    # Main Formula Text
    f_eq = get_font(72, bold=True)
    eq_str = "H_max  =  ( v₀² • sin² θ )  /  ( 2g )"
    bbox_e = draw.textbbox((0, 0), eq_str, font=f_eq)
    draw.text((cx1 + (card_w - (bbox_e[2] - bbox_e[0])) // 2, cy1 + 95), eq_str, font=f_eq, fill=COLOR_WHITE)

    # 2. Downward Explanatory Brackets & Callouts
    f_call_h = get_font(24, bold=True)
    f_call_d = get_font(22, bold=False)

    callouts = [
        (cx1 + 180, cy1 + card_h + 30, "INITIAL SPEED SQUARED (v₀²)", "Double the launch speed quadruples (4x) the maximum height!", COLOR_CYAN),
        (cx1 + 680, cy1 + card_h + 30, "ANGLE WITH HORIZONTAL (sin²θ)", "NEET TRAP: If angle given with vertical, this becomes cos²θ!", COLOR_AMBER),
        (cx1 + 1150, cy1 + card_h + 30, "GRAVITY ACCELERATION (2g)", "Inverted denominator; independent of projectile mass m.", COLOR_CORAL)
    ]

    for c_x, c_y, c_head, c_desc, c_col in callouts:
        # Bracket line
        draw.line([(c_x, cy1 + card_h), (c_x, c_y)], fill=c_col, width=3)
        draw.ellipse([c_x - 6, c_y - 6, c_x + 6, c_y + 6], fill=c_col)

        # Callout Box
        c_box = [c_x - 170, c_y + 20, c_x + 170, c_y + 170]
        draw.rounded_rectangle(c_box, radius=12, fill=(15, 23, 42), outline=c_col, width=2)
        draw.text((c_box[0] + 15, c_box[1] + 18), c_head, font=f_call_h, fill=c_col)
        
        # Word wrap desc
        words = c_desc.split()
        lines = []
        cur = []
        for w_item in words:
            cur.append(w_item)
            if len(" ".join(cur)) > 26:
                lines.append(" ".join(cur[:-1]))
                cur = [w_item]
        if cur:
            lines.append(" ".join(cur))
        
        for l_idx, l_str in enumerate(lines[:3]):
            draw.text((c_box[0] + 15, c_box[1] + 60 + l_idx * 28), l_str, font=f_call_d, fill=COLOR_WHITE)

    # 3. Bottom NEET Trap Warning Banner
    trap_y1 = h - 280
    draw.rounded_rectangle([120, trap_y1, w - 120, trap_y1 + 80], radius=14, fill=(35, 20, 5), outline=COLOR_AMBER, width=2)
    f_trap = get_font(26, bold=True)
    draw_star(draw, 160, trap_y1 + 40, 14, 6, fill=COLOR_AMBER)
    draw.text((195, trap_y1 + 24), "NEET TRAP ALERT: Always check whether the question specifies the angle θ with the horizontal or vertical!", font=f_trap, fill=COLOR_AMBER)

    draw_header_and_footer(
        draw, w, h,
        subject="Physics",
        code="ARCHETYPE 04 • FORMULA DECONSTRUCTION",
        title="Maximum Height Mathematical Surgery",
        subtitle="Dynamic Variable Breakdown & NEET Angle Trap Warnings",
        badge_text="CORE FORMULA DECONSTRUCTION"
    )

    out_p = OUTPUT_DIR / "archetype_4_formula_deconstruction.png"
    img.convert("RGB").save(str(out_p), "PNG", quality=95)
    return out_p

# -------------------------------------------------------------
# ARCHETYPE 5: MASTER NEURAL CONSTELLATION (CHAPTER ROADMAP GPS)
# -------------------------------------------------------------
def render_archetype_5() -> Path:
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Constellation Nodes Coordinates
    nodes = [
        (300, 320, "V01", "Frame of Ref", False),
        (520, 260, "V02", "Displacement", False),
        (740, 340, "V03", "Instant Velocity", False),
        (960, 250, "V04", "v-t Area Trap", False),
        (1180, 320, "V05", "Vector Split", False),
        (1400, 240, "V06", "Projectile 2D", False),
        (1620, 310, "V07", "Max Height Arc", True),   # ACTIVE NODE
        (380, 560, "V08", "Time of Flight", False),
        (600, 620, "V09", "Range Angles", False),
        (820, 540, "V10", "Centripetal Acc", False),
        (1040, 630, "V11", "Circular Traps", False),
        (1260, 550, "V12", "Rain-Boat Rel", False),
        (1480, 640, "V13", "Calculus Eqns", False),
        (1680, 550, "V14", "PYQ Speed Drill", False)
    ]

    # Connecting Fiber Lines
    for i in range(len(nodes) - 1):
        x1, y1, _, _, _ = nodes[i]
        x2, y2, _, _, _ = nodes[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=(25, 40, 65), width=2)

    # Cross Links
    draw.line([(nodes[0][0], nodes[0][1]), (nodes[7][0], nodes[7][1])], fill=(25, 40, 65), width=2)
    draw.line([(nodes[4][0], nodes[4][1]), (nodes[11][0], nodes[11][1])], fill=(25, 40, 65), width=2)

    f_node_id = get_font(20, bold=True)
    f_node_lbl = get_font(18, bold=False)

    for nx, ny, nid, nlbl, is_active in nodes:
        nr = 36 if not is_active else 48
        if is_active:
            # Radiant Spotlight Halo
            draw.ellipse([nx - nr - 20, ny - nr - 20, nx + nr + 20, ny + nr + 20], fill=(245, 158, 11, 45))
            draw.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], fill=(35, 20, 5), outline=COLOR_AMBER, width=4)
            draw.text((nx - 18, ny - 14), nid, font=get_font(26, bold=True), fill=COLOR_AMBER)
            
            # "YOU ARE HERE" Banner
            draw.rounded_rectangle([nx - 90, ny - nr - 55, nx + 90, ny - nr - 15], radius=8, fill=COLOR_AMBER)
            draw.text((nx - 75, ny - nr - 48), "YOU ARE HERE", font=get_font(18, bold=True), fill=(15, 23, 42))
            draw.text((nx - 60, ny + nr + 12), nlbl, font=get_font(20, bold=True), fill=COLOR_WHITE)
        else:
            draw.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], fill=(12, 18, 30), outline=COLOR_CYAN, width=2)
            draw.text((nx - 16, ny - 12), nid, font=f_node_id, fill=COLOR_CYAN)
            draw.text((nx - 45, ny + nr + 10), nlbl, font=f_node_lbl, fill=COLOR_MUTED)

    draw_header_and_footer(
        draw, w, h,
        subject="Physics",
        code="ARCHETYPE 05 • NEURAL CONSTELLATION",
        title="Kinematics Chapter GPS Roadmap",
        subtitle="14 Surgical Concepts • Complete NEET 2026 Unit 2 Coverage",
        badge_text="CHAPTER OVERVIEW GPS"
    )

    out_p = OUTPUT_DIR / "archetype_5_neural_constellation.png"
    img.convert("RGB").save(str(out_p), "PNG", quality=95)
    return out_p

def generate_all_archetypes():
    print("🎨 Rendering 5 Standardized Obsidian-Neon Storyboard UI Archetypes...")
    p1 = render_archetype_1()
    print(f"✅ Generated Archetype 1: {p1}")
    p2 = render_archetype_2()
    print(f"✅ Generated Archetype 2: {p2}")
    p3 = render_archetype_3()
    print(f"✅ Generated Archetype 3: {p3}")
    p4 = render_archetype_4()
    print(f"✅ Generated Archetype 4: {p4}")
    p5 = render_archetype_5()
    print(f"✅ Generated Archetype 5: {p5}")
    print("\n🎉 All 5 Storyboard UI Archetypes rendered successfully!")

if __name__ == "__main__":
    generate_all_archetypes()
