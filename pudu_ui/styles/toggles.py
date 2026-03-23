from dataclasses import dataclass, field

from pudu_ui.colors import (
    DARK_GRAY, GradientDirection, PURPLE, DARK_PURPLE,
    DARKER_PURPLE
)
from pudu_ui.styles.frames import FrameStyle


def dft_bg_style() -> FrameStyle:
    style = FrameStyle(
        start_color=DARKER_PURPLE,
        end_color=DARKER_PURPLE,
        gradient_direction=GradientDirection.HORIZONTAL
    )
    style.set_uniform_radius()
    return style


def thumb_style() -> FrameStyle:
    style = FrameStyle()
    return style


@dataclass
class ToggleStyle:
    background_style: FrameStyle = field(default_factory=dft_bg_style)
    thumb_style: FrameStyle = field(default_factory=thumb_style)


def dft_toggle_style() -> ToggleStyle:
    return ToggleStyle()
