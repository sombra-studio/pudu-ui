from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch


from pudu_ui import (
    Frame, FrameParams, Params, ProgressBar, ProgressBarParams,
    Widget, WidgetGroup
)
from pudu_ui.styles.sliders import SliderStyle
import pudu_ui


@dataclass
class SliderParams(Params):
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
        handle_size = int(round(self.style.handle_radius * 2))
        style = pudu_ui.styles.frames.FrameStyle()
        style.set_uniform_radius(self.style.handle_radius)
        style.set_solid_color(self.style.handle_color)
        style.border_color = self.style.handle_border_color
        params = FrameParams(
            x=self.width / 2.0 - handle_size / 2.0,
            width=handle_size, height=handle_size, focusable=True,
            style=style
        )
        frame = Frame(params)
        return frame

    def create_progress_bar(self) -> ProgressBar:
        style = self.style
        bar_style = pudu_ui.styles.progress_bars.ProgressBarStyle(
            left_color=style.left_color,
            right_color=style.right_color,
            opacity=style.opacity
        )
        params = ProgressBarParams()
        bar = ProgressBar()
        return bar





