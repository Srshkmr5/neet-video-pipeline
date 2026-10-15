"""
Draft Template: ModernArcVisualizer
Synthesized from reference video by Reference Analyzer.
Aspect Ratio: 16:9 (Landscape)
"""

from manim import *
import numpy as np
from render.templates.base import BaseNeetScene, TEXT_WHITE, MUTED_TEXT

# Extracted Visual Style
PALETTE = {
    "bg": "#0C0F16",
    "text": "#F5F5F5",
    "accent_1": "#38BDF8",
    "accent_2": "#F59E0B",
    "accent_3": "#10B981",
}

class ModernArcVisualizerScene(BaseNeetScene):
    def render_concept_beats(self):
        # 1. Custom Background Theme Override
        self.camera.background_color = PALETTE["bg"]
        
        # 2. Dynamic Visual Elements
        formula_str = self.parameters.get("latexFormula", r"v^2 = u^2 + 2as")
        plain_formula = self.parameters.get("plainFormula", "v^2 = u^2 + 2as")
        trap_text = self.parameters.get("trapWarning", "Pay close attention to vector direction & signs!")

        # --- BEAT 1: SETTLE ---
        settle_text = Text(self.serial_title, font_size=26, weight=BOLD, color=PALETTE["accent_1"])
        settle_text.move_to(ORIGIN + UP * 0.5)
        self.play(FadeIn(settle_text), run_time=1.5)
        self.wait(1.0)
        self.play(FadeOut(settle_text), run_time=0.8)

        # --- BEAT 2: CONTEXT / GRAPH SETUP ---
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6.5,
            y_length=3.8,
            axis_config={"color": MUTED_TEXT, "stroke_width": 2}
        ).to_edge(DOWN, buff=1.2)
        
        self.play(Create(axes), run_time=1.5)

        # --- BEAT 3: CRITICAL CONCEPT & MOTION ARC ---
        formula = self.create_formula_mobject(formula_str, plain_formula, font_size=38, color_val=PALETTE["accent_2"]).to_edge(UP, buff=1.2)
        self.play(Write(formula), run_time=1.8)

        # Reference-inspired motion curve & particle
        curve = axes.plot(lambda x: 1.5 * np.sin(x), color=PALETTE["accent_3"])
        dot = Dot(color=PALETTE["accent_1"], radius=0.1).move_to(axes.c2p(-2.5, 1.5 * np.sin(-2.5)))
        
        self.play(Create(curve), run_time=1.5)
        self.play(MoveAlongPath(dot, curve), run_time=2.5, rate_func=linear)

        # --- BEAT 4: NEET TRAP CALLOUT ---
        trap_box = Rectangle(
            width=9.5, height=1.1,
            fill_color="#18181B", fill_opacity=0.92,
            stroke_color=PALETTE["accent_1"], stroke_width=2
        ).to_edge(DOWN, buff=0.8)
        warning_icon = Text("⚠️ NEET TRAP:", font_size=16, weight=BOLD, color=PALETTE["accent_1"]).next_to(trap_box.get_left(), RIGHT, buff=0.3)
        trap_msg = Text(trap_text[:65], font_size=15, color=TEXT_WHITE).next_to(warning_icon, RIGHT, buff=0.2)
        trap_group = VGroup(trap_box, warning_icon, trap_msg)

        self.play(FadeIn(trap_group, shift=UP * 0.2), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(trap_group), run_time=0.8)

        # --- BEAT 5: CAPSULE SUMMARY ---
        self.wait(1.5)

        # --- BEAT 6: RELEASE / UP NEXT TEASER ---
        self.render_release_teaser(duration=3.5)
