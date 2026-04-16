from dataclasses import dataclass, field


from pudu_ui.colors import (
    DARK_GRAY, GRAY, LIGHT_GRAY, PRIMARY_BTN_FONT_COLOR,
    SECONDARY_BTN_FOCUS_BG_COLOR,
    SECONDARY_BTN_FOCUS_FONT_COLOR,
    SECONDARY_BTN_FONT_COLOR,
    SECONDARY_BTN_HOVER_BG_COLOR,
    SECONDARY_BTN_HOVER_FONT_COLOR
)
from pudu_ui.styles.arrows import ArrowStyle
from pudu_ui.styles.buttons import (
    ButtonStyle, DEFAULT_BTN_CORNER_RADIUS,
    dft_btn_focus_style, dft_btn_hover_style
)
from pudu_ui.styles.fonts import FontStyle, p1
from pudu_ui.styles.frames import FrameStyle, default_frame_style


FOCUS_FRAME_BORDER_WIDTH = 2
ITEM_RADIUS = 10


def dft_trg_arrow_style() -> ArrowStyle:
    style = ArrowStyle(color=LIGHT_GRAY, thickness=1.5)
    return style


@dataclass
class TriggerStyle:
    frame_style: FrameStyle = field(default_factory=default_frame_style)
    font_style: FontStyle = field(default_factory=p1)
    frame_visible: bool = False
    arrow_style: ArrowStyle = field(default_factory=dft_trg_arrow_style)


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


def dft_item_style() -> ButtonStyle:
    style = ButtonStyle()
    style.frame_visible = False
    style.font_style = p1()
    style.font_style.color = PRIMARY_BTN_FONT_COLOR
    return style


def dft_container_style() -> FrameStyle:
    style = FrameStyle(
        start_color=DARK_GRAY,
        border_color=GRAY,
        border_width=1
    )
    return style


@dataclass
class DropdownStyle:
    trigger_style: TriggerStyle = field(default_factory=dft_trigger_style)
    menu_container_style: FrameStyle = field(
        default_factory=dft_container_style
    )
    items_style: ButtonStyle = field(default_factory=dft_item_style)


def default_dropdown_style():
    return DropdownStyle()


def dft_dropdown_hover_style():
    style = DropdownStyle(
        trigger_style=dft_trigger_hover_style(),
        items_style=dft_btn_hover_style()
    )
    style.items_style.set_uniform_radius(ITEM_RADIUS)
    return style


def dft_dropdown_focus_style():
    style = DropdownStyle(
        trigger_style=dft_trigger_focus_style(),
        items_style=dft_btn_focus_style()
    )
    style.items_style.set_uniform_radius(ITEM_RADIUS)
    return style

