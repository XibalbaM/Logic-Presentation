from manim import *
from common import *

class History(Scene):
    """
    1. Logique intuitionniste
    2. Logique classique
    3. Logique moderne
    """
    def construct(self):
        title = Text("Un peu d'histoire de la logique", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)