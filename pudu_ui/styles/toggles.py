from dataclasses import dataclass, field


from pudu_ui.colors import (
    DARKER_GRAY, DARK_GRAY, GradientDirection, LIGHT_GRAY, PURPLE, DARK_PURPLE,
    DARKER_PURPLE
)
from pudu_ui.styles.frames import FrameStyle


DEFAULT_TOGGLE_THUMB_RADIUS = 12
DEFAULT_TOGGLE_RADIUS = 14
DEFAULT_TOGGLE_THUMB_BORDER_WIDTH = 2


def dft_on_bg_style() -> FrameStyle:
    style = FrameStyle(
        start_color=DARKER_PURPLE,
        end_color=DARK_PURPLE,
        gradient_direction=GradientDirection.HORIZONTAL
    )
    style.set_uniform_radius(DEFAULT_TOGGLE_RADIUS)
    return style


def dft_on_thumb_style() -> FrameStyle:
    style = FrameStyle(start_color=PURPLE)
    style.set_uniform_radius(DEFAULT_TOGGLE_THUMB_RADIUS)
    return style


def dft_off_bg_style() -> FrameStyle:
    style = dft_on_bg_style()
    style.start_color = DARK_GRAY
    style.end_color = DARKER_GRAY
    return style


def dft_off_thumb_style() -> FrameStyle:
    style = dft_on_thumb_style()
    style.start_color = LIGHT_GRAY
    return style


@dataclass
class ToggleStyle:
    background_style: FrameStyle = field(default_factory=dft_on_bg_style)
    thumb_style: FrameStyle = field(default_factory=dft_on_thumb_style)


def dft_on_toggle_style() -> ToggleStyle:
    return ToggleStyle()


def dft_off_toggle_style() -> ToggleStyle:
    style = ToggleStyle(
        background_style=dft_off_bg_style(),
        thumb_style=dft_off_thumb_style()
    )
    return style


def dft_on_focus_toggle_style() -> ToggleStyle:
    style = dft_on_toggle_style()
    style.thumb_style.border_width = DEFAULT_TOGGLE_THUMB_BORDER_WIDTH
    return style


def dft_off_focus_toggle_style() -> ToggleStyle:
    style = dft_off_toggle_style()
    style.thumb_style.border_width = DEFAULT_TOGGLE_THUMB_BORDER_WIDTH
    return style
