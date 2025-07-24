from manim import *
from .config import MAIN_COLOR, FONT

def title_text(text):
    return Text(text, font=FONT, color=MAIN_COLOR).scale(0.9).to_edge(UP)
