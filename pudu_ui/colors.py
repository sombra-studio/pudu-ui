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


class GradientDirection(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


WHITE = Color(r=255, g=255, b=255)
LIGHTER_GRAY = Color(220, 220, 220)
LIGHT_GRAY = Color(180, 180, 180)
GRAY = Color(r=122, g=122, b=122)
DARK_GRAY = Color(r=65, g=65, b=65)
DARKER_GRAY = Color(38, 38, 38)
BLACK = Color(r=0, g=0, b=0)

DARK_PURPLE = Color(75, 16, 80)
PURPLE = Color(94, 21, 101)
LIGHT_PURPLE = Color(r=108, g=24, b=116)
LIGHTER_PURPLE = Color(r=122, g=27, b=131)

MEDIUM_BLUE = Color(0, 91, 150)
LIGHT_BLUE_GREEN = Color(100, 151, 177)

DARK_RED = Color(r=125, g=0, b=0)
RED = Color(r=180, g=0, b=5)

PRIMARY_BTN_BG_COLOR = PURPLE
PRIMARY_BTN_HOVER_BG_COLOR = LIGHT_PURPLE
PRIMARY_BTN_FOCUS_BG_COLOR = LIGHT_PURPLE
PRIMARY_BTN_PRESS_BG_COLOR = DARK_PURPLE
PRIMARY_BTN_FONT_COLOR = LIGHTER_GRAY
PRIMARY_BTN_HOVER_FONT_COLOR = WHITE
PRIMARY_BTN_FOCUS_FONT_COLOR = WHITE
PRIMARY_BTN_PRESS_FONT_COLOR = GRAY

DEBUG_BORDER_COLOR = DARK_RED
