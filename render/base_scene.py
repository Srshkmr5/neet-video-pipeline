from pathlib import Path


class BaseScene:
    """Minimal reusable scene base for future Manim-based rendering."""

    def __init__(self, concept):
        self.concept = concept

    def build_cards(self):
        return {
            "headline": self.concept["headline"],
            "formula": self.concept["formula"],
            "bullets": self.concept["bullets"],
            "trap": self.concept["trap"],
        }

    def render(self, output_path: str | None = None):
        output = self.build_cards()
        target = Path(output_path) if output_path else Path("proof/output/last_render.json")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(str(output), encoding="utf-8")
        return str(target)
