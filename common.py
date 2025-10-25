from manim import *
from types import SimpleNamespace

Colors = SimpleNamespace(
    text=BLACK,
    background=WHITE,
    true=GREEN,
    false=RED
)

Durations = SimpleNamespace(
    animations=1,
    pauses=2
)

def ColorFromTruthValue(value: str):
    if value == "V":
        return Colors.true
    elif value == "F":
        return Colors.false
    else:
        return Colors.text