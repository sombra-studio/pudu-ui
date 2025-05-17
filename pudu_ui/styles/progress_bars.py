from dataclasses import dataclass, field


from pudu_ui.colors import *
from pudu_ui.styles.frames import FrameStyle


DEFAULT_PROGRESS_BAR_HEIGHT = 6
DEFAULT_PROGRESS_BAR_CORNER_RADIUS = DEFAULT_PROGRESS_BAR_HEIGHT // 2


#------------------------------------------------------------------------------
# Factory functions

def default_left_frame_style() -> FrameStyle:
    style = FrameStyle()
    style.set_uniform_radius(DEFAULT_PROGRESS_BAR_CORNER_RADIUS)
    style.set_solid_color(LIGHT_PURPLE)
    return style


def default_right_frame_style() -> FrameStyle:
    style = FrameStyle()
    style.set_uniform_radius(DEFAULT_PROGRESS_BAR_CORNER_RADIUS)
    style.set_solid_color(LIGHT_GRAY)
    return style

#------------------------------------------------------------------------------


@dataclass
class ProgressBarStyle:
    left_frame_style: FrameStyle = field(
        default_factory=default_left_frame_style
    )
    right_frame_style: FrameStyle = field(
        default_factory=default_right_frame_style
    )


def default_progress_bar_style() -> ProgressBarStyle:
    return ProgressBarStyle()
