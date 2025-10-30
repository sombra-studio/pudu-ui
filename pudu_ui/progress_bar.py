from dataclasses import dataclass, field
from copy import deepcopy

from pudu_ui import Params, Widget
from pudu_ui.primitives.quad import ProgressQuad
from pudu_ui.styles.progress_bars import ProgressBarStyle
import pudu_ui
from pyglet.graphics import Batch, Group


DEFAULT_PROGRESS_BAR_WIDTH = 200
DEFAULT_PROGRESS_BAR_HEIGHT = 20


@dataclass
class ProgressBarParams(Params):
    width: int = DEFAULT_PROGRESS_BAR_WIDTH
    height: int = DEFAULT_PROGRESS_BAR_HEIGHT
    min_value: float = 0.0
    max_value: float = 100.0
    value: float = 75.0
    style: ProgressBarStyle = field(
        default_factory=pudu_ui.styles.progress_bars.default_progress_bar_style
    )


class ProgressBar(Widget):
    def __init__(
        self,
        params: ProgressBarParams = None,
        batch: Batch = None, group: Group = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ProgressBarParams()
        super().__init__(params, batch=batch, group=group, parent=parent)
        self.min_value = params.min_value
        self.max_value = params.max_value
        self.value = params.value
        self.style = deepcopy(params.style)
        self.back_group = Group(order=0, parent=group)
        self.front_group = Group(order=1, parent=group)
        self.quad = self.create_quad()

    def change_style(self, style: ProgressBarStyle):
        if self.style == style:
            return
        self.style = deepcopy(style)

        # Change colors
        self.quad.left_color = style.left_color
        self.quad.right_color = style.right_color

        # Change corners
        self.quad.radius_top_left = style.radius_top_left
        self.quad.radius_top_right = style.radius_top_right
        self.quad.radius_bottom_left = style.radius_bottom_left
        self.quad.radius_bottom_right = style.radius_bottom_right

        # Change other uniforms
        self.quad.opacity = style.opacity
        self.quad.right_opacity = style.right_opacity
        self.quad.border_width = style.border_width
        self.quad.border_color = style.border_color
        self.quad.set_uniforms()

    def create_quad(self) -> ProgressQuad:
        style = self.style
        limit_x = self.get_limit_x()
        quad = ProgressQuad(
            width=self.width, height=self.height,
            left_color=style.left_color, right_color=style.right_color,
            opacity=style.opacity, right_opacity=style.right_opacity,
            radius_top_left=style.radius_top_left,
            radius_top_right=style.radius_top_right,
            radius_bottom_left=style.radius_bottom_left,
            radius_bottom_right=style.radius_bottom_right,
            border_width=style.border_width, border_color=style.border_color,
            limit_x=limit_x,
            batch=self.batch, group=self.group,
            parent=self
        )
        return quad

    def get_limit_x(self) -> int:
        progress = (
            (self.value - self.min_value) / (self.max_value - self.min_value)
        )
        limit_x: int = int(
            round(self.width * progress)
        )
        return limit_x

    def recompute(self):
        super().recompute()
        limit_x = self.get_limit_x()
        self.quad.width = self.width
        self.quad.height = self.height
        self.quad.limit_x = limit_x
        self.quad.recompute()
