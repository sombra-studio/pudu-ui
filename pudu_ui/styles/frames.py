from dataclasses import dataclass, field
from pudu_ui import colors
from pudu_ui.colors import Color, GradientDirection


#------------------------------------------------------------------------------
# Factory functions
def background_color():
    return colors.PURPLE

def background_end_color():
    return colors.DARK_PURPLE

def focus_color():
    return colors.LIGHT_PURPLE

def hover_color():
    return colors.LIGHTER_PURPLE

def highlight_color():
    return colors.WHITE

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
    highlight_width: float = 3
    highlight_color: Color = field(default_factory=highlight_color)

    def set_solid_color(self, color: Color):
        self.start_color = color
        self.end_color = color

    def set_uniform_radius(self, radius: float):
        self.radius_top_left = radius
        self.radius_top_right = radius
        self.radius_bottom_left = radius
        self.radius_bottom_right = radius
