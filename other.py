from manim import *
from manim_slides import Slide
from common import *

class OtherDomains(Slide):
    """
    1. Informatique
    2. Autres domaines
    """
    def construct(self):
        intro(self, "Autres domaines d'application")

        self.info()
        self.other_domains()

    def info(self):
        # Présentation images portes logiques depuis assets/
        title = Text("Applications de la logique en informatique", font_size=48, color=Colors.text).to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Scène spéciale pour half adder, montrer aussi addition-colonne-primaire.jpg
        self.play(FadeOut(title), run_time=Durations.animations)
        half_adder_image = ImageMobject("assets/half-adder.png").scale(1.5)
        addition_image = ImageMobject("assets/addition-colonne-primaire.jpg").scale(1.5).next_to(half_adder_image, RIGHT)
        half_adder_label = Text("Porte Additionneur", font_size=36, color=Colors.text).next_to(half_adder_image, UP)
        half_adder_group = Group(half_adder_image, addition_image, half_adder_label).move_to(ORIGIN)
        self.play(FadeIn(half_adder_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(half_adder_group), run_time=Durations.animations)
        
        # Affichage d'un "exemple de fin" avec full-cpu.png
        full_cpu_image = ImageMobject("assets/full-cpu.png").scale(1.5)
        full_cpu_label = Text("Exemple de CPU complet", font_size=36, color=Colors.text).next_to(full_cpu_image, UP)
        full_cpu_group = Group(full_cpu_image, full_cpu_label).move_to(ORIGIN)
        self.play(FadeIn(full_cpu_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(full_cpu_group), run_time=Durations.animations)

    def other_domains(self):
        title = Text("Applications dans d'autres domaines", font_size=48, color=Colors.text).to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)

        domains = [
            ("Philosophie", "Gottlob Frege, un philosophe/logicien allemand, disait : « Every good mathematician is at least half a philosopher, and every good philosopher is at least half a mathematician. »"),
            ("Linguistique", "Montague a systématisé comment traduire phrases anglaises en logique (ex. : Every student passed : ∀x (Student(x) → Passed(x)))"),
            ("Linguistique informatique", "Les théories de Montague ont servient de base pour l'étude des languages de programmation"),
            ("Droit/politique", "Analyse les discours, les arguments, trouver des failles dans les lois, théorie du vote"),
            ("Sciences cognitives", "Comprendre dans quelle mesure nous suivons les règles de la logique, nos biais cognitifs, etc."),
            ("Physique", "Article de Birkhoff & von Neumann introduit la *logic of quantum mechanics* où la conjonction/disjonction des propriétés suit des règles différentes"),
            ("Génétique", "Kauffman (1969) : modélisation par réseaux booléens, qui permet la simulation d'effets de mutations"),
        ]
        for domain, description in domains:
            domain_text = Text(domain, font_size=36, color=Colors.text).next_to(title, DOWN, buff=1)
            description_text = Paragraph(wrap_text(description, 65), font_size=28, color=Colors.text, alignment="center").next_to(domain_text, DOWN)
            self.play(Write(domain_text), Write(description_text), run_time=Durations.animations)
            self.wait(Durations.pauses)
            self.next_slide()
            self.play(FadeOut(domain_text), FadeOut(description_text), run_time=Durations.animations)
        self.play(FadeOut(title), run_time=Durations.animations)