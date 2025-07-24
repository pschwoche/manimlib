from manim import *
from manimlib.texts import title_text
from manimlib.plots import standard_axes

class AbleitungScene(Scene):
    def construct(self):
        self.add(title_text("Was ist eine Ableitung?"))

        axes = standard_axes()
        graph = axes.plot(lambda x: x**2, color=BLUE)

        self.play(Create(axes), Create(graph))
        self.wait()
