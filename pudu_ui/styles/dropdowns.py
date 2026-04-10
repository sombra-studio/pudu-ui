from dataclasses import dataclass, field


from pudu_ui import Color
from pudu_ui.colors import LIGHT_GRAY
from pudu_ui.styles.fonts import FontStyle, p1
from pudu_ui.styles.frames import FrameStyle, default_frame_style


def default_caret_color() -> Color:
    return LIGHT_GRAY


@dataclass
class DropdownItemStyle:
    background_style: FrameStyle = field(default_factory=default_frame_style)
    background_visible: bool = False
    font_style: FontStyle = field(default_factory=p1)


def default_dropdown_item_style() -> DropdownItemStyle:
    return DropdownItemStyle()


@dataclass
class DropdownStyle:
    trigger_style: FrameStyle = field(default_factory=default_frame_style)
    menu_container_style: FrameStyle = field(
        default_factory=default_frame_style
    )

    font_style: FontStyle = field(default_factory=p1)
    caret_color: Color = field(default_factory=default_caret_color)
    items_style: DropdownItemStyle = field(
        default_factory=default_dropdown_item_style
    )



def dft_dpdwn_item_hvr_style() -> DropdownItemStyle:
    return DropdownItemStyle()

def dft_dpdwn_item_focus_style() -> DropdownItemStyle:
    return DropdownItemStyle()


def default_dropdown_style():
    return DropdownStyle()


