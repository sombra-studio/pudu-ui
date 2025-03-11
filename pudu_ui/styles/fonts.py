from dataclasses import dataclass, field
from pudu_ui.colors import Color, BLACK
from pyglet.text import Weight
from typing import Union


#------------------------------------------------------------------------------
# Factory functions

def default_font_color():
    return BLACK

#------------------------------------------------------------------------------


@dataclass
class FontStyle:
    font_size: Union[float, int, str]
    font_name: str
    weight: Weight = Weight.NORMAL
    italic: bool = False
    color: Color  = field(default_factory=default_font_color)
    opacity: int = 255


# Header Styles

def h1():
    return FontStyle(font_size=23, font_name="Arial")


# Paragraph Styles

def p1():
    return FontStyle(font_size=23, font_name="Arial")


def p2():
    return FontStyle(font_size=18, font_name="Arial")


# Buttons Styles

def b1():
    return FontStyle(font_size=23, font_name="Arial")
