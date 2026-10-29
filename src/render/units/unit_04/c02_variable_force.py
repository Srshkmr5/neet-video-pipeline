from manim import *
import numpy as np

Text.set_default(font="Arial")
config.background_color = "#020B16"


class C02VariableForceScene(Scene):
    def construct(self):
        bg = "#020B16"
        panel = "#0F172A"
        accent_blue = "#7DD3FC"
        accent_gold = "#FBBF24"
        accent_green = "#34D399"
        accent_red = "#F87171"
        text_white = "#E2E8F0"
        muted = "#94A3B8"

        self.camera.background_color = bg

        header = Text(
            "Work, Energy & Power",
            font="Arial",
            font_size=18,
            color=muted
        ).to_edge(UP, buff=0.6).to_edge(LEFT, buff=0.9)

        title = Text(
            "Work Done by Variable Force and F-x Area",
            font="Arial",
            font_size=28,
            color=accent_blue,
            weight="BOLD"
        ).next_to(header, DOWN, buff=0.12).align_to(header, LEFT)

        subtitle = Text(
            "NCERT Class 11 Physics Part 1 • Chapter 5 • Section 5.4",
            font="Arial",
            font_size=15,
            color=accent_gold
        ).next_to(title, DOWN, buff=0.08).align_to(title, LEFT)

        main_box = RoundedRectangle(
            width=11.6,
            height=5.2,
            corner_radius=0.12,
            stroke_color=accent_blue,
            stroke_width=1.4,
            fill_color=panel,
            fill_opacity=0.85
        ).move_to(DOWN * 0.12)

        left_panel = RoundedRectangle(
            width=5.2,
            height=3.5,
            corner_radius=0.10,
            stroke_color="#334155",
            stroke_width=1.2,
            fill_color="#101B2A",
            fill_opacity=0.9
        ).move_to(LEFT * 2.3)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=4.0,
            y_length=2.2,
            axis_config={"color": "#64748B", "stroke_width": 2},
            tips=True
        ).move_to(LEFT * 2.2 + DOWN * 0.15)

        curve = axes.plot(
            lambda x: 1.0 + 1.8 * np.sin(x * 0.7) + 0.15 * x,
            color=accent_blue,
            stroke_width=3
        )

        shaded = axes.get_area(
            curve,
            x_range=[1.0, 5.0],
            color=accent_green,
            opacity=0.35
        )

        x_label = Text("x (m)", font="Arial", font_size=12, color=muted).next_to(axes.x_axis.get_end(), DOWN, buff=0.08)
        y_label = Text("F (N)", font="Arial", font_size=12, color=muted).next_to(axes.y_axis.get_end(), LEFT, buff=0.08)
        area_label = Text("Area = Work W", font="Arial", font_size=14, color=accent_gold, weight="BOLD").move_to(axes.c2p(3.2, 1.6))

        right_panel = RoundedRectangle(
            width=5.0,
            height=3.4,
            corner_radius=0.10,
            stroke_color=accent_gold,
            stroke_width=1.2,
            fill_color="#101B2A",
            fill_opacity=0.9
        ).move_to(RIGHT * 2.7)

        formula = Text(
            "W = ∫ F(x) dx  (from x_i to x_f)",
            font="Arial",
            font_size=20,
            weight="BOLD",
            color=accent_gold
        ).move_to(right_panel.get_center() + UP * 0.8)

        bullet_1 = Text(
            "• Work is the signed area under the F-x curve",
            font="Arial",
            font_size=12.5,
            color=text_white
        ).next_to(formula, DOWN, buff=0.30).align_to(right_panel, LEFT).shift(RIGHT * 0.25)

        bullet_2 = Text(
            "• Above axis is positive work; below axis is negative work",
            font="Arial",
            font_size=12.5,
            color=accent_green
        ).next_to(bullet_1, DOWN, buff=0.12).align_to(bullet_1, LEFT)

        bullet_3 = Text(
            "• Net work is total signed area under the curve",
            font="Arial",
            font_size=12.5,
            color=accent_blue
        ).next_to(bullet_2, DOWN, buff=0.12).align_to(bullet_2, LEFT)

        trap_box = RoundedRectangle(
            width=10.2,
            height=0.8,
            corner_radius=0.08,
            stroke_color=accent_red,
            stroke_width=1.5,
            fill_color="#1A0B0E",
            fill_opacity=0.9
        ).move_to(DOWN * 2.0)

        trap_text = Text(
            "NEET TRAP: work is not just magnitude; it is signed area",
            font="Arial",
            font_size=14,
            color=accent_red,
            weight="BOLD"
        ).move_to(trap_box.get_center())

        self.play(
            FadeIn(header),
            FadeIn(title),
            FadeIn(subtitle),
            FadeIn(main_box),
            FadeIn(left_panel),
            FadeIn(axes),
            FadeIn(curve),
            FadeIn(shaded),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(area_label),
            FadeIn(right_panel),
            FadeIn(formula),
            FadeIn(bullet_1),
            FadeIn(bullet_2),
            FadeIn(bullet_3),
            FadeIn(trap_box),
            FadeIn(trap_text),
        )

        self.wait(2.8)
