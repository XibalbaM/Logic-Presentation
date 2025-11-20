from manim import *
from manim_slides import Slide
from common import *

class Intro(Slide):
    def construct(self):
        title = Text("Bases de la logique", font_size=72, color=Colors.text).shift(UP)
        subtitle = Text("Des fondamentaux à ses applications", font_size=36, color=Colors.text).next_to(title, DOWN)
        by = Text("par Maël Porret et Boris Rennard", font_size=24, color=Colors.text).next_to(subtitle, DOWN)
        self.play(Write(title), run_time=Durations.animations)
        self.play(Write(VGroup(subtitle, by)), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(subtitle), FadeOut(by), run_time=Durations.animations)
        toc_title = Text("Table des matières", font_size=48, color=Colors.text).to_edge(UP)
        topics = """
            1. Les bases
            2. Applications en maths
            3. Applications dans d'autres domaines
            4. Quelques systèmes axiomatiques
            5. Quelques points qui font débat"""
        topics_text = Text(topics, font_size=32, color=Colors.text).next_to(toc_title, DOWN, buff=0.5)
        
        self.play(Transform(title, toc_title), run_time=Durations.animations)
        self.play(Write(topics_text), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(title), FadeOut(topics_text), run_time=Durations.animations)