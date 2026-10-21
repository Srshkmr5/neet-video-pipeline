"""
Base Templates for NEET UG Manim Animations
Supports both 2D (NEETVideoScene) and 3D (NEETVideoScene3D) architectures
Derived from MASTER_BLUEPRINT.md v1.1 & 3D Extension Specification
"""
import shutil
import textwrap
import re
import manimpango
from config import FONTS_DIR

# Register bundled font files natively in Manim
for _fname in [
    "Inter-Regular.otf", "Inter-Medium.otf", "Inter-Bold.otf",
    "Roboto-Regular.ttf", "Roboto-Medium.ttf", "Roboto-Bold.ttf"
]:
    _fpath = FONTS_DIR / _fname
    if _fpath.exists():
        try:
            manimpango.register_font(str(_fpath))
        except Exception:
            pass

from manim import (
    Scene, ThreeDScene, DEGREES, config, Text, MathTex, VGroup, Rectangle, RoundedRectangle, Line,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR,
    FadeIn, FadeOut, Write, Create, Transform, Indicate
)
from render.themes import get_theme, TypographyTheme, THEMES, DEFAULT_THEME_NAME
from config import DEFAULT_THEME

# Broadcast Safe-Zone Constants (90% Action/Title Safe Area)
# Standard 16:9 Manim camera width is ~14.22 units, height is 8.0 units
SAFE_WIDTH = 12.4
SAFE_HEIGHT = 7.0
SAFE_X_MIN = -6.2
SAFE_X_MAX = 6.2
SAFE_Y_MIN = -3.5
SAFE_Y_MAX = 3.5

# Pedagogical color palette fallbacks
BG_COLOR = "#0B0F19"
ACCENT_BLUE = "#38BDF8"
ACCENT_GOLD = "#FACC15"
ACCENT_RED = "#FB7185"
ACCENT_GREEN = "#34D399"
TEXT_WHITE = "#FFFFFF"
MUTED_TEXT = "#94A3B8"

# Typography Design System Standards (Three-Tier Harmony)
FONT_HEADER = "Verdana"          # Main topic & slide headers
FONT_CARD = "Cascadia Mono"      # Card titles, HUD telemetry, and container banners
FONT_BODY = "Consolas"           # Body bullets, rules, numbers & derivations (zero kerning gap)
FONT_PRIMARY = FONT_BODY
FONT_MONO = "Consolas"
FONT_MATH = "Consolas"
FONT_SERIF = "Georgia"

# Enforce clean default across all Manim text objects
Text.set_default(font=FONT_BODY)

# Root-level font safety net: guarantee any Text instance without explicit font gets FONT_BODY
_orig_manim_text_init = Text.__init__
def _safe_text_init(self, *args, **kwargs):
    if not kwargs.get("font"):
        kwargs["font"] = FONT_BODY
    return _orig_manim_text_init(self, *args, **kwargs)
Text.__init__ = _safe_text_init

SUPERSCRIPTS = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "+": "⁺", "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾",
    "n": "ⁿ", "i": "ⁱ", "x": "ˣ", "y": "ʸ"
}

DIGIT_SUBSCRIPTS = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
    "+": "₊", "-": "₋"
}

NAMED_SUBSCRIPTS = {
    "max": "ₘₐₓ",
    "min": "ₘᵢₙ",
    "net": "ₙₑₜ",
    "tot": "ₜₒₜ",
    "x": "ₓ",
    "y": "ᵧ",
    "t": "ₜ",
    "i": "ᵢ",
    "o": "ₒ"
}

GREEK_MAP = {
    r"\theta": "θ", "theta": "θ",
    r"\omega": "ω", "omega": "ω",
    r"\alpha": "α", "alpha": "α",
    r"\beta": "β", "beta": "β",
    r"\pi": "π", "pi": "π",
    r"\Delta": "Δ", "Delta": "Δ",
    r"\lambda": "λ", "lambda": "λ",
    r"\rho": "ρ", "rho": "ρ",
    r"\mu": "μ", "mu": "μ"
}

def format_math_unicode(text: str) -> str:
    """
    Universally converts raw mathematical notation (carets, underscores, asterisks, greek aliases)
    into publication-grade textbook Unicode typography.
    Examples:
      v_0^2 * sin^2(θ) -> v₀² · sin²θ
      y = x*tan(θ) - (g*x^2) / (2*v_0^2*cos^2(θ)) -> y = x · tan(θ) - (g · x²) / (2 · v₀² · cos²(θ))
      R = (v_0^2 * sin(2θ)) / g -> R = (v₀² · sin(2θ)) / g
    """
    if not text:
        return "" if text is None else text

    s = str(text)

    # Defensive guard: Normalize problematic Unicode letter subscripts that trigger missing glyph boxes
    s = s.replace("ₘₐₓ", "_max").replace("ₙₑₜ", "_net")
    s = s.replace("ₘ", "m").replace("ₐ", "a").replace("ₓ", "x").replace("ₙ", "n").replace("ₑ", "e").replace("ₜ", "t")

    # 0. Clean corrupted encoding / missing Greek characters
    s = re.sub(r"(sin|cos|tan)\(([^)]*)\?([^)]*)\)", r"\1(\2θ\3)", s)
    s = re.sub(r"(sin|cos|tan)\^([0-9]+)\(([^)]*)\?([^)]*)\)", r"\1^\2(\3θ\4)", s)

    # Common greek words/commands
    for k, v in GREEK_MAP.items():
        s = re.sub(r"(?<![a-zA-Z])" + re.escape(k) + r"(?![a-zA-Z])", v, s)

    # 1. Convert caret superscripts: e.g. ^2, ^3, ^(2), ^(-1), ^n
    def rep_sup(match):
        content = match.group(1) or match.group(2)
        return "".join(SUPERSCRIPTS.get(c, c) for c in content)

    s = re.sub(r"\^\(([^)]+)\)", rep_sup, s)
    s = re.sub(r"\^([0-9nixy\+\-]+)", rep_sup, s)

# 2. Convert underscore digit subscripts: e.g. _0, _1, _2
    def rep_sub(match):
        content = match.group(1) or match.group(2)
        if all(c in DIGIT_SUBSCRIPTS for c in content):
            return "".join(DIGIT_SUBSCRIPTS[c] for c in content)
        return match.group(0)

    s = re.sub(r"_\(([^)]+)\)", rep_sub, s)
    s = re.sub(r"_([0-9]+)", rep_sub, s)

    # 3. Clean multiplication symbols: replace ' * ' or '*' with ' · '
    s = re.sub(r"\s*\*\s*", " · ", s)

    return s

class NEETVideoScene(Scene):
    """
    Primary 2D Base Scene for NEET UG Video Engine.
    Handles canonical ID badge, PYQ tag, pacing beats, formulas, and revision capsule.
    """
    dimension = "2d"

    def __init__(self, node_data: dict = None, total_duration: float = 30.0, **kwargs):
        super().__init__(**kwargs)
        self.node_data = node_data or {}
        self.video_id = self.node_data.get("videoId", "P11-NEET")
        self.serial_title = self.node_data.get("serialTitle", "Core Concept")
        self.parameters = self.node_data.get("parameters", {})
        self.total_duration = total_duration
        self.has_latex = shutil.which("latex") is not None

        # Resolve Typography & Color Theme
        self.theme_name = self.node_data.get("theme") or DEFAULT_THEME
        self.theme = get_theme(self.theme_name)
        
        # Color mapping aliases from active theme
        self.bg_color = self.theme.bg_color
        self.topic_font = self.theme.topic_font
        self.body_font = self.theme.body_font
        self.formula_font = self.theme.formula_font
        self.accent_gold = self.theme.accent_gold
        self.accent_blue = self.theme.accent_blue
        self.accent_green = self.theme.accent_green
        self.accent_red = self.theme.accent_red
        self.muted_text = self.theme.muted_text

    def construct(self):
        self.camera.background_color = self.bg_color
        self.setup_header()
        self.render_concept_beats()

    def setup_header(self):
        """
        Open Broadcast Header (Distraction-Free Pedagogy Hierarchy):
        - Top-Center: Syllabus Code + Concept Title (e.g. '2.3.2. The Max Height Arc') in bold white, no box
        - Top-Right: High-Yield NEET PYQ Badge on the FIRST line in gold, no box
        - Bottom-Left: '4/14  2D', no box, no color, faded slate
        """
        # 1. Top-Center: Concatenated Syllabus Code + Concept Title (Dynamic Auto-Resolution)
        vid_id = str(self.node_data.get("videoId") or self.node_data.get("canonical_id") or "")
        match = re.search(r"C(\d+)-T(\d+)-V(\d+)", vid_id)
        if match:
            auto_ch, auto_top, auto_vid = int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            auto_ch, auto_top, auto_vid = 1, 1, 1

        ch_num = self.node_data.get("chapter_no", self.node_data.get("seq_chapter", auto_ch))
        top_num = self.node_data.get("topic_no", auto_top)
        vid_num = self.node_data.get("video_no", auto_vid)
        neet_code = str(self.node_data.get("neet_code", f"{ch_num}.{top_num}.{vid_num}")).strip()
        if neet_code.upper().startswith("S."):
            neet_code = neet_code[2:]
        elif neet_code.upper().startswith("S"):
            neet_code = neet_code[1:]

        title_text = self.serial_title
        if title_text == "Core Concept" and self.parameters.get("conceptTitle"):
            title_text = self.parameters.get("conceptTitle")

        full_title_text = f"{neet_code}. {title_text}"
        center_title = Text(full_title_text, font=self.topic_font, font_size=22, weight=self.theme.topic_weight, color=self.theme.topic_color)
        center_title.to_edge(UP, buff=0.45)

        header_items = [center_title]

        # 2. Top-Right: NEET PYQ Badge at maximum right on the First Line
        pyq_text = self.parameters.get("pyqBadge")
        right_pyq = None
        if pyq_text:
            right_pyq = Text(pyq_text, font=FONT_MONO, font_size=13, weight="BOLD", color=self.accent_gold)
            right_pyq.to_edge(UP, buff=0.45).to_edge(RIGHT, buff=0.25)
            header_items.append(right_pyq)


        # 3. Bottom-Left: Sequence Progress + 2D indicator (one line down, no box, no color, faded)
        seq_ch = self.node_data.get("seq_chapter", 1)
        tot_ch = self.node_data.get("total_chapter_videos", 14)
        dim_label = "3D" if getattr(self, "dimension", "2d") == "3d" else "2D"
        bot_left_text = f"{int(seq_ch)}/{int(tot_ch)}  {dim_label}"
        bot_left = Text(bot_left_text, font=self.body_font, font_size=11, color=self.muted_text)
        bot_left.set_opacity(0.55)
        bot_left.to_edge(LEFT, buff=0.45).to_edge(DOWN, buff=0.22)
        header_items.append(bot_left)



        # Guard against title collision with top-right PYQ badge
        if right_pyq:
            available_half_width = max(3.0, right_pyq.get_left()[0] - 0.40)
            if center_title.get_right()[0] > available_half_width:
                center_title.scale_to_fit_width(available_half_width * 2)
                center_title.to_edge(UP, buff=0.45)

        self.header = VGroup(*header_items)
        self.add(self.header)



    def build_release_teaser(self):
        """Builds Beat 5 / 6 release teaser mobjects (Up Next in Sequence)"""
        next_title = self.node_data.get("next_video_title")
        next_id = self.node_data.get("next_video_id")
        seq_ch = int(self.node_data.get("seq_chapter", 1))
        tot_ch = int(self.node_data.get("total_chapter_videos", 8))

        overlay = Rectangle(
            width=16, height=9,
            fill_color=BG_COLOR, fill_opacity=1.0,
            stroke_width=0
        )

        if next_title and next_id:
            badge = Text("UP NEXT IN SEQUENCE", font=FONT_CARD, font_size=20, weight="BOLD", color=ACCENT_BLUE)
            wrapped_next = textwrap.fill(f"Concept {seq_ch+1:02d}/{tot_ch:02d}: {next_title}", width=48)
            next_txt = Text(wrapped_next, font=FONT_HEADER, font_size=24, weight="BOLD", color=TEXT_WHITE)
            if next_txt.width > 11.5:
                next_txt.scale_to_fit_width(11.5)
            sub_txt = Text(f"Canonical ID: {next_id}", font=FONT_BODY, font_size=15, color=MUTED_TEXT)
            lab_badge = Text("INTERACTIVE LAB AVAILABLE IN APP TAB 2", font=FONT_CARD, font_size=13, weight="BOLD", color=ACCENT_GREEN)
            
            content_box = VGroup(badge, next_txt, sub_txt, lab_badge).arrange(DOWN, buff=0.32).move_to(ORIGIN)
            return VGroup(overlay, content_box)
        else:
            badge = Text("CHAPTER COMPLETE", font=FONT_CARD, font_size=20, weight="BOLD", color=ACCENT_GOLD)
            txt = Text(next_title if next_title else "Chapter 1 Complete • Ready for Unit 2: Kinematics", font=FONT_HEADER, font_size=24, weight="BOLD", color=ACCENT_GREEN)
            if txt.width > 11.5:
                txt.scale_to_fit_width(11.5)
            sub = Text(f"All {tot_ch}/{tot_ch} Core Concepts Verified", font=FONT_BODY, font_size=16, color=TEXT_WHITE)
            lab = Text("EXAM DIAGNOSTIC SUITE UNLOCKED IN APP TAB 3", font=FONT_CARD, font_size=13, weight="BOLD", color=ACCENT_BLUE)
            content_box = VGroup(badge, txt, sub, lab).arrange(DOWN, buff=0.32).move_to(ORIGIN)
            return VGroup(overlay, content_box)

    def render_release_teaser(self, duration: float = 3.5):
        """Beat 5 / 6: Transition teaser directing student to next sequential concept"""
        teaser_mobjects = self.build_release_teaser()
        self.play(FadeIn(teaser_mobjects), run_time=1.0)
        self.wait(max(1.0, duration - 2.0))
        self.play(FadeOut(teaser_mobjects), run_time=1.0)

    def create_formula_mobject(self, latex_str: str, plain_str: str = "", font_size: int = 34, color_val=None):
        """
        Creates formula Mobject: uses MathTex when LaTeX is installed,
        or clean mathematical typography via Text when LaTeX is not present.
        """
        f_color = color_val or self.theme.formula_color
        if self.has_latex and latex_str:
            try:
                return MathTex(latex_str, font_size=font_size, color=f_color)
            except Exception:
                pass
        
        display_text = format_math_unicode(plain_str if plain_str else latex_str)
        return Text(display_text, font=self.formula_font, font_size=font_size, weight=self.theme.formula_weight, color=f_color)

    def create_textbook_fraction(
        self,
        lhs: str = "H_max =",
        num: str = "v₀² · sin²θ",
        den: str = "2g",
        font_size: int = 28,
        color_val = None,
        bar_color = None
    ) -> VGroup:
        """
        Builds a textbook-grade vertical stacked fraction with active theme typography.
        """
        f_color = color_val or self.theme.formula_color
        b_color = bar_color or f_color
        f_font = self.formula_font
        f_weight = self.theme.formula_weight

        lhs = format_math_unicode(lhs)
        num = format_math_unicode(num)
        den = format_math_unicode(den)

        lhs_mobj = Text(lhs, font=f_font, font_size=font_size, weight=f_weight, color=f_color)
        num_mobj = Text(num, font=f_font, font_size=font_size - 2, weight=f_weight, color=f_color)
        den_mobj = Text(den, font=f_font, font_size=font_size - 2, weight=f_weight, color=f_color)

        fraction_width = max(num_mobj.width, den_mobj.width) + 0.35
        bar = Line(
            start=LEFT * (fraction_width / 2),
            end=RIGHT * (fraction_width / 2),
            color=b_color,
            stroke_width=2.5
        )

        num_mobj.next_to(bar, UP, buff=0.12)
        den_mobj.next_to(bar, DOWN, buff=0.12)

        frac_col = VGroup(num_mobj, bar, den_mobj)
        lhs_mobj.next_to(bar, LEFT, buff=0.22)

        return VGroup(lhs_mobj, frac_col)

    def create_smart_formula(self, formula_str: str, font_size: int = 28, color_val=None) -> VGroup:
        """
        Dynamically analyzes any formula string, applies universal Unicode mathematical
        formatting, and renders it as either a textbook vertical stacked fraction
        or a formatted inline expression.
        """
        f_color = color_val or self.theme.formula_color
        f_font = self.formula_font
        f_weight = self.theme.formula_weight

        if not formula_str:
            return Text("", font=f_font, font_size=font_size, color=f_color)

        formula_str = format_math_unicode(formula_str)

        if "=" in formula_str:
            parts = formula_str.split("=", 1)
            lhs = parts[0].strip() + " ="
            rhs = parts[1].strip()
        else:
            lhs = ""
            rhs = formula_str

        def strip_outer(s):
            s = s.strip()
            if s.startswith("(") and s.endswith(")"):
                depth = 0
                for i, c in enumerate(s):
                    if c == "(": depth += 1
                    elif c == ")": depth -= 1
                    if depth == 0 and i < len(s) - 1:
                        return s
                return s[1:-1].strip()
            return s

        if "/" in rhs and not any(sep in rhs for sep in [",", " + ", " - "]):
            num_den = rhs.split("/", 1)
            num = strip_outer(num_den[0])
            den = strip_outer(num_den[1])
            return self.create_textbook_fraction(
                lhs=lhs,
                num=num,
                den=den,
                font_size=font_size,
                color_val=f_color
            )
        else:
            txt_mobj = Text(formula_str, font=f_font, font_size=font_size, weight=f_weight, color=f_color)
            if txt_mobj.width > 9.5:
                txt_mobj.scale_to_fit_width(9.5)
            return VGroup(txt_mobj)

    def render_end_capsule(self, formula_mobj, trap_text: str, duration: float = 6.0):
        """
        Section 5: End-capsule 15s revision overlay
        Formula + Trap Warning + 3-Node Memory Flow
        """
        overlay = Rectangle(
            width=16, height=9,
            fill_color=self.bg_color, fill_opacity=1.0,
            stroke_width=0
        )

        capsule_title = Text("EXAM REVISION CAPSULE", font=self.topic_font, font_size=24, weight="BOLD", color=self.accent_gold)
        capsule_title.to_edge(UP, buff=1.2)

        # Centered formula card (Fresh instance at 100% solid opacity, zero murky fill)
        plain_formula = self.parameters.get("plainFormula", "")
        if plain_formula:
            capsule_formula = self.create_smart_formula(plain_formula, font_size=28, color_val=self.theme.formula_color)
        else:
            capsule_formula = self.create_textbook_fraction(
                lhs="H_max =",
                num="v₀² · sin²θ",
                den="2g",
                font_size=28,
                color_val=self.theme.formula_color
            )
        for sm in capsule_formula.get_family():
            sm.set_opacity(1.0)

        formula_box = RoundedRectangle(
            corner_radius=0.15,
            height=capsule_formula.height + 0.5,
            width=min(11.0, max(capsule_formula.width + 0.8, 6.0)),
            stroke_color=self.theme.formula_box_border,
            stroke_width=2,
            fill_color=self.theme.bg_color,
            fill_opacity=0.0
        )
        f_group = VGroup(formula_box, capsule_formula.move_to(formula_box)).next_to(capsule_title, DOWN, buff=0.35)

        # Trap Warning (Clean Segoe UI layout, zero emoji font bugs)
        trap_label = Text("NEET TRAP POINT", font=self.topic_font, font_size=16, weight="BOLD", color=self.theme.trap_color)
        wrapped_trap = textwrap.fill(trap_text, width=54)
        trap_body = Text(wrapped_trap, font=self.body_font, font_size=15, weight=self.theme.body_weight, color=self.theme.trap_body_color)
        if trap_body.width > 11.2:
            trap_body.scale_to_fit_width(11.2)

        trap_inner = VGroup(trap_label, trap_body).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        trap_box = RoundedRectangle(
            corner_radius=0.12,
            height=trap_inner.height + 0.35,
            width=min(11.8, max(trap_inner.width + 0.6, 7.5)),
            stroke_color=self.theme.trap_box_border,
            stroke_width=1.5,
            fill_color=self.theme.bg_color,
            fill_opacity=0.0
        )
        trap_group = VGroup(trap_box, trap_inner.move_to(trap_box)).next_to(f_group, DOWN, buff=0.3)

        # 3-Node memory recap flow (Scaled and auto-fitted dynamically)
        topic_label = self.parameters.get("topicName") or "Concept"
        concept_title = self.parameters.get("conceptTitle") or self.node_data.get("serialTitle", "Principle")
        f_display = plain_formula if plain_formula else "Core Formula"

        node1 = Text(f"1. {topic_label[:24]}", font=self.body_font, font_size=15, color=self.accent_blue)
        arr1 = Text("→", font=FONT_PRIMARY, font_size=17, color=self.muted_text)
        node2 = Text(f"2. {concept_title[:28]}", font=self.body_font, font_size=15, color=self.accent_green)
        arr2 = Text("→", font=FONT_PRIMARY, font_size=17, color=self.muted_text)
        node3 = Text(f"3. {f_display[:32]}", font=self.formula_font, font_size=15, weight="BOLD", color=self.theme.formula_color)
        flow_group = VGroup(node1, arr1, node2, arr2, node3).arrange(RIGHT, buff=0.2).next_to(trap_group, DOWN, buff=0.3)
        if flow_group.width > 11.5:
            flow_group.scale_to_fit_width(11.5)

        capsule_mobjects = VGroup(overlay, capsule_title, f_group, trap_group, flow_group)

        self.play(FadeIn(capsule_mobjects), run_time=1.0)
        self.wait(max(1.0, duration - 2.0))
        self.play(FadeOut(capsule_mobjects), run_time=1.0)

    def render_concept_beats(self):
        """To be overridden by child templates"""
        pass

# Maintain BaseNeetScene as alias for backwards compatibility
BaseNeetScene = NEETVideoScene


class NEETVideoScene3D(ThreeDScene):
    """
    Sibling 3D Base Scene for NEET UG Video Engine.
    Extends ThreeDScene while sharing the exact same beat structure, tier pacing,
    formula creation, and 15s end revision capsule.
    Pinned UI elements (header, formula overlay, revision capsule) are fixed in frame.
    """
    dimension = "3d"

    def __init__(self, node_data: dict = None, total_duration: float = 30.0, **kwargs):
        super().__init__(**kwargs)
        self.node_data = node_data or {}
        self.video_id = self.node_data.get("videoId", "P11-NEET-3D")
        self.serial_title = self.node_data.get("serialTitle", "3D Core Concept")
        self.parameters = self.node_data.get("parameters", {})
        self.total_duration = total_duration
        self.has_latex = shutil.which("latex") is not None

        # Resolve Typography & Color Theme
        self.theme_name = self.node_data.get("theme") or DEFAULT_THEME
        self.theme = get_theme(self.theme_name)
        self.bg_color = self.theme.bg_color
        self.topic_font = self.theme.topic_font
        self.body_font = self.theme.body_font
        self.formula_font = self.theme.formula_font
        self.accent_gold = self.theme.accent_gold
        self.accent_blue = self.theme.accent_blue
        self.accent_green = self.theme.accent_green
        self.accent_red = self.theme.accent_red
        self.muted_text = self.theme.muted_text

    def construct(self):
        self.camera.background_color = self.bg_color
        self.setup_3d_camera()
        self.setup_header()
        self.render_concept_beats()

    def setup_3d_camera(self, phi: float = 75 * DEGREES, theta: float = -45 * DEGREES):
        """Initializes default 3D camera orientation for physical clarity"""
        self.set_camera_orientation(phi=phi, theta=theta)

    def setup_header(self):
        """
        Open Broadcast Header for 3D Scenes (Flat HUD Screen Layer):
        - Top-Center: Syllabus Code + Concept Title (e.g. '2.3.2. The Max Height Arc') in bold white, no box
        - Top-Right: High-Yield NEET PYQ Badge on the FIRST line in gold, no box
        - Bottom-Left: '4/14  3D', no box, no color, faded slate
        """
        # 1. Top-Center: Concatenated Syllabus Code + Concept Title (Dynamic Auto-Resolution)
        vid_id = str(self.node_data.get("videoId") or self.node_data.get("canonical_id") or "")
        match = re.search(r"C(\d+)-T(\d+)-V(\d+)", vid_id)
        if match:
            auto_ch, auto_top, auto_vid = int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            auto_ch, auto_top, auto_vid = 1, 1, 1

        ch_num = self.node_data.get("chapter_no", self.node_data.get("seq_chapter", auto_ch))
        top_num = self.node_data.get("topic_no", auto_top)
        vid_num = self.node_data.get("video_no", auto_vid)
        neet_code = str(self.node_data.get("neet_code", f"{ch_num}.{top_num}.{vid_num}")).strip()
        if neet_code.upper().startswith("S."):
            neet_code = neet_code[2:]
        elif neet_code.upper().startswith("S"):
            neet_code = neet_code[1:]

        title_text = self.serial_title
        if title_text == "Core Concept" and self.parameters.get("conceptTitle"):
            title_text = self.parameters.get("conceptTitle")

        full_title_text = f"{neet_code}. {title_text}"
        center_title = Text(full_title_text, font=self.topic_font, font_size=22, weight=self.theme.topic_weight, color=self.theme.topic_color)
        center_title.to_edge(UP, buff=0.45)

        header_items = [center_title]

        # 2. Top-Right: NEET PYQ Badge at maximum right on the First Line
        pyq_text = self.parameters.get("pyqBadge")
        right_pyq = None
        if pyq_text:
            right_pyq = Text(pyq_text, font=FONT_MONO, font_size=13, weight="BOLD", color=self.accent_gold)
            right_pyq.to_edge(UP, buff=0.45).to_edge(RIGHT, buff=0.25)
            header_items.append(right_pyq)


        # 3. Bottom-Left: Sequence Progress + 3D indicator (one line down, no box, no color, faded)
        seq_ch = self.node_data.get("seq_chapter", 1)
        tot_ch = self.node_data.get("total_chapter_videos", 14)
        bot_left_text = f"{int(seq_ch)}/{int(tot_ch)}  3D"
        bot_left = Text(bot_left_text, font=self.body_font, font_size=11, color=self.muted_text)
        bot_left.set_opacity(0.55)
        bot_left.to_edge(LEFT, buff=0.45).to_edge(DOWN, buff=0.22)
        header_items.append(bot_left)



        # Guard against title collision with top-right PYQ badge
        if right_pyq:
            available_half_width = max(3.0, right_pyq.get_left()[0] - 0.40)
            if center_title.get_right()[0] > available_half_width:
                center_title.scale_to_fit_width(available_half_width * 2)
                center_title.to_edge(UP, buff=0.45)

        self.header = VGroup(*header_items)
        self.add_fixed_in_frame_mobjects(self.header)


    def create_formula_mobject(self, latex_str: str, plain_str: str = "", font_size: int = 34, color_val=ACCENT_GOLD):
        if self.has_latex and latex_str:
            try:
                return MathTex(latex_str, font_size=font_size, color=color_val)
            except Exception:
                pass
        display_text = plain_str if plain_str else latex_str
        return Text(display_text, font_size=font_size, weight="BOLD", color=color_val)

    def create_textbook_fraction(
        self,
        lhs: str = "H_max =",
        num: str = "v₀² · sin²θ",
        den: str = "2g",
        font_size: int = 28,
        color_val = ACCENT_GOLD,
        bar_color = ACCENT_GOLD
    ) -> VGroup:
        """
        Builds a textbook-grade vertical stacked fraction for 3D scenes:
               v₀² · sin²θ
        H_max = ───────────
                   2g
        """
        lhs_mobj = Text(lhs, font=FONT_PRIMARY, font_size=font_size, weight="BOLD", color=color_val)
        num_mobj = Text(num, font=FONT_PRIMARY, font_size=font_size - 2, weight="BOLD", color=color_val)
        den_mobj = Text(den, font=FONT_PRIMARY, font_size=font_size - 2, weight="BOLD", color=color_val)

        fraction_width = max(num_mobj.width, den_mobj.width) + 0.35
        bar = Line(
            start=LEFT * (fraction_width / 2),
            end=RIGHT * (fraction_width / 2),
            color=bar_color,
            stroke_width=2.5
        )

        num_mobj.next_to(bar, UP, buff=0.12)
        den_mobj.next_to(bar, DOWN, buff=0.12)

        frac_col = VGroup(num_mobj, bar, den_mobj)
        lhs_mobj.next_to(bar, LEFT, buff=0.22)

        return VGroup(lhs_mobj, frac_col)

    def render_end_capsule(self, formula_mobj, trap_text: str, duration: float = 6.0):
        overlay = Rectangle(
            width=16, height=9,
            fill_color=BG_COLOR, fill_opacity=1.0,
            stroke_width=0
        )
        capsule_title = Text("EXAM REVISION CAPSULE (3D GEOMETRY)", font=FONT_PRIMARY, font_size=23, weight="BOLD", color=ACCENT_GOLD).to_edge(UP, buff=1.2)
        formula_box = RoundedRectangle(
            corner_radius=0.15,
            height=formula_mobj.height + 0.5,
            width=min(11.0, max(formula_mobj.width + 0.8, 6.0)),
            stroke_color=ACCENT_GOLD,
            stroke_width=2,
            fill_color=self.bg_color,
            fill_opacity=0.0
        )
        f_group = VGroup(formula_box, formula_mobj.copy().move_to(formula_box)).next_to(capsule_title, DOWN, buff=0.35)

        trap_label = Text("NEET TRAP POINT", font=FONT_PRIMARY, font_size=16, weight="BOLD", color=ACCENT_RED)
        wrapped_trap = textwrap.fill(trap_text, width=54)
        trap_body = Text(wrapped_trap, font=FONT_PRIMARY, font_size=15, color=TEXT_WHITE)
        if trap_body.width > 11.2:
            trap_body.scale_to_fit_width(11.2)

        trap_inner = VGroup(trap_label, trap_body).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        trap_box = RoundedRectangle(
            corner_radius=0.12,
            height=trap_inner.height + 0.35,
            width=min(11.8, max(trap_inner.width + 0.6, 7.5)),
            stroke_color=ACCENT_RED,
            stroke_width=1.5,
            fill_color=self.bg_color,
            fill_opacity=0.0
        )
        trap_group = VGroup(trap_box, trap_inner.move_to(trap_box)).next_to(f_group, DOWN, buff=0.3)

        node1 = Text("1. 3D Spatial Trajectory", font=FONT_PRIMARY, font_size=15, color=ACCENT_BLUE)
        arr1 = Text("→", font=FONT_PRIMARY, font_size=17, color=MUTED_TEXT)
        node2 = Text("2. Apex: vy = 0 (vx Constant)", font=FONT_PRIMARY, font_size=15, color=ACCENT_GREEN)
        arr2 = Text("→", font=FONT_PRIMARY, font_size=17, color=MUTED_TEXT)
        node3 = Text("3. H_max = (v₀² sin²θ) / 2g", font=FONT_PRIMARY, font_size=15, color=ACCENT_GOLD)
        flow_group = VGroup(node1, arr1, node2, arr2, node3).arrange(RIGHT, buff=0.2).next_to(trap_group, DOWN, buff=0.3)
        if flow_group.width > 11.5:
            flow_group.scale_to_fit_width(11.5)

        capsule_mobjects = VGroup(overlay, capsule_title, f_group, trap_group, flow_group)
        self.add_fixed_in_frame_mobjects(capsule_mobjects)

        self.play(FadeIn(capsule_mobjects), run_time=1.0)
        self.wait(max(1.0, duration - 2.0))
        self.play(FadeOut(capsule_mobjects), run_time=1.0)

    def render_release_teaser(self, duration: float = 3.5):
        """Beat 6: Transition teaser in 3D scene"""
        next_title = self.node_data.get("next_video_title")
        next_id = self.node_data.get("next_video_id")
        seq_ch = int(self.node_data.get("seq_chapter", 1))
        tot_ch = int(self.node_data.get("total_chapter_videos", 14))

        overlay = Rectangle(
            width=16, height=9,
            fill_color=BG_COLOR, fill_opacity=1.0,
            stroke_width=0
        )

        if next_title:
            badge = Text("UP NEXT IN SEQUENCE", font=FONT_PRIMARY, font_size=22, weight="BOLD", color=ACCENT_BLUE)
            wrapped_next = textwrap.fill(f"Video {seq_ch+1:02d}/{tot_ch:02d}: {next_title}", width=48)
            next_txt = Text(wrapped_next, font=FONT_PRIMARY, font_size=24, weight="BOLD", color=TEXT_WHITE)
            if next_txt.width > 11.5:
                next_txt.scale_to_fit_width(11.5)
            lab_badge = Text("INTERACTIVE LAB AVAILABLE IN APP TAB 2", font=FONT_PRIMARY, font_size=15, weight="BOLD", color=ACCENT_GREEN)
            items = [badge, next_txt]
            if next_id:
                sub_txt = Text(f"Canonical ID: {next_id}", font=FONT_MONO, font_size=16, color=MUTED_TEXT)
                items.append(sub_txt)
            items.append(lab_badge)
            content_box = VGroup(*items).arrange(DOWN, buff=0.3).move_to(ORIGIN)
            teaser_mobjects = VGroup(overlay, content_box)
            self.add_fixed_in_frame_mobjects(teaser_mobjects)
            self.play(FadeIn(teaser_mobjects), run_time=1.0)
            self.wait(max(1.0, duration - 2.0))
            self.play(FadeOut(teaser_mobjects), run_time=1.0)

    def render_concept_beats(self):
        """To be overridden by child 3D templates in Phase 5"""
        pass
