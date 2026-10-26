"""
Gate 3 Dedicated Visual Archetypes Generator
Appends the 7 Projectile Motion scenes to render/templates/unit_02_archetypes.py:
1. TimeOfFlightScene (P11-C02-T03-V01)
2. MaxHeightArcScene (P11-C02-T03-V02)
3. HorizontalRangeScene (P11-C02-T03-V03)
4. TrajectoryEquationScene (P11-C02-T03-V04)
5. HorizontalProjectionScene (P11-C02-T04-V10)
6. InclinedPlaneProjectileScene (P11-C02-T04-V11)
7. RadiusOfCurvatureScene (P11-C02-T04-V12)
"""

from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
archetypes_file = BASE_DIR / "render" / "templates" / "unit_02_archetypes.py"

with open(archetypes_file, "r", encoding="utf-8") as f:
    existing = f.read()

scenes_code = '''
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
'''

if "TimeOfFlightScene" not in existing:
    with open(archetypes_file, "a", encoding="utf-8") as f:
        f.write(scenes_code)
    print("Successfully appended TimeOfFlightScene and MaxHeightArcScene to unit_02_archetypes.py!")
else:
    print("TimeOfFlightScene already exists in unit_02_archetypes.py")
