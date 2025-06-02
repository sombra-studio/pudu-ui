from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch


from pudu_ui import (
    Frame, FrameParams, Params, ProgressBar, ProgressBarParams,
    Widget, WidgetGroup
)
from pudu_ui.styles.sliders import (
    SliderStyle, DEFAULT_HANDLE_RADIUS, DEFAULT_SLIDER_CORNER_RADIUS
)
import pudu_ui


@dataclass
class SliderParams(Params):
    width: int = 200
    height: int = int(round(DEFAULT_HANDLE_RADIUS * 2))
    min_value: float = 0.0
    max_value: float = 100.0
    value: float = 75.0
    style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )
    hover_style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )
    focus_style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )
    press_style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )


class Slider(Widget):
    def __init__(
        self,
        params: SliderParams | None = None,
        batch: Batch | None = None,
        group: WidgetGroup | None = None,
        parent: Widget | None = None
    ):
        if not params:
            params = SliderParams()
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        self.min_value = params.min_value
        self.max_value = params.max_value
        self.value = params.value
        self.style = deepcopy(params.style)
        self.back_group = WidgetGroup(widget=self, order=0, parent=group)
        self.front_group = WidgetGroup(widget=self, order=1, parent=group)
        self.progress_bar = self.create_progress_bar()
        self.handle = self.create_handle()

    def create_handle(self) -> Frame:
        value_pos = (
            (self.value - self.min_value) / (self.max_value - self.min_value)
        ) * self.width
        params = FrameParams(
            x=value_pos - self.height / 2.0,
            width=self.height, height=self.height, focusable=True,
            style=self.style.handle_style
        )
        frame = Frame(
            params, batch=self.batch, group=self.front_group, parent=self
        )
        return frame

    def create_progress_bar(self) -> ProgressBar:
        bar_height = int(round(2 * self.style.bar_style.radius_top_left))
        params = ProgressBarParams(
            y=self.height / 2.0 - bar_height / 2.0,
            width=self.width, height=bar_height,
            min_value=self.min_value, max_value=self.max_value,
            value=self.value,
            style=self.style.bar_style
        )
        bar = ProgressBar(
            params, batch=self.batch, group=self.back_group, parent=self
        )
        return bar
