from manim import *
from manim_slides import Slide
from common import *

class Maths(Slide):
    """
    1. Quantificateurs
    2. Types de preuves
    3. Problèmes/exercices
    #2. Relations ?
    #3. Fonctions ?
    """
    def construct(self):
        intro(self, "Partie 2: Applications en mathématiques")

        section_1_title = Text("Quantificateurs", font_size=36, color=Colors.text).move_to(UP * 3)
        self.play(Write(section_1_title), run_time=Durations.animations)
        definition_subtitle = Text("Définitions", font_size=32, color=Colors.text).next_to(section_1_title, DOWN)
        examples_subtitle = Text("Exemples", font_size=32, color=Colors.text).next_to(section_1_title, DOWN)
        subtitle = definition_subtitle.copy()
        self.play(Write(subtitle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        cheatSheet = self.section_1_definitions()
        self.play(Transform(subtitle, examples_subtitle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.section_1_examples(cheatSheet)

        section_2_title = Text("Types de preuves", font_size=36, color=Colors.text).move_to(UP * 3)
        self.play(Transform(section_1_title, section_2_title), FadeOut(subtitle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.section_2(section_1_title)
    
    def section_1_definitions(self):
        definitions = [
            "Prédicat : Une proposition dépendant d'une ou plusieurs variables. On note $P(x)$.",
            "Quantificateur universel : Indique que la propriété est vraie pour tous les éléments d'un ensemble donné. On note $\\forall x \\in A, P(x)$.",
            "Quantificateur existentiel : Indique qu'il existe au moins un élément dans un ensemble donné pour lequel la propriété est vraie. On note $\\exists x \\in A, P(x)$.",
            "Quantificateur existentiel unique : Indique qu'il existe un et un seul élément dans un ensemble donné pour lequel la propriété est vraie. On note $\\exists! x \\in A, P(x)$."
        ]
        definition_texts = VGroup(*[Tex("\\begin{flushleft}" + defn + "\\end{flushleft}", font_size=28, color=Colors.text) for defn in definitions])
        definition_texts.arrange(DOWN, aligned_edge=LEFT)
        for defn_text in definition_texts:
            self.play(Write(defn_text), run_time=Durations.animations)
            self.wait(Durations.pauses)
        self.next_slide()
        cheatSheet = [
            "$P(x)$ : Prédicat",
            "$\\forall$ : pour tout",
            "$\\exists$ : il existe",
            "$\\exists!$ : il existe un et un seul"
        ]
        cheatSheet_texts = VGroup(*[Tex("\\begin{flushleft}" + item + "\\end{flushleft}", font_size=28, color=Colors.text) for item in cheatSheet])
        cheatSheet_texts.arrange(DOWN, aligned_edge=LEFT).to_edge(UP + LEFT)
        self.play(Transform(definition_texts, cheatSheet_texts), run_time=Durations.animations)
        cheatSheet_box = SurroundingRectangle(cheatSheet_texts, buff=0.1, color=Colors.text)
        self.play(Write(cheatSheet_box), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        return definition_texts, cheatSheet_box
    
    def section_1_examples(self, cheatSheet: tuple[VGroup, SurroundingRectangle]):
        # Avec des nombres
        examples = Tex("""
                   \\begin{itemize}
                    \\item $P(n)$ : "$n$ est pair"
                    \\item $\\forall n \\in \\mathbb{N}, n \\geq 0$
                    \\item $\\exists n \\in \\mathbb{Z}, P(n)$
                    \\item $\\exists! n \\in \\mathbb{N}, n = 0$
                   \\end{itemize}""",
                font_size=28, color=Colors.text)
        self.play(Write(examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        # Avec des matrices, des entiers, des suites et des limites (definition de la limite)
        other_examples = Tex("""
                        \\begin{itemize}
                            \\item $P(A) \\equiv \\exists B\\in \\mathcal M, AB=I$
                            \\item $Q(n) \\equiv \\forall m \\in \\mathbb{N}, m \\mid n \\implies m = 1 \\lor m = n$
                            \\item $R(a_n) \\equiv \\forall n \\in \\mathbb{N}, a_n \\geq 0$
                            \\item $lim_{x \\to k} f(x) = L \\equiv \\forall \\varepsilon > 0, \\exists \\delta > 0, \\forall x, |x - k| < \\delta \\implies |f(x) - L| < \\varepsilon$
                       \\end{itemize}""",
                       font_size=28, color=Colors.text)
        self.play(Transform(examples, other_examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        # Dangers (ordre, négation)
        other_examples_2_partial = Tex("""
                        \\begin{flushleft}
                        \\begin{itemize}
                               \\item $P(f) \\equiv \\forall x \\in \\mathbb{R}, \\exists! y \\in \\mathbb{R}, f(x) = y$
                               \\item $Q(f) \\equiv \\exists! y \\in \\mathbb{R}, \\forall x \\in \\mathbb{R}, f(x) = y$
                               \\item $\\neg (\\forall x \\in I) \\equiv ?$
                               \\item $\\neg (\\exists x \\in I) \\equiv ?$ 
                        \\end{itemize}
                        \\end{flushleft}""",#TODO FIX
                          font_size=28, color=Colors.text)
        self.play(Transform(examples, other_examples_2_partial), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        other_examples_2_final = Tex("""
                        \\begin{flushleft}
                        \\begin{itemize}
                               \\item $P(f) \\equiv \\forall x \\in \\mathbb{R}, \\exists! y \\in \\mathbb{R}, f(x) = y$
                               \\item $Q(f) \\equiv \\exists! y \\in \\mathbb{R}, \\forall x \\in \\mathbb{R}, f(x) = y$
                               \\item $\\neg (\\forall x \\in I) \\equiv \\exists x \\in I, \\neg P(x)$
                               \\item $\\neg (\\exists x \\in I) \\equiv \\forall x \\in I, \\neg P(x)$
                        \\end{itemize}
                        \\end{flushleft}""",
                          font_size=28, color=Colors.text)
        self.play(Transform(examples, other_examples_2_final), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(cheatSheet[0]), FadeOut(cheatSheet[1]), FadeOut(examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()

    def section_2(self, title_obj: Text):
        # 1. Preuve directe
        direct_proof_title = Text("Preuve directe", font_size=32, color=Colors.text).next_to(title_obj, DOWN)
        self.play(Write(direct_proof_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        direct_proof_principle = Tex("""
            \\begin{flushleft}
            \\textbf{Principe :} Pour prouver une implication $P \\implies Q$, on suppose que $P$ est vrai et on montre que $Q$ l'est aussi.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(direct_proof_title, DOWN, buff=0.5)
        self.play(Write(direct_proof_principle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        direct_proof_example = Tex("""
            \\begin{flushleft}
            \\textbf{Exemple :} J'espère que vous n'avez pas besoin d'exemples pour ça...
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(direct_proof_principle, DOWN)
        self.play(Write(direct_proof_example), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(direct_proof_title), FadeOut(direct_proof_principle), FadeOut(direct_proof_example), run_time=Durations.animations)

        # 2. Preuve par contraposée
        contrapositive_proof_title = Text("Preuve par contraposée", font_size=32, color=Colors.text).next_to(title_obj, DOWN)
        self.play(Write(contrapositive_proof_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        contrapositive_proof_principle = Tex("""
            \\begin{flushleft}
            \\textbf{Principe :} Pour prouver une implication $P \\implies Q$, on prouve sa contraposée $\\neg Q \\implies \\neg P$.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(contrapositive_proof_title, DOWN, buff=0.5)
        self.play(Write(contrapositive_proof_principle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        contrapositive_proof_example = Tex("""
            \\begin{flushleft}
            \\textbf{Exemple :} Idem, pas le temps de faire un exemple. Mais c'est le même principe que pour la preuve que $n^2 \\mid 2 \\implies n \\mid 2$.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(contrapositive_proof_principle, DOWN)
        self.play(Write(contrapositive_proof_example), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(contrapositive_proof_title), FadeOut(contrapositive_proof_principle), FadeOut(contrapositive_proof_example), run_time=Durations.animations)

        # 3. Preuve par l'absurde
        absurd_proof_title = Text("Preuve par l'absurde", font_size=32, color=Colors.text).next_to(title_obj, DOWN)
        self.play(Write(absurd_proof_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        absurd_proof_principle = Tex("""
            \\begin{flushleft}
            \\textbf{Principe :} Pour prouver une proposition $P$, on suppose que $\\neg P$ est vrai et on montre que cela conduit à une contradiction.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(absurd_proof_title, DOWN, buff=0.5)
        self.play(Write(absurd_proof_principle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        absurd_proof_example = Tex("""
            \\begin{flushleft}
            \\textbf{Exemple :} La preuve que $\\sqrt{2}$ est irrationnel (si $\\sqrt2=\\frac{p}{q}$ avec $p,q$ entiers premiers entre eux, alors $2q^2=p^2$ donc $p$ est pair, donc $q$ est pair, ce qui est une contradiction).
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(absurd_proof_principle, DOWN)
        self.play(Write(absurd_proof_example), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(absurd_proof_title), FadeOut(absurd_proof_principle), FadeOut(absurd_proof_example), run_time=Durations.animations)

        # 4. Preuve par récurrence
        induction_proof_title = Text("Preuve par récurrence", font_size=32, color=Colors.text).next_to(title_obj, DOWN)
        self.play(Write(induction_proof_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        induction_proof_principle = Tex("""
            \\begin{flushleft}
            \\textbf{Principe :} Si $P(0)$ est vraie et que $\\forall n \\in \\mathbb{N}, P(n) \\implies P(n+1)$, alors $\\forall n \\in \\mathbb{N}, P(n)$ est vraie. Mais pourquoi ça marche ?
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(induction_proof_title, DOWN, buff=0.5)#TODO bullet points
        self.play(Write(induction_proof_principle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        induction_proof_proof = Tex("""
            \\begin{flushleft}
            \\textbf{Preuve :} Soit $S = \\{ n \\in \\mathbb{N} \\mid P(n) \\text{ est fausse} \\}$. Si $S$ est non vide, alors il admet un plus petit élément $m$ (par le principe de bien ordonnancement). Comme $m \\neq 0$, on a $m-1 \\in \\mathbb{N}$ et donc $P(m-1)$ est vraie. Par hypothèse, cela implique que $P(m)$ est vraie, ce qui est une contradiction. Donc $S$ est vide et $P(n)$ est vraie pour tout $n$.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(induction_proof_principle, DOWN)
        self.play(Write(induction_proof_proof), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(induction_proof_title), FadeOut(induction_proof_principle), FadeOut(induction_proof_proof), run_time=Durations.animations)

        # 5. Preuve par cas
        case_proof_title = Text("Preuve par cas", font_size=32, color=Colors.text).next_to(title_obj, DOWN)
        self.play(Write(case_proof_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        case_proof_principle = Tex("""
            \\begin{flushleft}
            \\textbf{Principe :} Pour prouver une proposition $P$, on divise la situation en plusieurs cas exhaustifs et on prouve $P$ dans chaque cas.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(case_proof_title, DOWN, buff=0.5)
        self.play(Write(case_proof_principle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        case_proof_example = Tex("""
            \\begin{flushleft}
            \\textbf{Exemple :} Preuve que pour tout entier $n$, $n^2 \\equiv 0 \\text{ ou } 1 \\mod 4$. On considère les cas $n \\equiv 0, 1, 2, 3 \\mod 4$.
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(case_proof_principle, DOWN)
        self.play(Write(case_proof_example), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(case_proof_title), FadeOut(case_proof_principle), FadeOut(case_proof_example), run_time=Durations.animations)

        # 6. Analyse-synthèse
        analysis_synthesis_title = Text("Analyse-synthèse", font_size=32, color=Colors.text).next_to(title_obj, DOWN)
        self.play(Write(analysis_synthesis_title), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        analysis_synthesis_principle = Tex("""
            \\begin{flushleft}
            \\textbf{Principe :}
            \\begin{itemize}
                \\item \\textbf{Analyse :} On part du principe que la proposition est vraie pour x, et on trouve des contraintes sur x.
                \\item \\textbf{Synthèse :} On vérifie que si x satisfait les contraintes, alors la proposition est vraie.
            \\end{itemize}
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(analysis_synthesis_title, DOWN, buff=0.5)
        self.play(Write(analysis_synthesis_principle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        analysis_synthesis_example = Tex("""
            \\begin{flushleft}
            \\textbf{Exemple :} Les problèmes de maximum, on veut trouver le plus grand X tel que P(X) est vraie.
            \\begin{itemize}
                \\item \\textbf{Analyse :} On suppose P(X) vraie. On en déduit des contraintes sur X, par exemple $X \\leq Y$.
                \\item \\textbf{Synthèse :} On vérifie que si X satisfait les contraintes, alors P(X) est vraie.
            \\end{itemize}
            \\end{flushleft}
        """, font_size=28, color=Colors.text).next_to(analysis_synthesis_principle, DOWN)
        self.play(Write(analysis_synthesis_example), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()
        self.play(FadeOut(analysis_synthesis_title), FadeOut(analysis_synthesis_principle), FadeOut(analysis_synthesis_example), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.next_slide()