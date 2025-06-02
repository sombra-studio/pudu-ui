from dataclasses import dataclass, field


from pudu_ui.colors import DARK_GRAY, PURPLE
from pudu_ui.styles.frames import FrameStyle
from pudu_ui.styles.progress_bars import ProgressBarStyle

DEFAULT_HANDLE_RADIUS = 10.0
DEFAULT_SLIDER_CORNER_RADIUS = 4.0


def default_bar_style():
    style = ProgressBarStyle(
        left_color=PURPLE, right_color=DARK_GRAY, border_width=0
    )
    style.set_uniform_radius(DEFAULT_SLIDER_CORNER_RADIUS)
    return style


def default_handle_style():
    style = FrameStyle()
    style.set_solid_color(PURPLE)
    style.set_uniform_radius(DEFAULT_HANDLE_RADIUS)
    return style

def default_slider_style():
    return SliderStyle()


@dataclass
class SliderStyle:
    bar_style: ProgressBarStyle = field(default_factory=default_bar_style)
    handle_style: FrameStyle = field(default_factory=default_handle_style)
