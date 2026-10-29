from dataclasses import dataclass

@dataclass
class SceneCard:
    title: str
    body: str
    formula: str
    trap: str

class BaseScene:
    def __init__(self, concept):
        self.concept = concept

    def build_cards(self):
        return [
            SceneCard(
                title=self.concept.get("concept_title", ""),
                body=self.concept.get("ncert_core_rule", ""),
                formula=self.concept.get("latex_formula", ""),
                trap=self.concept.get("neet_trap_point", "")
            )
        ]

    def render(self):
        cards = self.build_cards()
        for card in cards:
            if len(card.body) > 200:
                raise ValueError("Card body too long for layout-safe rendering")
            if len(card.formula) > 120:
                raise ValueError("Formula too long")
        return cards
