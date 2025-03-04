from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui import Color, Params, Widget
from pudu_ui.colors import ColorGradient, ColorType, GradientDirection
import pudu_ui

#------------------------------------------------------------------------------
# factory functions
def background_color():
    return pudu_ui.colors.PURPLE

def focus_color():
    return pudu_ui.colors.LIGHT_PURPLE

def hover_color():
    return pudu_ui.colors.LIGHTER_PURPLE

def bg_gradient():
    return pudu_ui.colors.DEFAULT_FRAME_GRADIENT

def focus_gradient():
    return pudu_ui.colors.FOCUS_FRAME_GRADIENT

def hover_gradient():
    return pudu_ui.colors.HOVER_FRAME_GRADIENT
#------------------------------------------------------------------------------

@dataclass
class FrameParams(Params):
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


class Frame(Widget):
    def __init__(
        self, params: FrameParams, batch: Batch = None, group: Group = None
    ):
        super().__init__(params)
        if params.color_type == ColorType.SOLID:
            colors = (
                params.background_color, params.background_color,
                params.background_color, params.background_color
            )
        else:
            colors = (
                params.background_gradient.end_color,
                params.background_gradient.end_color,
                params.background_gradient.start_color,
                params.background_gradient.start_color
            )
        if params.gradient_direction == GradientDirection.HORIZONTAL:
            # this would be like swapping v0 with v2 colors
            colors = (colors[2], colors[1], colors[0], colors[3])
        self.background = pudu_ui.primitives.RoundedQuad(
            params.x,
            params.y,
            params.width,
            params.height,
            colors=colors,
            opacity=params.opacity,
            radius_top_left=params.radius_top_left,
            radius_top_right=params.radius_top_right,
            radius_bottom_left=params.radius_bottom_left,
            radius_bottom_right=params.radius_bottom_right,
            batch=batch,
            group=group
        )
