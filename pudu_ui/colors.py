from dataclasses import dataclass
from enum import Enum


@dataclass
class Color:
    r: int = 0
    g: int = 0
    b: int = 0

    def as_tuple(self) -> tuple[int, int, int]:
        return self.r, self.g, self.b

    def as_vec3(self) -> tuple[float, float, float]:
        return self.r / 255.0, self.g / 255.0, self.b / 255.0

    def as_vec4(self):
        return self.r / 255.0, self.g / 255.0, self.b / 255.0, 1.0

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.r == other.r and self.g == other.g and self.b == other.b
        return False

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            r = int(round(self.r * other))
            g = int(round(self.g * other))
            b = int(round(self.b * other))
            return Color(r=r, g=g, b=b)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)


class GradientDirection(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


WHITE = Color(255, 255, 255)
LIGHTER_GRAY = Color(220, 220, 220)
LIGHT_GRAY = Color(180, 180, 180)
GRAY = Color(122, 122, 122)
DARK_GRAY = Color(65, 65, 65)
DARKER_GRAY = Color(38, 38, 38)
BLACK = Color(0, 0, 0)

VIOLET = Color(240, 10, 178)

LIGHTER_PURPLE = Color(122, 27, 131)
LIGHT_PURPLE = Color(108, 24, 116)
PURPLE = Color(94, 21, 101)
DARK_PURPLE = Color(75, 16, 80)

MEDIUM_BLUE = Color(0, 91, 150)
BLUE = Color(14, 14, 232)

LIGHT_BLUE_GREEN = Color(100, 151, 177)
BLUE_GREEN = Color(3, 248, 252)

GREEN = Color(4, 194, 17)

YELLOW = Color(247, 235, 10)

ORANGE = Color(237, 151, 12)

RED = Color(230, 16, 15)
DARK_RED = Color(125, 0, 0)


PRIMARY_BTN_BG_COLOR = PURPLE
PRIMARY_BTN_HOVER_BG_COLOR = LIGHT_PURPLE
PRIMARY_BTN_FOCUS_BG_COLOR = LIGHT_PURPLE
PRIMARY_BTN_PRESS_BG_COLOR = DARK_PURPLE
PRIMARY_BTN_FONT_COLOR = LIGHTER_GRAY
PRIMARY_BTN_HOVER_FONT_COLOR = WHITE
PRIMARY_BTN_FOCUS_FONT_COLOR = WHITE
PRIMARY_BTN_PRESS_FONT_COLOR = GRAY

DEBUG_BORDER_COLOR = DARK_RED
DEBUG_TEXT_COLOR = LIGHT_GRAY
