from manim import *
from common import *

class BanachTarski(Scene):
    """
    1. Énoncé du paradoxe
    2. Idée de la preuve
    3. Conséquences philosophiques
    """
    def construct(self):
        title = Text("Paradoxe de Banach-Tarski", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)