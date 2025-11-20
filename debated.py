from manim import *
from manim_slides import Slide
from common import *

class Debated(Slide):
    """
    2. Logique intuitionniste vs classique
    3. Preuves constructives vs non-constructives
    4. Axiome du choix et paradoxes associés #TODO clin d'oeuil à ZF/ZFC

    """
    def construct(self):
        intro(self, "Petite (petite ?) histoire de la logique")
        self.intuitionistic_vs_classical() # TODO ajouter des noms
        self.constructive_vs_nonconstructive() # TODO ajouter des noms
        self.choice_axiom_and_paradoxes()
        # Todo mentionner les preuves assistées par ordinateur

    def intuitionistic_vs_classical(self):
        # Title
        title = Text("Logique intuitioniste vs classique", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Classical logic section
        classical_title = Text("Logique classique", font_size=36, color=Colors.text)
        classical_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(classical_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        classical_principles = [
            "• Une proposition est vraie ou fausse",
            "• Principe du tiers exclu : P ∨ ¬P",
            "• Double négation : ¬¬P ≡ P",
            "• Raisonnement par l'absurde",
        ]
        
        classical_group = VGroup()
        for principle in classical_principles:
            text = Text(principle, font_size=28, color=Colors.text)
            classical_group.add(text)
        
        classical_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        classical_group.next_to(classical_title, DOWN, buff=0.5)
        
        self.play(Write(classical_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        self.play(FadeOut(classical_group), FadeOut(classical_title), run_time=Durations.animations)
        
        # Intuitionistic logic section
        intuitionistic_title = Text("Logique intuitioniste", font_size=36, color=Colors.text)
        intuitionistic_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(intuitionistic_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        intuitionistic_principles = [
            "• Rejette le tiers exclu",
            "• ¬¬P ⇏ P en général",
            "• Une preuve doit être constructive",
            "• Vérité = existence d'une preuve"
        ]
        
        intuitionistic_group = VGroup()
        for principle in intuitionistic_principles:
            text = Text(principle, font_size=28, color=Colors.text)
            intuitionistic_group.add(text)
        
        intuitionistic_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        intuitionistic_group.next_to(intuitionistic_title, DOWN, buff=0.5)
        
        self.play(Write(intuitionistic_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        self.play(FadeOut(intuitionistic_group), FadeOut(intuitionistic_title), run_time=Durations.animations)
        
        # Example section
        examples_title = Text("Exemple", font_size=36, color=Colors.text)
        examples_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(examples_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Example: Proof that sqrt(2) is irrational
        ex_title = Text("Preuve de l'irrationalité de √2 :", font_size=30, color=Colors.text)
        ex_title.next_to(examples_title, DOWN, buff=0.5)
        self.play(Write(ex_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Classical approach
        classical_approach = Text("Approche classique (par l'absurde) :", font_size=28, color=Colors.text)
        classical_approach.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(classical_approach), run_time=Durations.animations)
        
        classical_proof = Text(
            wrap_text("On suppose √2 rationnel : √2 = p/q avec p,q premiers entre eux.\nAlors 2q² = p², donc p est pair, p = 2k.\nDonc 2q² = 4k², soit q² = 2k², donc q est pair.\nContradiction ! Donc √2 est irrationnel.", 60),
            font_size=24,
            color=Colors.text
        )
        classical_proof.next_to(classical_approach, DOWN, buff=0.3)
        self.play(Write(classical_proof), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        self.play(FadeOut(classical_approach), FadeOut(classical_proof), run_time=Durations.animations)
        
        # Intuitionistic remark
        intuitionistic_remark = Text("En logique intuitioniste :", font_size=28, color=Colors.text)
        intuitionistic_remark.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(intuitionistic_remark), run_time=Durations.animations)
        
        intuitionistic_explanation = Text(
            wrap_text("Cette preuve montre que √2 ne peut pas être rationnel,\nmais ne construit pas explicitement sa nature irrationnelle.\nUn intuitioniste accepte cette preuve car elle montre\nl'impossibilité de la forme rationnelle.", 55),
            font_size=24,
            color=Colors.text
        )
        intuitionistic_explanation.next_to(intuitionistic_remark, DOWN, buff=0.3)
        self.play(Write(intuitionistic_explanation), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(examples_title),
            FadeOut(ex_title),
            FadeOut(intuitionistic_remark),
            FadeOut(intuitionistic_explanation),
            run_time=Durations.animations
        )

    def constructive_vs_nonconstructive(self):
        # Title
        title = Text("Preuves constructives vs non-constructives", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Non-constructive proofs section
        nonconstructive_title = Text("Preuves non-constructives", font_size=36, color=Colors.text)
        nonconstructive_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(nonconstructive_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        nonconstructive_desc = Text(
            wrap_text("Prouvent l'existence d'un objet sans le construire explicitement.\nUtilisent souvent le raisonnement par l'absurde.", 60),
            font_size=28,
            color=Colors.text
        )
        nonconstructive_desc.next_to(nonconstructive_title, DOWN, buff=0.5)
        self.play(Write(nonconstructive_desc), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        self.play(FadeOut(nonconstructive_desc), FadeOut(nonconstructive_title), run_time=Durations.animations)
        
        # Constructive proofs section
        constructive_title = Text("Preuves constructives", font_size=36, color=Colors.text)
        constructive_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(constructive_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        constructive_desc = Text(
            wrap_text("Construisent explicitement l'objet dont on prouve l'existence.\nFournissent un algorithme ou une méthode de construction.", 60),
            font_size=28,
            color=Colors.text
        )
        constructive_desc.next_to(constructive_title, DOWN, buff=0.5)
        self.play(Write(constructive_desc), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        self.play(FadeOut(constructive_desc), FadeOut(constructive_title), run_time=Durations.animations)
        
        # Example section
        examples_title = Text("Exemples", font_size=36, color=Colors.text)
        examples_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(examples_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Example 1: Non-constructive proof
        ex1_title = Text("Exemple non-constructif :", font_size=30, color=Colors.text)
        ex1_title.next_to(examples_title, DOWN, buff=0.5)
        self.play(Write(ex1_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        ex1_statement = Text(
            wrap_text("Il existe un nombre premier supérieur à n pour tout n ∈ ℕ.", 60),
            font_size=26,
            color=Colors.text
        )
        ex1_statement.next_to(ex1_title, DOWN, buff=0.4)
        self.play(Write(ex1_statement), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        ex1_proof = Text(
            wrap_text("Preuve :\nIl existe une infinité de nombres premiers. On peut séparer tous les entiers en deux groupes : \nceux qui sont plus petits ou égaux à n et ceux qui sont plus grands que n.\nComme il y en a une infinité, et comme le premier groupe est finit, il y en a forcément un dans le deuxième. CQFD.", 55),
            font_size=24,
            color=Colors.text
        ) #TODO Btw, si vous trouves une preuve constructive, vous devenez l'homme le plus puissant du monde
        ex1_proof.next_to(ex1_statement, DOWN, buff=0.4)
        self.play(Write(ex1_proof), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        self.play(
            FadeOut(ex1_title),
            FadeOut(ex1_statement),
            FadeOut(ex1_proof),
            run_time=Durations.animations
        )
        
        # Example 2: Constructive proof
        ex2_title = Text("Exemple constructif :", font_size=30, color=Colors.text)
        ex2_title.next_to(examples_title, DOWN, buff=0.5)
        self.play(Write(ex2_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        ex2_statement = Text(
            wrap_text("Il existe un nombre premier supérieur à 100.", 60),
            font_size=26,
            color=Colors.text
        )
        ex2_statement.next_to(ex2_title, DOWN, buff=0.4)
        self.play(Write(ex2_statement), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        ex2_proof = Text(
            wrap_text("Preuve : 101 est premier.\nVérifions : 101 n'est divisible ni par 2, 3, 5, 7.\nComme √101 < 11, on a terminé.\nDonc 101 est un nombre premier > 100.", 55),
            font_size=24,
            color=Colors.text
        )
        ex2_proof.next_to(ex2_statement, DOWN, buff=0.4)
        self.play(Write(ex2_proof), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(examples_title),
            FadeOut(ex2_title),
            FadeOut(ex2_statement),
            FadeOut(ex2_proof),
            run_time=Durations.animations
        )

    def choice_axiom_and_paradoxes(self):
        # Title
        title = Text("Axiome du choix", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Statement
        stmt_title = Text("Énoncé", font_size=36, color=Colors.text)
        stmt_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(stmt_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        stmt_text = Text(
            wrap_text(
                "Pour toute famille d'ensembles non vides (Xi) indexée par I,\nil existe une fonction de choix f : I → ⋃ Xi telle que f(i) ∈ Xi pour tout i.",
                65,
            ),
            font_size=28,
            color=Colors.text,
        )
        stmt_text.next_to(stmt_title, DOWN, buff=0.4)
        self.play(Write(stmt_text), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(stmt_text), FadeOut(stmt_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # A few equivalents/consequences
        cons_title = Text("Conséquences et énoncés équivalents", font_size=34, color=Colors.text)
        cons_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(cons_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        consequences = [
            "• Théorème du bon ordre (tout ensemble peut être bien ordonné)",
            "• Principe du tiers exclu (théorème de Diaconescu) (avec l'extensionalité)",
            "• Existence d'ensembles non mesurables",
            "• Enormément d'autres résultats en analyse, algèbre, topologie... \nMais trop complexes pour être listés ici.",
        ]

        cons_group = VGroup(*[Text(c, font_size=28, color=Colors.text) for c in consequences])
        cons_group.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        cons_group.next_to(cons_title, DOWN, buff=0.4)
        self.play(Write(cons_group), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        self.play(FadeOut(cons_group), FadeOut(cons_title), run_time=Durations.animations)

        # Banach–Tarski paradox
        bt_title = Text("Paradoxe de Banach–Tarski", font_size=36, color=Colors.text)
        bt_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(bt_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        bt_desc = Text(
                wrap_text(
                    "En dimension 3, on peut décomposer une boule solide en un nombre fini de morceaux, puis, par des isométries (rotations/translations), reconstituer deux boulesidentiques à l'originale. Cela contredit l'intuition du volume classique.",
                    65,
                ),
                font_size=26,
                color=Colors.text,
            )
        bt_desc.next_to(bt_title, DOWN, buff=0.4)
        self.play(Write(bt_desc), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        bt_notes = Text(
                wrap_text(
                    "Le paradoxe utilise fortement l'axiome du choix et des ensembles non mesurables. Il ne s'applique pas au monde physique : les morceaux ne sont pas 'concrets' et la mesure de Lebesgue n'est pas préservée.",
                    65,
                ),
                font_size=24,
                color=Colors.text,
            )
        bt_notes.next_to(bt_desc, DOWN, buff=0.35)
        self.play(Write(bt_notes), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        self.play(FadeOut(bt_title), FadeOut(bt_desc), FadeOut(bt_notes), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Visual illustration of Banach-Tarski
        image = ImageMobject("assets/Banach-Tarski_Paradox.png")
        self.play(FadeIn(image), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        
        # Fade out everything
        self.play(FadeOut(image), FadeOut(title), run_time=Durations.animations)