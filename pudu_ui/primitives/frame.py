from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui import Color, Params, Widget
from pudu_ui.colors import ColorGradient, ColorType, GradientDirection
import pudu_ui


@dataclass
class FrameParams(Params):
    style: pudu_ui.styles.frames.FrameStyle = field(
        default_factory=pudu_ui.styles.frames.default_frame_style
    )
    # ATTENTION: By default Frame won't be focusable
    focusable: bool = False


class Frame(Widget):
    def __init__(
        self, params: FrameParams, batch: Batch = None, group: Group = None
    ):
        super().__init__(params)
        self.color_type = params.style.color_type
        self.gradient_direction = params.style.gradient_direction
        # set background, focus and hover colors
        self.background_colors = self.get_colors(
            params.style.background_color,
            params.style.background_gradient
        )
        self.focus_colors = self.get_colors(
            params.style.focus_color,
            params.style.focus_gradient
        )
        self.hover_colors = self.get_colors(
            params.style.hover_color,
            params.style.hover_gradient
        )
        self.quad = pudu_ui.primitives.RoundedQuad(
            params.x,
            params.y,
            params.width,
            params.height,
            colors=self.background_colors,
            opacity=params.style.opacity,
            radius_top_left=params.style.radius_top_left,
            radius_top_right=params.style.radius_top_right,
            radius_bottom_left=params.style.radius_bottom_left,
            radius_bottom_right=params.style.radius_bottom_right,
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
