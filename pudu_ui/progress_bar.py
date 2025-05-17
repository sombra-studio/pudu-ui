from dataclasses import dataclass, field
from copy import deepcopy

from pudu_ui import Frame, FrameParams, Params, Widget
from pudu_ui.styles.progress_bars import ProgressBarStyle
import pudu_ui
from pyglet.graphics import Batch, Group


@dataclass
class ProgressBarParams(Params):
    height: int = 6
    min_value: float = 0.0
    max_value: float = 100.0
    value: float = 50.0
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
        self.back_group = Group(order=1, parent=group)
        self.front_group = Group(order=0, parent=group)
        self.left_frame = self.create_left_frame()
        self.right_frame = self.create_right_frame()

    def recompute(self):
        super().recompute()
        self.left_frame.recompute()
        self.right_frame.recompute()

    def create_left_frame(self) -> Frame:
        limit_x = self.get_limit_x()
        style = self.style.left_frame_style
        style.set_uniform_radius(self.height // 2)
        params = FrameParams(
            width=limit_x,
            height=self.height,
            style=style
        )
        frame = Frame(
            params=params, batch=self.batch, group=self.back_group, parent=self
        )
        return frame

    def create_right_frame(self) -> Frame:
        limit_x = self.get_limit_x()
        style = self.style.right_frame_style
        style.set_uniform_radius(self.height // 2)
        params = FrameParams(
            x=limit_x,
            width=self.width - limit_x,
            height=self.height,
            style=style
        )
        frame = Frame(
            params=params, batch=self.batch, group=self.back_group, parent=self
        )
        return frame

    def get_limit_x(self) -> int:
        limit_x: int = int(round(self.width * (self.max_value / self.value)))
        return limit_x

