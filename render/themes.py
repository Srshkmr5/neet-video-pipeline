"""
NEET UG Video Engine - Modular Typography & Color Themes
Provides 4 curated educational design presets:
1. modern_edtech: Brilliant.org / Linear style (Inter Bold + Inter Medium + Monospace Formulas, Solar Gold & Slate)
2. academic_masterclass: Khan Academy / edX style (Inter Bold + Inter Regular + Cambria Math Serif Formulas, Midnight Navy & Solar Amber)
3. 3b1b: Grant Sanderson / 3Blue1Brown style (Roboto Bold + Roboto + Cambria/LaTeX Formulas, Matte Charcoal Void & 3b1b Pastels)
4. cupertino: Swiss Minimalist Studio style (Inter Display Bold + Inter Medium + Consolas Formulas, Pitch Obsidian & Electric Cyan/Orange)
"""
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class TypographyTheme:
    name: str
    display_name: str
    tagline: str
    bg_color: str
    
    # Topic Typography (Headers, Badges, Main Titles)
    topic_font: str
    topic_weight: str
    topic_color: str
    
    # Body Typography (Explanations, Nuance Notes, Trajectory Labels)
    body_font: str
    body_weight: str
    body_color: str
    
    # Formula Typography & Framing (Textbook stacked fractions & cards)
    formula_font: str
    formula_weight: str
    formula_color: str
    formula_box_bg: str
    formula_box_border: str
    formula_box_opacity: float
    
    # NEET Trap Alert Styling
    trap_font: str
    trap_head_weight: str
    trap_color: str
    trap_box_bg: str
    trap_box_border: str
    trap_body_color: str
    
    # Universal Palette Accents
    accent_blue: str
    accent_gold: str
    accent_green: str
    accent_red: str
    muted_text: str


THEMES: Dict[str, TypographyTheme] = {
    # --------------------------------------------------------------------------
    # 1. MODERN EDTECH (Brilliant / Linear Style) - Default Standard
    # --------------------------------------------------------------------------
    "modern_edtech": TypographyTheme(
        name="modern_edtech",
        display_name="Modern EdTech (Brilliant / Linear Style)",
        tagline="High-contrast modern geometric sans with clear formula isolation and radiant solar gold",
        bg_color="#0B0F19",
        # Topic
        topic_font="Verdana",
        topic_weight="BOLD",
        topic_color="#FFFFFF",
        # Body
        body_font="Consolas",
        body_weight="MEDIUM",
        body_color="#CBD5E1",
        # Formula (Radiant vibrant gold, zero dullness, clean transparent card)
        formula_font="Consolas",
        formula_weight="BOLD",
        formula_color="#FFE600",
        formula_box_bg="#000000",
        formula_box_border="#FFE600",
        formula_box_opacity=0.0,
        # Trap
        trap_font="Cascadia Mono",
        trap_head_weight="BOLD",
        trap_color="#FB7185",
        trap_box_bg="#24141E",
        trap_box_border="#F43F5E",
        trap_body_color="#FFFFFF",
        # Accents
        accent_blue="#38BDF8",
        accent_gold="#FFE600",
        accent_green="#34D399",
        accent_red="#FB7185",
        muted_text="#94A3B8"
    ),

    # --------------------------------------------------------------------------
    # 2. ACADEMIC MASTERCLASS (Khan Academy / edX Style)
    # --------------------------------------------------------------------------
    "academic_masterclass": TypographyTheme(
        name="academic_masterclass",
        display_name="Academic Masterclass (Khan Academy / edX Style)",
        tagline="Pedagogical prestige pairing clean modern headers with refined textbook math serif equations in radiant gold",
        bg_color="#0A0E1A",
        # Topic
        topic_font="Verdana",
        topic_weight="BOLD",
        topic_color="#FFFFFF",
        # Body
        body_font="Consolas",
        body_weight="NORMAL",
        body_color="#CBD5E1",
        # Formula (Radiant Cambria Math in pure bright gold, clean transparent card)
        formula_font="Cambria",
        formula_weight="BOLD",
        formula_color="#FFE600",
        formula_box_bg="#000000",
        formula_box_border="#FFE600",
        formula_box_opacity=0.0,
        # Trap
        trap_font="Cascadia Mono",
        trap_head_weight="BOLD",
        trap_color="#EF4444",
        trap_box_bg="#261318",
        trap_box_border="#DC2626",
        trap_body_color="#FFFFFF",
        # Accents
        accent_blue="#06B6D4",
        accent_gold="#FFE600",
        accent_green="#10B981",
        accent_red="#EF4444",
        muted_text="#A0AEC0"
    ),

    # --------------------------------------------------------------------------
    # 3. 3BLUE1BROWN MATHEMATICAL RIGOR (Grant Sanderson Style)
    # --------------------------------------------------------------------------
    "3b1b": TypographyTheme(
        name="3b1b",
        display_name="3Blue1Brown Mathematical Rigor (Grant Sanderson Style)",
        tagline="Matte chalkboard void with gentle pastel mathematical highlights and classic LaTeX serif equations",
        bg_color="#141414",
        # Topic
        topic_font="Roboto",
        topic_weight="BOLD",
        topic_color="#F0F0F0",
        # Body
        body_font="Consolas",
        body_weight="NORMAL",
        body_color="#A3A3A3",
        # Formula
        formula_font="Cambria",
        formula_weight="BOLD",
        formula_color="#FFFF55",
        formula_box_bg="#000000",
        formula_box_border="#58C4DD",
        formula_box_opacity=0.0,
        # Trap
        trap_font="Cascadia Mono",
        trap_head_weight="BOLD",
        trap_color="#FF6B6B",
        trap_box_bg="#2B1618",
        trap_box_border="#FF6B6B",
        trap_body_color="#F0F0F0",
        # Accents
        accent_blue="#58C4DD",
        accent_gold="#FFFF55",
        accent_green="#83C167",
        accent_red="#FF6B6B",
        muted_text="#A3A3A3"
    ),

    # --------------------------------------------------------------------------
    # 4. CUPERTINO MINIMALIST (Swiss Studio Style)
    # --------------------------------------------------------------------------
    "cupertino": TypographyTheme(
        name="cupertino",
        display_name="Cupertino Minimalist (Swiss Studio Style)",
        tagline="Ultra-clean Swiss studio minimalism with pitch obsidian background, electric cyan and stark white typography",
        bg_color="#08090D",
        # Topic
        topic_font="Verdana",
        topic_weight="BOLD",
        topic_color="#FFFFFF",
        # Body
        body_font="Consolas",
        body_weight="MEDIUM",
        body_color="#D4D4D8",
        # Formula (Radiant Electric Cyan, zero dull fill)
        formula_font="Consolas",
        formula_weight="BOLD",
        formula_color="#38BDF8",
        formula_box_bg="#000000",
        formula_box_border="#38BDF8",
        formula_box_opacity=0.0,
        # Trap
        trap_font="Cascadia Mono",
        trap_head_weight="BOLD",
        trap_color="#FB923C",
        trap_box_bg="#2A1810",
        trap_box_border="#F97316",
        trap_body_color="#FFFFFF",
        # Accents
        accent_blue="#38BDF8",
        accent_gold="#FFE600",
        accent_green="#34D399",
        accent_red="#FB923C",
        muted_text="#A1A1AA"
    )
}

DEFAULT_THEME_NAME = "modern_edtech"


def get_theme(name: Optional[str] = None) -> TypographyTheme:
    """Retrieves theme by key, falling back to DEFAULT_THEME_NAME if invalid or omitted."""
    if not name:
        return THEMES[DEFAULT_THEME_NAME]
    key = str(name).strip().lower().replace("-", "_").replace(" ", "_")
    return THEMES.get(key, THEMES[DEFAULT_THEME_NAME])
