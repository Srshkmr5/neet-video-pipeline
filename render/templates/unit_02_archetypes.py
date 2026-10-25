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
