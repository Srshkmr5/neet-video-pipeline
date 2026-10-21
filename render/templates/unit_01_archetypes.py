"""
Dedicated Visual Archetypes for Unit 1: Physics and Measurement
NCERT Class 11 Physics Part 1, Chapter 2 (Units and Measurements)

Provides modular build_beat_1(), build_beat_2(), build_beat_3(), build_beat_4()
for instant static screenshot verification and broadcast video animation.
"""

from manim import *
from render.templates.base import (
    FONT_HEADER, FONT_CARD, FONT_BODY,
    BaseNeetScene, BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN,
    TEXT_WHITE, MUTED_TEXT, FONT_PRIMARY, FONT_MONO
)

Text.set_default(font=FONT_BODY)

class ModularUnit1Scene(BaseNeetScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header_font = FONT_HEADER
        self.card_font = FONT_CARD
        self.body_font = FONT_BODY
        self.topic_font = FONT_HEADER

    def render_concept_beats(self):
        b1 = self.build_beat_1()
        self.play(FadeIn(b1, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(b1), run_time=0.8)

        b2 = self.build_beat_2()
        self.play(FadeIn(b2), run_time=1.2)
        self.wait(3.0)
        self.play(FadeOut(b2), run_time=0.8)

        b3 = self.build_beat_3()
        self.play(FadeIn(b3), run_time=1.2)
        self.wait(3.0)
        self.play(FadeOut(b3), run_time=0.8)

        b4 = self.build_beat_4()
        self.play(FadeIn(b4), run_time=1.0)
        self.wait(3.5)


# ---------------------------------------------------------------------------
# 1. BaseQuantitiesTable7Scene (P11-C01-T01-V01)
# ---------------------------------------------------------------------------
class BaseQuantitiesTable7Scene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("SI Base Quantities & Supplementary Units", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 16-18 (Table 2.1)", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        hud_box = RoundedRectangle(corner_radius=0.1, height=0.95, width=5.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).to_corner(UL, buff=1.0).shift(DOWN * 0.3)
        hud_title = Text("INTERNATIONAL SYSTEM OF UNITS (SI)", font_size=11, weight="BOLD", color=self.muted_text).next_to(hud_box.get_top(), DOWN, buff=0.10)
        hud_sub = Text("The 7 Fundamental Base Quantities & 2 Supplementary Units", font_size=10, weight="BOLD", color=self.accent_gold).next_to(hud_title, DOWN, buff=0.10)
        hud_group = VGroup(hud_box, hud_title, hud_sub)

        tbl_box = RoundedRectangle(corner_radius=0.08, height=3.2, width=5.8, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(LEFT * 3.1 + UP * 0.45)
        tbl_hdr = Text("7 FUNDAMENTAL SI BASE QUANTITIES", font_size=12, weight="BOLD", color=self.accent_gold).next_to(tbl_box.get_top(), DOWN, buff=0.14)
        col_hdr = Text("Physical Quantity       | SI Unit (Symbol) | Dim", font_size=10, weight="BOLD", color=self.accent_blue).next_to(tbl_hdr, DOWN, buff=0.10, aligned_edge=LEFT).shift(RIGHT * 0.2)
        div_line = Line(start=LEFT * 5.8 + UP * 1.35, end=LEFT * 0.4 + UP * 1.35, color=self.muted_text, stroke_width=1.0)

        row_items = [
            ("1. Length", "metre (m)", "[L]"),
            ("2. Mass", "kilogram (kg)", "[M]"),
            ("3. Time", "second (s)", "[T]"),
            ("4. Electric Current", "ampere (A)", "[A]"),
            ("5. Thermodynamic Temp", "kelvin (K)", "[K]"),
            ("6. Amount of Substance", "mole (mol)", "[mol]"),
            ("7. Luminous Intensity", "candela (cd)", "[cd]")
        ]
        rows_vgroup = VGroup()
        for q, u, d in row_items:
            r_txt = Text(f"{q:<24} | {u:<16} | {d}", font=self.body_font, font_size=10, color=TEXT_WHITE)
            rows_vgroup.add(r_txt)
        rows_vgroup.arrange(DOWN, buff=0.09, aligned_edge=LEFT).next_to(div_line, DOWN, buff=0.09).shift(RIGHT * 0.15)
        table_group = VGroup(tbl_box, tbl_hdr, col_hdr, div_line, rows_vgroup)

        supp_box = RoundedRectangle(corner_radius=0.08, height=1.1, width=5.8, stroke_color=self.accent_green, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(LEFT * 3.1 + DOWN * 1.85)
        supp_hdr = Text("2 Supplementary Units (Dimensionless: [M⁰ L⁰ T⁰]):", font_size=11, weight="BOLD", color=self.accent_green).next_to(supp_box.get_top(), DOWN, buff=0.10)
        supp_r1 = Text("• Plane Angle:  dθ = ds / r   ==> Unit: Radian (rad)", font_size=10, color=TEXT_WHITE).next_to(supp_hdr, DOWN, buff=0.06, aligned_edge=LEFT).shift(RIGHT * 0.2)
        supp_r2 = Text("• Solid Angle:  dΩ = dA / r²  ==> Unit: Steradian (sr)", font_size=10, color=TEXT_WHITE).next_to(supp_r1, DOWN, buff=0.05, aligned_edge=LEFT)
        supp_group = VGroup(supp_box, supp_hdr, supp_r1, supp_r2)

        return VGroup(hud_group, table_group, supp_group)

    def build_beat_3(self):
        card_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        card_title = Text("CORE PRINCIPLES OF THE SI SYSTEM", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).next_to(card_box.get_top(), DOWN, buff=0.25)

        p1_title = Text("1. Mutual Independence of Base Quantities", font_size=13, weight="BOLD", color=self.accent_blue).next_to(card_title, DOWN, buff=0.25, aligned_edge=LEFT).shift(RIGHT * 0.4)
        p1_desc = Text("   • None of the 7 base quantities can be derived from or resolved into any other.", font_size=12, color=TEXT_WHITE).next_to(p1_title, DOWN, buff=0.07, aligned_edge=LEFT)
        p1_sub = Text("   • They serve as the irreducible standards of modern measurement.", font_size=11, color=self.muted_text).next_to(p1_desc, DOWN, buff=0.05, aligned_edge=LEFT)

        p2_title = Text("2. Universal Foundation for All Derived Units", font_size=13, weight="BOLD", color=self.accent_blue).next_to(p1_sub, DOWN, buff=0.18, aligned_edge=LEFT)
        p2_desc = Text("   • All other physical quantities (Force, Energy, Pressure, etc.) are combinations", font_size=12, color=TEXT_WHITE).next_to(p2_title, DOWN, buff=0.07, aligned_edge=LEFT)
        p2_sub = Text("     of these 7 base standards (e.g. 1 N = 1 kg·m·s⁻²).", font_size=11, color=self.accent_green).next_to(p2_desc, DOWN, buff=0.05, aligned_edge=LEFT)

        p3_title = Text("3. Supplementary Units (Radian & Steradian)", font_size=13, weight="BOLD", color=self.accent_blue).next_to(p2_sub, DOWN, buff=0.18, aligned_edge=LEFT)
        p3_desc = Text("   • Pure geometric ratios: Arc/Radius (m/m) and Area/Radius² (m²/m²).", font_size=12, color=TEXT_WHITE).next_to(p3_title, DOWN, buff=0.07, aligned_edge=LEFT)
        p3_sub = Text("   • Unique status: Possess SI units (rad, sr) but strictly ZERO dimensions ([M⁰ L⁰ T⁰]).", font_size=11, color=self.accent_gold).next_to(p3_desc, DOWN, buff=0.05, aligned_edge=LEFT)

        return VGroup(card_box, card_title, p1_title, p1_desc, p1_sub, p2_title, p2_desc, p2_sub, p3_title, p3_desc, p3_sub)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)
        
        lines = [
            Text("1. Common Trap: Assuming all quantities with physical units must have dimensions.", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Reality: Radian & Steradian possess SI units but ZERO dimensions ([M⁰ L⁰ T⁰]).", font=self.body_font, font_size=11, color=self.accent_green),
            Text("2. Golden Rule (H.C. Verma):", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   A physical quantity CAN possess units without dimensions (rad, sr),", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("   but NO physical quantity can EVER possess dimensions without units!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.14, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.22)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 2. DerivedUnitsAlgebraicLadderScene (P11-C01-T01-V02)
# ---------------------------------------------------------------------------
class DerivedUnitsAlgebraicLadderScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Derived Units & Standard Metric Prefixes", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 17-20", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        ladder_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        ladder_title = Text("THE ALGEBRAIC LADDER OF DERIVED UNITS", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).next_to(ladder_box.get_top(), DOWN, buff=0.22)

        step1 = Text("Step 1 (Speed):      v = distance / time       ==>  [m] / [s]  =  m · s⁻¹", font=self.body_font, font_size=12, color=TEXT_WHITE)
        step2 = Text("Step 2 (Accel):      a = Δv / Δt               ==>  [m · s⁻¹] / [s]  =  m · s⁻²", font=self.body_font, font_size=12, color=TEXT_WHITE)
        step3 = Text("Step 3 (Force):      F = m · a                 ==>  [kg] · [m · s⁻²]  =  1 Newton (N)", font=self.body_font, font_size=12, color=self.accent_green)
        step4 = Text("Step 4 (Work/Energy): W = F · d                ==>  [N] · [m] = kg · m² · s⁻²  =  1 Joule (J)", font=self.body_font, font_size=12, color=self.accent_green)
        step5 = Text("Step 5 (Pressure):   P = F / Area              ==>  [N] / [m²] = kg · m⁻¹ · s⁻²  =  1 Pascal (Pa)", font=self.body_font, font_size=12, color=self.accent_green)
        
        ladder_steps = VGroup(step1, step2, step3, step4, step5).arrange(DOWN, buff=0.20, aligned_edge=LEFT).next_to(ladder_title, DOWN, buff=0.25).shift(LEFT * 0.5)
        return VGroup(ladder_box, ladder_title, ladder_steps)

    def build_beat_3(self):
        pfx_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        pfx_title = Text("STANDARD SI METRIC PREFIXES (POWERS OF 10)", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).next_to(pfx_box.get_top(), DOWN, buff=0.22)

        col1_hdr = Text("SUB-MULTIPLES (SMALL)", font_size=13, weight="BOLD", color=self.accent_blue).move_to(LEFT * 3.0 + UP * 0.9)
        col1_items = [
            "10⁻¹⁵ : femto (f)", "10⁻¹² : pico  (p)", "10⁻⁹  : nano  (n)",
            "10⁻⁶  : micro (μ)", "10⁻³  : milli (m)", "10⁻²  : centi (c)"
        ]
        col1_vg = VGroup(*[Text(it, font=self.body_font, font_size=11, color=TEXT_WHITE) for it in col1_items]).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(col1_hdr, DOWN, buff=0.15)

        div = Line(start=UP * 1.3, end=DOWN * 1.6, color=self.muted_text, stroke_width=1.0)

        col2_hdr = Text("MULTIPLES (LARGE)", font_size=13, weight="BOLD", color=self.accent_gold).move_to(RIGHT * 3.0 + UP * 0.9)
        col2_items = [
            "10³   : kilo  (k)", "10⁶   : mega  (M)", "10⁹   : giga  (G)",
            "10¹²  : tera  (T)", "10¹⁵  : peta  (P)", "10¹⁸  : exa   (E)"
        ]
        col2_vg = VGroup(*[Text(it, font=self.body_font, font_size=11, color=TEXT_WHITE) for it in col2_items]).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(col2_hdr, DOWN, buff=0.15)

        return VGroup(pfx_box, pfx_title, col1_hdr, col1_vg, div, col2_hdr, col2_vg)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. Strict SI Rule: Double prefixes are FORBIDDEN (D.C. Pandey).", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   WRONG: 1 μμF (micro-microfarad)   ===>   CORRECT: 1 pF (picofarad)", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("2. The Kilogram Trap:", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Since 'kg' already contains 'kilo', prefixes must be attached to 'gram'!", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   For 10⁻⁶ kg, do NOT write 1 μkg. Write 1 mg (milligram).", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.14, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.22)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 3. DimensionEquivalenceMatrixScene (P11-C01-T02-V03)
# ---------------------------------------------------------------------------
class DimensionEquivalenceMatrixScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Dimensions of Physical Quantities & Common Equivalences", font=self.header_font, font_size=30, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 22-24", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        mat_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        mat_title = Text("HIGH-FREQUENCY DIMENSIONAL EQUIVALENCES (NEET PYQ)", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).next_to(mat_box.get_top(), DOWN, buff=0.22)

        g1 = Text("• [M L² T⁻¹]  :  Planck's Constant (h)  =  Angular Momentum (L)", font=self.body_font, font_size=12, color=TEXT_WHITE)
        g2 = Text("• [M L⁻¹ T⁻²] :  Pressure  =  Stress  =  Modulus of Elasticity  =  Energy Density", font=self.body_font, font_size=12, color=self.accent_green)
        g3 = Text("• [M L² T⁻²]  :  Work  =  Kinetic Energy  =  Potential Energy  =  Torque (τ)", font=self.body_font, font_size=12, color=TEXT_WHITE)
        g4 = Text("• [M⁰ L⁰ T⁻¹] :  Frequency  =  Angular Velocity (ω)  =  Velocity Gradient  =  Decay Constant (λ)", font=self.body_font, font_size=12, color=self.accent_green)
        g5 = Text("• [M⁰ L⁰ T¹]  :  Time Constant: RC  =  L / R  =  √(LC)", font=self.body_font, font_size=12, color=self.accent_gold)

        matrix_rows = VGroup(g1, g2, g3, g4, g5).arrange(DOWN, buff=0.20, aligned_edge=LEFT).next_to(mat_title, DOWN, buff=0.25).shift(LEFT * 0.2)
        return VGroup(mat_box, mat_title, matrix_rows)

    def build_beat_3(self):
        comp_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        comp_title = Text("CRUCIAL DISTINCTION: IDENTICAL DIMENSIONS ≠ IDENTICAL NATURE", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).next_to(comp_box.get_top(), DOWN, buff=0.22)

        c1 = Text("Case Study: Work vs. Torque (Halliday & Resnick)", font_size=14, weight="BOLD", color=self.accent_blue).next_to(comp_title, DOWN, buff=0.30, aligned_edge=LEFT).shift(RIGHT * 0.4)
        c2 = Text("• Both possess identical dimensions: [M L² T⁻²]", font_size=13, color=TEXT_WHITE).next_to(c1, DOWN, buff=0.10, aligned_edge=LEFT)
        c3 = Text("• WORK is a SCALAR quantity (Dot Product: W = F · d). Unit: Joule (J)", font_size=13, color=self.accent_green).next_to(c2, DOWN, buff=0.12, aligned_edge=LEFT)
        c4 = Text("• TORQUE is a VECTOR quantity (Cross Product: τ = r × F). Unit: N · m (NEVER Joules!)", font_size=13, color=self.accent_gold).next_to(c3, DOWN, buff=0.12, aligned_edge=LEFT)
        c5 = Text("• Rule: Never express Torque in Joules, even though the base units match.", font_size=12, weight="BOLD", color=self.muted_text).next_to(c4, DOWN, buff=0.12, aligned_edge=LEFT)

        return VGroup(comp_box, comp_title, c1, c2, c3, c4, c5)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. Common Trap: Assuming physical quantities sharing dimensions can be added.", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Reality: You CANNOT add Work and Torque together (Scalar + Vector is invalid!).", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("2. Dimensionless Constant Trap:", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Refractive index, relative permittivity, and strain are dimensionless.", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   Formula: [M⁰ L⁰ T⁰]  ===>  They have neither dimensions NOR physical units!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.14, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.22)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 4. HomogeneityVanDerWaalsScene (P11-C01-T02-V04)
# ---------------------------------------------------------------------------
class HomogeneityVanDerWaalsScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Principle of Homogeneity of Dimensions", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 24-26", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        vdw_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        vdw_title = Text("VAN DER WAALS EQUATION: HOMOGENEITY IN ACTION (NEET CLASSIC)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).next_to(vdw_box.get_top(), DOWN, buff=0.22)

        eq_txt = Text("( P  +  a / V² ) ( V  -  b )  =  R · T", font=self.body_font, font_size=22, weight="BOLD", color=self.accent_blue).next_to(vdw_title, DOWN, buff=0.30)

        step1 = Text("1. Addition Rule: Only terms of identical dimensions can be added together.", font_size=12, color=TEXT_WHITE)
        step2 = Text("   ==> [a / V²]  =  [P]  (Pressure)", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)
        step3 = Text("   ==> [a]  =  [P] · [V²]  =  [M L⁻¹ T⁻²] · [L³]²  =  [M L⁵ T⁻²]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
        step4 = Text("2. Subtraction Rule: [b]  =  [V]  (Volume)  ==>  [b]  =  [L³]", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)

        breakdown_vg = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(eq_txt, DOWN, buff=0.25).shift(LEFT * 0.3)
        return VGroup(vdw_box, vdw_title, eq_txt, breakdown_vg)

    def build_beat_3(self):
        func_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        func_title = Text("HOMOGENEITY RULE FOR TRANSCENDENTAL FUNCTIONS", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).next_to(func_box.get_top(), DOWN, buff=0.22)

        r1 = Text("Golden Rule: Arguments of trigonometric, exponential, and logarithmic functions", font_size=13, weight="BOLD", color=TEXT_WHITE).next_to(func_title, DOWN, buff=0.30, aligned_edge=LEFT).shift(RIGHT * 0.4)
        r2 = Text("MUST ALWAYS BE PURE NUMBERS (DIMENSIONLESS: [M⁰ L⁰ T⁰]).", font_size=13, weight="BOLD", color=self.accent_green).next_to(r1, DOWN, buff=0.08, aligned_edge=LEFT)

        ex1 = Text("Example: In  y = A · sin(ωt - kx) :", font=self.body_font, font_size=13, color=self.accent_blue).next_to(r2, DOWN, buff=0.25, aligned_edge=LEFT)
        ex2 = Text("• [ωt] = [M⁰ L⁰ T⁰]   ==>   [ω] = [1 / t] = [T⁻¹]", font=self.body_font, font_size=12, color=TEXT_WHITE).next_to(ex1, DOWN, buff=0.10, aligned_edge=LEFT)
        ex3 = Text("• [kx] = [M⁰ L⁰ T⁰]   ==>   [k] = [1 / x] = [L⁻¹]", font=self.body_font, font_size=12, color=TEXT_WHITE).next_to(ex2, DOWN, buff=0.08, aligned_edge=LEFT)
        ex4 = Text("• [A]  = [y]          ==>   Amplitude shares the dimension of displacement [L]", font=self.body_font, font_size=12, color=self.accent_gold).next_to(ex3, DOWN, buff=0.08, aligned_edge=LEFT)

        return VGroup(func_box, func_title, r1, r2, ex1, ex2, ex3, ex4)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. Common Trap: Assuming dimensional consistency proves an equation is correct.", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Reality: Equation can be dimensionally valid but wrong: e.g. s = ut + at².", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("2. Blindness to Dimensionless Constants (H.C. Verma):", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Dimensional analysis can NEVER determine pure coefficients (like 1/2, 2π).", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   It only checks the dimensional power balance, never the numerical magnitude!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.14, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.22)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 5. MeasurementErrorDistributionScene (P11-C01-T03-V05)
# ---------------------------------------------------------------------------
class MeasurementErrorDistributionScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Classification of Errors & Mean Absolute Error", font=self.header_font, font_size=32, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 20-22", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        tax_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        tax_title = Text("TAXONOMY OF EXPERIMENTAL MEASUREMENT ERRORS", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).next_to(tax_box.get_top(), DOWN, buff=0.22)

        c1_box = RoundedRectangle(corner_radius=0.08, height=3.0, width=5.4, stroke_color=self.accent_blue, stroke_width=1.2, fill_color="#0F172A", fill_opacity=0.0).move_to(LEFT * 2.9 + DOWN * 0.3)
        c1_hdr = Text("SYSTEMATIC ERRORS (UNIDIRECTIONAL)", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_blue).next_to(c1_box.get_top(), DOWN, buff=0.14)
        c1_t1 = Text("• Constant bias in ONE direction (+ or -)", font=self.body_font, font_size=11, color=TEXT_WHITE)
        c1_t2 = Text("• Sources: Instrumental (zero error),", font=self.body_font, font_size=11, color=TEXT_WHITE)
        c1_t3 = Text("  imperfection in technique, personal bias", font=self.body_font, font_size=11, color=TEXT_WHITE)
        c1_t4 = Text("• Remedy: Re-calibration of apparatus", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green)
        c1_vg = VGroup(c1_t1, c1_t2, c1_t3, c1_t4).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(c1_hdr, DOWN, buff=0.18)

        c2_box = RoundedRectangle(corner_radius=0.08, height=3.0, width=5.4, stroke_color=self.accent_gold, stroke_width=1.2, fill_color="#0F172A", fill_opacity=0.0).move_to(RIGHT * 2.9 + DOWN * 0.3)
        c2_hdr = Text("RANDOM ERRORS (GAUSSIAN FLUCTUATIONS)", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_gold).next_to(c2_box.get_top(), DOWN, buff=0.14)
        c2_t1 = Text("• Unpredictable variations in sign & size", font=self.body_font, font_size=11, color=TEXT_WHITE)
        c2_t2 = Text("• Sources: Uncontrolled ambient temp, line", font=self.body_font, font_size=11, color=TEXT_WHITE)
        c2_t3 = Text("  voltage swings, mechanical vibrations", font=self.body_font, font_size=11, color=TEXT_WHITE)
        c2_t4 = Text("• Remedy: Arithmetic mean of N readings", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green)
        c2_vg = VGroup(c2_t1, c2_t2, c2_t3, c2_t4).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(c2_hdr, DOWN, buff=0.18)

        return VGroup(tax_box, tax_title, c1_box, c1_hdr, c1_vg, c2_box, c2_hdr, c2_vg)

    def build_beat_3(self):
        stat_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        stat_title = Text("MATHEMATICAL FORMULATION OF ERRORS (NCERT SECTION 2.6)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).next_to(stat_box.get_top(), DOWN, buff=0.22)

        m1 = Text("1. Arithmetic Mean (Best Estimate):      a_mean = ( Σ a_i ) / n", font=self.body_font, font_size=13, weight="BOLD", color=TEXT_WHITE)
        m2 = Text("2. Absolute Error of Reading i:          Δa_i = | a_mean - a_i |   (ALWAYS POSITIVE)", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)
        m3 = Text("3. Mean Absolute Error:                  Δa_mean = ( Σ |Δa_i| ) / n", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green)
        m4 = Text("4. Relative (Fractional) Error:          Δa_mean / a_mean", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)
        m5 = Text("5. Percentage Error (δa):                ( Δa_mean / a_mean ) × 100 %", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)

        stat_vg = VGroup(m1, m2, m3, m4, m5).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(stat_title, DOWN, buff=0.25).shift(LEFT * 0.3)
        return VGroup(stat_box, stat_title, stat_vg)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. The Zero Sum Trap (H.C. Verma Classic):", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   The algebraic sum of deviations from arithmetic mean is IDENTICALLY ZERO:", font=self.body_font, font_size=11, color=TEXT_WHITE),
            Text("   Σ (a_mean - a_i) = 0   ===> NEVER use signed deviations for mean error!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold),
            Text("2. Absolute Error Magnitude Rule:", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   You MUST take the absolute magnitude |Δa_i| before taking the arithmetic mean.", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   Absolute error is non-negative by definition (Δa_mean > 0).", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.20)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 6. PowerRuleCalculationTreeScene (P11-C01-T03-V06)
# ---------------------------------------------------------------------------
class PowerRuleCalculationTreeScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Combination & Propagation of Errors (Power Rule)", font=self.header_font, font_size=30, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 22-24", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        pwr_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        pwr_title = Text("THE MASTER POWER RULE FOR RELATIVE ERROR (WORST CASE)", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).next_to(pwr_box.get_top(), DOWN, buff=0.22)

        t_if = Text("If   Z  =  ( ", font=self.body_font, font_size=20, weight="BOLD", color=self.accent_blue)
        t_a = Text("A", font=self.body_font, font_size=20, weight="BOLD", color=self.accent_blue)
        t_p = Text("p", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(t_a, UR, buff=0.04).shift(DOWN * 0.08)
        t_dot = Text(" · ", font=self.body_font, font_size=20, weight="BOLD", color=self.accent_blue).next_to(t_p, RIGHT, buff=0.08)
        t_b = Text("B", font=self.body_font, font_size=20, weight="BOLD", color=self.accent_blue).next_to(t_dot, RIGHT, buff=0.08)
        t_q = Text("q", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(t_b, UR, buff=0.04).shift(DOWN * 0.08)
        t_div = Text(" ) / ", font=self.body_font, font_size=20, weight="BOLD", color=self.accent_blue).next_to(t_q, RIGHT, buff=0.08)
        t_c = Text("C", font=self.body_font, font_size=20, weight="BOLD", color=self.accent_blue).next_to(t_div, RIGHT, buff=0.08)
        t_r = Text("r", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_blue).next_to(t_c, UR, buff=0.04).shift(DOWN * 0.08)
        gen_eq = VGroup(t_if, t_a, t_p, t_dot, t_b, t_q, t_div, t_c, t_r).arrange(RIGHT, buff=0.03).next_to(pwr_title, DOWN, buff=0.25)
        
        prop_eq = Text("==>   ΔZ / Z  =  p · ( ΔA / A )  +  q · ( ΔB / B )  +  r · ( ΔC / C )", font=self.body_font, font_size=16, weight="BOLD", color=self.accent_green).next_to(gen_eq, DOWN, buff=0.25)

        note1 = Text("Key Principle: The relative error of a physical quantity raised to power 'p'", font_size=12, color=TEXT_WHITE).next_to(prop_eq, DOWN, buff=0.30)
        note2 = Text("is 'p' times the relative error of the individual quantity.", font_size=12, color=TEXT_WHITE).next_to(note1, DOWN, buff=0.06)

        return VGroup(pwr_box, pwr_title, gen_eq, prop_eq, note1, note2)

    def build_beat_3(self):
        tree_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        tree_title = Text("NUMERICAL STEP TREE: NEET FREQUENT PYQ PATTERN", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).next_to(tree_box.get_top(), DOWN, buff=0.22)

        prob = Text("Given: Z = ( A⁴ · B¹/³ ) / ( C · D³/² ), with errors: A=1%, B=3%, C=2%, D=4%", font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(tree_title, DOWN, buff=0.25)
        
        step_a = Text("• Contribution from A: 4 × (1%)          =  4.0%", font=self.body_font, font_size=12, color=self.accent_blue)
        step_b = Text("• Contribution from B: (1/3) × (3%)      =  1.0%", font=self.body_font, font_size=12, color=self.accent_blue)
        step_c = Text("• Contribution from C: 1 × (2%)          =  2.0%   (Added, NOT subtracted!)", font=self.body_font, font_size=12, color=self.accent_green)
        step_d = Text("• Contribution from D: (3/2) × (4%)      =  6.0%   (Added, NOT subtracted!)", font=self.body_font, font_size=12, color=self.accent_green)
        step_tot = Text("TOTAL MAXIMUM PERCENTAGE ERROR  =  4 + 1 + 2 + 6  =  13.0%", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold)

        calc_vg = VGroup(step_a, step_b, step_c, step_d, step_tot).arrange(DOWN, buff=0.14, aligned_edge=LEFT).next_to(prob, DOWN, buff=0.20).shift(LEFT * 0.4)
        return VGroup(tree_box, tree_title, prob, calc_vg)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. The Denominator Subtraction Trap (D.C. Pandey):", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Students see C in denominator and subtract: - r · (ΔC / C).", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("   FATAL ERROR! In worst-case analysis, ERRORS ALWAYS ACCUMULATE (ADD)!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_red),
            Text("2. Dominant Contributor Rule:", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   The quantity with the HIGHEST power coefficient dominates total uncertainty.", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   It must always be measured with the highest precision instrument!", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.20)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 7. VernierDualScaleVisualizerScene (P11-C01-T04-V07)
# ---------------------------------------------------------------------------
class VernierDualScaleVisualizerScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Measuring Instruments: Vernier Callipers & Screw Gauge", font=self.header_font, font_size=28, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2 Appendix & Lab Manual", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        v_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        v_title = Text("VERNIER CALLIPERS: PRINCIPLE & LEAST COUNT", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_gold).next_to(v_box.get_top(), DOWN, buff=0.22)

        f1 = Text("Principle: n divisions on Vernier Scale (VSD) = (n - 1) divisions on Main Scale (MSD)", font_size=12, color=TEXT_WHITE).next_to(v_title, DOWN, buff=0.25)
        f2 = Text("Least Count (Vernier Constant):   LC = 1 MSD - 1 VSD = ( 1 / n ) · MSD", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(f1, DOWN, buff=0.18)
        f3 = Text("Standard Case: 10 VSD = 9 MSD (where 1 MSD = 1 mm):", font_size=12, color=self.accent_blue).next_to(f2, DOWN, buff=0.20, aligned_edge=LEFT).shift(RIGHT * 1.5)
        f4 = Text("==> LC = 1 mm - (9/10) mm = 0.1 mm = 0.01 cm", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold).next_to(f3, DOWN, buff=0.10, aligned_edge=LEFT)
        f5 = Text("Total Reading  =  Main Scale Reading (MSR)  +  ( Coinciding VSD × LC )", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE).next_to(f4, DOWN, buff=0.18, aligned_edge=LEFT)

        return VGroup(v_box, v_title, f1, f2, f3, f4, f5)

    def build_beat_3(self):
        sg_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        sg_title = Text("SCREW GAUGE: PITCH & CIRCULAR SCALE LEAST COUNT", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).next_to(sg_box.get_top(), DOWN, buff=0.22)

        s1 = Text("• Pitch: Distance moved by screw on linear scale per 1 complete rotation (e.g. 1 mm)", font_size=12, color=TEXT_WHITE).next_to(sg_title, DOWN, buff=0.30, aligned_edge=LEFT).shift(RIGHT * 0.4)
        s2 = Text("• Least Count Formula:   LC = Pitch / ( Total Circular Divisions )", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_green).next_to(s1, DOWN, buff=0.15, aligned_edge=LEFT)
        s3 = Text("  Example: Pitch = 1 mm, Circular Divisions = 100", font_size=12, color=self.accent_blue).next_to(s2, DOWN, buff=0.15, aligned_edge=LEFT)
        s4 = Text("  ==> LC = 1 mm / 100 = 0.01 mm = 0.001 cm", font=self.body_font, font_size=13, weight="BOLD", color=self.accent_gold).next_to(s3, DOWN, buff=0.08, aligned_edge=LEFT)
        s5 = Text("• Total Reading = Linear Scale (PSR) + ( Coinciding CSR × LC ) - Zero Error", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE).next_to(s4, DOWN, buff=0.20, aligned_edge=LEFT)

        return VGroup(sg_box, sg_title, s1, s2, s3, s4, s5)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. Inverting Zero Error Signs (The #1 Negative Mark Trap in NEET):", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   POSITIVE Zero Error (+e)  ===>  SUBTRACT from observed reading:", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("   True Reading = Observed Reading - (+e)", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold),
            Text("   NEGATIVE Zero Error (-e)  ===>  ADD to observed reading:", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   True Reading = Observed Reading - (-e) = Observed Reading + e", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.20)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)


# ---------------------------------------------------------------------------
# 8. SignificantFiguresRulesBoxScene (P11-C01-T04-V08)
# ---------------------------------------------------------------------------
class SignificantFiguresRulesBoxScene(ModularUnit1Scene):
    def build_beat_1(self):
        settle_tag = Text("Physics and Measurement • Chapter 1", font_size=20, color=self.muted_text)
        settle_title = Text("Significant Figures & Arithmetic Rounding Rules", font=self.header_font, font_size=30, weight="BOLD", color=self.accent_blue)
        ncert_ref = Text("NCERT Class 11 Part 1, Chapter 2, Pages 27-30", font_size=16, color=self.accent_gold)
        return VGroup(settle_tag, settle_title, ncert_ref).arrange(DOWN, buff=0.35).move_to(ORIGIN)

    def build_beat_2(self):
        sf_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        sf_title = Text("THE 4 CORE RULES FOR SIGNIFICANT FIGURES (NCERT)", font=self.card_font, font_size=17, weight="BOLD", color=self.accent_gold).next_to(sf_box.get_top(), DOWN, buff=0.22)

        r1 = Text("1. All non-zero digits are significant:           e.g. 2384  ==> 4 SF", font=self.body_font, font_size=12, color=TEXT_WHITE)
        r2 = Text("2. Trapped zeros between non-zeros are sig:       e.g. 4007  ==> 4 SF", font=self.body_font, font_size=12, color=TEXT_WHITE)
        r3 = Text("3. Leading zeros before first non-zero NEVER sig: e.g. 0.0052 ==> 2 SF (zeros indicate position)", font=self.body_font, font_size=12, color=self.accent_green)
        r4 = Text("4. Trailing zeros WITH decimal point are sig:     e.g. 3.500 ==> 4 SF (indicates precision)", font=self.body_font, font_size=12, color=self.accent_green)
        r5 = Text("5. Trailing zeros WITHOUT decimal are NOT sig:    e.g. 4700  ==> 2 SF (use sci notation: 4.70 × 10³)", font=self.body_font, font_size=12, color=self.accent_gold)

        rules_vg = VGroup(r1, r2, r3, r4, r5).arrange(DOWN, buff=0.16, aligned_edge=LEFT).next_to(sf_title, DOWN, buff=0.25).shift(LEFT * 0.2)
        return VGroup(sf_box, sf_title, rules_vg)

    def build_beat_3(self):
        ops_box = RoundedRectangle(corner_radius=0.12, height=4.2, width=11.2, stroke_color=self.accent_blue, stroke_width=1.5, fill_color="#0F172A", fill_opacity=0.0).move_to(ORIGIN)
        ops_title = Text("ROUNDING IN ARITHMETIC OPERATIONS: ADDITION VS MULTIPLICATION", font=self.card_font, font_size=16, weight="BOLD", color=self.accent_gold).next_to(ops_box.get_top(), DOWN, buff=0.22)

        a1 = Text("ADDITION / SUBTRACTION RULE: Governed by LEAST DECIMAL PLACES", font_size=13, weight="BOLD", color=self.accent_blue).next_to(ops_title, DOWN, buff=0.25, aligned_edge=LEFT).shift(RIGHT * 0.4)
        a2 = Text("• 436.32 (2 dec) + 227.2 (1 dec) + 0.301 (3 dec) = 663.821", font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(a1, DOWN, buff=0.08, aligned_edge=LEFT)
        a3 = Text("• Result must retain only 1 decimal place  ==>  663.8", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green).next_to(a2, DOWN, buff=0.06, aligned_edge=LEFT)

        m1 = Text("MULTIPLICATION / DIVISION RULE: Governed by LEAST SIGNIFICANT FIGURES", font_size=13, weight="BOLD", color=self.accent_gold).next_to(a3, DOWN, buff=0.22, aligned_edge=LEFT)
        m2 = Text("• Density = Mass / Volume = 4.237 g (4 SF) / 2.51 cm³ (3 SF) = 1.68804...", font=self.body_font, font_size=11, color=TEXT_WHITE).next_to(m1, DOWN, buff=0.08, aligned_edge=LEFT)
        m3 = Text("• Result must retain only 3 significant figures  ==>  1.69 g/cm³", font=self.body_font, font_size=12, weight="BOLD", color=self.accent_green).next_to(m2, DOWN, buff=0.06, aligned_edge=LEFT)

        return VGroup(ops_box, ops_title, a1, a2, a3, m1, m2, m3)

    def build_beat_4(self):
        trap_box = RoundedRectangle(corner_radius=0.12, height=4.4, width=11.6, stroke_color=self.accent_red, stroke_width=2.0, fill_color="#1e1014", fill_opacity=0.3).move_to(ORIGIN)
        trap_title = Text("NEET HIGH-YIELD DISTRACTOR TRAP", font=self.card_font, font_size=18, weight="BOLD", color=self.accent_red).next_to(trap_box.get_top(), DOWN, buff=0.22)

        lines = [
            Text("1. Applying Multiplication Rule to Addition/Subtraction (NEET 2020 Trap):", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   Addition/Subtraction is governed strictly by LEAST DECIMAL PLACES, not sig figs!", font=self.body_font, font_size=11, color=self.accent_gold),
            Text("   Example: 9.99 m - 0.0099 m = 9.9801 m  ===>  Round to 2 decimal places: 9.98 m", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_green),
            Text("2. Trailing Zeros Ambiguity Rule:", font=self.body_font, font_size=12, weight="BOLD", color=TEXT_WHITE),
            Text("   4.700 m has 4 sig figs (decimal present), but 4700 m has only 2 sig figs!", font=self.body_font, font_size=11, color=self.accent_green),
            Text("   To avoid ambiguity, always write in scientific notation: 4.700 × 10³ m.", font=self.body_font, font_size=11, weight="BOLD", color=self.accent_gold)
        ]
        for l in lines:
            if l.width > 10.4:
                l.scale_to_fit_width(10.4)
        vg = VGroup(*lines).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(trap_title, DOWN, buff=0.20)
        vg.move_to(trap_box.get_center() + DOWN * 0.22)
        return VGroup(trap_box, trap_title, vg)

