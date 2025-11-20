from manim import *
from manim_slides import Slide
from common import *

class Axioms(Slide):
    """
    1. Axiomes de Peano
    2. Axiomes d'Euclide
    """
    def construct(self):
        intro(self, "Quelques systèmes axiomatiques")
        self.peano_axioms()
        self.euclid_axioms()

    def peano_axioms(self):
        #TODO Bien expliquer ce qu'est un axiome avant de commencer cette section
        # Title
        title = Text("Axiomes de Peano", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # List of Peano axioms
        axioms = [
            "1. 0 est un nombre naturel",
            "2. Tout nombre naturel n a un successeur S(n)",
            "3. 0 n'est le successeur d'aucun nombre",
            "4. Si S(n) = S(m), alors n = m",
            """5. Axiome de récurrence :\n
               Si P(0) est vrai et P(n) ⇒ P(S(n)),\n
               alors P(n) est vrai pour tout n""" #TODO expliquer qu'il est équivalent au principe de bien-ordonnancement
        ]
        
        axiom_group = VGroup()
        for i, axiom_text in enumerate(axioms):
            axiom = Text(axiom_text, font_size=28, color=Colors.text)
            axiom_group.add(axiom)
        
        axiom_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        axiom_group.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(axiom_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Fade out axioms
        self.play(FadeOut(axiom_group), run_time=Durations.animations)
        
        # Examples
        examples_title = Text("Exemples", font_size=36, color=Colors.text)
        examples_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(examples_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Example 1: Building numbers
        ex1_title = Text("Construction des nombres :", font_size=30, color=Colors.text)
        ex1_title.next_to(examples_title, DOWN, buff=0.7)
        self.play(Write(ex1_title), run_time=Durations.animations)
        
        numbers = VGroup()
        num_texts = ["0", "S(0) = 1", "S(S(0)) = 2", "S(S(S(0))) = 3", "..."]
        for num_text in num_texts:
            num = Text(num_text, font_size=28, color=Colors.text)
            numbers.add(num)
        
        numbers.arrange(RIGHT, buff=0.5)
        numbers.next_to(ex1_title, DOWN, buff=0.5)
        
        self.play(Write(numbers), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(ex1_title),FadeOut(numbers), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Example 2: Defining addition via recursion
        ex2_title = Text("Définition de l'addition :", font_size=30, color=Colors.text)
        ex2_title.next_to(examples_title, DOWN, buff=0.7)
        self.play(Write(ex2_title), run_time=Durations.animations)

        addition_def = VGroup()
        add_texts = [
            "a + 0 = a",
            "a + S(b) = S(a + b)"
        ]
        for add_text in add_texts:
            add = Text(add_text, font_size=28, color=Colors.text)
            addition_def.add(add)
        addition_def.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        addition_def.next_to(ex2_title, DOWN, buff=0.5)
        self.play(Write(addition_def), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Last example: Proof that 1 + 1 = 2
        ex3_title = Text("Preuve que 1 + 1 = 2 :", font_size=30, color=Colors.text)
        ex3_title.next_to(addition_def, DOWN, buff=0.7)
        self.play(Write(ex3_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        # Create a LaTeX aligned equation block
        proof_steps = MathTex(
            r"1 + 1 &= S(0) + S(0) \\",
            r"&= S(S(0) + 0) \quad \text{(par définition de l'addition)} \\",
            r"&= S(S(0)) \quad \text{(par définition de l'addition)} \\",
            r"&= 2 \quad \text{(par définition de 2)}",
            font_size=28,
            color=Colors.text
        )
        proof_steps.next_to(ex3_title, DOWN, buff=0.5)
        self.play(Write(proof_steps), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(examples_title),
            FadeOut(ex2_title),
            FadeOut(ex3_title),
            FadeOut(addition_def),
            FadeOut(proof_steps),
            run_time=Durations.animations
        )

    def euclid_axioms(self):
        # Title
        title = Text("Axiomes d'Euclide", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # List of Euclid's axioms (postulates)
        axioms = [
            "1. Par deux points distincts, on peut tracer une droite",
            "2. Un segment peut être prolongé indéfiniment",
            "3. On peut tracer un cercle de centre et rayon donnés",
            "4. Tous les angles droits sont égaux",
            """5. Axiome des parallèles :\n
               Par un point extérieur à une droite, passe\n
               une unique droite parallèle à cette droite"""
        ]
        
        axiom_group = VGroup()
        for i, axiom_text in enumerate(axioms):
            axiom = Text(axiom_text, font_size=28, color=Colors.text)
            axiom_group.add(axiom)
        
        axiom_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        axiom_group.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(axiom_group), run_time=Durations.animations * 2)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Fade out axioms
        self.play(FadeOut(axiom_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()