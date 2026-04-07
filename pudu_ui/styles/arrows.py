from dataclasses import dataclass, field

from pudu_ui.colors import LIGHTER_GRAY
from pudu_ui import Color


def default_arrow_color():
    return LIGHTER_GRAY


@dataclass
class ArrowStyle:
    color: Color = field(default_factory=default_arrow_color)
    opacity: int = 255
    thickness: float = 2.5


def default_arrow_style():
    return ArrowStyle()
