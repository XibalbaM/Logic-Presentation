from manim import *
from common import *

class Maths(Scene):
    """
    1. Quantificateurs
    2. Relations ?
    3. Fonctions ?
    4. Types de preuves
    5. Exemples de systèmes axiomatiques
    6. Problèmes/exercices
    """
    def construct(self):
        title = Text("Mathématiques et logique", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)