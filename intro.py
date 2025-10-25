from manim import *
from common import Colors

class Intro(Scene):
    def construct(self):
        title = Text("Bases de la logique", font_size=72, color=Colors.text).shift(UP)
        subtitle = Text("Des fondamentaux à ses applications", font_size=36, color=Colors.text).next_to(title, DOWN)
        by = Text("par Maël Porret et Boris Rennard", font_size=24, color=Colors.text).next_to(subtitle, DOWN)
        self.play(Write(title))
        self.play(Write(VGroup(subtitle, by)))
        self.wait(1)
        self.play(FadeOut(subtitle), FadeOut(by))
        toc_title = Text("Table des matières", font_size=48, color=Colors.text).to_edge(UP)
        topics = [
            "1. Les bases",
            "2. Applications en maths",
            "3. Applications dans d'autres domaines",
            "4. Un peu d'histoire",
            "5. Axiomes de la logique",
            "6. Paradoxe de Banach-Tarski",
            "7. Théorème d'incomplétude de Gödel"
        ]
        topic_texts = VGroup(*[Text(topic, font_size=32, color=Colors.text) for topic in topics])
        topic_texts.arrange(DOWN, aligned_edge=LEFT).next_to(toc_title, DOWN, buff=0.5)
        
        self.play(Transform(title, toc_title))
        for topic_text in topic_texts:
            self.play(Write(topic_text))
            self.wait(0.5)
        self.wait(1)
        self.play(FadeOut(title), *[FadeOut(topic_text) for topic_text in topic_texts])