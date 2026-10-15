"""
FormulaWithGraph 3D Scene Implementation (Visual Physics Simulation Tier)
Target: P11-C02-T03-V02 "The Max Height Arc"
Features:
- Physical Launch Cannon / Stage Apparatus
- Animated Projectile Sphere with Dynamic Trailing Neon Ribbon
- Moving Body-Anchored Vector Arrows (vx constant, vy shrinking to 0 at apex)
- Dynamic 3D Camera Orbit tracking the physics trajectory
- Pinned Screen-Safe 2D HUD (Zero Perspective Distortion)
"""

import numpy as np
from manim import (
    ThreeDAxes, DashedLine, Dot, Arrow, Text, MathTex, VGroup, Line, Circle,
    Rectangle, RoundedRectangle, DecimalNumber, ValueTracker,
    FadeIn, FadeOut, Create, Write, Transform, Indicate,
    UP, DOWN, LEFT, RIGHT, ORIGIN, OUT, IN, UL, UR, DL, DR,
    DEGREES, TAU, linear
)
from render.templates.base import (
    NEETVideoScene3D,
    BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN, TEXT_WHITE, MUTED_TEXT,
    FONT_PRIMARY, FONT_MONO
)

class FormulaWithGraph3DScene(NEETVideoScene3D):
    def render_concept_beats(self):
        latex_formula = self.parameters.get("latexFormula", r"H_{\max} = \frac{v_0^2 \sin^2\theta}{2g}")
        plain_formula = self.parameters.get("plainFormula", "H_max = (v_0^2 * sin^2(θ)) / (2g)")
        trap_text = self.parameters.get("trapWarning", "Angle θ MUST be measured relative to horizontal.")

        # Audio-aligned timing pacing
        target_dur = float(self.node_data.get("target_duration", 32.0))
        extra_time = max(0.0, target_dur - 31.8)
        hold_formula = 1.5 + (extra_time * 0.30)
        hold_trap = 2.0 + (extra_time * 0.30)
        capsule_dur = 6.0 + (extra_time * 0.40)

        # --- BEAT 1: SETTLE ---
        settle_text = Text("Visual Physics 3D Simulation — Projectile Apex", font_size=25, color=ACCENT_BLUE)
        settle_text.move_to(ORIGIN + UP * 0.5)
        self.add_fixed_in_frame_mobjects(settle_text)
        self.play(FadeIn(settle_text), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(settle_text), run_time=1.0)
        self.remove_fixed_in_frame_mobjects(settle_text)
        self.remove(settle_text)

        # --- BEAT 2: 3D STAGE & PHYSICAL APPARATUS SETUP ---
        # Set dynamic oblique 3D camera orientation
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES)

        # 3D Coordinate Stage
        axes_3d = ThreeDAxes(
            x_range=[0, 6.5, 1],
            y_range=[0, 5.0, 1],
            z_range=[-1.5, 1.5, 1],
            x_length=6.0,
            y_length=4.0,
            z_length=2.5,
            axis_config={"color": MUTED_TEXT, "stroke_width": 2}
        ).shift(DOWN * 1.5 + LEFT * 2.0)

        # Physical Ground Stage Grid
        ground_lines = VGroup()
        for x_val in range(1, 7):
            p1 = axes_3d.c2p(x_val, 0, -1.2)
            p2 = axes_3d.c2p(x_val, 0, 1.2)
            ground_lines.add(Line(p1, p2, color="#1E293B", stroke_width=1.0))
        for z_val in np.linspace(-1.2, 1.2, 5):
            p1 = axes_3d.c2p(0, 0, z_val)
            p2 = axes_3d.c2p(6.0, 0, z_val)
            ground_lines.add(Line(p1, p2, color="#1E293B", stroke_width=1.0))

        # Physical Launch Base Platform
        origin_pt = axes_3d.c2p(0, 0, 0)
        launch_base = Dot(point=origin_pt, color="#334155", radius=0.22)
        launch_barrel = Line(
            origin_pt,
            origin_pt + np.array([0.5, 0.65, 0.0]),
            color="#475569",
            stroke_width=6.0
        )
        apparatus_group = VGroup(ground_lines, axes_3d, launch_base, launch_barrel)

        self.play(Create(apparatus_group), run_time=1.8)

        # --- BEAT 3: FLIGHT SIMULATION WITH DYNAMIC VECTOR ARROWS ---
        # Launching projectile sphere
        ball = Dot(point=origin_pt, color=ACCENT_GOLD, radius=0.15)
        
        # Pinned Formula Panel (Fixed flat to screen frame)
        formula_mobj = self.create_textbook_fraction(
            lhs="H_max =",
            num="v₀² · sin²θ",
            den="2g",
            font_size=28,
            color_val=ACCENT_GOLD
        ).to_corner(UR, buff=1.3).shift(DOWN * 0.8)

        formula_title = Text("MAXIMUM HEIGHT (3D DERIVATION)", font_size=19, weight="BOLD", color=TEXT_WHITE)
        formula_title.next_to(formula_mobj, UP, buff=0.3)
        formula_panel = VGroup(formula_title, formula_mobj)
        self.add_fixed_in_frame_mobjects(formula_panel)

        # Pinned 3D Simulation Telemetry HUD Card
        hud_box = RoundedRectangle(
            corner_radius=0.1,
            height=0.92,
            width=3.7,
            stroke_color=ACCENT_BLUE,
            stroke_width=1.5,
            fill_color="#0F172A",
            fill_opacity=0.92
        ).to_corner(UL, buff=1.1).shift(DOWN * 0.3 + RIGHT * 0.4)

        hud_title = Text("SIMULATION TELEMETRY (3D)", font_size=11, weight="BOLD", color=MUTED_TEXT).next_to(hud_box.get_top(), DOWN, buff=0.10)

        def make_stats_group(vy_val: float, y_val: float):
            return VGroup(
                VGroup(Text("vy:", font_size=12, weight="BOLD", color=ACCENT_BLUE), Text(f"{vy_val:.1f}", font_size=14, color=ACCENT_BLUE), Text("m/s", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06),
                VGroup(Text("Height:", font_size=12, weight="BOLD", color=ACCENT_GOLD), Text(f"{y_val:.1f}", font_size=14, color=ACCENT_GOLD), Text("m", font_size=11, color=MUTED_TEXT)).arrange(RIGHT, buff=0.06)
            ).arrange(RIGHT, buff=0.22).next_to(hud_title, DOWN, buff=0.10)

        hud_stats = make_stats_group(20.0, 0.0)
        hud_group = VGroup(hud_box, hud_title, hud_stats)
        self.add_fixed_in_frame_mobjects(hud_group)

        # Simulate trajectory flight up to apex (t = 0 to 3.0)
        # Trajectory curve segments
        t_values = np.linspace(0, 3.0, 40)
        trail_segments = VGroup()
        for i in range(len(t_values) - 1):
            t1, t2 = t_values[i], t_values[i+1]
            p1 = axes_3d.c2p(t1, 3.0 * t1 - 0.5 * (t1 ** 2), 0.0)
            p2 = axes_3d.c2p(t2, 3.0 * t2 - 0.5 * (t2 ** 2), 0.0)
            trail_segments.add(Line(p1, p2, color=ACCENT_BLUE, stroke_width=4.5))

        time_tracker = ValueTracker(0.0)
        hud_stats.add_updater(lambda m: m.become(make_stats_group(
            max(0.0, 20.0 * (1.0 - time_tracker.get_value())),
            20.4 * (1.0 - (1.0 - time_tracker.get_value()) ** 2)
        )))

        self.play(FadeIn(hud_group), run_time=0.8)
        self.add(ball)
        self.play(
            Create(trail_segments),
            ball.animate.move_to(axes_3d.c2p(3.0, 4.5, 0.0)),
            time_tracker.animate.set_value(1.0),
            Write(formula_panel),
            run_time=2.5,
            rate_func=linear
        )
        hud_stats.clear_updaters()
        self.play(FadeOut(hud_group), run_time=0.6)
        self.remove_fixed_in_frame_mobjects(hud_group)

        # At Apex (x=3.0, y=4.5):
        apex_pos = axes_3d.c2p(3.0, 4.5, 0.0)
        ground_apex = axes_3d.c2p(3.0, 0.0, 0.0)
        h_line = DashedLine(start=apex_pos, end=ground_apex, color=ACCENT_GOLD, stroke_width=2.5)
        h_tag = Text("H_max", font_size=18, weight="BOLD", color=ACCENT_GOLD).next_to(h_line, RIGHT, buff=0.15)

        # Dynamic 3D Vectors AT APEX:
        # Constant Horizontal Velocity Vector (vx) pointing in +X
        vx_tip = axes_3d.c2p(4.4, 4.5, 0.0)
        vx_vector = Line(apex_pos, vx_tip, color=ACCENT_GREEN, stroke_width=5.0)
        vx_arrowhead = Dot(point=vx_tip, color=ACCENT_GREEN, radius=0.08)
        vx_label = Text("vx = v₀ cosθ (Constant)", font_size=16, weight="BOLD", color=ACCENT_GREEN)
        vx_label.next_to(vx_vector, UP, buff=0.15)

        # Vertical Velocity is ZERO indicator
        vy_zero_label = Text("vy = 0 (Vertical Stop)", font_size=16, weight="BOLD", color=ACCENT_RED)
        vy_zero_label.next_to(ball, LEFT, buff=0.25)

        apex_visuals = VGroup(h_line, h_tag, vx_vector, vx_arrowhead, vx_label, vy_zero_label)

        # Complete descending trajectory trail (from apex to ground x=6.0)
        descend_t = np.linspace(3.0, 6.0, 40)
        descend_segments = VGroup()
        for i in range(len(descend_t) - 1):
            t1, t2 = descend_t[i], descend_t[i+1]
            p1 = axes_3d.c2p(t1, 3.0 * t1 - 0.5 * (t1 ** 2), 0.0)
            p2 = axes_3d.c2p(t2, 3.0 * t2 - 0.5 * (t2 ** 2), 0.0)
            descend_segments.add(Line(p1, p2, color=MUTED_TEXT, stroke_width=2.5))

        self.play(
            FadeIn(apex_visuals),
            Create(descend_segments),
            run_time=2.0
        )

        # Cinematic 3D camera pan around the apex to emphasize 3D spatial depth
        self.move_camera(phi=75 * DEGREES, theta=-20 * DEGREES, run_time=2.5)

        # Variable explanations (Pinned in frame)
        v0_text = Text("v₀ = Launch velocity vector", font_size=17, color=ACCENT_BLUE)
        theta_text = Text("θ = Launch angle with horizontal", font_size=17, color=ACCENT_BLUE)
        apex_law = Text("Apex Rule: Vertical velocity vy = 0", font_size=17, weight="BOLD", color=ACCENT_GREEN)
        vars_group = VGroup(v0_text, theta_text, apex_law).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        vars_group.next_to(formula_mobj, DOWN, buff=0.45)
        self.add_fixed_in_frame_mobjects(vars_group)
        self.play(FadeIn(vars_group), run_time=1.5)
        self.wait(hold_formula)

        # --- BEAT 4: CRITICAL (NEET TRAP ANALYSIS & FORMULA TRANSFORMATION) ---
        self.play(FadeOut(vars_group), run_time=0.8)
        self.remove_fixed_in_frame_mobjects(vars_group)

        trap_title = Text("NEET TRAP: Angle from VERTICAL", font=FONT_PRIMARY, font_size=17, weight="BOLD", color=ACCENT_RED)
        trap_rule = Text("When θ is given relative to vertical axis:", font=FONT_PRIMARY, font_size=14, color=TEXT_WHITE)
        trap_vy = Text("Vertical component becomes: vy = v₀ cos θ", font=FONT_PRIMARY, font_size=15, color=ACCENT_BLUE)
        trap_label = Text("CORRECT FORMULA TRANSFORMATION:", font=FONT_PRIMARY, font_size=13, weight="BOLD", color=ACCENT_GOLD)
        trap_formula = self.create_textbook_fraction(
            lhs="H_max =",
            num="v₀² · cos²θ",
            den="2g",
            font_size=24,
            color_val=ACCENT_GOLD
        )
        trap_takeaway = Text("Rule: Replace sin²θ with cos²θ!", font=FONT_PRIMARY, font_size=14, weight="BOLD", color=ACCENT_RED)

        trap_panel = VGroup(
            trap_title,
            trap_rule,
            trap_vy,
            trap_label,
            trap_formula,
            trap_takeaway
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        trap_panel.next_to(formula_mobj, DOWN, buff=0.35)
        if trap_panel.get_right()[0] > 6.1:
            trap_panel.shift(LEFT * (trap_panel.get_right()[0] - 6.1))
        if trap_panel.get_bottom()[1] < -3.3:
            trap_panel.shift(UP * (-3.3 - trap_panel.get_bottom()[1]))

        self.add_fixed_in_frame_mobjects(trap_panel)
        self.play(FadeIn(trap_panel), run_time=1.5)
        self.play(Indicate(trap_formula, color=ACCENT_GOLD), run_time=1.5)
        self.wait(hold_trap)

        # Clear foreground fixed panels before entering end capsule to prevent ghosting
        self.play(FadeOut(trap_panel), FadeOut(formula_panel), run_time=0.6)
        self.remove_fixed_in_frame_mobjects(trap_panel, formula_panel)

        # --- BEAT 5: END CAPSULE REVISION ---
        self.render_end_capsule(formula_mobj, trap_text, duration=capsule_dur)

        # --- BEAT 6: RELEASE (TEASER) ---
        self.render_release_teaser(duration=3.5)
