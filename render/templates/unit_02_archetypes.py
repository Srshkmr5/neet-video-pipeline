"""
Dedicated Visual Archetypes for Unit 2: Kinematics
NCERT Class 11 Physics Part 1, Chapters 3 & 4 (Motion in a Straight Line & Motion in a Plane)

Provides modular build_beat_1(), build_beat_2(), build_beat_3(), build_beat_4()
for instant static screenshot verification and broadcast video animation.
Strictly adheres to Rules 8-14:
- Zero Page Numbers
- High-DPI typography floor (>= 11pt, Consolas / Cascadia Mono)
- 1:1 aspect ratio without vector squishing
"""

from manim import *
from render.templates.base import (
    FONT_HEADER, FONT_CARD, FONT_BODY,
    BaseNeetScene, BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN,
    TEXT_WHITE, MUTED_TEXT, FONT_PRIMARY, FONT_MONO
)

Text.set_default(font=FONT_BODY)

class ModularUnit2Scene(BaseNeetScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header_font = FONT_HEADER
        self.card_font = FONT_CARD
        self.body_font = FONT_BODY
        self.topic_font = FONT_HEADER

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

        # Beat 5: Transition Teaser (Up Next in Sequence)
        self.render_release_teaser(duration=3.5)


# ---------------------------------------------------------------------------
# 1. PositionTimeGraphsScene (P11-C02-T01-V01)
# ---------------------------------------------------------------------------
class PositionTimeGraphsScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Straight Line Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Position-Time Graphs (x-t)", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 3", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        # Master card container box
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        # Card Header inside top of card
        card_title = Text("POSITION-TIME GRAPHICAL ANALYSIS (x-t)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 3.2 • Instantaneous Velocity as the Tangent Derivative: v = dx/dt", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        # --- LEFT PANE: Coordinate Graph Stage ---
        axes = Axes(
            x_range=[0, 5.0, 1],
            y_range=[0, 4.0, 1],
            x_length=4.6,
            y_length=3.0,
            tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)

        x_lbl = Text("Time t (s)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Position x (m)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        # Accelerated position curve x(t) = 0.15 * t^2 + 0.2 * t
        curve = axes.plot(lambda t: 0.15 * (t ** 2) + 0.2 * t, x_range=[0, 4.2], color=self.accent_blue, stroke_width=3)
        tangent_pt = axes.c2p(2.5, 0.15 * (2.5**2) + 0.2 * 2.5)
        dot = Dot(tangent_pt, color=self.accent_gold, radius=0.08)
        
        # Tangent line at t = 2.5s (slope = 2*0.15*2.5 + 0.2 = 0.95)
        t_line = Line(
            start=axes.c2p(1.2, (0.15 * (2.5**2) + 0.2 * 2.5) - 0.95 * (2.5 - 1.2)),
            end=axes.c2p(3.8, (0.15 * (2.5**2) + 0.2 * 2.5) + 0.95 * (3.8 - 2.5)),
            color=self.accent_green, stroke_width=2
        )
        slope_tag = Text("Slope = v", font=self.body_font, font_size=11, color=self.accent_green).next_to(dot, UL, buff=0.15)

        left_group = VGroup(axes, x_lbl, y_lbl, curve, t_line, dot, slope_tag)

        # --- RIGHT PANE: Mathematical Derivation & Law ---
        right_center_x = card_box.get_right()[0] - 2.8

        eq_box = RoundedRectangle(corner_radius=0.1, width=5.2, height=1.0, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.1, 0]))
        eq_text = Text("v = dx / dt = tan θ", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq_box.get_center())
        eq_sub = Text("Instantaneous Velocity = Lim (Δt→0) Δx / Δt", font=self.body_font, font_size=10, color=self.muted_text).next_to(eq_box, DOWN, buff=0.10)

        # 3 Key Physical Interpretations
        rule1 = Text("• Positive Slope  (θ < 90°): v > 0 (Moving Forward)", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Zero Slope      (θ = 0°):  v = 0 (Stationary / Rest)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule3 = Text("• Negative Slope  (θ > 90°): v < 0 (Moving Backward)", font=self.body_font, font_size=11, color=self.accent_red)
        rules_v = VGroup(rule1, rule2, rule3).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(eq_sub, DOWN, buff=0.25).align_to(eq_box, LEFT).shift(RIGHT * 0.15)

        right_group = VGroup(eq_box, eq_text, eq_sub, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        # Principles / Comparative Scenarios Card
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("CORE KINEMATIC PRINCIPLES: 3 MOTION SCENARIOS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Interpreting Curvature & Concavity on Position-Time Graphs", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        # 3 Comparison Rows
        rows = []
        scenarios = [
            ("SCENARIO 1: REST (v = 0)", "Horizontal Flat Line (dx/dt = 0)", "Position is invariant with time; acceleration a = 0.", self.accent_blue),
            ("SCENARIO 2: UNIFORM VELOCITY", "Slanted Straight Line (dx/dt = const)", "Constant velocity; zero net acceleration (a = 0).", self.accent_green),
            ("SCENARIO 3: ACCELERATED MOTION", "Curved Parabolic Path (d²x/dt² != 0)", "Concave up (Cup) => a > 0. Concave down (Cap) => a < 0.", self.accent_gold)
        ]

        for title, curve_type, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(curve_type, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)

        # HCV Nuance Footer Box
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Negative slope indicates motion in opposite direction, NOT necessarily deceleration!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)

        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        # NEET Trap Card
        trap_box = RoundedRectangle(
            corner_radius=0.14, height=5.0, width=11.6,
            stroke_color=self.accent_red, stroke_width=1.8,
            fill_color="#18080C", fill_opacity=0.45
        ).move_to(DOWN * 0.1)

        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: SLOPE & GRAPH CONFUSION", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())

        trap_sub = Text("Students frequently confuse the slope of x-t graph with v-t graph, or assume flat slope means uniform motion!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        # Contrast Table: x-t Graph vs v-t Graph
        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)

        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("POSITION-TIME (x-t) GRAPH", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("VELOCITY-TIME (v-t) GRAPH", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Slope dx/dt = VELOCITY (v)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Slope dv/dt = ACCELERATION (a)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Horizontal Line: REST (v = 0)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Horizontal Line: CONSTANT VELOCITY (a = 0)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)

        # Golden Takeaway Badge
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: On an x-t graph, slope gives VELOCITY, never acceleration. Flat line = REST!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())

        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 2. VelocityTimeGraphsScene (P11-C02-T03-V08)
# ---------------------------------------------------------------------------
class VelocityTimeGraphsScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Straight Line Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Velocity-Time Graphs & Displacement", font=self.header_font, font_size=30, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 3", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("VELOCITY-TIME GRAPHICAL ANALYSIS (v-t)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 3.3 • Slope = dv/dt (Acceleration) • Area Under Curve = Displacement", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        # --- LEFT PANE: Coordinate Graph Stage ---
        axes = Axes(
            x_range=[0, 5.0, 1],
            y_range=[-1.0, 4.0, 1],
            x_length=4.6,
            y_length=3.0,
            tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)

        x_lbl = Text("Time t (s)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Velocity v (m/s)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        # Trapezoidal velocity profile
        pt_origin = axes.c2p(0, 0)
        pt_start = axes.c2p(0, 1.0)
        pt_ramp = axes.c2p(2.5, 3.5)
        pt_const = axes.c2p(4.0, 3.5)
        pt_end_x = axes.c2p(4.0, 0)

        # Shaded area under curve (displacement)
        area_polygon = Polygon(
            pt_origin, pt_start, pt_ramp, pt_const, pt_end_x,
            fill_color=self.accent_blue, fill_opacity=0.35, stroke_width=0
        )
        area_label = Text("Area = Displacement Δx", font=self.body_font, font_size=10, weight="BOLD", color=self.accent_blue).move_to(axes.c2p(2.0, 1.3))

        # Velocity line
        line1 = Line(pt_start, pt_ramp, color=self.accent_gold, stroke_width=3)
        line2 = Line(pt_ramp, pt_const, color=self.accent_green, stroke_width=3)
        slope_tag = Text("Slope = a", font=self.body_font, font_size=10, color=self.accent_gold).next_to(line1.get_center(), UL, buff=0.10)

        left_group = VGroup(axes, x_lbl, y_lbl, area_polygon, line1, line2, area_label, slope_tag)

        # --- RIGHT PANE: Mathematical Derivations ---
        right_center_x = card_box.get_right()[0] - 2.8

        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("Slope: a = dv / dt", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Area: Δx = ∫ v dt", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Slope > 0: Acceleration (Speeding up forward)", font=self.body_font, font_size=11, color=self.accent_gold)
        rule2 = Text("• Slope = 0: Uniform Velocity (Zero net force)", font=self.body_font, font_size=11, color=self.accent_green)
        rule3 = Text("• Area Above Axis: Positive Displacement (+x)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Area Below Axis: Negative Displacement (-x)", font=self.body_font, font_size=11, color=self.accent_red)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)

        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("CORE KINEMATIC PRINCIPLES: DISPLACEMENT VS DISTANCE", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Evaluating Positive and Negative Signed Areas on Velocity-Time Graphs", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("DISPLACEMENT (Vector Δx)", "Algebraic Net Sum: Δx = Area_up - Area_down", "Vector change in position; can be positive, negative, or zero.", self.accent_blue),
            ("DISTANCE TRAVELED (Scalar s)", "Total Geometric Area: s = |Area_up| + |Area_down|", "Total path length traversed; strictly positive and non-decreasing.", self.accent_green),
            ("UNIFORM ACCELERATION", "Constant Slope: a = (v - v₀) / t", "Enables kinematic relations: v² = v₀² + 2as and s = v₀t + 1/2 at².", self.accent_gold)
        ]

        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)

        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Negative area represents motion in reverse direction; never ignore the sign when finding displacement!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)

        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(
            corner_radius=0.14, height=5.0, width=11.6,
            stroke_color=self.accent_red, stroke_width=1.8,
            fill_color="#18080C", fill_opacity=0.45
        ).move_to(DOWN * 0.1)

        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: DISTANCE VS DISPLACEMENT AREA ERROR", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())

        trap_sub = Text("Students frequently subtract negative area when asked for total distance, or ignore sign for displacement!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)

        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("CALCULATING DISPLACEMENT (Δx)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("CALCULATING TOTAL DISTANCE (s)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Δx = Area(Up) - Area(Down)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("s = |Area(Up)| + |Area(Down)|", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Result can be NEGATIVE or ZERO", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Result is ALWAYS POSITIVE (> 0)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)

        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Distance sums absolute area magnitudes. Displacement takes signed net area!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())

        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 3. ResolutionOfVectorsScene (P11-C02-T02-V01)
# ---------------------------------------------------------------------------
class ResolutionOfVectorsScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Motion in a Plane", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Resolution of Vectors", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("ORTHOGONAL RESOLUTION OF 2D VECTORS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.5 • Decomposing Vector A into Independent Mutually Perpendicular Components", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        # --- LEFT PANE: Vector Coordinate Stage ---
        axes = Axes(
            x_range=[0, 5.0, 1],
            y_range=[0, 4.0, 1],
            x_length=4.6,
            y_length=3.0,
            tips=True,
            axis_config={"color": "#64748B", "stroke_width": 1.5}
        ).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)

        x_lbl = Text("X Axis", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Y Axis", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        # Main vector A at 37 degrees (cos=0.8, sin=0.6)
        pt_origin = axes.c2p(0, 0)
        pt_head = axes.c2p(3.6, 2.7)
        pt_x = axes.c2p(3.6, 0)
        pt_y = axes.c2p(0, 2.7)

        vec_arrow = Arrow(pt_origin, pt_head, buff=0, color=self.accent_blue, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        vec_label = Text("Vector A", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(vec_arrow.get_center(), UL, buff=0.15)

        # Projections
        dash_x = DashedLine(pt_head, pt_x, color="#475569", stroke_width=1.5, dash_length=0.08)
        dash_y = DashedLine(pt_head, pt_y, color="#475569", stroke_width=1.5, dash_length=0.08)

        # Component arrows
        arrow_x = Arrow(pt_origin, pt_x, buff=0, color=self.accent_gold, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        arrow_y = Arrow(pt_origin, pt_y, buff=0, color=self.accent_green, stroke_width=3, max_tip_length_to_length_ratio=0.12)

        lbl_ax = Text("Ax = A cos θ", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold).next_to(arrow_x, DOWN, buff=0.15)
        lbl_ay = Text("Ay = A sin θ", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).next_to(arrow_y, LEFT, buff=0.15)

        # Angle arc
        arc_theta = Arc(radius=0.7, start_angle=0, angle=36.87 * DEGREES, arc_center=pt_origin, color=TEXT_WHITE)
        theta_tag = Text("θ", font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(arc_theta, RIGHT, buff=0.08).shift(UP * 0.05)

        left_group = VGroup(axes, x_lbl, y_lbl, dash_x, dash_y, arrow_x, arrow_y, vec_arrow, vec_label, lbl_ax, lbl_ay, arc_theta, theta_tag)

        # --- RIGHT PANE: Mathematical Derivations ---
        right_center_x = card_box.get_right()[0] - 2.8

        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("A = Ax î + Ay ĵ", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Ax = A cos θ   |   Ay = A sin θ", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Magnitude:  |A| = √(Ax² + Ay²)", font=self.body_font, font_size=11, color=self.accent_gold)
        rule2 = Text("• Direction:  tan θ = Ay / Ax", font=self.body_font, font_size=11, color=self.accent_green)
        rule3 = Text("• Orthogonality: î · ĵ = 0 (Completely Independent)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Unit Vectors:  |î| = 1, |ĵ| = 1 along Cartesian axes", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)

        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("CORE VECTOR PRINCIPLES: ORTHOGONAL INDEPENDENCE", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Behavior of Vector Components in 2D Kinematics and Multi-Axis Motion", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("ANGLE WITH HORIZONTAL (θ)", "Ax = A cos θ  and  Ay = A sin θ", "Standard textbook resolution; adjacent side to horizontal axis.", self.accent_blue),
            ("ANGLE WITH VERTICAL (φ)", "Ay = A cos φ  and  Ax = A sin φ", "Cosine is strictly attached to the axis ADJACENT to the given angle!", self.accent_gold),
            ("INDEPENDENT KINEMATICS", "x(t) and y(t) proceed without mutual interference", "Motion along x does not affect y position, velocity, or acceleration.", self.accent_green)
        ]

        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)

        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Components along perpendicular coordinates have zero projection on each other and operate independently.", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)

        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(
            corner_radius=0.14, height=5.0, width=11.6,
            stroke_color=self.accent_red, stroke_width=1.8,
            fill_color="#18080C", fill_opacity=0.45
        ).move_to(DOWN * 0.1)

        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: AUTOMATIC COSINE ASSUMPTION", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())

        trap_sub = Text("Students automatically assign cosine to horizontal axis without verifying which axis angle is given with!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)

        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("ANGLE WITH HORIZONTAL (θ)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("ANGLE WITH VERTICAL (φ)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Ax = A cos θ   |   Ay = A sin θ", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Ax = A sin φ   |   Ay = A cos φ", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Horizontal is ADJACENT side", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Vertical is ADJACENT side (SWAP!)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)

        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: The side adjacent to the angle gets COSINE; the opposite side gets SINE!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())

        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 4. RelativeVelocityScene (P11-C02-T03-V09)
# ---------------------------------------------------------------------------
class RelativeVelocityScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Motion in a Plane", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Relative Velocity & River-Boat Vectors", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("RELATIVE VELOCITY VECTOR KINEMATICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.6 • Vector Addition of Relative Velocities: v_AB = v_A - v_B", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        # --- LEFT PANE: River-Boat Stage ---
        river_box = RoundedRectangle(corner_radius=0.08, width=4.6, height=3.2, stroke_color="#1E3A8A", stroke_width=1.0, fill_color="#0B192C", fill_opacity=0.6).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)

        bank_top = Line(river_box.get_left() + UP * 1.4, river_box.get_right() + UP * 1.4, color="#64748B", stroke_width=2)
        bank_bot = Line(river_box.get_left() + DOWN * 1.4, river_box.get_right() + DOWN * 1.4, color="#64748B", stroke_width=2)

        # River flow arrow vr
        flow_arrow = Arrow(river_box.get_left() + RIGHT * 0.8 + UP * 0.8, river_box.get_left() + RIGHT * 2.4 + UP * 0.8, buff=0, color="#38BDF8", stroke_width=2)
        flow_lbl = Text("River Flow: vr", font=self.body_font, font_size=10, color="#38BDF8").next_to(flow_arrow, UP, buff=0.08)

        # Boat velocity v_br angled upstream
        start_pt = bank_bot.get_center() + LEFT * 0.5
        vbr_end = start_pt + UP * 2.8 + LEFT * 1.2
        arrow_vbr = Arrow(start_pt, vbr_end, buff=0, color=self.accent_gold, stroke_width=3)
        lbl_vbr = Text("v_br (Steering)", font=self.body_font, font_size=10, color=self.accent_gold).next_to(arrow_vbr.get_center(), LEFT, buff=0.10)

        # River flow vector from vbr_end to straight top
        v_end = start_pt + UP * 2.8
        arrow_flow = Arrow(vbr_end, v_end, buff=0, color="#38BDF8", stroke_width=2)

        # Resultant boat velocity vb (straight across)
        arrow_vb = Arrow(start_pt, v_end, buff=0, color=self.accent_green, stroke_width=3)
        lbl_vb = Text("v_b (Ground)", font=self.body_font, font_size=10, weight="BOLD", color=self.accent_green).next_to(arrow_vb.get_center(), RIGHT, buff=0.10)

        left_group = VGroup(river_box, bank_top, bank_bot, flow_arrow, flow_lbl, arrow_vbr, lbl_vbr, arrow_flow, arrow_vb, lbl_vb)

        # --- RIGHT PANE: Mathematical Derivations ---
        right_center_x = card_box.get_right()[0] - 2.8

        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("v_b = v_br + v_r", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Shortest Path: sin θ = vr / vbr", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Resultant Speed: vb = √(vbr² - vr²)", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Crossing Time:  t = d / vb = d / √(vbr² - vr²)", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Shortest Time:  Aim directly across (θ = 90°)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Downstream Drift: x = vr · t_min", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)

        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(
            corner_radius=0.12, height=5.0, width=11.6,
            stroke_color=self.accent_blue, stroke_width=1.5,
            fill_color="#0F172A", fill_opacity=0.0
        ).move_to(DOWN * 0.1)

        card_title = Text("CORE PRINCIPLES: 2D RELATIVE MOTION SCENARIOS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Contrasting Shortest Path vs Shortest Time Across a Flowing River", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)

        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("SHORTEST PATH (Zero Drift)", "Aim upstream at sin θ = vr / vbr", "Resultant velocity is purely perpendicular to banks; drift is zero.", self.accent_blue),
            ("SHORTEST TIME (Minimum Duration)", "Aim directly across: t_min = d / vbr", "Fastest crossing possible; however, river flow causes downstream drift x = vr * t.", self.accent_green),
            ("RAIN-MAN PROBLEM", "v_rm = v_rain - v_man", "Relative velocity determines the umbrella angle tan α = v_man / v_rain.", self.accent_gold)
        ]

        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)

        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Crossing time is controlled ONLY by the velocity component perpendicular to river banks!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)

        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(
            corner_radius=0.14, height=5.0, width=11.6,
            stroke_color=self.accent_red, stroke_width=1.8,
            fill_color="#18080C", fill_opacity=0.45
        ).move_to(DOWN * 0.1)

        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: SHORTEST PATH VS SHORTEST TIME", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())

        trap_sub = Text("Students confuse crossing in the minimum time with crossing along the shortest physical distance!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)

        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("CONDITION: SHORTEST PATH (Zero Drift)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("CONDITION: SHORTEST TIME", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Aim UPSTREAM: sin θ = vr / vbr", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Aim PERPENDICULAR: θ = 90°", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Duration: t = d / √(vbr² - vr²)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Duration: t_min = d / vbr  (DRIFT OCCURS!)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)

        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Shortest time = head directly across (drifts). Shortest path = head upstream (takes longer)!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())

        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)

# ---------------------------------------------------------------------------
# 5. TimeOfFlightScene (P11-C02-T03-V01)
# ---------------------------------------------------------------------------
class TimeOfFlightScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Time of Flight (T)", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("PROJECTILE TIME OF FLIGHT DYNAMICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • Time in Air Determined Exclusively by Vertical Velocity Component", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 6.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        x_lbl = Text("X (Range)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Y (Height)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        traj = axes.plot(lambda x: 2.2 * x - 0.44 * (x**2), x_range=[0, 5.0], color=self.accent_blue, stroke_width=3)
        v0_arrow = Arrow(axes.c2p(0, 0), axes.c2p(1.2, 1.4), buff=0, color=self.accent_gold, stroke_width=3)
        v0_lbl = Text("v₀", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_gold).next_to(v0_arrow.get_end(), UR, buff=0.05)

        t_lbl = Text("T = 2v₀ sin θ / g", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(axes.c2p(2.5, 2.9))
        left_group = VGroup(axes, x_lbl, y_lbl, traj, v0_arrow, v0_lbl, t_lbl)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("T = (2 v₀ sin θ) / g", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("t_ascent = t_descent = (v₀ sin θ) / g", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Vertical Free Flight: Determined strictly by v_0y", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Horizontal Independence: vx = v0 cos θ has ZERO effect", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Symmetry: Time to apex equals time from apex to ground", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Maximum Duration: Occurs at vertical launch (θ = 90°)", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: TIME OF FLIGHT DYNAMICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Vertical Kinematics and Parabolic Temporal Symmetry", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("VERTICAL VELOCITY RESTORATION", "v_y(T) = - v_0y = - v_0 sin θ", "Magnitude of vertical velocity at impact equals launch value, opposite in sign.", self.accent_blue),
            ("HORIZONTALLY DRIVEN DISTANCE", "Range R = v_x * T = (v_0 cos θ) * T", "Horizontal travel is simply constant velocity multiplied by total flight time.", self.accent_green),
            ("TIME SYMMETRY", "t_ascent = t_descent = T / 2", "In absence of air resistance, parabolic trajectory is temporally symmetric.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Horizontal velocity vx has zero acceleration and exerts zero influence on time in the air!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: ANGLE WITH VERTICAL IN TIME FORMULA", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("When angle is given with VERTICAL, students blindly write 2v0 sin θ / g, which fails!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("LAUNCH ANGLE WITH HORIZONTAL (θ)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("LAUNCH ANGLE WITH VERTICAL (φ)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("v_y = v₀ sin θ", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("v_y = v₀ cos φ (SWAPPED!)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("T = (2 v₀ sin θ) / g", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("T = (2 v₀ cos φ) / g", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Time of flight uses VERTICAL component. If angle is with vertical, use COSINE!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 6. MaxHeightArcScene (P11-C02-T03-V02)
# ---------------------------------------------------------------------------
class MaxHeightArcScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("The Max Height Arc (H_max)", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("MAXIMUM HEIGHT TRAJECTORY DYNAMICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • At the Apex: Vertical Velocity vy = 0, Horizontal Velocity vx = v0 cos θ", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 6.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        x_lbl = Text("X (Range)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Y (Height)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        traj = axes.plot(lambda x: 2.2 * x - 0.44 * (x**2), x_range=[0, 5.0], color=self.accent_blue, stroke_width=3)
        apex_pt = axes.c2p(2.5, 2.75)
        dot_apex = Dot(apex_pt, color=self.accent_gold, radius=0.08)
        arrow_vx = Arrow(apex_pt, axes.c2p(3.5, 2.75), buff=0, color=self.accent_green, stroke_width=3)
        vx_lbl = Text("vx = v₀ cos θ (vy = 0)", font=self.body_font, font_size=10, weight="BOLD", color=self.accent_green).next_to(arrow_vx, UP, buff=0.08)

        h_line = DashedLine(axes.c2p(2.5, 0), apex_pt, color=self.accent_gold, stroke_width=1.5)
        h_tag = Text("H_max", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).next_to(h_line, LEFT, buff=0.10)
        left_group = VGroup(axes, x_lbl, y_lbl, traj, dot_apex, arrow_vx, vx_lbl, h_line, h_tag)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("H_max = (v₀² sin² θ) / (2g)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Apex Speed: v_top = v₀ cos θ  (≠ 0)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Kinetic Energy at Apex: K_top = 1/2 m (v0 cos θ)²", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Acceleration at Apex: a = g purely DOWNWARDS", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Velocity & Acceleration are PERPENDICULAR at top", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Non-Zero Motion: Particle continues moving horizontally", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: ENERGETICS & APEX VELOCITY", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Mechanical Energy Conservation Across the Trajectory Arc", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("KINETIC ENERGY FRACTION", "K_top / K_0 = cos² θ", "At 45° launch, exactly 50% of launch kinetic energy is retained at top.", self.accent_blue),
            ("POTENTIAL ENERGY FRACTION", "U_top / K_0 = sin² θ", "Complementary fraction converted to gravitational potential energy.", self.accent_green),
            ("ORTHOGONALITY AT APEX", "v_vec · a_vec = 0", "Velocity vector (horizontal) is strictly perpendicular to gravity vector (downward).", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Speed at the highest point is NOT zero; it is minimum and equals v0 cos θ!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: ZERO APEX VELOCITY ERROR", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students frequently assume speed and kinetic energy become zero at maximum height!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("VERTICAL VELOCITY AT TOP (vy)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("TOTAL VELOCITY AT TOP (v_net)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("vy = 0  (Momentary vertical rest)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("v_net = vx = v₀ cos θ  (≠ 0 !)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Vertical KE = 0", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Total KE = 1/2 m v₀² cos² θ  (NON-ZERO!)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Only vertical velocity is zero at apex! Speed and Kinetic Energy are MINIMUM, not zero!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)

# ---------------------------------------------------------------------------
# 7. HorizontalRangeScene (P11-C02-T03-V03)
# ---------------------------------------------------------------------------
class HorizontalRangeScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Horizontal Range & Complementary Angles", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("HORIZONTAL RANGE & COMPLEMENTARY ANGLES (θ & 90°-θ)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • Range Identity: R(θ) = R(90°-θ) = (v₀² sin 2θ) / g", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 6.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        x_lbl = Text("X (Range)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Y (Height)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        # 30 deg curve (low flat) vs 60 deg curve (high tall) -> same range 4.5
        t30 = axes.plot(lambda x: 0.577 * x - 0.128 * (x**2), x_range=[0, 4.5], color=self.accent_gold, stroke_width=3)
        t60 = axes.plot(lambda x: 1.732 * x - 0.385 * (x**2), x_range=[0, 4.5], color=self.accent_blue, stroke_width=3)

        lbl30 = Text("θ = 30°", font=self.body_font, font_size=10, color=self.accent_gold).move_to(axes.c2p(2.2, 0.85))
        lbl60 = Text("θ = 60° (Taller)", font=self.body_font, font_size=10, color=self.accent_blue).move_to(axes.c2p(2.2, 2.2))

        dot_land = Dot(axes.c2p(4.5, 0), color=self.accent_green, radius=0.08)
        lbl_r = Text("Same Range R", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_green).next_to(dot_land, UR, buff=0.08)

        left_group = VGroup(axes, x_lbl, y_lbl, t30, t60, lbl30, lbl60, dot_land, lbl_r)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("R = (v₀² sin 2θ) / g", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Max Range at θ = 45°: R_max = v₀² / g", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Complementary Equality: R(θ) = R(90° - θ)", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Maximum Range: sin(2 * 45°) = sin 90° = 1", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Height Ratio: H1 / H2 = tan² θ", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Time Product: T1 * T2 = (2 R) / g", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: COMPLEMENTARY PAIR RELATIONS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Mathematical Symmetry between Angles θ and (90° - θ)", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("RANGE IDENTITY", "sin 2(90° - θ) = sin(180° - 2θ) = sin 2θ", "Identical horizontal landing point for any complementary angle pair.", self.accent_blue),
            ("TIME OF FLIGHT PRODUCT", "T₁ · T₂ = (2 / g) · R", "Product of flight times is directly proportional to horizontal range.", self.accent_green),
            ("MAXIMUM HEIGHT PRODUCT", "H₁ · H₂ = R² / 16", "Geometric mean of maximum heights equals R / 4.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Although ranges are equal for θ and 90°-θ, heights and flight times are strictly UNEQUAL!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: ASSUMING EQUAL HEIGHTS FOR COMPLEMENTARY ANGLES", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students assume that because Range is equal, Time of Flight and Height must also be equal!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("LOW ANGLE (θ < 45°, e.g. 30°)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("HIGH ANGLE (90°-θ > 45°, e.g. 60°)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Range = R  (IDENTICAL)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Range = R  (IDENTICAL)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("H₁ is SMALLER, T₁ is SHORTER", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("H₂ is MUCH LARGER, T₂ is LONGER", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Complementary angles have IDENTICAL ranges, but strictly DIFFERENT heights and times!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 8. TrajectoryEquationScene (P11-C02-T03-V04)
# ---------------------------------------------------------------------------
class TrajectoryEquationScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Equation of Trajectory", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("PARABOLIC TRAJECTORY EQUATION ENGINE", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • Eliminating Time t to Relate Vertical Coordinate y to Horizontal Coordinate x", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 6.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        x_lbl = Text("X Coordinate", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Y Coordinate", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        traj = axes.plot(lambda x: 2.0 * x - 0.4 * (x**2), x_range=[0, 5.0], color=self.accent_blue, stroke_width=3)
        pt_sample = axes.c2p(3.0, 2.4)
        dot_pt = Dot(pt_sample, color=self.accent_gold, radius=0.08)
        lbl_pt = Text("P(x, y)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold).next_to(dot_pt, UR, buff=0.08)
        left_group = VGroup(axes, x_lbl, y_lbl, traj, dot_pt, lbl_pt)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("y = x tan θ - (g x²) / (2 v₀² cos² θ)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("HCV Form: y = x tan θ (1 - x / R)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Parabolic Nature: y = a x - b x² (Inverted Parabola)", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Initial Slope at Origin: (dy / dx) at x=0 is tan θ", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Range Intercept: When y = 0, x = 0 or x = R", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• HCV Shortcut: Instantly solves problems given range R", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: TRAJECTORY COEFFICIENT MATCHING", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Extracting Initial Speed and Launch Angle by Comparing Given Polynomial y = Ax - Bx²", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("COEFFICIENT A = tan θ", "Launch angle is directly θ = arctan(A)", "Independent of initial speed v0 and gravity g.", self.accent_blue),
            ("COEFFICIENT B = g / (2 v₀² cos² θ)", "v₀ = √[ g / (2 B cos² θ) ]", "Relates curvature directly to launch kinetic energy.", self.accent_green),
            ("RANGE FROM COEFFICIENTS", "R = A / B", "Ratio of linear to quadratic coefficient instantly yields horizontal range!", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Using y = x tan θ (1 - x/R) simplifies 90% of NEET trajectory problems in under 30 seconds!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: MISIDENTIFYING TRAJECTORY COEFFICIENTS", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students forget that the denominator contains cos² θ, not sin² θ or tan θ!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("CORRECT TRAJECTORY FORM", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("COMMON NEET TRAP BLUNDER", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("y = x tan θ - (g x²) / (2 v₀² cos² θ)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("y = x tan θ - (g x²) / (2 v₀² sin² θ)  [WRONG!]", font=self.body_font, font_size=11, color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Time substitution: t = x / (v₀ cos θ)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Horizontal motion uses vx = v0 cos θ ALWAYS", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Time t = x / (v₀ cos θ). Squaring time yields cos² θ in denominator!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)

# ---------------------------------------------------------------------------
# 9. HorizontalProjectionScene (P11-C02-T04-V10)
# ---------------------------------------------------------------------------
class HorizontalProjectionScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Horizontal Projection from a Height", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("HORIZONTAL PROJECTION KINEMATICS (INITIAL vy = 0)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • Semi-Parabolic Motion: Vertical Fall Identical to Free Drop from Rest", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 5.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        x_lbl = Text("X (Range)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Y (Height h)", font=self.body_font, font_size=11, color=self.muted_text).next_to(axes.y_axis.get_top(), UP, buff=0.12).shift(RIGHT * 0.3)

        cliff_pt = axes.c2p(0, 3.0)
        cliff_line = Line(axes.c2p(0, 0), cliff_pt, color="#64748B", stroke_width=3)
        arrow_v0 = Arrow(cliff_pt, axes.c2p(1.2, 3.0), buff=0, color=self.accent_gold, stroke_width=3)
        lbl_v0 = Text("v₀ (Pure Horizontal)", font=self.body_font, font_size=10, color=self.accent_gold).next_to(arrow_v0, UP, buff=0.08)

        traj = axes.plot(lambda x: 3.0 - 0.25 * (x**2), x_range=[0, 3.46], color=self.accent_blue, stroke_width=3)
        dot_impact = Dot(axes.c2p(3.46, 0), color=self.accent_green, radius=0.08)
        lbl_r = Text("Range R", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_green).next_to(dot_impact, UR, buff=0.08)

        left_group = VGroup(axes, x_lbl, y_lbl, cliff_line, arrow_v0, lbl_v0, traj, dot_impact, lbl_r)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("Time of Fall: t = √(2h / g)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Horizontal Range: R = v₀ · √(2h / g)", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Vertical Freedom: Fall time depends strictly on h and g", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Zero Effect of Speed: A fired bullet drops at same rate as dropped ball", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Impact Velocity: v_net = √(v₀² + 2gh)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Impact Angle: tan β = √(2gh) / v₀ with horizontal", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: HORIZONTAL LAUNCH DYNAMICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Simultaneous Ground Impact of Dropped vs Projected Bodies", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("DROPPED BODY (Free Fall)", "t = √(2h / g),   x = 0", "Initial horizontal and vertical velocity both zero.", self.accent_blue),
            ("HORIZONTALLY PROJECTED", "t = √(2h / g),   R = v₀ · t", "Takes EXACTLY identical time to hit ground; only horizontal landing shifts.", self.accent_green),
            ("VELOCITY VECTOR AT TIME t", "v_vec = v₀ î - (gt) ĵ", "Horizontal component remains strictly v0; vertical grows linearly under gravity.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Horizontal launch speed v0 has absolutely ZERO impact on the time taken to hit the ground!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: FASTER BULLET TAKES LONGER BLUNDER", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students assume that a projectile launched at 100 m/s stays in the air longer than one dropped from rest!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("DROPPED VERTICALLY FROM REST (h)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("FIRED HORIZONTALLY AT SPEED v₀ (h)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Time to strike: t = √(2h / g)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Time to strike: t = √(2h / g)  (EXACT SAME!)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Impact Speed: v = √(2gh)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Impact Speed: v = √(v₀² + 2gh)  (HIGHER SPEED)", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Both hit the ground SIMULTANEOUSLY! Only impact speed and landing distance differ!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 10. InclinedPlaneProjectileScene (P11-C02-T04-V11)
# ---------------------------------------------------------------------------
class InclinedPlaneProjectileScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Projectile on an Inclined Plane", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("PROJECTILE ON AN INCLINED PLANE (INCLINE ANGLE β, LAUNCH α)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • Resolving Gravity g along Incline (g sin β) and Perpendicular (g cos β)", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 5.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        # Incline line at beta = 20 deg
        incline_line = Line(axes.c2p(0, 0), axes.c2p(4.0, 1.45), color=self.accent_gold, stroke_width=3)
        lbl_incline = Text("Incline (β)", font=self.body_font, font_size=10, color=self.accent_gold).next_to(incline_line.get_center(), DR, buff=0.08)

        # Projectile arc landing on incline
        arc_incline = axes.plot(lambda x: 1.5 * x - 0.28 * (x**2), x_range=[0, 3.8], color=self.accent_blue, stroke_width=3)
        dot_hit = Dot(axes.c2p(3.8, 1.38), color=self.accent_green, radius=0.08)
        lbl_hit = Text("Range along incline", font=self.card_font, font_size=10, weight="BOLD", color=self.accent_green).next_to(dot_hit, UR, buff=0.08)

        left_group = VGroup(axes, incline_line, lbl_incline, arc_incline, dot_hit, lbl_hit)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("T = [2 v₀ sin(α - β)] / (g cos β)", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Effective Gravity: gx' = g sin β, gy' = g cos β", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• New Coordinate Axes: Set x' parallel and y' normal to incline", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Non-Zero Retardation along Incline: ax' = - g sin β", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Normal Restitution: ay' = - g cos β controls time of flight", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Max Range Up Incline: α = 45° + β/2", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: INCLINED PLANE FORMULATION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Comparison of Projecting UP the Incline vs DOWN the Incline", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("PROJECTING UP INCLINE", "Range R_up = [v₀² / (g cos² β)] · [sin(2α - β) - sin β]", "Gravity opposes motion along incline (ax' = -g sin β).", self.accent_blue),
            ("PROJECTING DOWN INCLINE", "Range R_down = [v₀² / (g cos² β)] · [sin(2α + β) + sin β]", "Gravity assists motion along incline (ax' = +g sin β).", self.accent_green),
            ("MAXIMUM RANGE UP INCLINE", "R_max = v₀² / [g (1 + sin β)]", "Optimal launch angle is bisector α = 45° + β/2.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Always rotate coordinates to incline axes: ax' = -g sin β, ay' = -g cos β!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: ASSUMING ZERO ACCELERATION ALONG INCLINE", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students treat motion along the incline as constant speed (ax = 0), completely forgetting g sin β!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("FLAT GROUND PROJECTILE", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("INCLINED PLANE PROJECTILE", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Horizontal acceleration ax = 0", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Acceleration along incline ax' = - g sin β (NON-ZERO!)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Range = vx · T", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Range = vx' · T - 1/2 (g sin β) · T²", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Acceleration along incline is NOT zero! Must include -1/2 (g sin β) T²!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 11. RadiusOfCurvatureScene (P11-C02-T04-V12)
# ---------------------------------------------------------------------------
class RadiusOfCurvatureScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Projectile Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Radius of Curvature at Apex", font=self.header_font, font_size=30, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("RADIUS OF CURVATURE AT PROJECTILE APEX", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.10 • Osculating Circle at Apex: ρ = v_apex² / a_normal = (v₀² cos² θ) / g", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        axes = Axes(x_range=[0, 6.0, 1], y_range=[0, 3.5, 1], x_length=4.6, y_length=3.0, tips=True, axis_config={"color": "#64748B", "stroke_width": 1.5}).move_to(card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3)
        traj = axes.plot(lambda x: 2.2 * x - 0.44 * (x**2), x_range=[0, 5.0], color=self.accent_blue, stroke_width=3)
        apex_pt = axes.c2p(2.5, 2.75)

        # Osculating circle fitting apex
        circle = Circle(radius=0.8, color=self.accent_gold, stroke_width=1.5).move_to(axes.c2p(2.5, 1.95))
        dot_c = Dot(axes.c2p(2.5, 1.95), color=self.accent_gold, radius=0.05)
        rad_line = Line(axes.c2p(2.5, 1.95), apex_pt, color=self.accent_gold, stroke_width=2)
        lbl_rho = Text("ρ = (v₀² cos² θ) / g", font=self.body_font, font_size=10, weight="BOLD", color=self.accent_gold).next_to(rad_line, LEFT, buff=0.08)

        left_group = VGroup(axes, traj, circle, dot_c, rad_line, lbl_rho)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("ρ = v² / a_n", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("At Apex: v = v₀ cos θ,   a_n = g", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Normal Acceleration: Component of g perpendicular to velocity", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• At Apex: Gravity g is PURELY NORMAL to horizontal velocity", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Minimum Radius: Apex is the sharpest curved point on trajectory", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• At Launch: ρ = v₀² / (g cos θ)  (Much larger radius)", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: CURVATURE DYNAMICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Radius of Curvature at Any General Point Along Trajectory", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("AT LAUNCH POINT (t = 0)", "ρ_launch = v₀² / (g cos θ)", "Speed is maximum v0; normal acceleration is g cos θ.", self.accent_blue),
            ("AT HIGHEST POINT (Apex)", "ρ_apex = (v₀ cos θ)² / g", "Speed is minimum vx = v0 cos θ; normal acceleration is entire g.", self.accent_green),
            ("GENERAL POINT (Angle φ)", "ρ = v³ / (g v₀ cos θ)", "Curvature is inversely proportional to normal force felt by particle.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("At apex, speed is strictly v0 cos θ, and acceleration g is 100% normal to velocity!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: USING TOTAL SPEED v₀ AT APEX", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students substitute launch speed v0 instead of horizontal apex speed (v0 cos θ)!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("CORRECT RADIUS AT APEX", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("COMMON NEET BLUNDER", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("ρ = (v₀ cos θ)² / g", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("ρ = v₀² / g  [FATAL ERROR!]", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Speed at apex is vx = v₀ cos θ", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Using v0 yields answer off by factor of cos² θ", font=self.body_font, font_size=11, color=self.accent_gold).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Always square the APEX horizontal speed: ρ = (v₀² cos² θ) / g!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)

# ---------------------------------------------------------------------------
# 12. CentripetalAccelerationScene (P11-C02-T04-V01)
# ---------------------------------------------------------------------------
class CentripetalAccelerationScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Uniform Circular Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Centripetal Acceleration", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CENTRIPETAL ACCELERATION DYNAMICS IN CIRCULAR PATHS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.11 • Radial Inward Acceleration: a_c = v² / r = ω² · r", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        center_pt = card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3
        circle = Circle(radius=1.3, color="#334155", stroke_width=2).move_to(center_pt)
        dot_o = Dot(center_pt, color="#64748B", radius=0.06)
        lbl_o = Text("O", font=self.body_font, font_size=10, color="#64748B").next_to(dot_o, DL, buff=0.05)

        particle_pt = center_pt + RIGHT * 1.3
        dot_p = Dot(particle_pt, color=self.accent_blue, radius=0.08)

        # Tangential velocity vector
        arrow_v = Arrow(particle_pt, particle_pt + UP * 1.2, buff=0, color=self.accent_green, stroke_width=3)
        lbl_v = Text("v (Tangential)", font=self.body_font, font_size=10, weight="BOLD", color=self.accent_green).next_to(arrow_v, RIGHT, buff=0.08)

        # Centripetal acceleration vector (inward)
        arrow_ac = Arrow(particle_pt, particle_pt + LEFT * 1.0, buff=0, color=self.accent_red, stroke_width=3)
        lbl_ac = Text("a_c (Radial Inward)", font=self.body_font, font_size=10, weight="BOLD", color=self.accent_red).next_to(arrow_ac.get_center(), DOWN, buff=0.10)

        left_group = VGroup(circle, dot_o, lbl_o, dot_p, arrow_v, lbl_v, arrow_ac, lbl_ac)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("a_c = v² / r = ω² · r", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Direction: Purely Radially Inward (Towards O)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Constant Speed, Changing Velocity: Direction changes continuously", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Perpendicular Force: a_c is strictly perpendicular to v (v · a_c = 0)", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Zero Work Done: Power P = F · v = 0 in uniform circular motion", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Frequency Relation: a_c = 4π² f² r = (4π² / T²) r", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: UNIFORM CIRCULAR MOTION LAWS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Velocity Vector Direction vs Speed Invariance", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("CONSTANT SPEED (|v| = const)", "Kinetic Energy K = 1/2 m v² = const", "Particle neither speeds up nor slows down; energy is constant.", self.accent_blue),
            ("ACCELERATED MOTION (a ≠ 0)", "Velocity vector rotates at angular rate ω", "Because direction alters every instant, acceleration is non-zero!", self.accent_green),
            ("PERIODIC EQUIVALENCE", "T = 2πr / v = 2π / ω", "Complete rotation time links linear speed directly to circumference.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Even when speed is perfectly uniform, circular motion is 100% accelerated motion!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: ASSUMING ZERO ACCELERATION IN UNIFORM CIRCULAR MOTION", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students assume that because speed is constant, acceleration must equal zero!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("SCALAR QUANTITY: SPEED (v)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("VECTOR QUANTITY: VELOCITY (v_vec)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("Speed is CONSTANT: dv/dt = 0", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("Velocity vector CHANGES DIRECTION continuously", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Tangential acceleration a_t = 0", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Centripetal acceleration a_c = v² / r  (NON-ZERO!)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: Constant speed ≠ Zero acceleration! Centripetal acceleration a_c is strictly NON-ZERO!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 13. AngularVelocityScene (P11-C02-T05-V13)
# ---------------------------------------------------------------------------
class AngularVelocityScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Uniform Circular Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Angular Velocity & Linear Speed Relation", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("LINEAR SPEED VS ANGULAR VELOCITY RELATION (v = ω · r)", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.11 • On a Rotating Body: Angular Velocity ω is Shared; Linear Speed v Scales with Radius r", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        center_pt = card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3
        c1 = Circle(radius=0.7, color="#334155", stroke_width=1.5).move_to(center_pt)
        c2 = Circle(radius=1.4, color="#475569", stroke_width=2).move_to(center_pt)
        dot_o = Dot(center_pt, color="#64748B", radius=0.06)

        p1 = center_pt + RIGHT * 0.7
        p2 = center_pt + RIGHT * 1.4
        dot1 = Dot(p1, color=self.accent_gold, radius=0.07)
        dot2 = Dot(p2, color=self.accent_green, radius=0.08)

        v1_arrow = Arrow(p1, p1 + UP * 0.6, buff=0, color=self.accent_gold, stroke_width=2.5)
        v2_arrow = Arrow(p2, p2 + UP * 1.2, buff=0, color=self.accent_green, stroke_width=3.5)

        lbl1 = Text("v₁ = ω r₁", font=self.body_font, font_size=9, color=self.accent_gold).next_to(v1_arrow, RIGHT, buff=0.05)
        lbl2 = Text("v₂ = ω r₂  (FASTER!)", font=self.body_font, font_size=9, weight="BOLD", color=self.accent_green).next_to(v2_arrow, RIGHT, buff=0.05)

        left_group = VGroup(c1, c2, dot_o, dot1, dot2, v1_arrow, v2_arrow, lbl1, lbl2)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("v = ω · r", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Vector Cross Product: v_vec = ω_vec × r_vec", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Universal ω: All points on rigid rotating body turn at same rate", font=self.body_font, font_size=11, color=self.accent_green)
        rule2 = Text("• Linear Speed Scaling: Points further from axis move faster", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Acceleration Ratio: a_c = ω² r  (Scales linearly with radius)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule4 = Text("• Angular Displacement: θ = s / r [radians]", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: RIGID BODY ROTATIONAL KINEMATICS", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Contrasting Constant Angular Frequency with Radial Velocity Gradients", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("SAME ANGULAR SPEED (ω)", "ω₁ = ω₂ = 2π / T", "Every particle on rotating disc sweeps identical angular displacement Δθ.", self.accent_blue),
            ("DIFFERENT LINEAR SPEEDS (v)", "v₂ / v₁ = r₂ / r₁", "Particles on outer perimeter travel longer arc length per second.", self.accent_green),
            ("CENTRIPETAL FORCE GRADIENT", "F_c = m ω² r", "Outward particles require greater inward tension/force to maintain circular path.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("All points on a spinning wheel have identical ω, but points near rim move much faster!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: INNER POINTS FASTER BLUNDER", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("Students confuse v = ω r (rigid body) with Kepler's orbital speed v ∝ 1/√r!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("RIGID BODY ROTATION (Wheel / Disc)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("PLANETARY ORBIT (Kepler Motion)", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("v = ω · r  (Linear speed ∝ r)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("v = √(GM / r)  (Speed ∝ 1/√r)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Outer rim moves FASTEST!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Inner planet moves FASTEST!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_blue).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: On any rotating rigid body, linear speed is DIRECTLY PROPORTIONAL to radius r!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)


# ---------------------------------------------------------------------------
# 14. NonUniformCircularScene (P11-C02-T05-V14)
# ---------------------------------------------------------------------------
class NonUniformCircularScene(ModularUnit2Scene):
    def build_beat_1(self):
        settle_tag = Text("Kinematics • Circular Motion", font=self.card_font, font_size=18, color=self.muted_text)
        settle_title = Text("Non-Uniform Circular Motion Acceleration", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Physics Part 1 • Unit 2: Kinematics • Chapter 4", font=self.card_font, font_size=14, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("NON-UNIFORM CIRCULAR MOTION: NET ACCELERATION", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("NCERT Section 4.11 • Two Orthogonal Accelerations: Radial Inward a_c and Tangential a_t = dv/dt", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)
        v_div = Line(start=h_div.get_center() + DOWN * 0.05, end=card_box.get_bottom() + UP * 0.2, color="#334155", stroke_width=1.0).shift(LEFT * 0.2)

        center_pt = card_box.get_left() + RIGHT * 2.7 + DOWN * 0.3
        circle = Circle(radius=1.3, color="#334155", stroke_width=2).move_to(center_pt)
        dot_o = Dot(center_pt, color="#64748B", radius=0.06)

        particle_pt = center_pt + RIGHT * 1.3
        dot_p = Dot(particle_pt, color=self.accent_blue, radius=0.08)

        # Inward radial arrow
        arrow_ac = Arrow(particle_pt, particle_pt + LEFT * 1.0, buff=0, color=self.accent_blue, stroke_width=3)
        lbl_ac = Text("a_c = v²/r", font=self.body_font, font_size=10, color=self.accent_blue).next_to(arrow_ac.get_center(), DOWN, buff=0.08)

        # Tangential arrow
        arrow_at = Arrow(particle_pt, particle_pt + UP * 0.8, buff=0, color=self.accent_gold, stroke_width=3)
        lbl_at = Text("a_t = dv/dt", font=self.body_font, font_size=10, color=self.accent_gold).next_to(arrow_at.get_center(), RIGHT, buff=0.08)

        # Net acceleration arrow (resultant)
        arrow_anet = Arrow(particle_pt, particle_pt + LEFT * 1.0 + UP * 0.8, buff=0, color=self.accent_green, stroke_width=3.5)
        lbl_anet = Text("a_net", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_green).next_to(arrow_anet.get_end(), UL, buff=0.05)

        left_group = VGroup(circle, dot_o, dot_p, arrow_ac, lbl_ac, arrow_at, lbl_at, arrow_anet, lbl_anet)

        right_center_x = card_box.get_right()[0] - 2.8
        eq1_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).move_to(np.array([right_center_x, card_box.get_center()[1] + 1.25, 0]))
        eq1_text = Text("a_net = √(a_c² + a_t²)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).move_to(eq1_box.get_center())

        eq2_box = RoundedRectangle(corner_radius=0.08, width=5.2, height=0.75, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#1E293B", fill_opacity=0.5).next_to(eq1_box, DOWN, buff=0.15)
        eq2_text = Text("Angle with Radius: tan θ = a_t / a_c", font=self.card_font, font_size=13, weight="BOLD", color=self.accent_blue).move_to(eq2_box.get_center())

        rule1 = Text("• Radial Component a_c: Changes velocity DIRECTION (points inward)", font=self.body_font, font_size=11, color=self.accent_blue)
        rule2 = Text("• Tangential Component a_t: Changes velocity MAGNITUDE (speed)", font=self.body_font, font_size=11, color=self.accent_gold)
        rule3 = Text("• Speed Increasing: a_t parallel to v (Angle < 90° with v)", font=self.body_font, font_size=11, color=self.accent_green)
        rule4 = Text("• Speed Decreasing: a_t anti-parallel to v (Retardation)", font=self.body_font, font_size=11, color=self.muted_text)
        rules_v = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(eq2_box, DOWN, buff=0.20).align_to(eq2_box, LEFT).shift(RIGHT * 0.15)
        right_group = VGroup(eq1_box, eq1_text, eq2_box, eq2_text, rules_v)

        return VGroup(card_box, card_title, card_sub, h_div, v_div, left_group, right_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=5.0, width=11.6, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(DOWN * 0.1)
        card_title = Text("CORE PRINCIPLES: THREE CIRCULAR ACCELERATION MODES", font=self.card_font, font_size=15, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.15)
        card_sub = Text("Behavior of Net Acceleration Under Varying Tangential Acceleration", font=self.body_font, font_size=10, color=self.muted_text).next_to(card_title, DOWN, buff=0.08)
        h_div = Line(start=card_box.get_left() + RIGHT * 0.3, end=card_box.get_right() + LEFT * 0.3, color="#334155", stroke_width=1.0).next_to(card_sub, DOWN, buff=0.10)

        rows = []
        scenarios = [
            ("UNIFORM CIRCULAR (a_t = 0)", "a_net = a_c = v² / r", "Net acceleration points 100% radially inward to center.", self.accent_blue),
            ("ACCELERATED CIRCULAR (a_t > 0)", "a_net = √(a_c² + a_t²),  angle < 90° with v", "Particle speeds up; net acceleration points inward and forward.", self.accent_green),
            ("DECELERATED CIRCULAR (a_t < 0)", "a_net = √(a_c² + a_t²),  angle > 90° with v", "Particle slows down; net acceleration points inward and backward.", self.accent_gold)
        ]
        for title, formula_txt, phys_meaning, color in scenarios:
            row_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.92, stroke_color=color, stroke_width=1.0, fill_color="#1E293B", fill_opacity=0.35)
            t_txt = Text(title, font=self.card_font, font_size=12, weight="BOLD", color=color).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(UP * 0.18)
            c_txt = Text(formula_txt, font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(t_txt, RIGHT, buff=0.30)
            p_txt = Text(phys_meaning, font=self.body_font, font_size=10, color=self.muted_text).next_to(row_box.get_left(), RIGHT, buff=0.25).shift(DOWN * 0.18)
            rows.append(VGroup(row_box, t_txt, c_txt, p_txt))

        rows_group = VGroup(*rows).arrange(DOWN, buff=0.15).next_to(h_div, DOWN, buff=0.18)
        nuance_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color="#A855F7", stroke_width=1.0, fill_color="#3B0764", fill_opacity=0.30).next_to(rows_group, DOWN, buff=0.15)
        nuance_tag = Text("H.C. VERMA NUANCE:", font=self.card_font, font_size=10, weight="BOLD", color="#C084FC").next_to(nuance_box.get_left(), RIGHT, buff=0.20)
        nuance_txt = Text("Tangential acceleration changes speed; radial acceleration changes direction!", font=self.body_font, font_size=10, color="#E9D5FF").next_to(nuance_tag, RIGHT, buff=0.15)
        nuance_group = VGroup(nuance_box, nuance_tag, nuance_txt)
        return VGroup(card_box, card_title, card_sub, h_div, rows_group, nuance_group)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.14, height=5.0, width=11.6, stroke_color=self.accent_red, stroke_width=1.8, fill_color="#18080C", fill_opacity=0.45).move_to(DOWN * 0.1)
        trap_banner = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.55, stroke_color=self.accent_red, stroke_width=1.0, fill_color=self.accent_red, fill_opacity=0.20).next_to(trap_box.get_top(), DOWN, buff=0.15)
        trap_title = Text("CRITICAL NEET TRAP: FORGETTING TANGENTIAL ACCELERATION", font=self.card_font, font_size=14, weight="BOLD", color=self.accent_red).move_to(trap_banner.get_center())
        trap_sub = Text("When a question says speed increases at 2 m/s², students calculate total acceleration as just v²/r!", font=self.body_font, font_size=11, color=self.muted_text).next_to(trap_banner, DOWN, buff=0.15)

        comp_box = RoundedRectangle(corner_radius=0.10, width=11.0, height=2.2, stroke_color="#334155", stroke_width=1.0, fill_color="#0F172A", fill_opacity=0.6).next_to(trap_sub, DOWN, buff=0.15)
        h_mid = Line(start=comp_box.get_left(), end=comp_box.get_right(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())
        v_mid = Line(start=comp_box.get_top(), end=comp_box.get_bottom(), color="#334155", stroke_width=1.0).move_to(comp_box.get_center())

        col1_hdr = Text("SPEED IS INCREASING / DECREASING", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.25)
        col2_hdr = Text("COMMON NEET TRAP ERROR", font=self.card_font, font_size=12, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.25)

        row1_left = Text("a_net = √[ (v²/r)² + (dv/dt)² ]", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green).move_to(comp_box.get_corner(UL) + RIGHT * 2.75 + DOWN * 0.70)
        row1_right = Text("a_net = v² / r  [FORGETS TANGENTIAL!]", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red).move_to(comp_box.get_corner(UR) + LEFT * 2.75 + DOWN * 0.70)

        row2_left = Text("Two perpendicular components present", font=self.body_font, font_size=11, color=TEXT_WHITE).move_to(comp_box.get_corner(DL) + RIGHT * 2.75 + UP * 0.45)
        row2_right = Text("Fails whenever tangential force/rate is given", font=self.body_font, font_size=11, color=self.accent_gold).move_to(comp_box.get_corner(DR) + LEFT * 2.75 + UP * 0.45)

        table_group = VGroup(comp_box, h_mid, v_mid, col1_hdr, col2_hdr, row1_left, row1_right, row2_left, row2_right)
        takeaway_box = RoundedRectangle(corner_radius=0.08, width=11.0, height=0.65, stroke_color=self.accent_gold, stroke_width=1.0, fill_color="#2D1C03", fill_opacity=0.4).next_to(comp_box, DOWN, buff=0.18)
        takeaway_txt = Text("NEET RULE: When speed is changing in circular motion, total acceleration a_net = √(a_c² + a_t²)!", font=self.card_font, font_size=11, weight="BOLD", color=self.accent_gold).move_to(takeaway_box.get_center())
        return VGroup(trap_box, trap_banner, trap_title, trap_sub, table_group, takeaway_box, takeaway_txt)
