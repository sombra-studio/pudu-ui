from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


import pudu_ui
from pudu_ui import Color, Params, Widget
from pudu_ui.colors import GradientDirection
from pudu_ui.styles.frames import FrameStyle


@dataclass
class FrameParams(Params):
    style: FrameStyle = field(
        default_factory=pudu_ui.styles.frames.default_frame_style
    )
    # ATTENTION: By default Frame won't be focusable
    focusable: bool = False


class Frame(Widget):
    def __init__(
        self, params: FrameParams, batch: Batch = None, group: Group = None
    ):
        super().__init__(params)
        self.style = deepcopy(params.style)
        # If we just want a solid color, leave end_color as None, and it will
        # take the same value as start_color
        if not self.style.end_color:
            self.style.end_color = self.style.start_color
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
            self.style.end_color,
            self.style.end_color,
            self.style.start_color,
            self.style.start_color
        )
        if self.style.gradient_direction == GradientDirection.HORIZONTAL:
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

    def change_style(self, style: FrameStyle):
        if self.style == style:
            return
        self.style = deepcopy(style)

        # Change colors
        new_colors = self.get_colors_tuple()
        self.change_quad_colors(new_colors)

        # Change corners
        self.quad.radius_top_left = style.radius_top_left
        self.quad.radius_top_right = style.radius_top_right
        self.quad.radius_bottom_left = style.radius_bottom_left
        self.quad.radius_bottom_right = style.radius_bottom_right
        self.quad.opacity = style.opacity
        self.quad.set_uniforms()
