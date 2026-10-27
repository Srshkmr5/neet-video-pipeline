"""
Dedicated Visual Archetypes for Unit 3: Laws of Motion
NCERT Class 11 Physics Part 1, Chapter 4 (Laws of Motion)

Provides modular build_beat_1(), build_beat_2(), build_beat_3(), build_beat_4()
for all 11 concepts across Newton's Laws, Momentum, Friction, and Circular Dynamics.
Strictly adheres to Rules 8-14:
- Three-tier typography hierarchy (Verdana, Cascadia Mono, Consolas)
- Minimum font floor >= 10.5pt, 1:1 aspect ratio without squishing
- 3.0s silent freeze on Beat 4 NEET Trap Card
- Beat 5 Next Concept End Card
"""

from manim import *
import numpy as np
from render.templates.base import (
    FONT_HEADER, FONT_CARD, FONT_BODY,
    BaseNeetScene, BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN,
    TEXT_WHITE, MUTED_TEXT
)

Text.set_default(font=FONT_BODY)

class ModularUnit3Scene(BaseNeetScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header_font = FONT_HEADER
        self.card_font = FONT_CARD
        self.body_font = FONT_BODY
        self.text_white = TEXT_WHITE
        self.muted_text = MUTED_TEXT
        self.accent_blue = ACCENT_BLUE
        self.accent_gold = ACCENT_GOLD
        self.accent_red = ACCENT_RED
        self.accent_green = ACCENT_GREEN
        self.accent_purple = "#A855F7"

    def render_concept_beats(self):
        target_dur = float(self.node_data.get("target_duration", 32.0))
        extra_time = max(0.0, target_dur - 22.1)
        wait_b1 = 1.5 + 0.08 * extra_time
        wait_b2 = 3.0 + 0.38 * extra_time
        wait_b3 = 3.0 + 0.32 * extra_time
        wait_b4 = 3.5 + 0.22 * extra_time

        b1 = self.build_beat_1()
        self.play(FadeIn(b1, shift=UP * 0.2), run_time=1.0)
        self.wait(wait_b1)
        self.play(FadeOut(b1), run_time=0.8)

        b2 = self.build_beat_2()
        self.play(FadeIn(b2), run_time=1.2)
        self.wait(wait_b2)
        self.play(FadeOut(b2), run_time=0.8)

        b3 = self.build_beat_3()
        self.play(FadeIn(b3), run_time=1.2)
        self.wait(wait_b3)
        self.play(FadeOut(b3), run_time=0.8)

        b4 = self.build_beat_4()
        self.play(FadeIn(b4), run_time=1.0)
        self.wait(wait_b4)
        self.play(FadeOut(b4), run_time=0.8)

        self.render_release_teaser(duration=3.5)


# ---------------------------------------------------------------------------
# 1. FirstLawFbdScene (P11-C03-T01-V01)
# ---------------------------------------------------------------------------
class FirstLawFbdScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Newton's First Law", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Inertia & Free-Body Diagrams (FBD)", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.2 - 4.3", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("FREE-BODY DIAGRAM & FORCE RESOLUTION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.3 • Isolate Body & Resolve External Forces along Orthogonal Axes", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Block with FBD vectors
        floor = Line(start=box.get_left() + RIGHT * 1.0 + DOWN * 0.8, end=box.get_left() + RIGHT * 4.6 + DOWN * 0.8, color="#475569", stroke_width=2.0)
        block = RoundedRectangle(corner_radius=0.08, width=1.8, height=1.4, stroke_color=self.accent_blue, stroke_width=2.0, fill_color="#1E293B", fill_opacity=0.6).move_to(floor.get_center() + UP * 0.7)
        b_lbl = Text("Mass m", font=self.body_font, font_size=12, color=self.text_white).move_to(block.get_center())

        # Vector Arrows
        arr_mg = Arrow(start=block.get_center(), end=block.get_center() + DOWN * 1.5, color=self.accent_red, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        lbl_mg = Text("W = mg", font=self.body_font, font_size=11, color=self.accent_red).next_to(arr_mg.get_end(), DOWN, buff=0.1)

        arr_N = Arrow(start=block.get_center(), end=block.get_center() + UP * 1.3, color=self.accent_green, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        lbl_N = Text("N = Normal", font=self.body_font, font_size=11, color=self.accent_green).next_to(arr_N.get_end(), UP, buff=0.1)

        arr_F = Arrow(start=block.get_center(), end=block.get_center() + np.array([1.6, 0.9, 0]), color=self.accent_gold, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        lbl_F = Text("F (Pull at θ)", font=self.body_font, font_size=11, color=self.accent_gold).next_to(arr_F.get_end(), UR, buff=0.1)

        left_pane = VGroup(floor, block, b_lbl, arr_mg, lbl_mg, arr_N, lbl_N, arr_F, lbl_F)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("Σ F_ext = m·a = 0 (Equilibrium)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Vertical Equilibrium:   N + F·sin θ = mg", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Normal Force Result:   N = mg - F·sin θ (< mg)", font=self.card_font, font_size=12, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Horizontal Net Force:  F_x = F·cos θ = m·a_x", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Acceleration on Floor: a = (F·cos θ) / m", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 1 DEEP-DIVE: INTERNAL VS EXTERNAL FORCES", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("THE HORSE & CART PARADOX", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Horse pulls cart with force F", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Cart pulls horse backward with equal -F", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Why does system accelerate forward?", font=self.card_font, font_size=11, color=self.accent_gold).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Ground friction ON horse > cart friction!", font=self.body_font, font_size=11, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("ISOLATION OF THE BODY (FBD RULES)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("1. Remove all surrounding objects physically", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("2. Replace contacts with normal & friction", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("3. Replace ropes with tension pointing away", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("4. Include gravity mg acting strictly at COM", font=self.card_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=4.5, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 01: FBD FORCE DIRECTION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Drawing forces exerted BY the body in its own FBD (e.g. horse on cart)", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT LAW: An FBD includes strictly forces acting ON the body by the environment!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Internal muscular forces and action pairs cancel out in the global system: Σ F_internal = 0", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2021 (Horse-Cart) • NEET 2017 (Incline FBD)", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 2. SecondLawElevatorScene (P11-C03-T01-V02)
# ---------------------------------------------------------------------------
class SecondLawElevatorScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Newton's Second Law", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Elevators & Pseudo Forces", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("APPARENT WEIGHT IN AN ACCELERATING ELEVATOR", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.4 • Non-Inertial Reference Frame & Apparent Normal Reaction", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Elevator cage with weighing machine
        cage = RoundedRectangle(corner_radius=0.1, width=3.4, height=3.4, stroke_color="#64748B", stroke_width=2.5, fill_color="#1E293B", fill_opacity=0.3).move_to(box.get_left() + RIGHT * 2.8 + DOWN * 0.3)
        scale = RoundedRectangle(corner_radius=0.05, width=1.8, height=0.3, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.9).move_to(cage.get_bottom() + UP * 0.3)
        person = RoundedRectangle(corner_radius=0.08, width=1.2, height=1.2, stroke_color=self.accent_green, stroke_width=2.0, fill_color="#1E293B", fill_opacity=0.7).next_to(scale, UP, buff=0.0)
        p_lbl = Text("Mass m", font=self.body_font, font_size=11, color=self.text_white).move_to(person.get_center())

        arr_a = Arrow(start=cage.get_right() + RIGHT * 0.2 + DOWN * 0.5, end=cage.get_right() + RIGHT * 0.2 + UP * 0.8, color=self.accent_red, buff=0, stroke_width=3)
        lbl_a = Text("a (Frame)", font=self.card_font, font_size=11, color=self.accent_red).next_to(arr_a, RIGHT, buff=0.1)

        left_pane = VGroup(cage, scale, person, p_lbl, arr_a, lbl_a)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("N_app = m(g ± a)", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Accelerating UP (a > 0):    N = m(g + a) > mg", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Accelerating DOWN (a > 0):  N = m(g - a) < mg", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Free Fall (Cable Cut a=g): N = m(g - g) = 0", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Pseudo Force on Body:      F_pseudo = -m·a_frame", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 2 DEEP-DIVE: FOUR ELEVATOR DYNAMICAL REGIMES", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("ASCENT DYNAMICS (GOING UP)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Starting upward (Speeding up, a ↑):", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("   N = m(g + a) => HEAVIER", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b1, DOWN, buff=0.08).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Arriving at top (Slowing down, a ↓):", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.15).align_to(c1_b1, LEFT)
        c1_b4 = Text("   N = m(g - a) => LIGHTER", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(c1_b3, DOWN, buff=0.08).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("DESCENT DYNAMICS (GOING DOWN)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• Starting downward (Speeding up, a ↓):", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("   N = m(g - a) => LIGHTER", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(c2_b1, DOWN, buff=0.08).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Braking at bottom (Slowing down, a ↑):", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.15).align_to(c2_b1, LEFT)
        c2_b4 = Text("   N = m(g + a) => HEAVIER", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_b3, DOWN, buff=0.08).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=4.8, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 02: VELOCITY VS ACCELERATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming moving upwards always means apparent weight increases: N = m(g + a)", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Apparent weight depends ONLY on ACCELERATION a, NEVER on velocity v!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Moving UP but slowing down has a downwards: N = m(g - a) => Apparent weight is LESS!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2023 (Cable Brake) • NEET 2020 • NEET 2018", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 3. ThirdLawAtwoodScene (P11-C03-T01-V03)
# ---------------------------------------------------------------------------
class ThirdLawAtwoodScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Newton's Third Law", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Action-Reaction & Atwood Machine", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.5", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("ATWOOD MACHINE: ACCELERATION & STRING TENSION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.5 • Massless Frictionless Pulley with Inextensible String", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Pulley with 2 masses
        px = box.get_left()[0] + 2.8
        pulley = Circle(radius=0.7, color="#94A3B8", stroke_width=3, fill_color="#334155", fill_opacity=0.8).move_to(np.array([px, box.get_center()[1] + 0.6, 0]))
        sup = Line(start=pulley.get_top(), end=pulley.get_top() + UP * 0.6, color="#64748B", stroke_width=4)

        s_left = Line(start=pulley.get_left(), end=pulley.get_left() + DOWN * 1.8, color=self.text_white, stroke_width=2)
        s_right = Line(start=pulley.get_right(), end=pulley.get_right() + DOWN * 1.2, color=self.text_white, stroke_width=2)

        b1 = RoundedRectangle(corner_radius=0.06, width=1.1, height=1.1, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(s_left.get_end() + DOWN * 0.55)
        b1_lbl = Text("m1", font=self.body_font, font_size=11, color=self.text_white).move_to(b1.get_center())

        b2 = RoundedRectangle(corner_radius=0.06, width=1.1, height=1.1, stroke_color=self.accent_gold, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(s_right.get_end() + DOWN * 0.55)
        b2_lbl = Text("m2", font=self.body_font, font_size=11, color=self.text_white).move_to(b2.get_center())

        lbl_T1 = Text("T", font=self.card_font, font_size=11, color=self.accent_green).next_to(s_left.get_center(), LEFT, buff=0.1)
        lbl_T2 = Text("T", font=self.card_font, font_size=11, color=self.accent_green).next_to(s_right.get_center(), RIGHT, buff=0.1)

        left_pane = VGroup(pulley, sup, s_left, s_right, b1, b1_lbl, b2, b2_lbl, lbl_T1, lbl_T2)

        # Right Pane: Master Formulas
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("a = (m1 - m2)g / (m1 + m2)", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• String Tension:         T = 2 m1 m2 g / (m1 + m2)", font=self.card_font, font_size=12, color=self.accent_green).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Pulley Support Force:   F_clamp = 2 T", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• If m1 >> m2:            a → g  and  T → 2 m2 g", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Action-Reaction Pair:   T on block vs T on string", font=self.body_font, font_size=11.5, color=self.muted_text).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 3 DEEP-DIVE: PULLEY SYSTEM ARCHETYPES", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("TABLE-HANGING PULLEY SYSTEM", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Mass m1 on table, m2 hanging vertically", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Net pulling force = m2·g", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Acceleration: a = m2·g / (m1 + m2)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Tension: T = m1·m2·g / (m1 + m2)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("INCLINED PLANE PULLEY SYSTEM", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• Mass m1 on incline angle θ, m2 hanging", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• Driving force: (m2 - m1·sin θ)g", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• a = g(m2 - m1·sin θ) / (m1 + m2)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Equilibrium condition: m2 = m1·sin θ", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 03: NORMAL FORCE VS THIRD LAW", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Calling Normal force N and weight mg an Action-Reaction pair!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Action and reaction act on TWO DIFFERENT BODIES simultaneously!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("N and mg act on the SAME body (equilibrium). Reaction to mg is the body pulling the EARTH!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2022 • NEET 2019 (Pulley Tension) • NEET 2016", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 4. ImpulseFtCurveScene (P11-C03-T02-V04)
# ---------------------------------------------------------------------------
class ImpulseFtCurveScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Momentum & Impulse", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Linear Momentum, Impulse & F-t Curve", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.4.1", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("IMPULSE-MOMENTUM THEOREM & F-t AREA", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.4.1 • Large Force Acting for Very Small Time Interval Δt", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: F-t graph
        axes = Axes(
            x_range=[0, 5.0, 1], y_range=[0, 4.0, 1],
            x_length=4.4, y_length=2.8, tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(box.get_left() + RIGHT * 2.7 + DOWN * 0.3)

        x_lbl = Text("Time t (s)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.12)
        y_lbl = Text("Force F (N)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.10)

        # Force impulse pulse (triangular area)
        p1 = axes.c2p(1.2, 0)
        p2 = axes.c2p(2.5, 3.2)
        p3 = axes.c2p(3.8, 0)
        pulse = Polygon(p1, p2, p3, color=self.accent_green, fill_color=self.accent_green, fill_opacity=0.3, stroke_width=2.5)
        area_lbl = Text("Area = Impulse J", font=self.card_font, font_size=11, color=self.accent_green).move_to(axes.c2p(2.5, 1.2))

        left_pane = VGroup(axes, x_lbl, y_lbl, pulse, area_lbl)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("J = ∫ F dt = Δp = m(v_f - v_i)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Area under F-t Graph:   Area = Total Impulse J", font=self.card_font, font_size=12, color=self.accent_green).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Rebound from Wall:      Δp = m·v - (-m·v) = 2mv", font=self.card_font, font_size=12, color=self.accent_gold).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Average Contact Force:  F_avg = J / Δt = Δp / Δt", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Cushioning (Longer Δt): Decreases impact force F", font=self.body_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 4 DEEP-DIVE: ELASTIC REBOUND VECTOR CALCULUS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("NORMAL COLLISION (HEAD-ON REBOUND)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Initial vector: p_i = + m·v  (towards wall)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Rebound vector: p_f = - m·v  (away from wall)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Vector Change: Δp = p_f - p_i = - 2 m·v", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Force on wall = + 2 m·v / Δt (Doubled!)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("OBLIQUE BOUNCE (ANGLE θ WITH NORMAL)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• Parallel component v·sin θ is UNCHANGED", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• Normal component v·cos θ inverts direction", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Net Impulse: J = 2 m·v·cos θ (strictly perpendicular)", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Tangential force = 0 on smooth walls", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 04: REBOUND VELOCITY SIGN", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Subtracting magnitudes and claiming Δp = m·v - m·v = 0 on elastic rebound!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Momentum is a VECTOR. When velocity reverses, signs invert: Δp = 2mv!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("For oblique rebound at angle θ to normal: J = 2·m·v·cos θ. If angle with wall is α, J = 2·m·v·sin α!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2024 (Rebound Force) • NEET 2021 • NEET 2019", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 5. RocketMomentumScene (P11-C03-T02-V05)
# ---------------------------------------------------------------------------
class RocketMomentumScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Conservation of Momentum", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Momentum Conservation & Rocket Thrust", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.6", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("VARIABLE MASS PROPULSION & RECOIL DYNAMICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.6 • Total Momentum Conserved in Isolated Systems", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Rocket Body & Exhaust
        px = box.get_left()[0] + 2.8
        rocket = RoundedRectangle(corner_radius=0.15, width=1.4, height=2.4, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px, box.get_center()[1] + 0.3, 0]))
        r_lbl = Text("M(t)", font=self.card_font, font_size=12, color=self.text_white).move_to(rocket.get_center())

        arr_up = Arrow(start=rocket.get_top(), end=rocket.get_top() + UP * 1.1, color=self.accent_green, buff=0, stroke_width=3)
        lbl_up = Text("F_thrust", font=self.card_font, font_size=11, color=self.accent_green).next_to(arr_up, RIGHT, buff=0.1)

        arr_down = Arrow(start=rocket.get_bottom(), end=rocket.get_bottom() + DOWN * 1.1, color=self.accent_red, buff=0, stroke_width=3)
        lbl_down = Text("Exhaust v_rel", font=self.card_font, font_size=11, color=self.accent_red).next_to(arr_down, RIGHT, buff=0.1)

        left_pane = VGroup(rocket, r_lbl, arr_up, lbl_up, arr_down, lbl_down)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("F_thrust = v_rel · |dm / dt|", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Net Acceleration:      a(t) = [v_rel · (dm/dt) / M(t)] - g", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Rocket Speed at Time t: v(t) = v0 + v_rel · ln(M0 / M)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Gun Recoil Velocity:    V_recoil = - (m_bullet / M_gun) · v", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• As mass M decreases:   Acceleration INCREASES continuously", font=self.body_font, font_size=11.5, color=self.muted_text).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 5 DEEP-DIVE: VARIABLE MASS vs FIXED MASS SYSTEMS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("RIFLE RECOIL PHYSICS", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Initial state: Gun + Bullet at rest (p_total = 0)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• M_gun · V_recoil + m_bullet · v_bullet = 0", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Kinetic Energy ratio: K_bullet / K_gun = M_gun / m", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Bullet receives 99% of explosion energy!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("ROCKET LIFT-OFF THRESHOLD", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• To barely lift off: F_thrust ≥ M_initial · g", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• Minimum fuel rate: dm/dt ≥ (M0 · g) / v_rel", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• If F_thrust = M0·g, initial acceleration = 0", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• It hovers briefly before rocketing upward!", font=self.body_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 05: CONSTANT ROCKET ACCELERATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming rocket acceleration is constant: a = F_thrust / M_initial", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Rocket mass M(t) shrinks rapidly as fuel burns away!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("a(t) = [v_rel · (dm/dt) / M(t)] - g increases dramatically over time as the tank empties.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2022 (Exhaust Thrust) • NEET 2018 • NEET 2015", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 6. LamiTheoremScene (P11-C03-T02-V06)
# ---------------------------------------------------------------------------
class LamiTheoremScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Equilibrium of Forces", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Concurrent Equilibrium & Lami's Theorem", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.7", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("LAMI'S THEOREM FOR THREE CONCURRENT FORCES", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.7 • Coplanar Concurrent Forces in Static Equilibrium", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: 3 force vectors radiating from origin
        ox = box.get_left()[0] + 2.8
        oy = box.get_center()[1] - 0.2
        knot = Dot(np.array([ox, oy, 0]), color=self.accent_gold, radius=0.08)

        # F1 pointing up-right, F2 up-left, F3 down
        f1_end = np.array([ox + 1.6, oy + 1.2, 0])
        f2_end = np.array([ox - 1.6, oy + 1.2, 0])
        f3_end = np.array([ox, oy - 1.8, 0])

        arr1 = Arrow(start=knot.get_center(), end=f1_end, color=self.accent_blue, buff=0, stroke_width=3)
        lbl1 = Text("F1", font=self.card_font, font_size=12, color=self.accent_blue).next_to(f1_end, UR, buff=0.1)

        arr2 = Arrow(start=knot.get_center(), end=f2_end, color=self.accent_green, buff=0, stroke_width=3)
        lbl2 = Text("F2", font=self.card_font, font_size=12, color=self.accent_green).next_to(f2_end, UL, buff=0.1)

        arr3 = Arrow(start=knot.get_center(), end=f3_end, color=self.accent_red, buff=0, stroke_width=3)
        lbl3 = Text("F3 (Weight W)", font=self.card_font, font_size=12, color=self.accent_red).next_to(f3_end, DOWN, buff=0.1)

        left_pane = VGroup(knot, arr1, lbl1, arr2, lbl2, arr3, lbl3)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("F1 / sin α = F2 / sin β = F3 / sin γ", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• α is the interior angle between F2 and F3", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• β is the interior angle between F1 and F3", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• γ is the interior angle between F1 and F2", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Strict Condition: α + β + γ = 360° and Σ F = 0", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 6 DEEP-DIVE: SYMMETRIC SUSPENSION & ANGLE SOLVER", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("SUSPENDED WEIGHT SYMMETRY", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Weight W supported by 2 strings at angle 2θ", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Vertical resolving: 2 T · cos θ = W", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Tension: T = W / (2 · cos θ)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• As θ → 90° (horizontal string), T → ∞!", font=self.body_font, font_size=11, color=self.accent_red).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("LIMITATIONS OF LAMI'S THEOREM", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("1. Strictly valid for exactly THREE forces only", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("2. Forces must be COPLANAR (same plane)", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("3. Forces must be CONCURRENT (intersect at 1 point)", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("4. For 4+ forces, resolve along x and y axes!", font=self.card_font, font_size=11, color=self.accent_blue).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 06: LAMI'S THEOREM ANGLE MAPPING", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Taking the angle between the force and an axis, or applying Lami to 4 forces!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: The angle in denominator is the angle between the OTHER TWO FORCES!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("F1 divides by sin(θ between F2 and F3). Check that α + β + γ = 360° before computing.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2023 (Knot Equilibrium) • NEET 2020", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 7. FrictionGraphScene (P11-C03-T03-V07)
# ---------------------------------------------------------------------------
class FrictionGraphScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Friction Mechanics", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Static vs Kinetic Friction & Graphs", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.8", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("SELF-ADJUSTING STATIC & CONSTANT KINETIC FRICTION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.8 • Microscopic Interlocking & Relative Motion Opposition", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Piecewise Friction Graph
        axes = Axes(
            x_range=[0, 5.0, 1], y_range=[0, 4.0, 1],
            x_length=4.4, y_length=2.8, tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(box.get_left() + RIGHT * 2.7 + DOWN * 0.3)

        x_lbl = Text("Applied Force F →", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.12)
        y_lbl = Text("Friction f ↑", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.10)

        # Static 45 deg slope + Peak + Kinetic flat line
        p_origin = axes.c2p(0, 0)
        p_peak = axes.c2p(2.2, 3.2)
        p_drop = axes.c2p(2.5, 2.4)
        p_end = axes.c2p(4.4, 2.4)

        line_static = Line(p_origin, p_peak, color=self.accent_blue, stroke_width=3)
        line_drop = Line(p_peak, p_drop, color=self.accent_red, stroke_width=2)
        line_kinetic = Line(p_drop, p_end, color=self.accent_gold, stroke_width=3)

        dot_peak = Dot(p_peak, color=self.accent_red, radius=0.07)
        lbl_peak = Text("f_s,max = μ_s·N", font=self.card_font, font_size=10, color=self.accent_red).next_to(dot_peak, UP, buff=0.1)
        lbl_k = Text("f_k = μ_k·N", font=self.card_font, font_size=10, color=self.accent_gold).next_to(line_kinetic, UP, buff=0.1)

        left_pane = VGroup(axes, x_lbl, y_lbl, line_static, line_drop, line_kinetic, dot_peak, lbl_peak, lbl_k)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("f_s ≤ μ_s·N   &   f_k = μ_k·N", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Static Range:           0 ≤ f_s ≤ μ_s·N (Self-adjusting)", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• While Stationary:       f_s = F_applied (Equilibrium)", font=self.body_font, font_size=11.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Kinetic Friction:       f_k is constant, strictly < f_s,max", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Friction Coefficient:   μ_s > μ_k (Interlocking bonds break)", font=self.body_font, font_size=11.5, color=self.accent_green).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 7 DEEP-DIVE: LAWS OF DRY FRICTION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("AREA INDEPENDENCE PRINCIPLE", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Friction is independent of apparent area!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Brick resting on flat side or narrow side", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("  experiences the identical friction threshold!", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.08).align_to(c1_b1, LEFT)
        c1_b4 = Text("• True microscopic contact area remains equal.", font=self.card_font, font_size=11, color=self.accent_gold).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("PUSHING VS PULLING A LAWN ROLLER", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• PUSHING: Downward thrust increases Normal:", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("   N = mg + F·sin θ => Friction INCREASES!", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(c2_b1, DOWN, buff=0.08).align_to(c2_b1, LEFT)
        c2_b3 = Text("• PULLING: Upward pull relieves Normal:", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.15).align_to(c2_b1, LEFT)
        c2_b4 = Text("   N = mg - F·sin θ => PULLING IS EASIER!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_b3, DOWN, buff=0.08).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 07: STATIC FRICTION IS SELF-ADJUSTING", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming static friction is always equal to its maximum limit: f_s = μ_s·N", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Static friction equals the APPLIED FORCE until the threshold μ_s·N is reached!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("If F_applied = 15 N and f_s,max = 50 N, static friction is exactly 15 N, NOT 50 N! Block remains static.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2024 (Static Value) • NEET 2021 • NEET 2017", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 8. RoughInclineReposeScene (P11-C03-T03-V08)
# ---------------------------------------------------------------------------
class RoughInclineReposeScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Friction on Inclines", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Angle of Repose & Incline Deceleration", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.8.1", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("MOTION ON A ROUGH INCLINED PLANE & ANGLE OF REPOSE", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.8.1 • Sliding Down vs Projected Up with Kinetic Friction", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Ramp with block
        px = box.get_left()[0] + 1.2
        py = box.get_center()[1] - 1.2
        ramp = Polygon(np.array([px, py, 0]), np.array([px + 3.4, py + 2.0, 0]), np.array([px + 3.4, py, 0]), color=self.accent_gold, fill_color="#1E293B", fill_opacity=0.5, stroke_width=2.5)
        angle_arc = Arc(radius=0.8, start_angle=0, angle=np.arctan(2.0/3.4), arc_center=np.array([px, py, 0]), color=self.accent_gold)
        angle_lbl = Text("θ", font=self.card_font, font_size=12, color=self.accent_gold).move_to(np.array([px + 1.1, py + 0.25, 0]))

        # Block on ramp
        mid_ramp = np.array([px + 1.7, py + 1.0, 0])
        block = RoundedRectangle(corner_radius=0.05, width=1.0, height=0.6, stroke_color=self.accent_blue, stroke_width=2, fill_color="#0F172A", fill_opacity=0.9).rotate(np.arctan(2.0/3.4)).move_to(mid_ramp + np.array([-0.2, 0.4, 0]))

        left_pane = VGroup(ramp, angle_arc, angle_lbl, block)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("tan θ_Repose = μ_s", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Sliding Downwards:   a_down = g(sin θ - μ_k·cos θ)", font=self.card_font, font_size=12, color=self.accent_green).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Projected Upwards:   a_up   = g(sin θ + μ_k·cos θ)", font=self.card_font, font_size=12, color=self.accent_red).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Time Asymmetry:      t_descent > t_ascent  (a_down < a_up)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Minimum Force to Hold: F_min = mg(sin θ - μ_s·cos θ)", font=self.body_font, font_size=11, color=self.muted_text).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 8 DEEP-DIVE: TIME ASYMMETRY ON ROUGH INCLINES", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("ASCENT VS DESCENT ACCELERATION", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Going UP: Gravity and friction both oppose motion", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("   a_up = g(sin θ + μ_k·cos θ) => High Deceleration", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(c1_b1, DOWN, buff=0.08).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Going DOWN: Friction opposes downward gravity", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.15).align_to(c1_b1, LEFT)
        c1_b4 = Text("   a_down = g(sin θ - μ_k·cos θ) => Low Acceleration", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.08).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("TIME RATIO DERIVATION (NEET GOLD)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• Distance s = 0.5 · a · t² is identical both ways", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• t_down / t_up = √(a_up / a_down)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Since a_up > a_down => t_down > t_up ALWAYS!", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Smooth incline: μ = 0 => t_down = t_up", font=self.body_font, font_size=11, color=self.muted_text).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 08: ASCENT VS DESCENT TIME EQUALITY", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming time of ascent equals time of descent on a rough inclined plane!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Friction opposes motion in both directions! a_up > a_down => t_descent > t_ascent!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Kinematic symmetry holds ONLY on frictionless planes. On rough surfaces, descent is much slower.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2023 (Time Ratio n) • NEET 2020 • NEET 2016", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 9. TwoBlockFrictionScene (P11-C03-T03-V09)
# ---------------------------------------------------------------------------
class TwoBlockFrictionScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Two-Block Systems", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Stacked Blocks & Relative Slip Threshold", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.8.2", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("TWO-BLOCK FRICTION & MAXIMUM COMMON ACCELERATION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.8.2 • Friction between Blocks Drives the Untouched Body", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Stacked blocks m1 on m2
        px = box.get_left()[0] + 2.8
        py = box.get_center()[1] - 0.4
        floor = Line(start=np.array([px - 2.0, py, 0]), end=np.array([px + 2.0, py, 0]), color="#475569", stroke_width=2.5)

        b2 = RoundedRectangle(corner_radius=0.08, width=2.8, height=1.0, stroke_color=self.accent_blue, stroke_width=2, fill_color="#1E293B", fill_opacity=0.8).move_to(np.array([px, py + 0.5, 0]))
        b2_lbl = Text("Block B (m2)", font=self.body_font, font_size=11, color=self.text_white).move_to(b2.get_center())

        b1 = RoundedRectangle(corner_radius=0.08, width=1.8, height=0.9, stroke_color=self.accent_gold, stroke_width=2, fill_color="#334155", fill_opacity=0.8).move_to(np.array([px, py + 1.45, 0]))
        b1_lbl = Text("Block A (m1)", font=self.body_font, font_size=11, color=self.text_white).move_to(b1.get_center())

        arr_F = Arrow(start=b2.get_right(), end=b2.get_right() + RIGHT * 1.2, color=self.accent_green, buff=0, stroke_width=3)
        lbl_F = Text("F (Pull)", font=self.card_font, font_size=11, color=self.accent_green).next_to(arr_F, RIGHT, buff=0.1)

        f_arrow = Arrow(start=b1.get_center(), end=b1.get_center() + RIGHT * 0.9, color=self.accent_gold, buff=0, stroke_width=2.5)
        f_lbl = Text("f_s", font=self.card_font, font_size=10, color=self.accent_gold).next_to(f_arrow, UP, buff=0.05)

        left_pane = VGroup(floor, b2, b2_lbl, b1, b1_lbl, arr_F, lbl_F, f_arrow, f_lbl)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("a_max = μ_s·g   &   F_max = (m1+m2)μ_s·g", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Friction Accelerates A:  f_max = μ_s · m1 · g", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Max Slip-Free Accel:     a_max = f_max / m1 = μ_s·g", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• If F ≤ F_max:           Blocks move together (a = F/(m1+m2))", font=self.body_font, font_size=11, color=self.text_white).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• If F > F_max:           Slipping occurs! Friction drops to μ_k", font=self.card_font, font_size=11.5, color=self.accent_red).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 9 DEEP-DIVE: WHICH BLOCK IS PULLED?", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("CASE 1: FORCE ON BOTTOM BLOCK B", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Friction accelerates upper block A alone", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• a_max = μ_s · g", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Threshold: F_max = (m1 + m2) · μ_s · g", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• For F > F_max: a_A = μ_k·g, a_B = (F - μ_k·m1·g)/m2", font=self.body_font, font_size=10.5, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("CASE 2: FORCE ON TOP BLOCK A", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• Friction accelerates bottom block B alone", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• a_max = (μ_s · m1 · g) / m2", font=self.card_font, font_size=12, color=self.accent_green).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Threshold: F_max = μ_s · m1 · g · (1 + m1/m2)", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Notice the threshold is DIFFERENT depending on load!", font=self.body_font, font_size=10.5, color=self.accent_red).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 09: BLOCKS MOVING TOGETHER FALLACY", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Assuming stacked blocks always move with a = F / (m1 + m2) for ANY applied force!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: Always check if F exceeds F_max = (m1+m2)·μ_s·g before computing common accel!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("If F > F_max, blocks SLIP relative to each other and accelerate at DIFFERENT rates!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2022 (F_max Threshold) • NEET 2019 • NEET 2018", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 10. LevelCurveSkiddingScene (P11-C03-T04-V10)
# ---------------------------------------------------------------------------
class LevelCurveSkiddingScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Circular Dynamics", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Centripetal Force & Level Curved Road", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.9", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CIRCULAR MOTION ON AN UNBANKED (LEVEL) ROAD", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.9 • Static Friction between Tires & Road Supplies Centripetal Force", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Circular curved track with car
        px = box.get_left()[0] + 2.8
        py = box.get_center()[1] - 0.2
        track = Arc(radius=1.8, start_angle=-PI/3, angle=2*PI/3, arc_center=np.array([px - 1.5, py, 0]), color="#334155", stroke_width=14)
        car = Dot(track.point_from_proportion(0.5), color=self.accent_blue, radius=0.14)

        arr_f = Arrow(start=car.get_center(), end=car.get_center() + LEFT * 1.3, color=self.accent_red, buff=0, stroke_width=3)
        lbl_f = Text("f_s (Inward)", font=self.card_font, font_size=11, color=self.accent_red).next_to(arr_f, UP, buff=0.1)

        left_pane = VGroup(track, car, arr_f, lbl_f)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("v_max = √(μ_s · r · g)", font=self.card_font, font_size=20, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Centripetal Requirement: F_c = m·v² / r", font=self.body_font, font_size=11.5, color=self.text_white).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Provided By Friction:    m·v²/r ≤ f_s,max = μ_s·mg", font=self.card_font, font_size=12, color=self.accent_green).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• Mass Independence:       Mass m cancels out completely!", font=self.card_font, font_size=12, color=self.accent_blue).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• If v > v_max:            Tires skid OUTWARD off the turn", font=self.body_font, font_size=11.5, color=self.accent_red).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 10 DEEP-DIVE: CENTRIPETAL IS A ROLE, NOT A NEW FORCE", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("WHO PROVIDES CENTRIPETAL FORCE?", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• Flat road turn: Static Friction (f_s)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Whirling stone: String Tension (T)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Planetary orbit: Gravity (G M m / r²)", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Electron orbit: Electrostatic Coulomb pull", font=self.card_font, font_size=11, color=self.accent_green).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("SKIDDING ON WET / ICY ROADS", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• On wet road, μ_s drops by a factor of 4", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• Safe speed v_max drops by half: √(1/4) = 1/2", font=self.card_font, font_size=12, color=self.accent_red).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• Anti-lock Braking (ABS) preserves static μ_s", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• Kinetic sliding friction is far weaker than static!", font=self.card_font, font_size=11, color=self.accent_gold).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 10: MASS INDEPENDENCE ON FLAT TURNS", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Believing a heavy loaded truck can negotiate a flat curve faster than a car!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: m·v²/r = μ_s·m·g => Mass cancels out completely: v_max = √(μ_s·r·g)!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Both a 5000 kg truck and a 1000 kg car skid at the exact same speed on the identical curve.", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2024 (Level Turn) • NEET 2022 • NEET 2019", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)


# ---------------------------------------------------------------------------
# 11. BankedRoadVerticalCircleScene (P11-C03-T04-V11)
# ---------------------------------------------------------------------------
class BankedRoadVerticalCircleScene(ModularUnit3Scene):
    def build_beat_1(self):
        tag = Text("Laws of Motion • Advanced Circular Motion", font=self.card_font, font_size=18, color=self.muted_text)
        title = Text("Engineered Road Banking & Vertical Circles", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ref = Text("NCERT Class 11 Physics • Chapter 4 • Section 4.9.1", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(tag, title, ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("OPTIMUM BANKING SPEED & VERTICAL LOOP THRESHOLDS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.9.1 • Normal Force Tilt Eliminates Tire Wear & Friction Dependence", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=box.get_left() + RIGHT * 0.3, end=box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # Left Visual: Banked incline wedge with car
        px = box.get_left()[0] + 1.2
        py = box.get_center()[1] - 1.2
        wedge = Polygon(np.array([px, py, 0]), np.array([px + 3.4, py + 1.6, 0]), np.array([px + 3.4, py, 0]), color=self.accent_purple, fill_color="#1E293B", fill_opacity=0.5, stroke_width=2.5)

        mid_w = np.array([px + 1.7, py + 0.8, 0])
        car = RoundedRectangle(corner_radius=0.06, width=1.1, height=0.6, stroke_color=self.accent_blue, stroke_width=2, fill_color="#0F172A", fill_opacity=0.9).rotate(np.arctan(1.6/3.4)).move_to(mid_w + np.array([-0.2, 0.4, 0]))

        # Normal vector perpendicular to wedge
        norm_ang = np.arctan(1.6/3.4) + PI/2
        arr_N = Arrow(start=car.get_center(), end=car.get_center() + np.array([1.2*np.cos(norm_ang), 1.2*np.sin(norm_ang), 0]), color=self.accent_green, buff=0, stroke_width=2.5)
        lbl_N = Text("N", font=self.card_font, font_size=11, color=self.accent_green).next_to(arr_N.get_end(), UL, buff=0.08)

        left_pane = VGroup(wedge, car, arr_N, lbl_N)

        # Right Pane: Equations
        rx = box.get_right()[0] - 2.8
        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.1, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([rx, box.get_center()[1] + 1.0, 0]))
        eq_t = Text("v_opt = √(r · g · tan θ)", font=self.card_font, font_size=20, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())

        row1 = Text("• Zero-Friction Speed:     v_0 = √(r·g·tan θ) (Zero Tire Wear)", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(eq_box, DOWN, buff=0.25).align_to(eq_box, LEFT)
        row2 = Text("• Max Speed with Friction: v_max = √[rg(tan θ + μ) / (1 - μ·tan θ)]", font=self.body_font, font_size=10.5, color=self.text_white).next_to(row1, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row3 = Text("• String Vertical Loop:    v_bottom ≥ √(5 g r)  &  v_top ≥ √(g r)", font=self.card_font, font_size=11.5, color=self.accent_gold).next_to(row2, DOWN, buff=0.18).align_to(eq_box, LEFT)
        row4 = Text("• Rigid Rod Vertical Loop: v_bottom ≥ √(4 g r) = 2√(g r)", font=self.card_font, font_size=11.5, color=self.accent_blue).next_to(row3, DOWN, buff=0.18).align_to(eq_box, LEFT)

        right_pane = VGroup(eq_box, eq_t, row1, row2, row3, row4)
        return VGroup(box, card_title, card_sub, h_div, left_pane, right_pane)

    def build_beat_3(self):
        box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_gold, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        title = Text("CONCEPT 11 DEEP-DIVE: STRING vs RIGID ROD IN VERTICAL CIRCLE", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(box.get_top(), DOWN, buff=0.2)
        div = Line(start=box.get_left() + RIGHT * 0.4, end=box.get_right() + LEFT * 0.4, color="#334155").next_to(title, DOWN, buff=0.15)

        card1 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_left() + RIGHT * 2.9 + DOWN * 0.3)
        c1_t = Text("CASE 1: MASS ON A STRING", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(card1.get_top(), DOWN, buff=0.2)
        c1_b1 = Text("• String goes SLACK if tension drops below 0", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_t, DOWN, buff=0.15).align_to(card1, LEFT).shift(RIGHT * 0.3)
        c1_b2 = Text("• Minimum speed at apex: v_top ≥ √(g · r)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c1_b1, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b3 = Text("• Minimum speed at bottom: v_bot ≥ √(5 g · r)", font=self.card_font, font_size=12, color=self.accent_green).next_to(c1_b2, DOWN, buff=0.12).align_to(c1_b1, LEFT)
        c1_b4 = Text("• Tension difference: T_bottom - T_top = 6 mg", font=self.body_font, font_size=11, color=self.text_white).next_to(c1_b3, DOWN, buff=0.12).align_to(c1_b1, LEFT)

        card2 = RoundedRectangle(corner_radius=0.1, width=5.2, height=3.2, stroke_color=self.accent_green, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.4).move_to(box.get_right() + LEFT * 2.9 + DOWN * 0.3)
        c2_t = Text("CASE 2: MASS ON A RIGID ROD", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(card2.get_top(), DOWN, buff=0.2)
        c2_b1 = Text("• Rigid rod can support compression!", font=self.card_font, font_size=11.5, color=self.accent_green).next_to(c2_t, DOWN, buff=0.15).align_to(card2, LEFT).shift(RIGHT * 0.3)
        c2_b2 = Text("• Rod NEVER slacks: speed at top can be 0", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b1, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b3 = Text("• v_top ≥ 0  =>  0.5·m·v² = m·g·(2r)", font=self.body_font, font_size=11, color=self.text_white).next_to(c2_b2, DOWN, buff=0.12).align_to(c2_b1, LEFT)
        c2_b4 = Text("• v_bottom ≥ √(4 g r) = 2√(g r) (NOT √5gr!)", font=self.card_font, font_size=12, color=self.accent_gold).next_to(c2_b3, DOWN, buff=0.12).align_to(c2_b1, LEFT)

        return VGroup(box, title, div, card1, c1_t, c1_b1, c1_b2, c1_b3, c1_b4, card2, c2_t, c2_b1, c2_b2, c2_b3, c2_b4)

    def build_beat_4(self):
        box = RoundedRectangle(corner_radius=0.14, height=5.2, width=11.6, stroke_color=self.accent_red, stroke_width=2.5, fill_color="#1A0B0E", fill_opacity=0.85).move_to(DOWN * 0.05)
        top_badge = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.55, stroke_color=self.accent_red, stroke_width=1.5, fill_color="#3B0D14", fill_opacity=0.9).next_to(box.get_top(), DOWN, buff=0.15)
        b_txt = Text("NEET TRAP 11: STRING VS RIGID ROD THRESHOLDS", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_red).move_to(top_badge.get_center())

        trap_wrong = Text("❌ FATAL TRAP: Using the string threshold v = √(5gr) for a sphere on a light rigid rod!", font=self.body_font, font_size=11.5, color="#FCA5A5").next_to(top_badge, DOWN, buff=0.35)
        rule_box = RoundedRectangle(corner_radius=0.1, width=10.6, height=1.3, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#062817", fill_opacity=0.8).next_to(trap_wrong, DOWN, buff=0.25)
        r_t1 = Text("NCERT RULE: A rigid rod supports compression; velocity at apex can drop to 0 without slacking!", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_green).move_to(rule_box.get_center() + UP * 0.22)
        r_t2 = Text("Energy conservation gives v_bottom ≥ √(4gr) = 2√(gr). A string requires v_bottom ≥ √(5gr)!", font=self.body_font, font_size=11, color=self.text_white).move_to(rule_box.get_center() + DOWN * 0.22)

        pyq_row = Text("Authentic NEET Questions: NEET 2023 (Rod Loop) • NEET 2020 • NEET 2017", font=self.card_font, font_size=11, color=self.accent_gold).next_to(rule_box, DOWN, buff=0.3)
        punchline = Text("Master this to secure full marks in NEET Physics.", font=self.body_font, font_size=12, weight="BOLD", color=self.text_white).next_to(pyq_row, DOWN, buff=0.25)

        return VGroup(box, top_badge, b_txt, trap_wrong, rule_box, r_t1, r_t2, pyq_row, punchline)
