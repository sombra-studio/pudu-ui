from dataclasses import dataclass, field

from pudu_ui.colors import GRAY, LIGHTER_GRAY
from pudu_ui.styles.buttons import ButtonStyle, default_button_style
from pudu_ui.styles.fonts import FontStyle, h2, p1
from pudu_ui.styles.frames import FrameStyle


def dft_bg_style():
    style = FrameStyle(
        start_color=LIGHTER_GRAY,
        border_width=2,
        border_color=GRAY
    )
    return style


def dft_title_style():
    style = h2()
    return style


def dft_description_style():
    style = p1()
    return style


def dft_btn_1_style():
    style = default_button_style()
    return style


@dataclass
class PopUpStyle:
    background_style: FrameStyle = field(default_factory=dft_bg_style)
    title_style: FontStyle = field(default_factory=dft_title_style)
    description_style: FontStyle = field(default_factory=dft_description_style)
    btn_1_style: ButtonStyle = field(default_factory=dft_btn_1_style)


def default_popup_style():
    return PopUpStyle()
