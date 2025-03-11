from dataclasses import dataclass
from enum import Enum


@dataclass
class Color:
    r: int = 0
    g: int = 0
    b: int = 0


@dataclass
class ColorGradient:
    start_color: Color
    end_color:Color


class ColorType(Enum):
    SOLID = 1
    GRADIENT = 2


class GradientDirection(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


WHITE = Color(r=255, g=255, b=255)
GRAY = Color(r=122, g=122, b=122)
BLACK = Color(r=0, g=0, b=0)
PURPLE = Color(r=94, g=21, b=101)
LIGHT_PURPLE = Color(r=108, g=24, b=116)
LIGHTER_PURPLE = Color(r=122, g=27, b=131)
MEDIUM_BLUE = Color(0, 91, 150)
LIGHT_BLUE_GREEN = Color(100, 151, 177)

PRIMARY_BTN_BG_COLOR = PURPLE
PRIMARY_BTN_HOVER_BG_COLOR = LIGHT_PURPLE
PRIMARY_BTN_FOCUS_BG_COLOR = LIGHT_PURPLE
PRIMARY_BTN_PRESS_BG_COLOR = LIGHTER_PURPLE
PRIMARY_BTN_FONT_COLOR = WHITE

DEFAULT_FRAME_GRADIENT = ColorGradient(start_color=PURPLE, end_color=BLACK)
FOCUS_FRAME_GRADIENT = ColorGradient(start_color=LIGHT_PURPLE, end_color=BLACK)
HOVER_FRAME_GRADIENT = ColorGradient(
    start_color=LIGHTER_PURPLE, end_color=BLACK
)


