from manim import *
from types import SimpleNamespace

Colors = SimpleNamespace(
    text=WHITE,
    background=BLACK,
    true=GREEN,
    false=RED
)

Durations = SimpleNamespace(
    animations=0.01,
    pauses=0.02
)

def ColorFromTruthValue(value: str):
    if value == "V":
        return Colors.true
    elif value == "F":
        return Colors.false
    else:
        return Colors.text
    
def intro(scene: Scene, title_text: str):
    title = Text(title_text, font_size=48, color=Colors.text)
    scene.play(Write(title), run_time=Durations.animations)
    scene.wait(Durations.pauses)
    scene.play(FadeOut(title, shift=UP * 3), run_time=Durations.animations)