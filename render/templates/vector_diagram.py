"""
VectorDiagram Template Implementation
Visualizes vector resolution, orthogonal projections, magnitude-direction trigonometry,
and circular motion centripetal acceleration vectors with NEET traps.
Derived from MASTER_BLUEPRINT.md v1.1 Section 10
"""
import textwrap
import numpy as np
from manim import (
    Axes, DashedLine, Dot, Arrow, Arc, MathTex, Text, VGroup, RoundedRectangle, Circle,
    FadeIn, FadeOut, Create, Write, Transform, Indicate, ValueTracker, DecimalNumber,
    Line, RightAngle,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR,
    DEGREES, linear
)
from render.templates.base import (
    BaseNeetScene,
    BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN, TEXT_WHITE, MUTED_TEXT,
    FONT_PRIMARY, FONT_MONO
)

class VectorDiagramScene(BaseNeetScene):
    def render_concept_beats(self):
        canonical_id = self.node_data.get("videoId", "").split("_")[0]
        concept_title = self.parameters.get("conceptTitle") or self.node_data.get("serialTitle", "Resolution of Vectors")
        topic_name = self.parameters.get("topicName") or self.node_data.get("subject", "Vectors")
        chapter_name = self.parameters.get("chapterName", "Kinematics")
        plain_formula = self.parameters.get("plainFormula", "A = Ax·i + Ay·j")
        trap_text = self.parameters.get("trapWarning", "Adjacent side with angle θ is cosine; opposite side is sine.")
        author_nuance = self.parameters.get("authorNuance", "")

        is_centripetal = (canonical_id == "P11-C02-T04-V01" or "centripetal" in concept_title.lower())

        # Dynamic beat pacing aligned with audio narration duration
        target_dur = float(self.node_data.get("target_duration", 32.0))
        extra_time = max(0.0, target_dur - 31.8)
        hold_formula = 1.5 + (extra_time * 0.30)
        hold_trap = 2.0 + (extra_time * 0.30)
        capsule_dur = 6.0 + (extra_time * 0.40)

        # =========================================================================
        # --- BEAT 1: SETTLE ---
        # =========================================================================
        settle_tag = Text(f"{chapter_name} • {topic_name}", font=self.body_font, font_size=18, color=self.muted_text)
        settle_title = Text(concept_title, font=self.topic_font, font_size=30, weight="BOLD", color=self.accent_blue)
        if settle_title.width > 12.0:
            settle_title.scale_to_fit_width(12.0)
        settle_group = VGroup(settle_tag, settle_title).arrange(DOWN, buff=0.25).move_to(ORIGIN + UP * 0.5)

        self.play(FadeIn(settle_group), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(settle_group), run_time=0.8)

        # =========================================================================
        # --- BEAT 2: CONTEXT / VECTOR COORDINATE SYSTEM SETUP ---
        # =========================================================================
        axes = Axes(
            x_range=[0, 6.0, 1],
            y_range=[0, 5.0, 1],
            x_length=5.2,
            y_length=4.0,
            tips=True,
            axis_config={"color": MUTED_TEXT, "stroke_width": 2}
        ).to_corner(DL, buff=1.2).shift(RIGHT * 0.8 + UP * 0.1)

        x_label = Text("x (î)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = Text("y (ĵ)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.15)
        graph_group = VGroup(axes, x_label, y_label)

        # Simulation Telemetry HUD Card
        hud_box = RoundedRectangle(
            corner_radius=0.1,
            height=0.88,
            width=3.6,
            stroke_color=ACCENT_BLUE,
            stroke_width=1.5,
            fill_color="#0F172A",
            fill_opacity=0.0
        ).to_corner(UL, buff=1.1).shift(RIGHT * 0.1 + UP * 0.2)

        hud_title = Text("VECTOR TELEMETRY", font_size=11, weight="BOLD", color=MUTED_TEXT).next_to(hud_box.get_top(), DOWN, buff=0.10)

        if is_centripetal:
            stat1_txt = Text("Speed |v|: Constant", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("ac = v²/r (Inward)", font_size=12, weight="BOLD", color=ACCENT_RED)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.25).next_to(hud_title, DOWN, buff=0.10)
        else:
            theta_deg = 36.87  # Standard 3-4-5 right triangle
            ax_val = 4.0
            ay_val = 3.0
            a_mag = 5.0
            stat1_txt = Text(f"|A| = {a_mag:.1f}", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            stat2_txt = Text(f"θ = {theta_deg:.1f}°", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.35).next_to(hud_title, DOWN, buff=0.10)

        hud_group = VGroup(hud_box, hud_title, hud_stats)

        if is_centripetal:
            circle_center = axes.c2p(2.8, 2.3)
            circ_r = 1.6
            orbit_circle = Circle(radius=circ_r, color=MUTED_TEXT, stroke_width=2.5).move_to(circle_center)
            center_dot = Dot(point=circle_center, color=MUTED_TEXT, radius=0.07)
            # 45 deg particle position
            p_pos = circle_center + np.array([circ_r * 0.7071, circ_r * 0.7071, 0])
            particle_dot = Dot(point=p_pos, color=ACCENT_GOLD, radius=0.12)
            r_line = DashedLine(start=circle_center, end=p_pos, color=MUTED_TEXT, stroke_width=1.5)
            r_lbl = Text("Radius r", font_size=11, color=MUTED_TEXT).next_to(circle_center, DOWN, buff=0.08)

            vector_intro = VGroup(orbit_circle, center_dot, particle_dot, r_line, r_lbl)
        else:
            origin_pt = axes.c2p(0, 0)
            tip_pt = axes.c2p(ax_val, ay_val)
            vector_a = Arrow(start=origin_pt, end=tip_pt, buff=0, color=ACCENT_GOLD, stroke_width=5, max_tip_length_to_length_ratio=0.15)
            vector_label = Text("A", font_size=20, weight="BOLD", color=ACCENT_GOLD).next_to(vector_a.get_center(), UL, buff=0.15)
            angle_arc = Arc(radius=0.85, start_angle=0, angle=np.radians(theta_deg), arc_center=origin_pt, color=ACCENT_BLUE, stroke_width=2.5)
            arc_label = Text("θ", font_size=15, weight="BOLD", color=ACCENT_BLUE).next_to(angle_arc, RIGHT, buff=0.10).shift(UP * 0.08)
            vector_intro = VGroup(vector_a, vector_label, angle_arc, arc_label)

        self.play(Create(graph_group), run_time=1.5)
        self.play(FadeIn(hud_group), run_time=0.8)
        self.play(Create(vector_intro), run_time=2.0)

        # =========================================================================
        # --- BEAT 3: CRITICAL (ORTHOGONAL DECOMPOSITION / VECTORS) ---
        # =========================================================================
        if is_centripetal:
            v_arrow = Arrow(start=p_pos, end=p_pos + np.array([-0.95, 0.95, 0]), buff=0, color=ACCENT_BLUE, stroke_width=4.0)
            v_lbl = Text("v (Tangential)", font_size=12, weight="BOLD", color=ACCENT_BLUE).next_to(v_arrow, UL, buff=0.08)
            ac_arrow = Arrow(start=p_pos, end=p_pos + np.array([-1.05, -1.05, 0]), buff=0, color=ACCENT_RED, stroke_width=4.0)
            ac_lbl = Text("ac = v²/r", font_size=12, weight="BOLD", color=ACCENT_RED).next_to(ac_arrow, DR, buff=0.08)
            perp_lbl = Text("v perp to ac", font_size=11, weight="BOLD", color=ACCENT_GOLD).next_to(p_pos, UR, buff=0.18)
            components_group = VGroup(v_arrow, v_lbl, ac_arrow, ac_lbl, perp_lbl)
            self.play(Create(v_arrow), Write(v_lbl), Create(ac_arrow), Write(ac_lbl), Write(perp_lbl), run_time=2.0)
        else:
            x_proj_pt = axes.c2p(ax_val, 0)
            y_proj_pt = axes.c2p(0, ay_val)
            dash_v = DashedLine(start=tip_pt, end=x_proj_pt, color=MUTED_TEXT, stroke_width=2.0)
            dash_h = DashedLine(start=tip_pt, end=y_proj_pt, color=MUTED_TEXT, stroke_width=2.0)
            arrow_x = Arrow(start=origin_pt, end=x_proj_pt, buff=0, color=ACCENT_BLUE, stroke_width=4.5, max_tip_length_to_length_ratio=0.16)
            label_x = Text("Ax = A·cos θ", font_size=14, weight="BOLD", color=ACCENT_BLUE).next_to(arrow_x, DOWN, buff=0.12)
            arrow_y = Arrow(start=origin_pt, end=y_proj_pt, buff=0, color=ACCENT_GREEN, stroke_width=4.5, max_tip_length_to_length_ratio=0.18)
            label_y = Text("Ay = A·sin θ", font_size=14, weight="BOLD", color=ACCENT_GREEN).next_to(arrow_y, LEFT, buff=0.12)
            components_group = VGroup(dash_v, dash_h, arrow_x, label_x, arrow_y, label_y)
            self.play(Create(dash_v), Create(dash_h), run_time=1.2)
            self.play(Create(arrow_x), Write(label_x), Create(arrow_y), Write(label_y), run_time=2.0)

        # Dynamic formula panel on right side
        formula_mobj = self.create_smart_formula(
            formula_str=plain_formula,
            font_size=28,
            color_val=self.theme.formula_color
        ).to_corner(UR, buff=1.3).shift(DOWN * 0.7)

        header_text = f"{concept_title.upper()} FORMULA"
        formula_title = Text(header_text, font=self.topic_font, font_size=18, weight="BOLD", color=self.theme.topic_color)
        if formula_title.width > 5.2:
            formula_title.scale_to_fit_width(5.2)
        formula_title.next_to(formula_mobj, UP, buff=0.35)
        if formula_title.get_right()[0] > 6.0:
            formula_title.shift(LEFT * (formula_title.get_right()[0] - 6.0))

        formula_panel = VGroup(formula_title, formula_mobj)
        self.play(Write(formula_panel), run_time=2.0)

        # Critical Beat Repetition: Radiant highlight pulse
        self.wait(1.0)
        self.play(Indicate(formula_mobj, color=self.theme.formula_color, scale_factor=1.06), run_time=1.4)
        for sm in formula_mobj.get_family():
            sm.set_opacity(1.0)

        # Dynamic Variable Explanations
        if is_centripetal:
            ac_text = Text("a_c = v² / r = ω² · r  [Centripetal acceleration]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
            v_text = Text("v = Tangential speed (constant in uniform circular)", font=self.body_font, font_size=13, color=self.accent_blue)
            w_text = Text("ω = Angular velocity (ω = v / r,  rad/s)", font=self.body_font, font_size=13, color=self.muted_text)
            vars_group = VGroup(ac_text, v_text, w_text).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        else:
            eq_x = Text("Ax = |A| · cos θ   (Horizontal component)", font=self.body_font, font_size=14, color=ACCENT_BLUE)
            eq_y = Text("Ay = |A| · sin θ   (Vertical component)", font=self.body_font, font_size=14, color=ACCENT_GREEN)
            eq_mag = Text("|A| = √(Ax² + Ay²)   tan θ = Ay / Ax", font=self.body_font, font_size=14, color=ACCENT_GOLD)
            vars_group = VGroup(eq_x, eq_y, eq_mag).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        vars_group.next_to(formula_mobj, DOWN, buff=0.42)
        if vars_group.width > 5.5:
            vars_group.scale_to_fit_width(5.5)
        if vars_group.get_right()[0] > 6.1:
            vars_group.shift(LEFT * (vars_group.get_right()[0] - 6.1))

        self.play(FadeIn(vars_group), run_time=1.5)
        self.wait(hold_formula)

        # =========================================================================
        # --- BEAT 4: CRITICAL (NEET TRAP ANALYSIS) ---
        # =========================================================================
        self.play(FadeOut(vars_group), run_time=0.8)

        trap_title = Text("NEET TRAP ALERT", font=self.topic_font, font_size=17, weight="BOLD", color=self.theme.trap_color)
        wrapped_trap = textwrap.fill(trap_text, width=46)
        trap_body = Text(wrapped_trap, font=self.body_font, font_size=14, weight=self.theme.body_weight, color=self.theme.trap_body_color)
        if trap_body.width > 5.8:
            trap_body.scale_to_fit_width(5.8)

        if is_centripetal:
            trans_lbl = Text("Crucial NEET Circular Distinction:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Constant SPEED does NOT mean zero acceleration!", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            rule2 = Text("• Velocity changes direction continuously → a_c = v²/r!", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            rule3 = Text("• a_c is perpendicular to v → Centripetal force does ZERO work!", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_gold)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2, rule3).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        else:
            trans_lbl = Text("Golden Rule of Vector Components:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Angle touches axis → uses COSINE: Ax = A·cos θ", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_blue)
            rule2 = Text("• Opposite perpendicular axis → uses SINE: Ay = A·sin θ", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)
            rule3 = Text("• IF angle is with Vertical: Ay = A·cos α, Ax = A·sin α!", font=self.body_font, font_size=13, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2, rule3).arrange(DOWN, aligned_edge=LEFT, buff=0.10)

        trap_panel.next_to(formula_mobj, DOWN, buff=0.32)
        if trap_panel.get_right()[0] > 6.1:
            trap_panel.shift(LEFT * (trap_panel.get_right()[0] - 6.1))
        if trap_panel.get_bottom()[1] < -3.3:
            trap_panel.shift(UP * (-3.3 - trap_panel.get_bottom()[1]))

        self.play(FadeIn(trap_panel), run_time=1.5)
        self.wait(hold_trap)

        # Clear active scene elements before end capsule
        self.play(
            FadeOut(trap_panel),
            FadeOut(formula_panel),
            FadeOut(graph_group),
            FadeOut(vector_intro),
            FadeOut(components_group),
            FadeOut(hud_group),
            run_time=0.6
        )

        # =========================================================================
        # --- BEAT 5: END CAPSULE REVISION ---
        # =========================================================================
        self.render_end_capsule(formula_mobj, trap_text, duration=capsule_dur)

        # =========================================================================
        # --- BEAT 6: RELEASE (WITH NEXT CONCEPT TEASER) ---
        # =========================================================================
        self.render_release_teaser(duration=3.5)
