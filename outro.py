from manim import *
from manim_slides import Slide
from common import *


class Outro(Slide):
    def construct(self):
        thanks_text = "Merci pour votre attention !"
        thanks = Text(thanks_text, font_size=48, color=Colors.text)
        subtext = "J'espère ne pas vous avoir trop perdus."
        sub = Text(subtext, font_size=28, color=Colors.text)
        sub.next_to(thanks, DOWN, buff=0.5)
        self.play(Write(thanks), Write(sub), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()