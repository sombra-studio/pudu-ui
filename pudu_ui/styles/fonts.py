from dataclasses import dataclass, field
from pudu_ui.colors import Color, BLACK
from pyglet.text import Weight
from typing import Union


DEFAULT_FONT_SIZE = 23
DEFAULT_FONT_NAME = "Arial"

#------------------------------------------------------------------------------
# Factory functions

def default_font_color():
    return BLACK

#------------------------------------------------------------------------------


@dataclass
class FontStyle:
    font_size: Union[float, int, str] = DEFAULT_FONT_SIZE
    font_name: str = DEFAULT_FONT_NAME
    weight: Weight = Weight.NORMAL
    italic: bool = False
    color: Color  = field(default_factory=default_font_color)
    opacity: int = 255


# Header Styles

def h1():
    return FontStyle(font_size=32, font_name=DEFAULT_FONT_NAME)

def h2():
    style = h1()
    style.font_size = 24
    return style


# Paragraph Styles

def p1():
    return FontStyle(font_size=DEFAULT_FONT_SIZE, font_name=DEFAULT_FONT_NAME)


def p2():
    return FontStyle(font_size=18, font_name=DEFAULT_FONT_NAME)

def p3():
    style = p1()
    style.font_size = 16
    return style


# Buttons Styles

def b1():
    return FontStyle(font_size=DEFAULT_FONT_SIZE, font_name=DEFAULT_FONT_NAME)
