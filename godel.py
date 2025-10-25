from manim import *
from common import *

class Godel(Scene):
    """
    1. Énoncé du théorème
    2. Idée de la preuve
    3. Conséquences philosophiques
    """
    def construct(self):
        title = Text("Théorème d'incomplétude de Gödel", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)