from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui import Color, Params, Widget
from pudu_ui.colors import GradientDirection
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
        self.start_color = params.style.start_color
        self.end_color = params.style.end_color
        # If we just want a solid color, leave end_color as None, and it will
        # take the same value as start_color
        if not self.end_color:
            self.end_color = self.start_color
        self.gradient_direction = params.style.gradient_direction
        self.quad = pudu_ui.primitives.RoundedQuad(
            params.x,
            params.y,
            params.width,
            params.height,
            colors=self.get_colors_tuple(),
            opacity=params.style.opacity,
            radius_top_left=params.style.radius_top_left,
            radius_top_right=params.style.radius_top_right,
            radius_bottom_left=params.style.radius_bottom_left,
            radius_bottom_right=params.style.radius_bottom_right,
            batch=batch,
            group=group
        )

    def get_colors_tuple(self):
        colors = (
            self.end_color,
            self.end_color,
            self.start_color,
            self.start_color
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
