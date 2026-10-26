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
