from dataclasses import dataclass, field
from pudu_ui import colors
from pudu_ui.colors import Color, ColorType, ColorGradient, GradientDirection


#------------------------------------------------------------------------------
# Factory functions
def background_color():
    return colors.PURPLE

def focus_color():
    return colors.LIGHT_PURPLE

def hover_color():
    return colors.LIGHTER_PURPLE

def bg_gradient():
    return colors.DEFAULT_FRAME_GRADIENT

def focus_gradient():
    return colors.FOCUS_FRAME_GRADIENT

def hover_gradient():
    return colors.HOVER_FRAME_GRADIENT

def default_frame_style():
    return FrameStyle()

#------------------------------------------------------------------------------


@dataclass
class FrameStyle:
    background_color: Color = field(default_factory=background_color)
    focus_color: Color = field(default_factory=focus_color)
    hover_color: Color = field(default_factory=hover_color)
    color_type: ColorType = ColorType.SOLID
    background_gradient: ColorGradient = field(default_factory=bg_gradient)
    focus_gradient: ColorGradient = field(default_factory=focus_gradient)
    hover_gradient: ColorGradient = field(default_factory=hover_gradient)
    opacity: int = 255
    radius_top_left: float = 0
    radius_top_right: float = 0
    radius_bottom_left: float = 0
    radius_bottom_right: float = 0
    gradient_direction: GradientDirection = GradientDirection.VERTICAL
