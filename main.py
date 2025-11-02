from manim import *
from intro import Intro as IntroA
from basics import Basics as BasicsA
from maths import Maths as MathsA
from other import OtherDomains as OtherDomainsA
from axioms import Axioms as AxiomsA
from debated import Debated as DebatedA
from godel import Godel as GodelA
from outro import Outro as OutroA

class Intro(IntroA):
    def construct(self):
        super().construct()

class Basics(BasicsA):
    def construct(self):
        super().construct()

class Maths(MathsA):
    def construct(self):
        super().construct()

class OtherDomains(OtherDomainsA):
    def construct(self):
        super().construct()

class Axioms(AxiomsA):
    def construct(self):
        super().construct()

class Debated(DebatedA):
    def construct(self):
        super().construct()

class Godel(GodelA):
    def construct(self):
        super().construct()

class Outro(OutroA):
    def construct(self):
        super().construct()