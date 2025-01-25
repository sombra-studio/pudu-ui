from dataclasses import dataclass
from pyglet.text import Weight
from typing import Union


@dataclass
class FontStyle:
    font_size: Union[float, int, str]
    font_name: str
    weight: Weight = Weight.NORMAL
    italic: bool = False
    color: tuple[int, int, int, int] = (0, 0, 0, 255)
    background_color: tuple[int, int, int, int] = None


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
