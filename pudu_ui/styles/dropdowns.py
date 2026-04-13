from dataclasses import dataclass, field


from pudu_ui import Color
from pudu_ui.colors import (
    LIGHT_GRAY, SECONDARY_BTN_FOCUS_BG_COLOR, SECONDARY_BTN_FOCUS_FONT_COLOR,
    SECONDARY_BTN_FONT_COLOR,
    SECONDARY_BTN_HOVER_BG_COLOR,
    SECONDARY_BTN_HOVER_FONT_COLOR
)
from pudu_ui.styles.buttons import (
    ButtonStyle, DEFAULT_BTN_CORNER_RADIUS, default_button_style,
    dft_btn_focus_style, dft_btn_hover_style
)
from pudu_ui.styles.frames import FrameStyle, default_frame_style


FOCUS_FRAME_BORDER_WIDTH = 2


def default_caret_color() -> Color:
    return LIGHT_GRAY


@dataclass
class TriggerStyle(ButtonStyle):
    frame_visible: bool = False
    caret_color: Color = field(default_factory=default_caret_color)


def dft_trigger_style() -> TriggerStyle:
    style = TriggerStyle()
    style.frame_style.set_uniform_radius(DEFAULT_BTN_CORNER_RADIUS)
    style.font_style.color = SECONDARY_BTN_FONT_COLOR
    return style


def dft_trigger_hover_style() -> TriggerStyle:
    style = dft_trigger_style()
    style.frame_visible = True
    style.frame_style.start_color = SECONDARY_BTN_HOVER_BG_COLOR
    style.font_style.color = SECONDARY_BTN_HOVER_FONT_COLOR
    return style


def dft_trigger_focus_style() -> TriggerStyle:
    style = dft_trigger_style()
    style.frame_visible = True
    style.frame_style.start_color = SECONDARY_BTN_FOCUS_BG_COLOR
    style.font_style.color = SECONDARY_BTN_FOCUS_FONT_COLOR
    return style


@dataclass
class DropdownStyle:
    trigger_style: TriggerStyle = field(default_factory=dft_trigger_style)
    menu_container_style: FrameStyle = field(
        default_factory=default_frame_style
    )
    items_style: ButtonStyle = field(default_factory=default_button_style)


def default_dropdown_style():
    return DropdownStyle()


def dft_dropdown_hover_style():
    style = DropdownStyle(
        trigger_style=dft_trigger_hover_style(),
        items_style=dft_btn_hover_style()
    )
    return style


def dft_dropdown_focus_style():
    style = DropdownStyle(
        trigger_style=dft_trigger_focus_style(),
        items_style=dft_btn_focus_style()
    )
    return style

