from dataclasses import dataclass


@dataclass
class Color:
    r: int = 0
    g: int = 0
    b: int = 0


WHITE = Color(r=255, g=255, b=255)
GRAY = Color(r=122, g=122, b=122)
BLACK = Color(r=0, g=0, b=0)
PURPLE = Color(r=94, g=21, b=101)
LIGHT_PURPLE = Color(r=108, g=24, b=116)
LIGHTER_PURPLE = Color(r=122, g=27, b=131)
