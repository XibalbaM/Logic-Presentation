from manim import *
from common import *

class Basics(Scene):
    """
    1. Propositions et connecteurs logiques de base
    2. L'égalité
    3. Tables de vérité
    4. Implications et équivalences
    5. Quantificateurs
    6. Comment prouver ?
    7. Quelques problèmes 
    """
    #TODO predicates
    #TODO construction ?
    def construct(self):

        # title = Text("Partie 1: Les bases", font_size=48, color=Colors.text)
        # self.play(Write(title), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.play(FadeOut(title, shift = UP * 3), run_time=Durations.animations)

        section_1_title = Text("Propositions et connecteurs", font_size=36, color=Colors.text).move_to(UP * 3)
        self.play(Write(section_1_title), run_time=Durations.animations)
        definition_subtitle = Text("Définitions", font_size=32, color=Colors.text).next_to(section_1_title, DOWN)
        examples_subtitle = Text("Exemples", font_size=32, color=Colors.text).next_to(section_1_title, DOWN)
        subtitle = definition_subtitle.copy()
        # self.play(Write(subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_1_definitions()
        # self.play(Transform(subtitle, examples_subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_1_examples()

        # section_2_title = Text("L'égalité", font_size=36, color=Colors.text).move_to(UP * 3)
        # self.play(Transform(section_1_title, section_2_title), Transform(subtitle, definition_subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        right_cheatSheet = self.section_2_definitions()
        # self.play(Transform(subtitle, examples_subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_2_examples()

        # section_3_title = Text("Tables de vérité", font_size=36, color=Colors.text).move_to(UP * 3)
        # self.play(Transform(section_1_title, section_3_title), FadeOut(subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_3()

        section_4_title = Text("Implications", font_size=36, color=Colors.text).move_to(UP * 3)
        self.play(Transform(section_1_title, section_4_title), Transform(subtitle, definition_subtitle), FadeIn(subtitle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.section_4_definitions(right_cheatSheet)
        self.play(Transform(subtitle, examples_subtitle), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.section_4_examples()

        # section_5_title = Text("Quantificateurs", font_size=36, color=Colors.text).move_to(UP * 3)
        # self.play(Transform(section_1_title, section_5_title), Transform(subtitle, definition_subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_5_definitions()
        # self.play(Transform(subtitle, examples_subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_5_examples()

        # section_6_title = Text("Comment prouver ?", font_size=36, color=Colors.text).move_to(UP * 3)
        # self.play(Transform(section_1_title, section_6_title), FadeOut(subtitle), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_6()

        # section_7_title = Text("Quelques problèmes", font_size=36, color=Colors.text).move_to(UP * 3)
        # self.play(Transform(section_1_title, section_7_title), run_time=Durations.animations)
        # self.wait(Durations.pauses)
        # self.section_7()

    def section_1_definitions(self):
        definitions = [
            "Proposition : Une proposition $P$ est un énoncé qui est soit vrai, soit faux.",
            "Négation : La négation d'une proposition $P$, notée $\\neg P$, est vraie si et seulement si $P$ est fausse.",
            "Conjonction : La conjonction de deux propositions $P$ et $Q$, notée $P \\land Q$, est vraie si et seulement si $P$ et $Q$ sont toutes deux vraies.",
            "Disjonction : La disjonction de deux propositions $P$ et $Q$, notée $P \\lor Q$, est vraie si au moins une des propositions $P$ ou $Q$ est vraie."
        ]
        definition_texts = VGroup(*[Tex("\\begin{flushleft}" + defn + "\\end{flushleft}", font_size=28, color=Colors.text) for defn in definitions])
        definition_texts.arrange(DOWN, aligned_edge=LEFT)
        for defn_text in definition_texts:
            self.play(Write(defn_text), run_time=Durations.animations)
            self.wait(Durations.pauses)
        cheatSheet = [
            "Proposition : $P$, $Q$",
            "Négation : $\\neg P$",
            "Conjonction : $P \\land Q$",
            "Disjonction : $P \\lor Q$"
        ]
        cheatSheet_texts = VGroup(*[Tex("\\begin{flushleft}" + item + "\\end{flushleft}", font_size=28, color=Colors.text) for item in cheatSheet])
        cheatSheet_texts.arrange(DOWN, aligned_edge=LEFT).to_edge(UP + LEFT)
        self.play(Transform(definition_texts, cheatSheet_texts))
        cheatSheet_box = SurroundingRectangle(cheatSheet_texts, buff=0.1, color=Colors.text)
        self.play(Write(cheatSheet_box))
        self.wait(Durations.pauses)
    
    def section_1_examples(self):
        #TODO add counterexamples
        examples = Tex("""
                   \\begin{itemize}
                    \\item $P$ : \"On est jeudi.\"
                    \\item $Q$ : \"Il fait beau.\"
                    \\item $\\neg P \\land Q$ : \"On n'est pas jeudi, mais il fait beau.\"
                    \\item $P \\lor \\neg Q$ : \"On est jeudi ou il ne fait pas beau.\"
                   \\end{itemize}""",
                font_size=28, color=Colors.text)
        self.play(Write(examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        other_examples = Tex("""
                        \\begin{itemize}
                           \\item $2 + 2 = 4$
                           \\item $4 + 2 = 42$
                           \\item $3 > 5$
                           \\item $f$ est croissante sur $\\mathbb{R}$
                       \\end{itemize}""",
                       font_size=28, color=Colors.text)
        self.play(Transform(examples, other_examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        other_examples_2 = Tex("""
                        \\begin{flushleft}
                        Soient $A$ et $B$ des propositions quelconques :
                        \\begin{itemize}
                            \\item $A \\lor \\neg A$ est toujours vrai (tautologie).
                            \\item $A \\land \\neg A$ est toujours faux (contradiction).
                            \\item $A = B$ signifie que $A$ et $B$ ont la même valeur de vérité.
                            \\item $A = B$ est donc aussi une proposition.
                        \\end{itemize}
                        \\end{flushleft}""",
                          font_size=28, color=Colors.text)
        self.play(Transform(examples, other_examples_2), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
    
    def section_2_definitions(self):
        definitions = [
            "Égalité \"interne\" ou équivalence : Deux propositions $P$ et $Q$ sont équivalentes, notées $P = Q$ ou $P \\iff Q$, si elles ont la même valeur de vérité. L'objet \" $P = Q$ \" est lui-même une proposition.",
            "Égalité \"externe\" ou définitionnelle : Deux propositions $A$ et $B$ sont égales, notées $A \\equiv B$, si ce n'est en fait qu'une seule proposition. $A \\equiv B$ n'est pas une proposition, car elle est forcément vraie, par définition. On peut alors remplacer $A$ par $B$ partout sans changer la valeur de vérité."
            "Vrai et faux : On note $\\top$ la proposition toujours vraie, et $\\bot$ la proposition toujours fausse."
        ]
        definition_texts = VGroup(*[Tex("\\begin{flushleft}" + defn + "\\end{flushleft}", font_size=28, color=Colors.text) for defn in definitions])
        definition_texts.arrange(DOWN, aligned_edge=LEFT)
        for defn_text in definition_texts:
            self.play(Write(defn_text), run_time=Durations.animations)
            self.wait(Durations.pauses)
        cheatSheet = [
            "Équivalence : $P \\iff Q$",
            "Définition : $A \\equiv B$",
            "Vrai : $\\top$, Faux : $\\bot$",
        ]
        cheatSheet_texts = VGroup(*[Tex("\\begin{flushleft}" + item + "\\end{flushleft}", font_size=28, color=Colors.text) for item in cheatSheet])
        cheatSheet_texts.arrange(DOWN, aligned_edge=RIGHT).to_edge(UP + RIGHT)
        self.play(Transform(definition_texts, cheatSheet_texts))
        cheatSheet_box = SurroundingRectangle(cheatSheet_texts, buff=0.1, color=Colors.text)
        self.play(Write(cheatSheet_box))
        self.wait(Durations.pauses)
        return (cheatSheet_texts, cheatSheet_box)
    
    def section_2_examples(self):
        examples = Tex("""
                   \\begin{itemize}
                    \\item Soient $P$ et $Q$ deux propositions. Alors, $P \\iff Q$ est vraie si $P$ et $Q$ sont toutes deux vraies ou toutes deux fausses.
                    \\item Soient $R$ et $S$ deux propositions. On peut définir la nouvelle proposition $T$ par $T \\equiv R \\land S$. Ainsi, $T$ est vraie si et seulement si $R$ et $S$ sont toutes deux vraies.
                   \\end{itemize}""",
                font_size=28, color=Colors.text)
        self.play(Write(examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        other_examples = Tex("""
                        \\begin{flushleft}
                        On peut utiliser l'égalité définitionnelle pour donner des identités :
                        \\begin{itemize}
                            \\item $P \\equiv \\neg(\\neg P)$
                            \\item $P \\land Q \\equiv Q \\land P$
                            \\item $P \\lor Q \\equiv Q \\lor P$
                            \\item $P \\land (Q \\lor R) \\equiv (P \\land Q) \\lor (P \\land R)$
                        \\end{itemize}
                        \\end{flushleft}""",
                       font_size=28, color=Colors.text)
        self.play(Transform(examples, other_examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercises = Tex("""
                        \\begin{flushleft}
                        Exercice : Donnez des expressions plus simples définitionnellement équivalentes à :
                        \\begin{itemize}
                            \\item $P \\land (Q \\land R)$
                            \\item $P \\lor (Q \\lor R)$
                            \\item $P \\lor \\bot$
                            \\item $P \\land \\top$
                        \\end{itemize}
                        \\end{flushleft}""",
                       font_size=28, color=Colors.text)
        self.play(Transform(examples, exercises), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(examples), run_time=Durations.animations)
        self.wait(Durations.pauses)
    
    def section_3(self):
        table = Table(
            [["$P$", "$Q$", "$\\neg P$", "$P \\land Q$", "$P \\lor Q$"],
             ["V", "V", "F", "V", "V"],
             ["V", "F", "F", "F", "V"],
             ["F", "V", "V", "F", "V"],
             ["F", "F", "V", "F", "F"]], 
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Write(table), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(table), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices = Tex("""\\begin{flushleft}
            Deux exercices : simplifiez les expressions suivantes :
            \\begin{itemize}
            \\item $\\neg(P \\land Q)$
            \\item $\\neg(P \\lor Q)$
            \\end{itemize}
        \\end{flushleft}""", font_size=28, color=Colors.text)
        self.play(Write(exercices), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(exercices), run_time=Durations.animations)
        exercise_one_one = Table(
            [["$P$", "$Q$", "$P \\land Q$", "$\\neg(P \\land Q)$", "?"],
             ["V", "V", "?", "?", "?"],
             ["V", "F", "?", "?", "?"],
             ["F", "V", "?", "?", "?"],
             ["F", "F", "?", "?", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Write(exercise_one_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices_one_two = Table(
            [["$P$", "$Q$", "$P \\land Q$", "$\\neg(P \\land Q)$", "?"],
             ["V", "V", "V", "?", "?"],
             ["V", "F", "F", "?", "?"],
             ["F", "V", "F", "?", "?"],
             ["F", "F", "F", "?", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercices_one_two), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices_one_three = Table(
            [["$P$", "$Q$", "$P \\land Q$", "$\\neg(P \\land Q)$", "?"],
             ["V", "V", "V", "F", "?"],
             ["V", "F", "F", "V", "?"],
             ["F", "V", "F", "V", "?"],
             ["F", "F", "F", "V", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercices_one_three), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices_one_solution = Table(
            [["$P$", "$Q$", "$P \\land Q$", "$\\neg(P \\land Q)$", "$\\neg P \\lor \\neg Q$"],
             ["V", "V", "V", "F", "F"],
             ["V", "F", "F", "V", "V"],
             ["F", "V", "F", "V", "V"],
             ["F", "F", "F", "V", "V"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercices_one_solution), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercise_two_one = Table(
            [["$P$", "$Q$", "$P \\lor Q$", "$\\neg(P \\lor Q)$", "?"],
             ["V", "V", "?", "?", "?"],
             ["V", "F", "?", "?", "?"],
             ["F", "V", "?", "?", "?"],
             ["F", "F", "?", "?", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercise_two_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices_two_two = Table(
            [["$P$", "$Q$", "$P \\lor Q$", "$\\neg(P \\lor Q)$", "?"],
             ["V", "V", "V", "?", "?"],
             ["V", "F", "V", "?", "?"],
             ["F", "V", "V", "?", "?"],
             ["F", "F", "F", "?", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercices_two_two), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices_two_three = Table(
            [["$P$", "$Q$", "$P \\lor Q$", "$\\neg(P \\lor Q)$", "?"],
             ["V", "V", "V", "F", "?"],
             ["V", "F", "V", "F", "?"],
             ["F", "V", "V", "F", "?"],
             ["F", "F", "F", "V", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercices_two_three), run_time=Durations.animations)
        self.wait(Durations.pauses)
        exercices_two_solution = Table(
            [["$P$", "$Q$", "$P \\lor Q$", "$\\neg(P \\lor Q)$", "$\\neg P \\land \\neg Q$"],
             ["V", "V", "V", "F", "F"],
             ["V", "F", "V", "F", "F"],
             ["F", "V", "V", "F", "F"],
             ["F", "F", "F", "V", "V"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(exercise_one_one, exercices_two_solution), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(exercise_one_one), run_time=Durations.animations)
        self.wait(Durations.pauses)

    def section_4_definitions(self, right_cheatSheet):
        definitions = [
            "Implication : L'implication entre deux propositions $P$ et $Q$, notée $P \\implies Q$, est vraie si et seulement si soit $P$ est fausse, soit $Q$ est vraie (ou les deux).",
            "Nouvelle définition de l'équivalence : Deux propositions $P$ et $Q$ sont équivalentes, notées $P \\iff Q$, si les deux implications $P \\implies Q$ et $Q \\implies P$ sont vraies."
        ]
        definition_texts = VGroup(*[Tex("\\begin{flushleft}" + defn + "\\end{flushleft}", font_size=28, color=Colors.text) for defn in definitions])
        definition_texts.arrange(DOWN, aligned_edge=LEFT)
        for defn_text in definition_texts:
            self.play(Write(defn_text), run_time=Durations.animations)
            self.wait(Durations.pauses)
        newCheatSheetElements = [
            "Implication : $P \\implies Q$"
        ]
        (oldCheatSheet, oldCheatSheetBox) = right_cheatSheet
        newCheatSheet_texts = VGroup(*[Tex("\\begin{flushleft}" + item + "\\end{flushleft}", font_size=28, color=Colors.text) for item in newCheatSheetElements])
        newCheatSheet = oldCheatSheet.add(newCheatSheet_texts)
        newCheatSheet.arrange(DOWN, aligned_edge=RIGHT).to_edge(UP + RIGHT)
        self.play(Transform(definition_texts, newCheatSheet_texts), Transform(oldCheatSheetBox, SurroundingRectangle(newCheatSheet, buff=0.1, color=Colors.text)))
        self.wait(Durations.pauses)

    def section_4_examples(self):
        # On construit la table de vérité de l'implication (ligne par ligne)
        implication_one = Table(
            [["$P$", "$Q$", "$P \\implies Q$"],
             ["V", "V", "?"],
             ["V", "F", "?"],
             ["F", "V", "?"],
             ["F", "F", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Write(implication_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        implication_two = Table(
            [["$P$", "$Q$", "$P \\implies Q$"],
                ["V", "V", "V"],
                ["V", "F", "?"],
                ["F", "V", "?"],
                ["F", "F", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(implication_one, implication_two), run_time=Durations.animations)
        self.wait(Durations.pauses)
        implication_three = Table(
            [["$P$", "$Q$", "$P \\implies Q$"],
                ["V", "V", "V"],
                ["V", "F", "F"],
                ["F", "V", "?"],
                ["F", "F", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(implication_one, implication_three), run_time=Durations.animations)
        self.wait(Durations.pauses)
        implication_four = Table(
            [["$P$", "$Q$", "$P \\implies Q$"],
                ["V", "V", "V"],
                ["V", "F", "F"],
                ["F", "V", "V"],
                ["F", "F", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(implication_one, implication_four), run_time=Durations.animations)
        self.wait(Durations.pauses)
        implication_five = Table(
            [["$P$", "$Q$", "$P \\implies Q$"],
                ["V", "V", "V"],
                ["V", "F", "F"],
                ["F", "V", "V"],
                ["F", "F", "V"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(implication_one, implication_five), run_time=Durations.animations)
        self.wait(Durations.pauses)
        # On remarque que l'implication est équivalente à ¬P ∨ Q
        implication_six = Table(
            [["$P$", "$Q$", "$P \\implies Q$", "$\\neg P \\lor Q$"],
                ["V", "V", "V", "V"],
                ["V", "F", "F", "F"],
                ["F", "V", "V", "V"],
                ["F", "F", "V", "V"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(implication_one, implication_six), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(implication_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        # On montre que A \iff B \equiv (A \implies B) \land (B \implies A) (étape par étape)
        iff_one = Table(
            [["$A$", "$B$", "$A \\implies B$", "$B \\implies A$", "$A \\iff B$"],
                ["V", "V", "?", "?", "?"],
                ["V", "F", "?", "?", "?"],
                ["F", "V", "?", "?", "?"],
                ["F", "F", "?", "?", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Write(iff_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        iff_two = Table(
            [["$A$", "$B$", "$A \\implies B$", "$B \\implies A$", "$A \\iff B$"],
                ["V", "V", "V", "V", "?"],
                ["V", "F", "F", "V", "?"],
                ["F", "V", "V", "F", "?"],
                ["F", "F", "V", "V", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(iff_one, iff_two), run_time=Durations.animations)
        self.wait(Durations.pauses)
        iff_three = Table(
            [["$A$", "$B$", "$A \\implies B$", "$B \\implies A$", "$A \\iff B$"],
                ["V", "V", "V", "V", "V"],
                ["V", "F", "F", "V", "F"],
                ["F", "V", "V", "F", "F"],
                ["F", "F", "V", "V", "V"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(iff_one, iff_three), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(iff_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        # On montre que A \implies B \equiv \neg B \implies \neg A (étape par étape)
        contrapositive_one = Table(
            [["$A$", "$B$", "$A \\implies B$", "$\\neg B \\implies \\neg A$"],
                ["V", "V", "?", "?"],
                ["V", "F", "?", "?"],
                ["F", "V", "?", "?"],
                ["F", "F", "?", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Write(contrapositive_one), run_time=Durations.animations)
        self.wait(Durations.pauses)
        contrapositive_two = Table(
            [["$A$", "$B$", "$A \\implies B$", "$\\neg B \\implies \\neg A$"],
                ["V", "V", "V", "?"],
                ["V", "F", "F", "?"],
                ["F", "V", "V", "?"],
                ["F", "F", "V", "?"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(contrapositive_one, contrapositive_two), run_time=Durations.animations)
        self.wait(Durations.pauses)
        contrapositive_three = Table(
            [["$A$", "$B$", "$A \\implies B$", "$\\neg B \\implies \\neg A$"],
                ["V", "V", "V", "V"],
                ["V", "F", "F", "F"],
                ["F", "V", "V", "V"],
                ["F", "F", "V", "V"]],
            include_outer_lines=True,
            line_config={"stroke_color": Colors.text},
            element_to_mobject=lambda x: Tex(x, font_size=28, color=ColorFromTruthValue(x))
        ).scale(0.7)
        self.play(Transform(contrapositive_one, contrapositive_three), run_time=Durations.animations)
        self.wait(Durations.pauses)
        self.play(FadeOut(contrapositive_one), run_time=Durations.animations)
        self.wait(Durations.pauses)