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
    Line, Circle,
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
        is_xt_graph = ("position-time" in concept_title.lower() or canonical_id == "P11-C02-T01-V01")
        is_vt_graph = ("velocity-time" in concept_title.lower() or canonical_id == "P11-C02-T03-V08")
        is_river = ("river" in concept_title.lower() or "relative" in concept_title.lower() or canonical_id == "P11-C02-T03-V09")
        is_height_proj = (canonical_id == "P11-C02-T04-V10" or "height" in concept_title.lower())
        is_incline_proj = (canonical_id == "P11-C02-T04-V11" or "inclined" in concept_title.lower())
        is_roc = (canonical_id == "P11-C02-T04-V12" or "curvature" in concept_title.lower())
        is_v_omega = (canonical_id == "P11-C02-T05-V13" or "angular" in concept_title.lower())
        is_non_uniform_circ = (canonical_id == "P11-C02-T05-V14" or "non-uniform" in concept_title.lower())

        axes = Axes(
            x_range=[0, 6.5, 1],
            y_range=[0, 5.0, 1],
            x_length=5.6,
            y_length=3.8,
            tips=True,
            axis_config={"color": MUTED_TEXT, "stroke_width": 2}
        ).to_corner(DL, buff=1.2).shift(RIGHT * 0.8 + UP * 0.2)

        if is_xt_graph:
            x_label = Text("Time t (s)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis, DOWN, buff=0.25)
            y_label = Text("Position x (m)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.18).shift(RIGHT * 0.4)
        elif is_vt_graph:
            x_label = Text("Time t (s)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis, DOWN, buff=0.25)
            y_label = Text("Velocity v (m/s)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.18).shift(RIGHT * 0.4)
        elif is_river:
            x_label = Text("Downstream x (m)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis, DOWN, buff=0.25)
            y_label = Text("River Width y (m)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.18).shift(RIGHT * 0.4)
        elif is_height_proj:
            x_label = Text("Range x (m)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis, DOWN, buff=0.25)
            y_label = Text("Height y (m)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.18).shift(RIGHT * 0.4)
        elif is_v_omega or is_non_uniform_circ:
            x_label = Text("x (m)", font_size=16, color=MUTED_TEXT).next_to(axes.x_axis, DOWN, buff=0.25)
            y_label = Text("y (m)", font_size=16, color=MUTED_TEXT).next_to(axes.y_axis.get_top(), UP, buff=0.18).shift(RIGHT * 0.4)
        else:
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

        if is_xt_graph:
            stat1_num = DecimalNumber(0.0, num_decimal_places=2, font_size=14, color=ACCENT_BLUE, mob_class=Text)
            stat1_row = VGroup(Text("t:", font_size=12, weight="BOLD", color=ACCENT_BLUE), stat1_num, Text("s", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            stat2_txt = Text("Slope: dx/dt = v", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            stat1_num.add_updater(lambda m: m.set_value(5.0 * time_tracker.get_value()))
            hud_stats = VGroup(stat1_row, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_vt_graph:
            stat1_num = DecimalNumber(0.0, num_decimal_places=2, font_size=14, color=ACCENT_BLUE, mob_class=Text)
            stat1_row = VGroup(Text("v:", font_size=12, weight="BOLD", color=ACCENT_BLUE), stat1_num, Text("m/s", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            stat2_txt = Text("Area: ∫ v dt = s", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            stat1_num.add_updater(lambda m: m.set_value(0.8 + 3.0 * time_tracker.get_value()))
            hud_stats = VGroup(stat1_row, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_river:
            stat1_txt = Text("v_river = 3.0 m/s", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("v_boat = 4.0 m/s", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_height_proj:
            stat1_txt = Text("Height h: 20 m", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("v₀: 15 m/s", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_incline_proj:
            stat1_txt = Text("Incline β: 20°", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("Launch α: 50°", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_roc:
            stat1_txt = Text("Apex vy: 0 m/s", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("Apex vx: v₀ cos θ", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_v_omega:
            stat1_txt = Text("ω = 2.0 rad/s", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("v = ω · r", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif is_non_uniform_circ:
            stat1_txt = Text("ac = v²/r (Radial)", font_size=12, weight="BOLD", color=ACCENT_BLUE)
            stat2_txt = Text("at = dv/dt (Tangent)", font_size=12, weight="BOLD", color=ACCENT_GOLD)
            hud_stats = VGroup(stat1_txt, stat2_txt).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        elif canonical_id == "P11-C02-T03-V01":  # Time of Flight
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

        # Trajectory / Curve rendering
        if is_xt_graph:
            # Accelerated position curve x(t) = 0.12 * t^2 + 0.1 * t
            trajectory = axes.plot(lambda t: 0.12 * (t ** 2) + 0.1 * t, x_range=[0, 5.5], color=ACCENT_BLUE, stroke_width=4)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    5.5 * time_tracker.get_value(),
                    0.12 * ((5.5 * time_tracker.get_value()) ** 2) + 0.1 * (5.5 * time_tracker.get_value())
                )
            ))
        elif is_vt_graph:
            trajectory = axes.plot(lambda t: 0.6 * t + 0.8, x_range=[0, 5.5], color=ACCENT_GREEN, stroke_width=4)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0.8))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    5.5 * time_tracker.get_value(),
                    0.6 * (5.5 * time_tracker.get_value()) + 0.8
                )
            ))
        elif is_river:
            trajectory = axes.plot(lambda x: (3.8 / 3.0) * x, x_range=[0, 3.0], color=ACCENT_GOLD, stroke_width=4)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    3.0 * time_tracker.get_value(),
                    3.8 * time_tracker.get_value()
                )
            ))
        elif is_height_proj:
            cliff_line = Line(start=axes.c2p(0, 0), end=axes.c2p(0, 3.8), color=MUTED_TEXT, stroke_width=4)
            traj_curve = axes.plot(lambda x: 3.8 - (3.8 / (4.8 ** 2)) * (x ** 2), x_range=[0, 4.8], color=ACCENT_GOLD, stroke_width=4)
            drop_path = DashedLine(start=axes.c2p(0, 3.8), end=axes.c2p(0, 0), color=ACCENT_GREEN, stroke_width=2.5)
            trajectory = VGroup(cliff_line, traj_curve, drop_path)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 3.8))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    4.8 * time_tracker.get_value(),
                    3.8 - (3.8 / (4.8 ** 2)) * ((4.8 * time_tracker.get_value()) ** 2)
                )
            ))
        elif is_incline_proj:
            incline_line = Line(start=axes.c2p(0, 0), end=axes.c2p(5.2, 1.89), color=MUTED_TEXT, stroke_width=3.5)
            traj_curve = axes.plot(lambda x: 2.4 * x - 0.484 * (x ** 2), x_range=[0, 4.2], color=ACCENT_GOLD, stroke_width=4)
            trajectory = VGroup(incline_line, traj_curve)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    4.2 * time_tracker.get_value(),
                    2.4 * (4.2 * time_tracker.get_value()) - 0.484 * ((4.2 * time_tracker.get_value()) ** 2)
                )
            ))
        elif is_roc:
            traj_curve = axes.plot(lambda x: 3.0 * x - 0.5 * (x ** 2), x_range=[0, 6.0], color=ACCENT_BLUE, stroke_width=4)
            trajectory = VGroup(traj_curve)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    3.0 * time_tracker.get_value(),
                    3.0 * (3.0 * time_tracker.get_value()) - 0.5 * ((3.0 * time_tracker.get_value()) ** 2)
                )
            ))
        elif is_v_omega:
            circ_c = axes.c2p(3.0, 2.3)
            c1 = Circle(radius=0.9, color=MUTED_TEXT, stroke_width=2.0).move_to(circ_c)
            c2 = Circle(radius=1.8, color=ACCENT_BLUE, stroke_width=2.5).move_to(circ_c)
            center_dot = Dot(point=circ_c, color=MUTED_TEXT, radius=0.07)
            trajectory = VGroup(c1, c2, center_dot)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.10).move_to(circ_c + np.array([1.8, 0, 0]))
            flight_ball.add_updater(lambda m: m.move_to(
                circ_c + np.array([
                    1.8 * np.cos(2 * np.pi * time_tracker.get_value()),
                    1.8 * np.sin(2 * np.pi * time_tracker.get_value()),
                    0
                ])
            ))
        elif is_non_uniform_circ:
            circ_c = axes.c2p(3.0, 2.3)
            c_orbit = Circle(radius=1.7, color=ACCENT_BLUE, stroke_width=2.5).move_to(circ_c)
            center_dot = Dot(point=circ_c, color=MUTED_TEXT, radius=0.07)
            trajectory = VGroup(c_orbit, center_dot)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(circ_c + np.array([0, 1.7, 0]))
            flight_ball.add_updater(lambda m: m.move_to(
                circ_c + np.array([
                    -1.7 * np.sin(2 * np.pi * time_tracker.get_value()),
                    1.7 * np.cos(2 * np.pi * time_tracker.get_value()),
                    0
                ])
            ))
        elif canonical_id == "P11-C02-T03-V03":  # Two complementary arcs
            traj1 = axes.plot(lambda x: 3.0 * x - 0.5 * (x ** 2), x_range=[0, 6.0], color=ACCENT_BLUE, stroke_width=3.5)
            traj2 = axes.plot(lambda x: 1.0 * x - (1.0 / 6.0) * (x ** 2), x_range=[0, 6.0], color=ACCENT_GREEN, stroke_width=3.5)
            trajectory = VGroup(traj1, traj2)
            flight_ball = Dot(color=ACCENT_GOLD, radius=0.12).move_to(axes.c2p(0, 0))
            flight_ball.add_updater(lambda m: m.move_to(
                axes.c2p(
                    3.0 * time_tracker.get_value(),
                    3.0 * (3.0 * time_tracker.get_value()) - 0.5 * ((3.0 * time_tracker.get_value()) ** 2)
                )
            ))
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
        if is_xt_graph:
            # Tangent line at t=3.5 showing slope = dx/dt
            t_pt = 3.5
            x_pt = 0.12 * (t_pt ** 2) + 0.1 * t_pt
            pt_coords = axes.c2p(t_pt, x_pt)
            slope_val = 2 * 0.12 * t_pt + 0.1  # ~0.94
            tangent_start = axes.c2p(t_pt - 1.5, x_pt - 1.5 * slope_val)
            tangent_end = axes.c2p(t_pt + 1.5, x_pt + 1.5 * slope_val)
            tangent_line = Line(start=tangent_start, end=tangent_end, color=ACCENT_GOLD, stroke_width=3)
            touch_dot = Dot(point=pt_coords, color=ACCENT_GOLD, radius=0.1)
            tangent_label = Text("Tangent Slope = dx/dt = v", font_size=15, weight="BOLD", color=ACCENT_GOLD).next_to(touch_dot, UL, buff=0.18)
            feature_group = VGroup(tangent_line, touch_dot, tangent_label)

        elif is_vt_graph:
            # Shaded region under curve representing displacement
            area_poly = axes.get_area(trajectory, x_range=[1.0, 4.5], color=ACCENT_BLUE, opacity=0.3)
            area_label = Text("Area = ∫ v dt = Displacement s", font_size=15, weight="BOLD", color=ACCENT_GOLD).move_to(axes.c2p(2.75, 1.2))
            feature_group = VGroup(area_poly, area_label)

        elif is_river:
            # River bank lines & velocity vector addition
            bank_line = DashedLine(start=axes.c2p(0, 3.8), end=axes.c2p(6.0, 3.8), color=ACCENT_GREEN, stroke_width=2.5)
            bank_label = Text("Opposite Bank (Width d)", font_size=12, color=ACCENT_GREEN).next_to(axes.c2p(4.6, 3.8), UP, buff=0.10)
            v_br_arrow = Arrow(start=axes.c2p(0, 0), end=axes.c2p(0, 3.8), buff=0, color=ACCENT_BLUE, stroke_width=3.5)
            v_br_lbl = Text("v_br (Heading)", font_size=12, weight="BOLD", color=ACCENT_BLUE).next_to(v_br_arrow, LEFT, buff=0.10)
            v_r_arrow = Arrow(start=axes.c2p(0, 3.8), end=axes.c2p(3.0, 3.8), buff=0, color=ACCENT_RED, stroke_width=3.5)
            v_r_lbl = Text("v_r (River Flow)", font_size=12, weight="BOLD", color=ACCENT_RED).next_to(v_r_arrow, UP, buff=0.10)
            feature_group = VGroup(bank_line, bank_label, v_br_arrow, v_br_lbl, v_r_arrow, v_r_lbl)

        elif is_height_proj:
            land_point = axes.c2p(4.8, 0.0)
            launch_point = axes.c2p(0, 3.8)
            v0_arrow = Arrow(start=launch_point, end=axes.c2p(1.5, 3.8), buff=0, color=ACCENT_GOLD, stroke_width=3.5)
            v0_label = Text("v₀ (Horizontal)", font_size=12, weight="BOLD", color=ACCENT_GOLD).next_to(v0_arrow, UP, buff=0.08)
            r_line = DashedLine(start=axes.c2p(0, 0), end=land_point, color=ACCENT_GREEN, stroke_width=2.5)
            r_label = Text("Range R = v₀ · t", font_size=12, weight="BOLD", color=ACCENT_GREEN).next_to(r_line, DOWN, buff=0.12)
            h_line = DashedLine(start=axes.c2p(-0.2, 0), end=axes.c2p(-0.2, 3.8), color=ACCENT_BLUE, stroke_width=2.5)
            h_label = Text("Height h", font_size=12, weight="BOLD", color=ACCENT_BLUE).next_to(h_line, LEFT, buff=0.08)
            drop_label = Text("Free Fall: t = √(2h/g)", font_size=11, color=ACCENT_GREEN).next_to(axes.c2p(0, 1.9), RIGHT, buff=0.12)
            feature_group = VGroup(v0_arrow, v0_label, r_line, r_label, h_line, h_label, drop_label)

        elif is_incline_proj:
            v0_arrow = Arrow(start=axes.c2p(0, 0), end=axes.c2p(1.2, 1.43), buff=0, color=ACCENT_GOLD, stroke_width=3.5)
            v0_label = Text("v₀ (Launch α)", font_size=12, weight="BOLD", color=ACCENT_GOLD).next_to(v0_arrow, UL, buff=0.08)
            land_dot = Dot(point=axes.c2p(4.2, 1.53), color=ACCENT_GOLD, radius=0.1)
            land_lbl = Text("Landing Point (Range R)", font_size=12, weight="BOLD", color=ACCENT_GREEN).next_to(land_dot, UR, buff=0.15).shift(UP * 0.15)
            g_lbl = Text("g_perp = g cos β  |  g_par = g sin β", font_size=12, weight="BOLD", color=ACCENT_BLUE).next_to(axes.c2p(2.2, 0.4), DOWN, buff=0.12)
            feature_group = VGroup(v0_arrow, v0_label, land_dot, land_lbl, g_lbl)

        elif is_roc:
            apex_dot = Dot(point=axes.c2p(3.0, 4.5), color=ACCENT_GOLD, radius=0.1)
            apex_badge = Text("Apex: vy = 0, vx = v₀ cos θ", font_size=12, weight="BOLD", color=ACCENT_GOLD).next_to(apex_dot, UP, buff=0.16)
            rho_arrow = Arrow(start=axes.c2p(3.0, 2.5), end=axes.c2p(3.0, 4.5), buff=0, color=ACCENT_GREEN, stroke_width=3.0)
            rho_lbl = Text("Radius ρ = vx² / g", font_size=12, weight="BOLD", color=ACCENT_GREEN).next_to(rho_arrow, LEFT, buff=0.12)
            vx_arrow = Arrow(start=axes.c2p(3.0, 4.5), end=axes.c2p(4.4, 4.5), buff=0, color=ACCENT_BLUE, stroke_width=3.0)
            vx_lbl = Text("v_apex", font_size=11, weight="BOLD", color=ACCENT_BLUE).next_to(vx_arrow, RIGHT, buff=0.08)
            feature_group = VGroup(apex_dot, apex_badge, rho_arrow, rho_lbl, vx_arrow, vx_lbl)

        elif is_v_omega:
            circ_c = axes.c2p(3.0, 2.3)
            pt1 = circ_c + np.array([0.9, 0, 0])
            r1_line = DashedLine(start=circ_c, end=pt1, color=ACCENT_BLUE, stroke_width=2.0)
            r1_lbl = Text("r₁", font_size=11, color=ACCENT_BLUE).next_to(circ_c + np.array([0.45, 0, 0]), DOWN, buff=0.10)
            v1_arrow = Arrow(start=pt1, end=pt1 + np.array([0, 0.7, 0]), buff=0, color=ACCENT_GREEN, stroke_width=3.0)
            v1_lbl = Text("v₁ = ω·r₁", font_size=10, weight="BOLD", color=ACCENT_GREEN).next_to(v1_arrow, LEFT, buff=0.06)
            pt2 = circ_c + np.array([1.8, 0, 0])
            r2_line = DashedLine(start=circ_c, end=pt2, color=ACCENT_BLUE, stroke_width=2.0)
            r2_lbl = Text("r₂", font_size=11, color=ACCENT_BLUE).next_to(circ_c + np.array([1.35, 0, 0]), DOWN, buff=0.10)
            v2_arrow = Arrow(start=pt2, end=pt2 + np.array([0, 1.4, 0]), buff=0, color=ACCENT_GOLD, stroke_width=3.5)
            v2_lbl = Text("v₂ = ω·r₂", font_size=11, weight="BOLD", color=ACCENT_GOLD).next_to(v2_arrow, RIGHT, buff=0.08)
            speed_note = Text("v₂ > v₁  (Same ω, faster at outer rim)", font_size=11, weight="BOLD", color=ACCENT_GOLD).next_to(circ_c + UP * 1.95, UP, buff=0.08)
            feature_group = VGroup(r1_line, r1_lbl, v1_arrow, v1_lbl, r2_line, r2_lbl, v2_arrow, v2_lbl, speed_note)

        elif is_non_uniform_circ:
            circ_c = axes.c2p(3.0, 2.3)
            pt = circ_c + np.array([0, 1.7, 0])
            p_dot = Dot(point=pt, color=ACCENT_GOLD, radius=0.10)
            ac_arrow = Arrow(start=pt, end=pt + np.array([0, -1.0, 0]), buff=0, color=ACCENT_BLUE, stroke_width=3.5)
            ac_lbl = Text("a_c (Radial)", font_size=11, weight="BOLD", color=ACCENT_BLUE).next_to(ac_arrow, RIGHT, buff=0.08)
            at_arrow = Arrow(start=pt, end=pt + np.array([-1.0, 0, 0]), buff=0, color=ACCENT_GREEN, stroke_width=3.5)
            at_lbl = Text("a_t (Tangential)", font_size=11, weight="BOLD", color=ACCENT_GREEN).next_to(at_arrow, UP, buff=0.08)
            anet_arrow = Arrow(start=pt, end=pt + np.array([-1.0, -1.0, 0]), buff=0, color=ACCENT_GOLD, stroke_width=3.5)
            anet_lbl = Text("a_net", font_size=12, weight="BOLD", color=ACCENT_GOLD).next_to(anet_arrow.get_end(), DL, buff=0.08)
            perp_note = Text("a_c is perpendicular to a_t  (Right angle)", font_size=11, weight="BOLD", color=ACCENT_GOLD).move_to(circ_c + DOWN * 0.85)
            feature_group = VGroup(p_dot, ac_arrow, ac_lbl, at_arrow, at_lbl, anet_arrow, anet_lbl, perp_note)

        elif canonical_id == "P11-C02-T03-V01":  # Time of Flight landing highlight
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
        if formula_title.width > 5.2:
            formula_title.scale_to_fit_width(5.2)
        formula_title.next_to(formula_mobj, UP, buff=0.35)
        if formula_title.get_right()[0] > 6.0:
            formula_title.shift(LEFT * (formula_title.get_right()[0] - 6.0))

        formula_panel = VGroup(formula_title, formula_mobj)
        self.play(Write(formula_panel), run_time=2.0)

        # Critical Beat Repetition: Radiant highlight pulse (100% solid opacity)
        self.wait(1.0)
        self.play(Indicate(formula_mobj, color=self.theme.formula_color, scale_factor=1.06), run_time=1.4)
        for sm in formula_mobj.get_family():
            sm.set_opacity(1.0)

        # Dynamic Variable Explanations
        if is_xt_graph:
            dx_text = Text("dx = Infinitesimal displacement", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.accent_blue)
            dt_text = Text("dt = Infinitesimal time interval", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.accent_blue)
            slope_text = Text("Slope m = tan θ = Instantaneous Velocity v", font=self.body_font, font_size=15, weight="BOLD", color=self.accent_gold)
            vars_group = VGroup(dx_text, dt_text, slope_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_vt_graph:
            v_text = Text("v = Velocity function over time", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.accent_blue)
            area_text = Text("Area under curve = Integral ∫ v dt", font=self.body_font, font_size=15, weight="BOLD", color=self.accent_gold)
            disp_text = Text("s = Net displacement of particle", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.muted_text)
            vars_group = VGroup(v_text, area_text, disp_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_river:
            v_ab_text = Text("v_net = v_br + v_r  (Vector sum in water)", font=self.body_font, font_size=14, color=self.accent_blue)
            t_min_text = Text("t_min = d / v_br  (Shortest time condition)", font=self.body_font, font_size=14, weight="BOLD", color=self.accent_gold)
            drift_text = Text("Drift x = v_r · t_min  (Downstream distance)", font=self.body_font, font_size=14, color=self.muted_text)
            vars_group = VGroup(v_ab_text, t_min_text, drift_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_height_proj:
            t_text = Text("t = √(2h / g)  [Drop time independent of v₀!]", font=self.body_font, font_size=14, weight="BOLD", color=self.accent_gold)
            r_text = Text("R = v₀ · √(2h / g)  [Horizontal ground range]", font=self.body_font, font_size=14, color=self.accent_blue)
            v_text = Text("v_impact = √(v₀² + 2gh)  [Final impact speed]", font=self.body_font, font_size=14, color=self.muted_text)
            vars_group = VGroup(t_text, r_text, v_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_incline_proj:
            t_text = Text("T = 2v₀·sin(α-β) / (g·cos β)  [Flight time on incline]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
            r_text = Text("R = Range measured along incline surface", font=self.body_font, font_size=13, color=self.accent_blue)
            g_text = Text("Effective gravity: g_perp = g·cos β,  g_par = g·sin β", font=self.body_font, font_size=13, color=self.muted_text)
            vars_group = VGroup(t_text, r_text, g_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_roc:
            rho_text = Text("ρ = (v₀² · cos² θ) / g  [Radius of Curvature at apex]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
            vx_text = Text("v_apex = v₀ · cos θ  [Purely horizontal velocity]", font=self.body_font, font_size=13, color=self.accent_blue)
            an_text = Text("a_n = g  [Normal acceleration is full gravity]", font=self.body_font, font_size=13, color=self.muted_text)
            vars_group = VGroup(rho_text, vx_text, an_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_v_omega:
            v_text = Text("v = ω · r  [Linear speed proportional to radius]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
            w_text = Text("ω = dθ / dt  [Angular speed is identical across body]", font=self.body_font, font_size=13, color=self.accent_blue)
            s_text = Text("s = r · θ  [Arc length traversed along circumference]", font=self.body_font, font_size=13, color=self.muted_text)
            vars_group = VGroup(v_text, w_text, s_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif is_non_uniform_circ:
            anet_text = Text("a_net = √(a_c² + a_t²)  [Total resultant acceleration]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
            ac_text = Text("a_c = v² / r  [Radial component alters direction]", font=self.body_font, font_size=13, color=self.accent_blue)
            at_text = Text("a_t = dv / dt = r · α  [Tangential alters linear speed]", font=self.body_font, font_size=13, color=self.muted_text)
            vars_group = VGroup(anet_text, ac_text, at_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        elif "sin" in plain_formula or "cos" in plain_formula or "tan" in plain_formula:
            v0_text = Text("v₀ = Initial launch velocity", font=self.body_font, font_size=16, weight=self.theme.body_weight, color=self.accent_blue)
            theta_text = Text("θ = Angle from horizontal ground", font=self.body_font, font_size=16, weight=self.theme.body_weight, color=self.accent_blue)
            g_text = Text("g = Acceleration due to gravity (9.8 m/s²)", font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.muted_text)
            vars_group = VGroup(v0_text, theta_text, g_text).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        else:
            wrapped_nuance = textwrap.fill(author_nuance, width=38) if author_nuance else "Governing Physical Relationship"
            principle_text = Text(wrapped_nuance, font=self.body_font, font_size=14, weight=self.theme.body_weight, color=self.accent_blue)
            if principle_text.width > 5.6:
                principle_text.scale_to_fit_width(5.6)
            vars_group = VGroup(principle_text)

        vars_group.next_to(formula_mobj, DOWN, buff=0.45)
        if vars_group.width > 5.5:
            vars_group.scale_to_fit_width(5.5)
        if vars_group.get_right()[0] > 6.1:
            vars_group.shift(LEFT * (vars_group.get_right()[0] - 6.1))
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
        if is_xt_graph:
            trans_lbl = Text("Crucial NEET Distinction:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Slope of x-t graph = Velocity (v)", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)
            rule2 = Text("• Slope of v-t graph = Acceleration (a)", font=self.body_font, font_size=13, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_vt_graph:
            trans_lbl = Text("Crucial NEET Distinction:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Area under v-t graph = Displacement (s)", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)
            rule2 = Text("• Slope of v-t graph = Acceleration (a)", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_river:
            trans_lbl = Text("River Crossing NEET Traps:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Shortest Time: Head 90° to flow (drift downstream)", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            rule2 = Text("• Shortest Path: Head upstream (zero drift, sin θ = v_r/v_b)", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_height_proj:
            trans_lbl = Text("Golden NEET Principle:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Dropped & projected balls hit ground SIMULTANEOUSLY!", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            rule2 = Text("• Launch speed v₀ increases Range R, NOT flight time t!", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_incline_proj:
            trans_lbl = Text("Crucial NEET Incline Trap:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Acceleration along incline is NOT zero: a_x' = -g sin β!", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            rule2 = Text("• Up-incline vs Down-incline have different flight ranges!", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_roc:
            trans_lbl = Text("High-Frequency NEET Trap:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Use apex velocity v₀ cos θ in numerator, NOT initial v₀!", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            rule2 = Text("• At apex, normal acceleration is 100% gravity g (a_n = g)", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_v_omega:
            trans_lbl = Text("Golden NEET Principle:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Angular velocity ω is IDENTICAL for all points on rotating disc!", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            rule2 = Text("• Linear velocity v increases with radius r (v = ω · r)!", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif is_non_uniform_circ:
            trans_lbl = Text("Crucial NEET Distinction:", font=self.topic_font, font_size=14, weight="BOLD", color=self.accent_gold)
            rule1 = Text("• Uniform Circular Motion: Speed constant, a_t = 0, a_net = a_c", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green)
            rule2 = Text("• Non-Uniform Motion: Speed changes, BOTH a_c and a_t exist!", font=self.body_font, font_size=12, weight="BOLD", color=self.theme.trap_color)
            trap_panel = VGroup(trap_title, trap_body, trans_lbl, rule1, rule2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        elif canonical_id == "P11-C02-T03-V01":  # Time of Flight vertical angle trap
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
        if trap_panel.width > 5.2:
            trap_panel.scale_to_fit_width(5.2)
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
