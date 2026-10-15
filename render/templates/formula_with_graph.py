"""
FormulaWithGraph Template Implementation (Generalized Dynamic Engine)
Supports Projectile Motion Family & Coordinate Physics Visualizations
Derived from MASTER_BLUEPRINT.md v1.1
"""
import textwrap
import numpy as np
from manim import (
    Axes, DashedLine, Dot, Arrow, Arc, MathTex, Text, VGroup, RoundedRectangle,
    FadeIn, FadeOut, Create, Write, Transform, Indicate, ValueTracker, DecimalNumber,
    Line,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR,
    DEGREES, linear
)
from render.templates.base import (
    BaseNeetScene,
    BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN, TEXT_WHITE, MUTED_TEXT,
    FONT_PRIMARY, FONT_MONO
)

class FormulaWithGraphScene(BaseNeetScene):
    def render_concept_beats(self):
        canonical_id = self.node_data.get("videoId", "").split("_")[0]
        concept_title = self.parameters.get("conceptTitle") or self.node_data.get("serialTitle", "Key Concept")
        topic_name = self.parameters.get("topicName") or self.node_data.get("subject", "Kinematics")
        chapter_name = self.parameters.get("chapterName", "Kinematics")
        plain_formula = self.parameters.get("plainFormula", "H_max = (v_0^2 * sin^2(θ)) / (2g)")
        trap_text = self.parameters.get("trapWarning", "Angle θ MUST be measured relative to horizontal.")
        author_nuance = self.parameters.get("authorNuance", "")

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
        # --- BEAT 2: CONTEXT / GRAPH SETUP ---
        # =========================================================================
        axes = Axes(
            x_range=[0, 6.5, 1],
            y_range=[0, 5.0, 1],
            x_length=5.6,
            y_length=3.8,
            tips=True,
            axis_config={"color": MUTED_TEXT, "stroke_width": 2}
        ).to_corner(DL, buff=1.2).shift(RIGHT * 0.8 + UP * 0.2)

        x_label = Text("Range (x)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("Height (y)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.18).shift(RIGHT * 0.4)
        graph_group = VGroup(axes, x_label, y_label)

        # Simulation Telemetry HUD Card
        hud_box = RoundedRectangle(
            corner_radius=0.1,
            height=0.92,
            width=3.7,
            stroke_color=ACCENT_BLUE,
            stroke_width=1.5,
            fill_color="#0F172A",
            fill_opacity=0.0
        ).to_corner(UL, buff=1.1).shift(DOWN * 0.3 + RIGHT * 0.4)

        hud_title = Text("SIMULATION TELEMETRY", font_size=11, weight="BOLD", color=MUTED_TEXT).next_to(hud_box.get_top(), DOWN, buff=0.10)

        # Concept-specific simulation parameters
        time_tracker = ValueTracker(0.0)

        if canonical_id == "P11-C02-T03-V01":  # Time of Flight
            stat1_num = DecimalNumber(0.0, num_decimal_places=2, font_size=14, color=ACCENT_BLUE, mob_class=Text)
            stat1_row = VGroup(Text("t:", font_size=12, weight="BOLD", color=ACCENT_BLUE), stat1_num, Text("s", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            stat2_num = DecimalNumber(2.04, num_decimal_places=2, font_size=14, color=ACCENT_GOLD, mob_class=Text)
            stat2_row = VGroup(Text("T_total:", font_size=12, weight="BOLD", color=ACCENT_GOLD), stat2_num, Text("s", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            stat1_num.add_updater(lambda m: m.set_value(2.04 * time_tracker.get_value()))
            hud_stats = VGroup(stat1_row, stat2_row).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif canonical_id == "P11-C02-T03-V03":  # Horizontal Range & Complementary
            stat1_num = DecimalNumber(0.0, num_decimal_places=1, font_size=14, color=ACCENT_BLUE, mob_class=Text)
            stat1_row = VGroup(Text("x:", font_size=12, weight="BOLD", color=ACCENT_BLUE), stat1_num, Text("m", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            stat2_txt = Text("θ: 30° / 60°", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            stat1_num.add_updater(lambda m: m.set_value(60.0 * time_tracker.get_value()))
            hud_stats = VGroup(stat1_row, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif canonical_id == "P11-C02-T03-V04":  # Equation of Trajectory
            stat1_txt = Text("Path: y(x)", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("Shape: Parabola", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        else:  # Max Height Arc & General Fallback
            vy_num = DecimalNumber(20.0, num_decimal_places=1, font_size=14, color=ACCENT_BLUE, mob_class=Text)
            vy_row = VGroup(Text("vy:", font_size=12, weight="BOLD", color=ACCENT_BLUE), vy_num, Text("m/s", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            y_num = DecimalNumber(0.0, num_decimal_places=1, font_size=14, color=ACCENT_GOLD, mob_class=Text)
            y_row = VGroup(Text("Height:", font_size=12, weight="BOLD", color=ACCENT_GOLD), y_num, Text("m", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            vy_num.add_updater(lambda m: m.set_value(max(0.0, 20.0 * (1.0 - time_tracker.get_value()))))
            y_num.add_updater(lambda m: m.set_value(20.4 * (1.0 - (1.0 - time_tracker.get_value()) ** 2)))
            hud_stats = VGroup(vy_row, y_row).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        hud_group = VGroup(hud_box, hud_title, hud_stats)

        # Trajectory rendering
        if canonical_id == "P11-C02-T03-V03":  # Two complementary arcs
            traj1 = axes.plot(lambda x: 3.0 * x - 0.5 * (x ** 2), x_range=[0, 6.0], color=ACCENT_BLUE, stroke_width=3.5)
            traj2 = axes.plot(lambda x: 1.0 * x - (1.0 / 6.0) * (x ** 2), x_range=[0, 6.0], color=ACCENT_GREEN, stroke_width=3.5)
            trajectory = VGroup(traj1, traj2)
        else:
            trajectory = axes.plot(lambda x: 3.0 * x - 0.5 * (x ** 2), x_range=[0, 6.0], color=ACCENT_BLUE, stroke_width=4)

        flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0))
        flight_ball.add_updater(lambda m: m.move_to(
            axes.c2p(
                3.0 * time_tracker.get_value(),
                3.0 * (3.0 * time_tracker.get_value()) - 0.5 * ((3.0 * time_tracker.get_value()) ** 2)
            )
        ))

        self.play(Create(graph_group), run_time=1.5)
        self.play(FadeIn(hud_group), run_time=0.8)
        self.add(flight_ball)
        self.play(
            Create(trajectory),
            time_tracker.animate.set_value(1.0),
            run_time=2.5,
            rate_func=linear
        )
        flight_ball.clear_updaters()

        # =========================================================================
        # --- BEAT 3: CRITICAL (FORMULA & DERIVATION) ---
        # =========================================================================
        if canonical_id == "P11-C02-T03-V01":  # Time of Flight landing highlight
            land_point = axes.c2p(6.0, 0.0)
            target_dot = Dot(point=land_point, color=ACCENT_GOLD, radius=0.1)
            target_label = Text("T_flight: y = 0", font_size=15, weight="BOLD", color=ACCENT_GOLD).next_to(target_dot, UP, buff=0.15)
            feature_group = VGroup(target_dot, target_label)
        elif canonical_id == "P11-C02-T03-V03":  # Complementary equal range highlight
            land_point = axes.c2p(6.0, 0.0)
            target_dot = Dot(point=land_point, color=ACCENT_GOLD, radius=0.1)
            target_label = Text("Identical Range R", font_size=15, weight="BOLD", color=ACCENT_GOLD).next_to(target_dot, UP, buff=0.15)
            feature_group = VGroup(target_dot, target_label)
        else:  # Apex highlight (Max Height & General)
            apex_point = axes.c2p(3.0, 4.5)
            ground_point = axes.c2p(3.0, 0.0)
            peak_dot = Dot(point=apex_point, color=ACCENT_GOLD, radius=0.09)
            h_line = DashedLine(start=apex_point, end=ground_point, color=ACCENT_GOLD, stroke_width=2.5)
            h_label = Text("H_max", font_size=20, weight="BOLD", color=ACCENT_GOLD).next_to(h_line, RIGHT, buff=0.15)
            apex_badge = Text("Apex: vy = 0", font_size=12, weight="BOLD", color=ACCENT_GREEN).next_to(peak_dot, UP, buff=0.12)
            feature_group = VGroup(peak_dot, h_line, h_label, apex_badge)

        self.play(FadeIn(feature_group), FadeOut(hud_group), run_time=1.5)

        # Dynamic formula display on right side
        formula_mobj = self.create_smart_formula(
            formula_str=plain_formula,
            font_size=28,
            color_val=self.theme.formula_color
        ).to_corner(UR, buff=1.3).shift(DOWN * 0.8)

        # Dynamic Formula Card Header
        header_text = f"{concept_title.upper()} FORMULA"
        formula_title = Text(header_text, font=self.topic_font, font_size=18, weight="BOLD", color=self.theme.topic_color)
        if formula_title.width > 6.2:
            formula_title.scale_to_fit_width(6.2)
        formula_title.next_to(formula_mobj, UP, buff=0.35)

        formula_panel = VGroup(formula_title, formula_mobj)
        self.play(Write(formula_panel), run_time=2.0)

        # Critical Beat Repetition: Radiant highlight pulse (100% solid opacity)
        self.wait(1.0)
        self.play(Indicate(formula_mobj, color=self.theme.formula_color, scale_factor=1.06), run_time=1.4)
        for sm in formula_mobj.get_family():
            sm.set_opacity(1.0)

        # Dynamic Variable Explanations
        if "sin" in plain_formula or "cos" in plain_formula or "tan" in plain_formula:
            v0_text = Text("v₀ = Initial launch velocity", font=self.body_font, font_size=16, weight=self.theme.body_weight, color=self.accent_blue)
            theta_text = Text("θ = Angle from horizontal ground", font=self.body_font, font_size=16, weight=self.theme.body_weight, color=self.accent_blue)
            g_text = Text("g = Acceleration due to gravity (9.8 m/s²)", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.muted_text)
            vars_group = VGroup(v0_text, theta_text, g_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        else:
            principle_text = Text(author_nuance[:52] if author_nuance else "Governing Physical Relationship", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.accent_blue)
            vars_group = VGroup(principle_text)

        vars_group.next_to(formula_mobj, DOWN, buff=0.45)
        self.play(FadeIn(vars_group), run_time=1.5)
        self.wait(hold_formula)

        # =========================================================================
        # --- BEAT 4: CRITICAL (NEET TRAP ANALYSIS & FORMULA TRANSFORMATION) ---
        # =========================================================================
        self.play(FadeOut(vars_group), run_time=0.8)

        trap_title = Text("NEET TRAP ALERT", font=self.topic_font, font_size=17, weight="BOLD", color=self.theme.trap_color)
        wrapped_trap = textwrap.fill(trap_text, width=46)
        trap_body = Text(wrapped_trap, font=self.body_font, font_size=14, weight=self.theme.body_weight, color=self.theme.trap_body_color)
        if trap_body.width > 5.8:
            trap_body.scale_to_fit_width(5.8)

        # Transformation sub-panel if applicable
        if canonical_id == "P11-C02-T03-V01":  # Time of Flight vertical angle trap
            trans_lbl = Text("Vertical Angle Transformation:", font=self.topic_font, font_size=13, weight="BOLD", color=self.accent_gold)
            trans_form = self.create_smart_formula("T = (2 * v_0 * cos(θ)) / g", font_size=22, color_val=self.theme.formula_color)
            trans_rule = Text("Rule: Swap sin θ → cos θ!", font=self.body_font, font_size=13, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, trans_form, trans_rule).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif canonical_id == "P11-C02-T03-V02":  # Max Height vertical angle trap
            trans_lbl = Text("Vertical Angle Transformation:", font=self.topic_font, font_size=13, weight="BOLD", color=self.accent_gold)
            trans_form = self.create_smart_formula("H_max = (v_0^2 * cos^2(θ)) / (2g)", font_size=22, color_val=self.theme.formula_color)
            trans_rule = Text("Rule: Replace sin²θ with cos²θ!", font=self.body_font, font_size=13, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, trans_form, trans_rule).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif canonical_id == "P11-C02-T03-V03":  # Complementary angles trap
            trans_lbl = Text("Critical Complementary Distinction:", font=self.topic_font, font_size=13, weight="BOLD", color=self.accent_gold)
            trans_rule1 = Text("• Range: R(θ) = R(90° - θ)  [IDENTICAL]", font=self.body_font, font_size=13, color=self.accent_green)
            trans_rule2 = Text("• Height & Time: H₁ ≠ H₂  and  T₁ ≠ T₂  [UNEQUAL]", font=self.body_font, font_size=13, color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, trans_rule1, trans_rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        else:
            trap_panel = VGroup(trap_title, trap_body).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        trap_panel.next_to(formula_mobj, DOWN, buff=0.35)
        if trap_panel.get_right()[0] > 6.1:
            trap_panel.shift(LEFT * (trap_panel.get_right()[0] - 6.1))
        if trap_panel.get_bottom()[1] < -3.3:
            trap_panel.shift(UP * (-3.3 - trap_panel.get_bottom()[1]))

        self.play(FadeIn(trap_panel), run_time=1.5)
        self.wait(hold_trap)

        # Clear all active foreground & graph elements before entering end capsule revision
        self.play(
            FadeOut(trap_panel),
            FadeOut(formula_panel),
            FadeOut(graph_group),
            FadeOut(trajectory),
            FadeOut(feature_group),
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
