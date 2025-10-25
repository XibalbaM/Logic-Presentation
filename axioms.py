from manim import *
from common import *

class Axioms(Scene):
    """
    1. Axiome du choix
    2. Axiome d'extensionalité
    3. Autres axiomes ?
    """
    def construct(self):
        title = Text("Axiomes de la logique", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)