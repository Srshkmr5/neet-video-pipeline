from render.base_scene import BaseScene


class IntroCardScene(BaseScene):
    """Example scene archetype for a single educational beat."""

    def build_cards(self):
        cards = super().build_cards()
        return {
            "title": cards["headline"],
            "formula": cards["formula"],
            "learning_points": cards["bullets"],
            "trap": cards["trap"],
            "style": {
                "font_family": "Arial",
                "min_font_size": 16,
                "max_lines_per_card": 3,
                "no_auto_shrink": True,
            },
        }
