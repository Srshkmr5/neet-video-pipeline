from manim import *
import numpy as np

# Safe, proportional typography only (Arial / Segoe UI with Pango - no LaTeX dependency)
Text.set_default(font="Arial")
config.background_color = "#020B16"


class C01DotProductScene(Scene):
    def construct(self):
        # ---------- Colors ----------
        bg = "#020B16"
        panel = "#0F172A"
        accent_blue = "#7DD3FC"
        accent_gold = "#FBBF24"
        accent_green = "#34D399"
        accent_red = "#F87171"
        text_white = "#E2E8F0"
        muted = "#94A3B8"

        # ---------- Background ----------
        self.camera.background_color = bg

        # ---------- Header ----------
        header = Text(
            "Work, Energy & Power",
            font="Arial",
            font_size=20,
            color=muted,
            weight="NORMAL",
        ).to_edge(UP, buff=0.6).to_edge(LEFT, buff=0.9)

        title = Text(
            "Scalar Product and Work Done by Constant Force",
            font="Arial",
            font_size=30,
            color=accent_blue,
            weight="BOLD"
        ).next_to(header, DOWN, buff=0.15).align_to(header, LEFT)

        subtitle = Text(
            "NCERT Class 11 Physics Part 1 • Chapter 5 • Section 5.2–5.3",
            font="Arial",
            font_size=16,
            color=accent_gold
        ).next_to(title, DOWN, buff=0.10).align_to(title, LEFT)

        # ---------- Main layout frame ----------
        main_box = RoundedRectangle(
            width=11.6,
            height=5.2,
            corner_radius=0.12,
            stroke_color=accent_blue,
            stroke_width=1.5,
            fill_color=panel,
            fill_opacity=0.85,
        ).move_to(DOWN * 0.15)

        # ---------- Left visual panel ----------
        left_panel = RoundedRectangle(
            width=5.2,
            height=3.6,
            corner_radius=0.10,
            stroke_color="#334155",
            stroke_width=1.2,
            fill_color="#101B2A",
            fill_opacity=0.9
        ).move_to(LEFT * 2.2)

        # ground line
        ground = Line(
            start=LEFT*2.2 + DOWN*1.0,
            end=RIGHT*2.2 + DOWN*1.0,
            color="#475569",
            stroke_width=2.5
        )

        # block
        block = RoundedRectangle(
            width=1.4,
            height=1.0,
            corner_radius=0.08,
            stroke_color=accent_blue,
            stroke_width=2.0,
            fill_color="#1E293B",
            fill_opacity=0.8
        ).move_to(LEFT * 2.2 + DOWN * 0.45)

        block_label = Text(
            "m",
            font="Arial",
            font_size=15,
            color=text_white,
            weight="BOLD"
        ).move_to(block.get_center())

        # displacement arrow along x
        displacement_start = block.get_left() + LEFT * 0.05
        displacement_end = block.get_right() + RIGHT * 1.35
        displacement_arrow = Arrow(
            start=displacement_start,
            end=displacement_end,
            color=accent_gold,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18
        )
        displacement_label = Text(
            "displacement d",
            font="Arial",
            font_size=14,
            color=accent_gold
        ).next_to(displacement_arrow, DOWN, buff=0.12)

        # force arrow at angle theta
        force_start = block.get_center()
        force_end = block.get_center() + np.array([1.5, 1.0, 0])
        force_arrow = Arrow(
            start=force_start,
            end=force_end,
            color=accent_green,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.18
        )
        force_label = Text(
            "force F",
            font="Arial",
            font_size=14,
            color=accent_green
        ).next_to(force_arrow.get_end(), UP, buff=0.08)

        # projection component along x
        proj_start = block.get_center()
        proj_end = block.get_center() + np.array([1.5, 0, 0])
        proj_arrow = DashedLine(
            start=proj_start,
            end=proj_end,
            color="#64748B",
            stroke_width=2
        )
        proj_label = Text(
            "F cos θ",
            font="Arial",
            font_size=13,
            color=accent_blue
        ).next_to(proj_arrow, DOWN, buff=0.06)

        # angle arc
        theta_arc = Arc(
            radius=0.7,
            start_angle=0,
            angle=0.6,
            arc_center=block.get_center(),
            color=accent_gold,
            stroke_width=2.0
        )
        theta_label = Text(
            "θ",
            font="Arial",
            font_size=16,
            color=accent_gold,
            weight="BOLD"
        ).next_to(theta_arc, RIGHT, buff=0.05)

        # ---------- Right formula panel ----------
        right_panel = RoundedRectangle(
            width=5.0,
            height=3.4,
            corner_radius=0.10,
            stroke_color=accent_gold,
            stroke_width=1.2,
            fill_color="#101B2A",
            fill_opacity=0.9
        ).move_to(RIGHT * 2.6)

        formula = Text(
            "W = F · d = F d cos θ",
            font="Arial",
            font_size=24,
            weight="BOLD",
            color=accent_gold
        ).move_to(right_panel.get_center() + UP * 0.9)

        bullet_1 = Text(
            "• Work is a scalar quantity, measured in joules",
            font="Arial",
            font_size=13,
            color=text_white
        ).next_to(formula, DOWN, buff=0.35).align_to(right_panel, LEFT).shift(RIGHT * 0.25)

        bullet_2 = Text(
            "• Positive if angle < 90° and force helps motion",
            font="Arial",
            font_size=13,
            color=accent_green
        ).next_to(bullet_1, DOWN, buff=0.12).align_to(bullet_1, LEFT)

        bullet_3 = Text(
            "• Zero when θ = 90° or displacement is zero",
            font="Arial",
            font_size=13,
            color=accent_blue
        ).next_to(bullet_2, DOWN, buff=0.12).align_to(bullet_2, LEFT)

        bullet_4 = Text(
            "• Negative when friction opposes displacement",
            font="Arial",
            font_size=13,
            color=accent_red
        ).next_to(bullet_3, DOWN, buff=0.12).align_to(bullet_3, LEFT)

        # ---------- Trap alert ----------
        trap_box = RoundedRectangle(
            width=10.6,
            height=0.9,
            corner_radius=0.10,
            stroke_color=accent_red,
            stroke_width=1.5,
            fill_color="#1A0B0E",
            fill_opacity=0.9
        ).move_to(DOWN * 2.0)

        trap_title = Text(
            "NEET TRAP: work is not done whenever force is applied",
            font="Arial",
            font_size=15,
            color=accent_red,
            weight="BOLD"
        ).move_to(trap_box.get_center())

        # ---------- Compose scene ----------
        self.play(
            FadeIn(header),
            FadeIn(title),
            FadeIn(subtitle),
            FadeIn(main_box),
            FadeIn(left_panel),
            FadeIn(right_panel),
            FadeIn(ground),
            FadeIn(block),
            FadeIn(block_label),
            FadeIn(displacement_arrow),
            FadeIn(displacement_label),
            FadeIn(force_arrow),
            FadeIn(force_label),
            FadeIn(proj_arrow),
            FadeIn(proj_label),
            FadeIn(theta_arc),
            FadeIn(theta_label),
            FadeIn(formula),
            FadeIn(bullet_1),
            FadeIn(bullet_2),
            FadeIn(bullet_3),
            FadeIn(bullet_4),
            FadeIn(trap_box),
            FadeIn(trap_title),
        )

        self.wait(2.5)
