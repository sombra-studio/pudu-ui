from dataclasses import dataclass, field


from pudu_ui.colors import *


DEFAULT_PROGRESS_BAR_WIDTH = 200
DEFAULT_PROGRESS_BAR_HEIGHT = 20
# DEFAULT_PROGRESS_BAR_CORNER_RADIUS = DEFAULT_PROGRESS_BAR_HEIGHT / 2.0
DEFAULT_PROGRESS_BAR_CORNER_RADIUS = 0.0
DEFAULT_PROGRESS_BAR_BORDER_WIDTH = 4

#------------------------------------------------------------------------------
# Factory functions

def default_left_color():
    return RED


def default_right_color():
    return BLACK


def default_border_color():
    return WHITE

#------------------------------------------------------------------------------

@dataclass
class ProgressBarStyle:
    left_color: Color = field(default_factory=default_left_color)
    right_color: Color = field(default_factory=default_right_color)
    opacity: int = 255
    radius_top_left: float = DEFAULT_PROGRESS_BAR_CORNER_RADIUS
    radius_top_right: float = DEFAULT_PROGRESS_BAR_CORNER_RADIUS
    radius_bottom_left: float = DEFAULT_PROGRESS_BAR_CORNER_RADIUS
    radius_bottom_right: float = DEFAULT_PROGRESS_BAR_CORNER_RADIUS
    border_width: int = 2
    border_color: Color = field(default_factory=default_border_color)

    def set_uniform_radius(self, radius: float):
        self.radius_top_left = radius
        self.radius_top_right = radius
        self.radius_bottom_left = radius
        self.radius_bottom_right = radius


def default_progress_bar_style() -> ProgressBarStyle:
    return ProgressBarStyle()
