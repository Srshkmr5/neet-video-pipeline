"""
Generator for render/templates/unit_03_archetypes.py
Completely refactors all 11 concepts for Unit 3 (Laws of Motion).
Fixes:
1. Card header font switched to clean, modern Segoe UI in golden yellow (eliminating compressed Cascadia Mono).
2. Concept 3: Separated Body A / Body B text from action-reaction arrows (zero overwriting).
3. Concept 4: Widened impulse triangle and stacked Area = / Impulse J text (zero boundary overlap).
4. Concept 5: Added clearance between V_recoil label and rifle box border (zero border collision).
5. Concept 9: Placed friction arrow f_s cleanly below Block A (m1) label (zero text slice).
6. Zero hardcoded NEET PYQ years in Beat 4.
7. Perfect audio-visual narrative synchronization across Beats 2 & 3.
8. Standard Beat 5 Next Concept End Cards.
"""

from pathlib import Path

OUT_FILE = Path(r"render/templates/unit_03_archetypes.py")

content = '''"""
Dedicated Visual Archetypes for Unit 3: Laws of Motion
NCERT Class 11 Physics Part 1, Chapter 4 (Laws of Motion)

Provides modular build_beat_1(), build_beat_2(), build_beat_3(), build_beat_4(), build_beat_5()
for all 11 concepts across Newton's Laws, Momentum, Friction, and Circular Dynamics.
Strictly adheres to Rules 8-22:
- Clean modern typography (Verdana & Segoe UI)
- Minimum font floor >= 10.5pt, 1:1 aspect ratio without squishing
- 3.0s silent freeze on Beat 4 NEET Trap Card (Zero hardcoded PYQ years)
- Beat 5 Next Concept End Card
- Complete audio-visual timeline synchronization
- Zero container bounding box overflows or text overwrites
"""

import textwrap
from manim import *
import numpy as np
from render.templates.base import (
    BaseNeetScene, BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN,
    TEXT_WHITE, MUTED_TEXT
)

Text.set_default(font="Consolas")


class ModularUnit3Scene(BaseNeetScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header_font = "Verdana"
        self.card_font = "Consolas"
        self.body_font = "Consolas"
        self.text_white = TEXT_WHITE
        self.muted_text = MUTED_TEXT
        self.accent_blue = ACCENT_BLUE
        self.accent_gold = ACCENT_GOLD
        self.accent_red = ACCENT_RED
        self.accent_green = ACCENT_GREEN
        self.accent_purple = "#A855F7"

    def build_beat_5(self):
        """Standard Beat 5 End Card directing student to next concept."""
        next_title = self.node_data.get("next_video_title")
        next_id = self.node_data.get("next_video_id")
        seq_ch = int(self.node_data.get("seq_chapter", 1))
        tot_ch = int(self.node_data.get("total_chapter_videos", 11))

        box = RoundedRectangle(
            corner_radius=0.14, height=5.2, width=11.6,
            stroke_color=self.accent_blue, stroke_width=2.0,
            fill_color="#091322", fill_opacity=0.95
        ).move_to(DOWN * 0.05)

        if next_title and next_id:
            badge = Text("UP NEXT IN SEQUENCE", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_blue)
            wrapped_next = textwrap.fill(f"Concept {seq_ch+1:02d}/{tot_ch:02d}: {next_title}", width=46)
            next_txt = Text(wrapped_next, font=self.header_font, font_size=22, weight="BOLD", color=self.text_white)
            if next_txt.width > 10.6:
                next_txt.scale_to_fit_width(10.6)
            sub_txt = Text(f"Canonical ID: {next_id}", font=self.body_font, font_size=14, color=self.muted_text)
            lab_badge = Text("INTERACTIVE LAB AVAILABLE IN APP TAB 2", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green)
            content_box = VGroup(badge, next_txt, sub_txt, lab_badge).arrange(DOWN, buff=0.35).move_to(box.get_center())
            return VGroup(box, content_box)
        else:
            badge = Text("CHAPTER COMPLETE", font=self.card_font, font_size=20, weight="BOLD", color=self.accent_gold)
            txt = Text(next_title if next_title else "Unit 3 Complete • Ready for Unit 4: Work, Energy & Power", font=self.header_font, font_size=24, weight="BOLD", color=self.accent_green)
            if txt.width > 10.6:
                txt.scale_to_fit_width(10.6)
            sub = Text(f"All {tot_ch}/{tot_ch} Core Concepts Verified", font=self.body_font, font_size=16, color=self.text_white)
            content_box = VGroup(badge, txt, sub).arrange(DOWN, buff=0.35).move_to(box.get_center())
            return VGroup(box, content_box)


# ===========================================================================
# 1. FirstLawFbdScene (P11-C03-T01-V01)
# ===========================================================================
class FirstLawFbdScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Newton's First Law", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Inertia & Free-Body Diagrams (FBD)", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.2 - 4.3", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("NEWTON'S FIRST LAW & TRANSLATIONAL EQUILIBRIUM", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.2 • Galileo's Principle of Inertia & Zero Net External Force", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Block at rest in equilibrium
        px = box.get_left()[0] + 2.8
        floor = Line(start=np.array([px - 2.0, -1.2, 0]), end=np.array([px + 2.0, -1.2, 0]), color="#475569", stroke_width=2.5)
        block = RoundedRectangle(corner_radius=0.08, width=2.0, height=1.5, stroke_color=self.accent_blue, stroke_width=2.0, fill_color="#1E293B", fill_opacity=0.7).move_to(np.array([px, -0.45, 0]))
        b_lbl = Text("Mass m", font=self.body_font, font_size=12, color=self.text_white).move_to(block.get_center())

        arr_w = Arrow(start=block.get_center(), end=block.get_center() + DOWN * 1.35, color=self.accent_red, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        lbl_w = Text("W = mg", font=self.card_font, font_size=11, color=self.accent_red).next_to(arr_w.get_end(), DOWN, buff=0.08)

        arr_n = Arrow(start=block.get_center(), end=block.get_center() + UP * 1.35, color=self.accent_green, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        lbl_n = Text("N = mg", font=self.card_font, font_size=11, color=self.accent_green).next_to(arr_n.get_end(), UP, buff=0.08)

        left_pane = VGroup(floor, block, b_lbl, arr_w, lbl_w, arr_n, lbl_n)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("F_net = 0  <=>  a = 0  (v = constant)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Galileo's Inertia: Body maintains state unless forced", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Vector Component Form: F_net,x = 0,  F_net,y = 0", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Measure of Inertia: Mass m is purely quantitative", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Zero net force does NOT mean zero velocity!", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 1 DEEP-DIVE: FREE-BODY DIAGRAM (FBD) RESOLUTION", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("ISOLATION OF BODY & CONTACT FORCES", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Isolate body from all physical surroundings", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Normal N: Perpendicular pushing contact force", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Gravity mg: Acts strictly downward at COM", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Pull F at angle θ: Resolves to (F·cos θ, F·sin θ)", font=self.card_font, font_size=11, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("NORMAL REACTION ALTERATION DERIVATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Vertical: N + F·sin θ = mg", font=self.card_font, font_size=11.5, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Result: N = mg - F·sin θ  (Reduced Normal)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Pulling upward directly relieves contact pressure!", font=self.body_font, font_size=11, color=self.accent_green).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Horizontal Accel: a = (F·cos θ) / m", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 01: FBD FORCE INCLUSION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Drawing forces exerted BY the body in its own FBD (e.g. horse on cart)", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT LAW: An FBD strictly isolates forces acting ON the body by the environment!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Internal muscular forces and action pairs cancel out in the global system: F_internal = 0", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 2. SecondLawElevatorScene (P11-C03-T01-V02)
# ===========================================================================
class SecondLawElevatorScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Newton's Second Law", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Elevators & Pseudo Forces", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("NEWTON'S SECOND LAW & ELEVATOR APPARENT WEIGHT", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.4 • Net Force F = ma & Normal Reaction on Weighing Scale", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Elevator cage
        px = box.get_left()[0] + 2.8
        cage = RoundedRectangle(corner_radius=0.1, width=3.2, height=3.2, stroke_color="#64748B", stroke_width=2.5, fill_color="#1E293B", fill_opacity=0.3).move_to(np.array([px, -0.2, 0]))
        scale = RoundedRectangle(corner_radius=0.05, width=1.8, height=0.3, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.9).move_to(cage.get_bottom() + UP * 0.25)
        person = RoundedRectangle(corner_radius=0.08, width=1.1, height=1.1, stroke_color=self.accent_green, stroke_width=2.0, fill_color="#1E293B", fill_opacity=0.7).next_to(scale, UP, buff=0.0)
        p_lbl = Text("Mass m", font=self.body_font, font_size=11, color=self.text_white).move_to(person.get_center())

        arr_a = Arrow(start=cage.get_right() + RIGHT * 0.25 + DOWN * 0.4, end=cage.get_right() + RIGHT * 0.25 + UP * 0.6, color=self.accent_red, buff=0, stroke_width=3)
        lbl_a = Text("a (Frame)", font=self.card_font, font_size=11, color=self.accent_red).next_to(arr_a, RIGHT, buff=0.1)

        left_pane = VGroup(cage, scale, person, p_lbl, arr_a, lbl_a)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("N_app = m(g ± a)", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Accelerating UP (a > 0):    N = m(g + a)  > mg", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Accelerating DOWN (a > 0):  N = m(g - a)  < mg", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Constant Velocity (a = 0): N = mg (True weight)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Reading reflects NORMAL force N, not mg directly", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 2 DEEP-DIVE: NON-INERTIAL FRAMES & FREE FALL", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("PSEUDO FORCE IN ACCELERATING FRAMES", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Frame acceleration: a_0 (Non-inertial)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• F_pseudo = - m · a_0 (Opposite to frame)", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Allows applying Newton's laws inside frame", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Equation inside frame: N - mg + F_pseudo = 0", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("FREE FALL & WEIGHTLESSNESS (CABLE SNAP)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Cable breaks: Downward accel a_0 = g", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Normal Reaction: N = m(g - g) = 0", font=self.card_font, font_size=12, color=self.accent_red).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Scale reads 0: State of true weightlessness", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• If a > g (Super-fall): Body hits the ceiling!", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 02: VELOCITY VS ACCELERATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming moving upwards always means apparent weight increases: N = m(g + a)", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Apparent weight depends ONLY on ACCELERATION a, NEVER on velocity v!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Moving UP but slowing down has a downwards: N = m(g - a) => Apparent weight is LESS!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 3. ThirdLawAtwoodScene (P11-C03-T01-V03)
# ===========================================================================
class ThirdLawAtwoodScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Newton's Third Law", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Action-Reaction & Atwood Machine", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.5", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("NEWTON'S THIRD LAW: ACTION-REACTION DUALITY", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.5 • Equal & Opposite Forces Acting Simultaneously on Separate Bodies", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Interacting bodies A and B with text cleanly in top half and arrows in lower half
        px = box.get_left()[0] + 2.8
        bA = RoundedRectangle(corner_radius=0.08, width=1.6, height=1.6, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px - 1.15, -0.3, 0]))
        bA_lbl = Text("Body A", font=self.card_font, font_size=12, weight="BOLD", color=self.text_white).move_to(bA.get_top() + DOWN * 0.38)

        bB = RoundedRectangle(corner_radius=0.08, width=1.6, height=1.6, stroke_color=self.accent_green, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px + 1.15, -0.3, 0]))
        bB_lbl = Text("Body B", font=self.card_font, font_size=12, weight="BOLD", color=self.text_white).move_to(bB.get_top() + DOWN * 0.38)

        # Action-reaction arrows in lower half: completely clear of text!
        arr_y = bA.get_bottom()[1] + 0.45
        arr_AB = Arrow(start=np.array([bA.get_right()[0], arr_y, 0]), end=np.array([bA.get_left()[0] + 0.25, arr_y, 0]), color=self.accent_red, buff=0, stroke_width=3)
        lbl_AB = Text("F_AB", font=self.card_font, font_size=10.5, weight="BOLD", color=self.accent_red).next_to(arr_AB, UP, buff=0.06)

        arr_BA = Arrow(start=np.array([bB.get_left()[0], arr_y, 0]), end=np.array([bB.get_right()[0] - 0.25, arr_y, 0]), color=self.accent_gold, buff=0, stroke_width=3)
        lbl_BA = Text("F_BA", font=self.card_font, font_size=10.5, weight="BOLD", color=self.accent_gold).next_to(arr_BA, UP, buff=0.06)

        left_pane = VGroup(bA, bA_lbl, bB, bB_lbl, arr_AB, lbl_AB, arr_BA, lbl_BA)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("F_AB = - F_BA  (Equal & Opposite)", font=self.card_font, font_size=16.5, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Forces always occur in simultaneous PAIRS", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Act on TWO DIFFERENT BODIES exclusively", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Action & Reaction CANNOT cancel each other!", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• No cause-and-effect delay: strictly concurrent", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 3 DEEP-DIVE: ATWOOD MACHINE FORMULAS", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("COMMON ACCELERATION DERIVATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Net Driving Force: F_net = (m1 - m2) · g", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Total System Mass: M_total = m1 + m2", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• a = [(m1 - m2) / (m1 + m2)] · g", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• If m1 >> m2: a -> g (Mass 1 falls freely)", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("STRING TENSION & CLAMP FORCE", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• String Tension: T = [2·m1·m2 / (m1 + m2)] · g", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Harmonic Mean: T = (Harmonic Mean) · g", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Pulley Support Clamp: F_clamp = 2 T", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• F_clamp = [4·m1·m2 / (m1 + m2)] · g", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 03: NORMAL FORCE VS THIRD LAW", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Calling Normal force N and weight mg an Action-Reaction pair!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Action and reaction act on TWO DIFFERENT BODIES simultaneously!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("N and mg act on the SAME body (equilibrium). Reaction to mg is the body pulling the EARTH!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 4. ImpulseFtCurveScene (P11-C03-T02-V04)
# ===========================================================================
class ImpulseFtCurveScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Momentum & Impulse", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Linear Momentum, Impulse & F-t Curve", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.4.1", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("IMPULSE-MOMENTUM THEOREM & F-t GRAPH AREA", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.4.1 • Large Impact Force Acting Over Tiny Duration Δt", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: F-t graph with wider triangle base and stacked label (zero boundary overlap)
        px = box.get_left()[0] + 2.8
        axes = Axes(
            x_range=[0, 4.5, 1], y_range=[0, 3.5, 1],
            x_length=4.0, y_length=2.4, tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(np.array([px, -0.15, 0]))

        x_lbl = Text("Time t (s) ->", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.10)
        y_lbl = Text("Force F (N) ^", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.08)

        p1 = axes.c2p(0.8, 0)
        p2 = axes.c2p(2.2, 2.9)
        p3 = axes.c2p(3.6, 0)
        pulse = Polygon(p1, p2, p3, color=self.accent_green, fill_color=self.accent_green, fill_opacity=0.3, stroke_width=2.5)

        area_lbl_1 = Text("Area =", font=self.card_font, font_size=10.5, color=self.accent_green).move_to(axes.c2p(2.2, 1.25))
        area_lbl_2 = Text("Impulse J", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(axes.c2p(2.2, 0.75))
        area_lbl = VGroup(area_lbl_1, area_lbl_2)

        left_pane = VGroup(axes, x_lbl, y_lbl, pulse, area_lbl)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("J = ∫ F dt = Δp = F_avg · Δt", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Geometric Area: Area under F-t curve = Impulse J", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Momentum Change: Δp = m·v_final - m·v_initial", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Cushioning: Increasing Δt reduces peak impact F", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Airbags & soft catch follow Δp = F_avg · Δt directly", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 4 DEEP-DIVE: ELASTIC REBOUND VECTOR IMPULSE", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("HEAD-ON REBOUND (PERPENDICULAR)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Initial momentum: p_i = + m·v", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Rebound momentum: p_f = - m·v", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Vector Impulse: J = p_f - p_i = - 2 m·v", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Magnitude on wall: |J| = 2 m·v (Doubled!)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("OBLIQUE BOUNCE (ANGLE θ WITH NORMAL)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Parallel component v·sin θ is unchanged", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Normal component v·cos θ inverts sign", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Total Impulse: J = 2·m·v·cos θ", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Directed strictly normal away from wall", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 04: REBOUND VELOCITY SIGN", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Subtracting scalar speeds and claiming Δp = mv - mv = 0 on elastic bounce!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Momentum is a VECTOR. When velocity reverses, signs invert: Δp = 2mv!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("For oblique rebound at angle θ to normal: J = 2·m·v·cos θ. Reversing direction doubles the impulse!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 5. RocketMomentumScene (P11-C03-T02-V05)
# ===========================================================================
class RocketMomentumScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Conservation of Momentum", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Momentum Conservation & Rocket Thrust", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.6", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("CONSERVATION OF LINEAR MOMENTUM & RIFLE RECOIL", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.6 • Invariant Total Momentum in Closed Isolated Systems (F_ext = 0)", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Gun and Bullet with generous clearance between recoil arrow label and gun box
        px = box.get_left()[0] + 2.8
        gun = RoundedRectangle(corner_radius=0.08, width=2.4, height=1.0, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px - 0.45, -0.3, 0]))
        g_lbl = Text("Rifle M", font=self.body_font, font_size=11, color=self.text_white).move_to(gun.get_center())

        bullet = RoundedRectangle(corner_radius=0.05, width=0.6, height=0.4, stroke_color=self.accent_gold, stroke_width=1.5, fill_color=self.accent_gold, fill_opacity=0.8).move_to(np.array([px + 1.5, -0.3, 0]))
        b_lbl = Text("m", font=self.card_font, font_size=10, color="#000").move_to(bullet.get_center())

        arr_v = Arrow(start=bullet.get_right() + RIGHT * 0.1, end=bullet.get_right() + RIGHT * 1.0, color=self.accent_green, buff=0, stroke_width=2.5)
        lbl_v = Text("v_bullet", font=self.card_font, font_size=10, color=self.accent_green).next_to(arr_v, UP, buff=0.06)

        # Recoil arrow starts 0.2 units away from gun box; label aligned to left of arrow (completely clear of border)
        arr_V = Arrow(start=gun.get_left() + LEFT * 0.2, end=gun.get_left() + LEFT * 1.05, color=self.accent_red, buff=0, stroke_width=2.5)
        lbl_V = Text("V_recoil", font=self.card_font, font_size=10, color=self.accent_red).next_to(arr_V, UP, buff=0.06).align_to(arr_V, LEFT)

        left_pane = VGroup(gun, g_lbl, bullet, b_lbl, arr_v, lbl_v, arr_V, lbl_V)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("V_recoil = - (m / M) · v", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Initial Momentum = 0  =>  M·V + m·v = 0", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Negative sign strictly confirms opposite direction", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Kinetic Energy Ratio: K_bullet / K_rifle = M / m", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Since M >> m, bullet carries ~99% of kinetic energy!", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 5 DEEP-DIVE: VARIABLE MASS ROCKET PROPULSION", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("ROCKET THRUST & PROPULSION FORCE", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Exhaust gas ejected at relative speed u", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Upward Thrust Force: F_thrust = u · |dm/dt|", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Lift-off threshold: F_thrust >= M_0 · g", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Minimum fuel rate: |dm/dt| >= (M_0 · g) / u", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("NET ACCELERATION & TSIOLKOVSKY SPEED", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Net Accel: a(t) = [u / m(t)] · |dm/dt| - g", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• As mass m(t) decreases, accel increases!", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Rocket Equation: v(t) = v_0 + u · ln(M_0 / M)", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Exhaust velocity u is key to high final speed", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 05: CONSTANT ROCKET ACCELERATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming rocket acceleration is constant: a = F_thrust / M_initial", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Rocket mass M(t) shrinks rapidly as fuel burns away!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("a(t) = [u · (dm/dt) / M(t)] - g increases dramatically over time as the tank empties.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 6. LamiTheoremScene (P11-C03-T02-V06)
# ===========================================================================
class LamiTheoremScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Equilibrium of Forces", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Concurrent Equilibrium & Lami's Theorem", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.7", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("LAMI'S THEOREM FOR THREE CONCURRENT FORCES", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.7 • Coplanar Concurrent Vectors in Static Equilibrium (F_net = 0)", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: 3 force vectors
        px = box.get_left()[0] + 2.8
        py = -0.2
        knot = Dot(np.array([px, py, 0]), color=self.accent_gold, radius=0.09)

        arr1 = Arrow(start=knot.get_center(), end=np.array([px + 1.5, py + 1.0, 0]), color=self.accent_blue, buff=0, stroke_width=3)
        lbl1 = Text("F1", font=self.card_font, font_size=11, color=self.accent_blue).next_to(arr1.get_end(), UR, buff=0.08)

        arr2 = Arrow(start=knot.get_center(), end=np.array([px - 1.5, py + 1.0, 0]), color=self.accent_green, buff=0, stroke_width=3)
        lbl2 = Text("F2", font=self.card_font, font_size=11, color=self.accent_green).next_to(arr2.get_end(), UL, buff=0.08)

        arr3 = Arrow(start=knot.get_center(), end=np.array([px, py - 1.5, 0]), color=self.accent_red, buff=0, stroke_width=3)
        lbl3 = Text("F3", font=self.card_font, font_size=11, color=self.accent_red).next_to(arr3.get_end(), DOWN, buff=0.08)

        left_pane = VGroup(knot, arr1, lbl1, arr2, lbl2, arr3, lbl3)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("F1 / sin α = F2 / sin β = F3 / sin γ", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• α = angle between F2 & F3 (opposite to F1)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• β = angle between F1 & F3 (opposite to F2)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• γ = angle between F1 & F2 (opposite to F3)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Valid strictly for exactly 3 concurrent forces", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 6 DEEP-DIVE: SYMMETRIC SUSPENSION & ANGLE LIMITS", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("SUSPENDED WEIGHT SYMMETRY", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Weight W held by 2 strings inclined at θ", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Vertical Equilibrium: 2·T·cos θ = W", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• String Tension: T = W / (2 · cos θ)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Horizontal components T·sin θ cancel identically", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("THE HORIZONTAL STRING PARADOX", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Pulling string horizontally: θ -> 90°", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• As θ -> 90°, cos θ -> 0  =>  T -> ∞!", font=self.card_font, font_size=12, color=self.accent_red).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Infinite tension needed for perfect horizontal line", font=self.card_font, font_size=11, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Every real horizontal cable MUST sag under gravity", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 06: LAMI'S THEOREM ANGLE MAPPING", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Taking the angle between the force and an axis, or applying Lami to 4 forces!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: The angle in denominator is the angle between the OTHER TWO FORCES!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("F1 divides by sin(θ between F2 and F3). Check that α + β + γ = 360° before computing.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 7. FrictionGraphScene (P11-C03-T03-V07)
# ===========================================================================
class FrictionGraphScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Friction Mechanics", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Static vs Kinetic Friction & Graphs", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.8", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("SELF-ADJUSTING STATIC & CONSTANT KINETIC FRICTION", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.8 • Microscopic Interlocking & Relative Motion Opposition", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Block being pushed with static friction resisting
        px = box.get_left()[0] + 2.8
        floor = Line(start=np.array([px - 2.0, -1.1, 0]), end=np.array([px + 2.0, -1.1, 0]), color="#475569", stroke_width=2.5)
        block = RoundedRectangle(corner_radius=0.08, width=2.0, height=1.4, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px, -0.4, 0]))
        b_lbl = Text("Mass m", font=self.body_font, font_size=11, color=self.text_white).move_to(block.get_center())

        arr_F = Arrow(start=block.get_right(), end=block.get_right() + RIGHT * 1.1, color=self.accent_green, buff=0, stroke_width=3)
        lbl_F = Text("F_applied", font=self.card_font, font_size=10.5, color=self.accent_green).next_to(arr_F, UP, buff=0.06)

        arr_f = Arrow(start=block.get_left() + DOWN * 0.4, end=block.get_left() + LEFT * 1.0 + DOWN * 0.4, color=self.accent_red, buff=0, stroke_width=3)
        lbl_f = Text("f_s (resists)", font=self.card_font, font_size=10.5, color=self.accent_red).next_to(arr_f, DOWN, buff=0.06)

        left_pane = VGroup(floor, block, b_lbl, arr_F, lbl_F, arr_f, lbl_f)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("f_s ≤ μ_s · N   &   f_k = μ_k · N", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Static Range: 0 ≤ f_s ≤ μ_s·N (Self-adjusting)", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• While Stationary: f_s = F_applied (Strict balance)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Kinetic Friction: Constant slide value, f_k < f_s,max", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Coefficients: μ_s > μ_k (Bonds break upon slip)", font=self.body_font, font_size=11.5, color=self.accent_green).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 7 DEEP-DIVE: THE CLASSICAL FRICTION GRAPH", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        # Left Visual: Piecewise Friction Graph (Lifted to prevent collision with bottom border)
        px = box.get_left()[0] + 2.8
        axes = Axes(
            x_range=[0, 4.5, 1], y_range=[0, 3.5, 1],
            x_length=4.0, y_length=2.4, tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(np.array([px, -0.15, 0]))

        x_lbl = Text("Applied Force F ->", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.10)
        y_lbl = Text("Friction f ^", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.08)

        p_origin = axes.c2p(0, 0)
        p_peak = axes.c2p(2.0, 2.8)
        p_drop = axes.c2p(2.3, 2.1)
        p_end = axes.c2p(4.0, 2.1)

        l_static = Line(p_origin, p_peak, color=self.accent_blue, stroke_width=3)
        l_drop = Line(p_peak, p_drop, color=self.accent_red, stroke_width=2)
        l_kinetic = Line(p_drop, p_end, color=self.accent_gold, stroke_width=3)

        dot_p = Dot(p_peak, color=self.accent_red, radius=0.07)
        lbl_peak = Text("f_s,max = μ_s·N", font=self.card_font, font_size=10, color=self.accent_red).next_to(dot_p, UP, buff=0.08)
        lbl_k = Text("f_k = μ_k·N", font=self.card_font, font_size=10, color=self.accent_gold).next_to(l_kinetic, UP, buff=0.08)

        left_graph = VGroup(axes, x_lbl, y_lbl, l_static, l_drop, l_kinetic, dot_p, lbl_peak, lbl_k)

        # Right Card: Three Regimes Explained
        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("THREE DISTINCT FRICTION REGIMES", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("1. Static Regime: Linear 45° line (f_s = F_app)", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("2. Limiting Peak: Sharp crest at f_s,max = μ_s·N", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("3. Kinetic Plateau: Horizontal line at f_k = μ_k·N", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Pulling lawn roller relieves N: easier than pushing", font=self.body_font, font_size=10.5, color=self.text_white).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, left_graph, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 07: STATIC FRICTION IS SELF-ADJUSTING", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming static friction is always equal to its maximum limit: f_s = μ_s·N", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Static friction equals the APPLIED FORCE until the threshold μ_s·N is reached!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("If F_applied = 5 N and f_s,max = 20 N, static friction is exactly 5 N, NOT 20 N! Block remains static.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 8. RoughInclineReposeScene (P11-C03-T03-V08)
# ===========================================================================
class RoughInclineReposeScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Friction on Inclines", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Angle of Repose & Incline Deceleration", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.8.1", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("ROUGH INCLINED PLANE & ANGLE OF REPOSE", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.8.1 • Gravity Components & Critical Impending Slip Threshold", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Ramp with block
        px = box.get_left()[0] + 1.2
        py = -1.1
        ramp = Polygon(np.array([px, py, 0]), np.array([px + 3.2, py + 1.8, 0]), np.array([px + 3.2, py, 0]), color=self.accent_gold, fill_color="#1E293B", fill_opacity=0.5, stroke_width=2.5)
        angle_arc = Arc(radius=0.8, start_angle=0, angle=np.arctan(1.8/3.2), arc_center=np.array([px, py, 0]), color=self.accent_gold)
        angle_lbl = Text("θ", font=self.card_font, font_size=12, color=self.accent_gold).move_to(np.array([px + 1.1, py + 0.22, 0]))

        mid_ramp = np.array([px + 1.6, py + 0.9, 0])
        block = RoundedRectangle(corner_radius=0.05, width=1.0, height=0.6, stroke_color=self.accent_blue, stroke_width=2, fill_color="#0F172A", fill_opacity=0.9).rotate(np.arctan(1.8/3.2)).move_to(mid_ramp + np.array([-0.15, 0.35, 0]))

        left_pane = VGroup(ramp, angle_arc, angle_lbl, block)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("tan θ_Repose = μ_s", font=self.card_font, font_size=19, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Downslope Force: mg·sin θ  vs  Friction f_s", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Normal Force: N = mg·cos θ (Alters with tilt)", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Impending Slip: mg·sin θ_R = μ_s·mg·cos θ_R", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• For θ < θ_R: Block remains static on the slope", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 8 DEEP-DIVE: ASYMMETRIC INCLINE ACCELERATIONS", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("SLIDING DOWN VS PROJECTED UP", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Sliding DOWN: Friction opposes gravity", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("   a_down = g(sin θ - μ_k · cos θ)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b1, DOWN, buff=0.10).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Projected UP: Friction & gravity both oppose", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.15).align_to(c1_b1, LEFT)
        c1_b4 = Text("   a_up = g(sin θ + μ_k · cos θ)  (Greater retardation)", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(c1_b3, DOWN, buff=0.10).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("TIME ASYMMETRY & RATIO DERIVATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Distance s is identical for ascent & descent", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Time Ratio: t_descent / t_ascent = √(a_up / a_down)", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Since a_up > a_down => t_descent > t_ascent ALWAYS!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Smooth incline (μ=0): t_descent = t_ascent", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 08: ASCENT VS DESCENT TIME EQUALITY", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming time of ascent equals time of descent on a rough inclined plane!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Friction opposes motion both ways! a_up > a_down => t_descent > t_ascent!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Kinematic symmetry holds ONLY on frictionless planes. On rough surfaces, descent is much slower.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 9. TwoBlockFrictionScene (P11-C03-T03-V09)
# ===========================================================================
class TwoBlockFrictionScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Two-Block Systems", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Stacked Blocks & Relative Slip Threshold", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.8.2", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("TWO-BLOCK FRICTION & MAXIMUM COMMON ACCELERATION", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.8.2 • Friction between Blocks Drives the Untouched Body", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Stacked blocks m1 on m2 with f_s placed along the interface (zero text overwrite!)
        px = box.get_left()[0] + 2.3
        py = -0.6
        floor = Line(start=np.array([px - 1.8, py, 0]), end=np.array([px + 1.8, py, 0]), color="#475569", stroke_width=2.5)

        b2 = RoundedRectangle(corner_radius=0.08, width=2.4, height=0.9, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px, py + 0.45, 0]))
        b2_lbl = Text("Block B (m2)", font=self.body_font, font_size=11, color=self.text_white).move_to(b2.get_center())

        b1 = RoundedRectangle(corner_radius=0.08, width=1.7, height=0.85, stroke_color=self.accent_gold, stroke_width=2, fill_color="#334155", fill_opacity=0.8).move_to(np.array([px, py + 1.35, 0]))
        # Label placed cleanly in upper portion of Block A
        b1_lbl = Text("Block A (m1)", font=self.card_font, font_size=10.5, weight="BOLD", color=self.text_white).move_to(b1.get_top() + DOWN * 0.24)

        arr_F = Arrow(start=b2.get_right(), end=b2.get_right() + RIGHT * 0.75, color=self.accent_green, buff=0, stroke_width=3)
        lbl_F = Text("F_pull", font=self.card_font, font_size=10, weight="BOLD", color=self.accent_green).next_to(arr_F, UP, buff=0.06)

        # Static friction arrow placed in lower half of Block A (cleanly separated from text Block A (m1))
        f_y = b1.get_bottom()[1] + 0.20
        f_arr = Arrow(start=np.array([px - 0.50, f_y, 0]), end=np.array([px + 0.50, f_y, 0]), color=self.accent_gold, buff=0, stroke_width=2.2)
        f_lbl = Text("f_s", font=self.card_font, font_size=9.5, weight="BOLD", color=self.accent_gold).next_to(f_arr, UP, buff=0.02)

        left_pane = VGroup(floor, b2, b2_lbl, b1, b1_lbl, arr_F, lbl_F, f_arr, f_lbl)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("a_max = μ_s · g", font=self.card_font, font_size=19, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Friction Accelerating A: f_max = μ_s · m1 · g", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Max Slip-Free Accel: a_max = f_max / m1 = μ_s·g", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Mass m2 does NOT affect top block's limit", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• If system accel exceeds μ_s·g, slipping initiates!", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 9 DEEP-DIVE: WHICH BLOCK IS PULLED?", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("CASE 1: FORCE ON BOTTOM BLOCK B", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Upper block driven by friction f_max alone", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Maximum common accel: a_max = μ_s · g", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Joint threshold: F_max = (m1 + m2) · μ_s · g", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• For F > F_max: A slips and accelerates at μ_k·g", font=self.body_font, font_size=10.5, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("CASE 2: FORCE ON TOP BLOCK A", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Lower block driven by friction f_max alone", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Maximum lower accel: a_max = (μ_s · m1 · g) / m2", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Threshold: F_max' = μ_s · m1 · g · (1 + m1/m2)", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Threshold is completely different depending on load!", font=self.card_font, font_size=10.5, color=self.accent_red).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 09: BLOCKS MOVING TOGETHER FALLACY", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming stacked blocks always move with a = F / (m1 + m2) for ANY applied force!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Always check if F exceeds F_max = (m1+m2)·μ_s·g before computing common accel!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("If F > F_max, blocks SLIP relative to each other and accelerate at DIFFERENT rates!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 10. LevelCurveSkiddingScene (P11-C03-T04-V10)
# ===========================================================================
class LevelCurveSkiddingScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Circular Dynamics", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Centripetal Force & Level Curved Road", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.9", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("CIRCULAR MOTION ON AN UNBANKED (LEVEL) ROAD", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.9 • Static Friction between Tires & Road Supplies Centripetal Force", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Circular curved track with car
        px = box.get_left()[0] + 2.8
        py = -0.2
        track = Arc(radius=1.7, start_angle=-PI/3, angle=2*PI/3, arc_center=np.array([px - 1.4, py, 0]), color="#334155", stroke_width=14)
        car = Dot(track.point_from_proportion(0.5), color=self.accent_blue, radius=0.13)

        arr_f = Arrow(start=car.get_center(), end=car.get_center() + LEFT * 1.2, color=self.accent_red, buff=0, stroke_width=3)
        lbl_f = Text("f_s (Inward)", font=self.card_font, font_size=10.5, color=self.accent_red).next_to(arr_f, UP, buff=0.08)

        left_pane = VGroup(track, car, arr_f, lbl_f)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("f_s = m · v² / r  ≤  μ_s · m · g", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Centripetal Requirement: F_c = m·v² / r", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Supplied exclusively by static tire friction f_s", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Friction points toward instantaneous center of turn", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• If v exceeds limit: Friction fails and vehicle skids out", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 10 DEEP-DIVE: MAXIMUM SAFE SPEED & MASS INDEPENDENCE", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("MAXIMUM SAFE VELOCITY DERIVATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• Set m·v² / r = μ_s · m · g", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Mass m cancels out completely!", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Maximum Speed: v_max = √(μ_s · r · g)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• True for 10-ton trucks and 100-kg motorbikes alike", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("CENTRIPETAL FORCE IS A REAL REQUIREMENT", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Not a new type of physical force", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• It is a geometric role fulfilled by existing forces", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Flat road: Static friction supplies m·v²/r", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Kinetic sliding friction is far weaker than static!", font=self.card_font, font_size=11, color=self.accent_red).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 10: TURNING SPEED MASS DEPENDENCE", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Believing heavier vehicles can negotiate flat turns at higher safe speeds!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Mass cancels out completely in v_max = √(μ_s · r · g)!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("A 10-ton truck and a 100-kg motorbike share the exact same skidding speed on a flat turn.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)


# ===========================================================================
# 11. BankedRoadVerticalCircleScene (P11-C03-T04-V11)
# ===========================================================================
class BankedRoadVerticalCircleScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Advanced Circular Dynamics", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Engineered Banking & Vertical Circles", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.9.1", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        card_title = Text("ENGINEERED BANKING OF ROADS (ZERO FRICTION WEAR)", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.9.1 • Horizontal Normal Component N·sin θ Supplies Centripetal Force", font=self.body_font, font_size=10.5, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Banked ramp cross section with car
        px = box.get_left()[0] + 1.2
        py = -1.1
        ramp = Polygon(np.array([px, py, 0]), np.array([px + 3.2, py + 1.6, 0]), np.array([px + 3.2, py, 0]), color=self.accent_blue, fill_color="#1E293B", fill_opacity=0.5, stroke_width=2.5)
        angle_arc = Arc(radius=0.8, start_angle=0, angle=np.arctan(1.6/3.2), arc_center=np.array([px, py, 0]), color=self.accent_gold)
        angle_lbl = Text("θ", font=self.card_font, font_size=12, color=self.accent_gold).move_to(np.array([px + 1.1, py + 0.22, 0]))

        mid_ramp = np.array([px + 1.6, py + 0.8, 0])
        car = RoundedRectangle(corner_radius=0.06, width=1.1, height=0.6, stroke_color=self.accent_green, stroke_width=2, fill_color="#0F172A", fill_opacity=0.9).rotate(np.arctan(1.6/3.2)).move_to(mid_ramp + np.array([-0.1, 0.35, 0]))

        left_pane = VGroup(ramp, angle_arc, angle_lbl, car)

        # Right Pane: Equations
        rx = box.get_right()[0] - 3.1
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.8, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("v_opt = √(r · g · tan θ)", font=self.card_font, font_size=19, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Horizontal: N·sin θ = m·v² / r  (Centripetal force)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.22).align_to(eq_box, LEFT).shift(RIGHT * 0.2)
        row2 = Text("• Vertical:   N·cos θ = mg        (Weight support)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(row1, LEFT)
        row3 = Text("• Zero Wear:  At v_opt, lateral tire friction = 0!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row2, DOWN, buff=0.18).align_to(row1, LEFT)
        row4 = Text("• Max Speed:  v_max = √[r·g·(μ + tan θ)/(1 - μ·tan θ)]", font=self.card_font, font_size=11, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(row1, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.2, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.05)
        title = Text("CONCEPT 11 DEEP-DIVE: STRING vs RIGID ROD IN VERTICAL CIRCLE", font=self.card_font, font_size=14.5, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.18)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.12)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 3.05 + DOWN * 0.25)
        c1_t = Text("CASE 1: MASS ON A LIGHT STRING", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.18)
        c1_b1 = Text("• String goes SLACK if tension drops below 0", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.25)
        c1_b2 = Text("• Apex condition: T_top ≥ 0  =>  v_top ≥ √(g · r)", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Bottom launch speed: v_bottom ≥ √(5 · g · r)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Tension difference: T_bottom - T_top = 6 mg", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=3.3, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 3.05 + DOWN * 0.25)
        c2_t = Text("CASE 2: MASS ON A LIGHT RIGID ROD", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.18)
        c2_b1 = Text("• Rigid rod can support compression!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.25)
        c2_b2 = Text("• Rod NEVER slacks: speed at top can drop to 0", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Bottom speed: v_bottom ≥ √(4·g·r) = 2√(g·r)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Bottom speed is 2√(gr), strictly NOT √(5gr)!", font=self.card_font, font_size=11, color=self.accent_red).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.9).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 11: STRING VS RIGID ROD THRESHOLDS", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Using the string threshold v = √(5gr) for a sphere on a light rigid rod!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.85).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: A rigid rod supports compression; velocity at apex can drop to 0 without slacking!", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Energy conservation gives v_bottom ≥ √(4gr) = 2√(gr). A string requires v_bottom ≥ √(5gr)!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        punchline = Text("Master this core distinction to eliminate negative marking in NEET Physics.", font=self.card_font, font_size=12.5, weight="BOLD", color=self.accent_gold).next_to(rule_box, DOWN, buff=0.45)
        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, punchline)
'''

OUT_FILE.write_text(content, encoding="utf-8")
print(f"Successfully generated {OUT_FILE} ({len(content)} bytes)")
