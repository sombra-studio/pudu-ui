from dataclasses import dataclass


from pudu_ui.colors import LIGHTER_GRAY
from pudu_ui import Color


@dataclass
class ArrowStyle:
    color: Color = LIGHTER_GRAY
    opacity: int = 255
    thickness: float = 2.5


def default_arrow_style():
    return ArrowStyle()
