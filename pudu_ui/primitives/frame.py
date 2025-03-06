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
    # ATTENTION: By default Frame won't be focusable
    focusable: bool = False


class Frame(Widget):
    def __init__(
        self, params: FrameParams, batch: Batch = None, group: Group = None
    ):
        super().__init__(params)
        self.color_type = params.color_type
        self.gradient_direction = params.gradient_direction
        # set background, focus and hover colors
        self.background_colors = self.get_colors(
            params.background_color, params.background_gradient
        )
        self.focus_colors = self.get_colors(
            params.focus_color, params.focus_gradient
        )
        self.hover_colors = self.get_colors(
            params.hover_color, params.hover_gradient
        )
        self.quad = pudu_ui.primitives.RoundedQuad(
            params.x,
            params.y,
            params.width,
            params.height,
            colors=self.background_colors,
            opacity=params.opacity,
            radius_top_left=params.radius_top_left,
            radius_top_right=params.radius_top_right,
            radius_bottom_left=params.radius_bottom_left,
            radius_bottom_right=params.radius_bottom_right,
            batch=batch,
            group=group
        )

    def get_colors(
        self, color: Color, gradient: ColorGradient
    ):
        if self.color_type == ColorType.SOLID:
            colors = (
                color, color,
                color, color
            )
        else:
            colors = (
                gradient.end_color,
                gradient.end_color,
                gradient.start_color,
                gradient.start_color
            )
        if self.gradient_direction == GradientDirection.HORIZONTAL:
            # this would be like swapping v0 with v2 colors
            colors = (colors[2], colors[1], colors[0], colors[3])
        return colors

    def change_quad_colors(self, colors: tuple[Color, Color, Color, Color]):
        self.quad.colors = colors
        self.quad.set_data()
        # data comes like a tuple with (format, data_list)
        # data['vertex_color'] will be like ('Bn', [100, 23, 90, 120, 80, ...])
        # so we only care about the second part here
        new_colors = self.quad.data['vertex_color'][1]
        self.quad.vertex_list.vertex_color[:] = new_colors

    def on_unfocus(self):
        self.change_quad_colors(self.background_colors)

    def on_hover(self):
        self.change_quad_colors(self.hover_colors)
