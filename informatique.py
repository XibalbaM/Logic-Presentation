from manim import *
from common import Colors


class Informatique(Scene):
    """
    Présentation des applications de la logique en informatique.
    """
    def construct(self):
        # Présentation images portes logiques depuis assets/
        title = Text("Applications de la logique en informatique", font_size=48, color=Colors.text).to_edge(UP)
        self.play(Write(title))
        gate_images = ["assets/not.jpeg", "assets/and.png", "assets/or.png", "assets/xor.png", "assets/xor_active.png"]
        gate_texts = ["Porte NOT", "Porte AND", "Porte OR", "Porte XOR", "Porte XOR (1 1)"]
        # Montrer chaque porte logique avec son étiquette un par un par slide
        for img_path, gate_text in zip(gate_images, gate_texts):
            gate_image = ImageMobject(img_path).scale(1.5)
            gate_label = Text(gate_text, font_size=36, color=Colors.text).next_to(gate_image, DOWN)
            gate_group = Group(gate_image, gate_label).move_to(ORIGIN)
            self.play(FadeIn(gate_group))
            self.wait(2)
            self.play(FadeOut(gate_group))
        
        # Scène spéciale pour half adder, montrer aussi addition-colonne-primaire.jpg
        self.play(FadeOut(title))
        half_adder_image = ImageMobject("assets/half-adder.png").scale(1.5)
        addition_image = ImageMobject("assets/addition-colonne-primaire.jpg").scale(1.5).next_to(half_adder_image, RIGHT)
        half_adder_label = Text("Porte Additionneur", font_size=36, color=Colors.text).next_to(half_adder_image, UP)
        half_adder_group = Group(half_adder_image, addition_image, half_adder_label).move_to(ORIGIN)
        self.play(FadeIn(half_adder_group))
        self.wait(3)
        self.play(FadeOut(half_adder_group))
        
        # Affichage d'un "exemple de fin" avec full-cpu.png
        full_cpu_image = ImageMobject("assets/full-cpu.png").scale(1.5)
        full_cpu_label = Text("Exemple de CPU complet", font_size=36, color=Colors.text).next_to(full_cpu_image, UP)
        full_cpu_group = Group(full_cpu_image, full_cpu_label).move_to(ORIGIN)
        self.play(FadeIn(full_cpu_group))
        self.wait(3)
        self.play(FadeOut(full_cpu_group))
