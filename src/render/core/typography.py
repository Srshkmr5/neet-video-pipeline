import textwrap

class TypographyRules:
    PROPORTIONAL_FONTS = ["Segoe UI", "Arial", "Inter", "Verdana"]
    RESTRICTED_FONTS = ["Consolas"]

    MIN_FONT_SIZE_PT = 16
    HEADER_MIN_FONT_SIZE_PT = 22
    TITLE_MIN_FONT_SIZE_PT = 28
    MAX_CHARS_PER_LINE = 32
    MAX_LINES_PER_CARD = 4
    MAX_FORMULA_CHARS = 120

    @classmethod
    def wrap_to_budget(cls, text: str, max_chars: int = MAX_CHARS_PER_LINE) -> str:
        if not text:
            return ""
        return "\n".join(textwrap.wrap(text, width=max_chars))

    @classmethod
    def validate_text(cls, text: str, is_title: bool = False, is_formula: bool = False):
        if not text:
            return
        if is_formula:
            if len(text) > cls.MAX_FORMULA_CHARS:
                raise ValueError(f"Formula exceeds max chars ({len(text)} > {cls.MAX_FORMULA_CHARS}): {text[:80]}")
            return

        lines = text.splitlines()
        max_chars = 48 if is_title else cls.MAX_CHARS_PER_LINE
        for line in lines:
            if len(line.strip()) > max_chars:
                raise ValueError(f"Text too long for card ({len(line)} > {max_chars}): {line[:80]}")

    @classmethod
    def choose_font(cls, kind: str = "body"):
        if kind == "title":
            return "Verdana"
        if kind == "header":
            return "Arial"
        return "Segoe UI"
