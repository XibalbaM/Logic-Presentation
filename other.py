from manim import *
from common import *

class OtherDomains(Scene):
    """
    1. Informatique
    2. Philosophie
    3. Linguistique
    4. Autres domaines
    """
    def construct(self):
        title = Text("Autres domaines d'application", font_size=48, color=Colors.text)
        self.play(FadeIn(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(title), run_time=Durations.animations)