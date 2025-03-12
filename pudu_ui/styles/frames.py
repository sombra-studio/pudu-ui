from dataclasses import dataclass, field
from pudu_ui import colors
from pudu_ui.colors import Color, GradientDirection


#------------------------------------------------------------------------------
# Factory functions
def end_gradient_color():
    return colors.DARK_PURPLE

def background_color():
    return colors.PURPLE

def focus_color():
    return colors.LIGHT_PURPLE

def hover_color():
    return colors.LIGHTER_PURPLE

def default_frame_style():
    return FrameStyle()

#------------------------------------------------------------------------------


@dataclass
class FrameStyle:
    start_color: Color = field(default_factory=background_color)
    end_color: Color = None
    opacity: int = 255
    radius_top_left: float = 0
    radius_top_right: float = 0
    radius_bottom_left: float = 0
    radius_bottom_right: float = 0
    gradient_direction: GradientDirection = GradientDirection.VERTICAL
