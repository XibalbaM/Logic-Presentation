from manim import *
from manim_slides import Slide
from common import *

class Godel(Slide):
    """
    1. Énoncé du théorème
    2. Idée de la preuve
    3. Conséquences philosophiques
    """
    def construct(self):
        intro(self, "Le théorème d'incomplétude de Gödel")

        self.statement()
        self.proof_idea()

    def statement(self):
        # Title
        title = Text("Énoncé du théorème", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Statement (First incompleteness theorem)
        lines = [
            "Hypothèses :",
            wrap_text("T est un système formel effectif (axiomes et règles énumérables)", 70),
            wrap_text("T est cohérent (ne prouve pas à la fois P et ¬P)", 70),
            wrap_text("T est assez expressif pour l'arithmétique (ex. : Peano)", 70),
            "Conclusion :",
            wrap_text("Il existe une proposition G telle que T ⊬ G et T ⊬ ¬G", 70),
        ]

        statement_group = VGroup(*[
            Text(txt, font_size=28, color=Colors.text) for txt in lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        statement_group.next_to(title, DOWN, buff=0.8)

        self.play(Write(statement_group), run_time=Durations.animations * 2)
        self.wait(Durations.pauses)
        self.next_slide()

        # Optional compact symbolic view
        symbolic = MathTex(r"\exists G:\ T\ \text{cohérent} \Rightarrow T \nvdash G \ \wedge\ T \nvdash \lnot G",
                           font_size=32, color=Colors.text)
        symbolic.next_to(statement_group, DOWN, buff=0.6)
        self.play(Write(symbolic), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Fade out statement
        self.play(FadeOut(statement_group), FadeOut(symbolic), run_time=Durations.animations)

        # Examples
        examples_title = Text("Exemples", font_size=36, color=Colors.text)
        examples_title.next_to(title, DOWN, buff=0.6)
        self.play(Write(examples_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Example 1: An inconsistent system that quickly leads to contradiction
        ex1_title = Text("Exemple 1 : Système incohérent", font_size=30, color=Colors.text)
        ex1_title.next_to(examples_title, DOWN, buff=0.7)
        self.play(Write(ex1_title), run_time=Durations.animations)

        ex1_lines = VGroup(
            Text("Axiomes de Péano + l'infini est un nombre (exemple peu rigoureux)", font_size=28, color=Colors.text),
            Text("Conséquence : 1=2", font_size=28, color=Colors.text),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        ex1_lines.next_to(ex1_title, DOWN, buff=0.4)

        self.play(Write(ex1_lines), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(ex1_title), FadeOut(ex1_lines), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Example 2: A consistent but incomplete system (e.g., Peano Arithmetic)
        ex2_title = Text("Exemple 2 : Système cohérent mais incomplet", font_size=30, color=Colors.text)
        ex2_title.next_to(examples_title, DOWN, buff=0.7)
        self.play(Write(ex2_title), run_time=Durations.animations)

        ex2_lines = VGroup(
            Text("Axiomes de Peano (PA)", font_size=28, color=Colors.text),
            Text(wrap_text("Assez expressif pour l'arithmétique des entiers", 65), font_size=28, color=Colors.text),
            Text(wrap_text("Il existe une proposition vraie G sur ℕ mais indémontrable dans PA", 65), font_size=28, color=Colors.text),
            Text(wrap_text("Intuition : G affirme sa propre non-démontrabilité (phrase de Gödel)", 65), font_size=26, color=Colors.text),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        ex2_lines.next_to(ex2_title, DOWN, buff=0.4)

        g_sentence = MathTex(r"G:\ \text{« Cette phrase n'est pas démontrable dans PA »}", font_size=28, color=Colors.text)
        g_sentence.next_to(ex2_lines, DOWN, buff=0.5)

        self.play(Write(ex2_lines), run_time=Durations.animations)
        self.play(Write(g_sentence), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Fade out everything for this section
        self.play(
            FadeOut(examples_title),
            FadeOut(ex2_title),
            FadeOut(ex2_lines),
            FadeOut(g_sentence),
            FadeOut(title),
            run_time=Durations.animations
        )
        self.wait(Durations.pauses)
        self.next_slide()

    def proof_idea(self): #TODO review
        # Title
        title = Text("Idée de la preuve", font_size=40, color=Colors.text)
        title.to_edge(UP)
        self.play(Write(title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Step 1: Arithmétisation (Gödel numbering)
        step1_title = Text("1) Arithmétisation du langage", font_size=30, color=Colors.text)
        step1_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(step1_title), run_time=Durations.animations)

        step1_lines = VGroup(
            Text(wrap_text("On code symboles, formules et preuves par des nombres (numéros de Gödel)", 70), font_size=28, color=Colors.text),
            Text(wrap_text("Les propriétés syntaxiques deviennent des propriétés arithmétiques sur ℕ", 70), font_size=28, color=Colors.text),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        step1_lines.next_to(step1_title, DOWN, buff=0.4)

        code_eq = MathTex(r"\text{Formule } \varphi\ \longleftrightarrow\ \langle \varphi \rangle \in \mathbb{N}", font_size=30, color=Colors.text)
        code_eq.next_to(step1_lines, DOWN, buff=0.5)

        self.play(Write(step1_lines), run_time=Durations.animations)
        self.play(Write(code_eq), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(step1_title), FadeOut(step1_lines), FadeOut(code_eq), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Step 2: Provability predicate
        step2_title = Text("2) Provabilité arithmétisée", font_size=30, color=Colors.text)
        step2_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(step2_title), run_time=Durations.animations)

        step2_lines = VGroup(
            Text(wrap_text("Définir Prov_T(x): « x est le code d'une preuve dans T »", 70), font_size=28, color=Colors.text),
            Text(wrap_text("Prov_T(x) est représentable dans T (formule arithmétique)", 70), font_size=28, color=Colors.text),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        step2_lines.next_to(step2_title, DOWN, buff=0.4)

        prov_tex = MathTex(r"\mathrm{Prov}_T(x)\ :\ \exists y\, \mathrm{Proof}_T(y,x)", font_size=30, color=Colors.text)
        prov_tex.next_to(step2_lines, DOWN, buff=0.5)

        self.play(Write(step2_lines), run_time=Durations.animations)
        self.play(Write(prov_tex), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(step2_title), FadeOut(step2_lines), FadeOut(prov_tex), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Step 3: Diagonalisation (self-reference)
        step3_title = Text("3) Lemme de diagonalisation", font_size=30, color=Colors.text)
        step3_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(step3_title), run_time=Durations.animations)

        step3_lines = VGroup(
            Text(wrap_text("Pour toute formule φ(x), il existe G telle que T ⊢ G ↔ φ(⟨G⟩)", 70), font_size=28, color=Colors.text),
            Text(wrap_text("Choisir φ(x) := ¬Prov_T(x) et poser G ↔ ¬Prov_T(⟨G⟩)", 70), font_size=28, color=Colors.text),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        step3_lines.next_to(step3_title, DOWN, buff=0.4)

        g_equiv = MathTex(r"G\ \leftrightarrow\ \lnot\,\mathrm{Prov}_T(\langle G \rangle)", font_size=34, color=Colors.text)
        g_equiv.next_to(step3_lines, DOWN, buff=0.5)

        self.play(Write(step3_lines), run_time=Durations.animations)
        self.play(Write(g_equiv), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(step3_title), FadeOut(step3_lines), FadeOut(g_equiv), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Step 4: Conséquences (incomplétude)
        step4_title = Text("4) Conséquences", font_size=30, color=Colors.text)
        step4_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(step4_title), run_time=Durations.animations)

        step4_lines = VGroup(
            Text(wrap_text("Si T prouve G, alors (idée) T prouve aussi Prov_T(⟨G⟩), contredisant G ↔ ¬Prov_T(⟨G⟩)", 70), font_size=28, color=Colors.false),
            Text(wrap_text("Donc, si T est cohérent, T ne prouve pas G", 70), font_size=28, color=Colors.text),
            Text(wrap_text("Pour ¬G : sous ω-cohérence (ou via la variante de Rosser), T ne prouve pas ¬G", 70), font_size=28, color=Colors.text),
            Text(wrap_text("Conclusion : T est incomplet", 50), font_size=28, color=Colors.true),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        step4_lines.next_to(step4_title, DOWN, buff=0.4)

        concl_tex = MathTex(r"T\ \text{ cohérent } \Rightarrow \exists G:\ T \nvdash G \ \wedge\ T \nvdash \lnot G", font_size=30, color=Colors.text)
        concl_tex.next_to(step4_lines, DOWN, buff=0.5)

        self.play(Write(step4_lines), run_time=Durations.animations)
        self.play(Write(concl_tex), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

        # Fade out all
        self.play(
            FadeOut(step4_title),
            FadeOut(step4_lines),
            FadeOut(concl_tex),
            FadeOut(title),
            run_time=Durations.animations
        )
        self.wait(Durations.pauses)
        self.next_slide()