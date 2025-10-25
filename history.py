from manim import *
from common import *

class History(Scene):
    """
    1. Logique intuitionniste vs classique
    4. Preuve constructive/non-constructive
    (5. Ordinateurs et preuves formelles)
    6. Systemes axiomatiques
    """
    def construct(self):
        title = Text("Un peu d'histoire de la logique", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)