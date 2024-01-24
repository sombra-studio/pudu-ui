from dataclasses import dataclass
from typing import Union


@dataclass
class FontStyle:
    font_size: Union[float, int, str]
    font_name: str
    bold: bool = False
    italic: bool = False
    color: tuple[int, int, int, int] = (0, 0, 0, 255)
    background_color: tuple[int, int, int, int] = None


P1 = FontStyle(font_size=23, font_name="Arial")
P2 = FontStyle(font_size=18, font_name="Arial")
