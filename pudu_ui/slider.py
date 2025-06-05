from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch


from pudu_ui import (
    Frame, FrameParams, Params, ProgressBar, ProgressBarParams,
    Widget, WidgetGroup
)
from pudu_ui.styles.sliders import SliderStyle
import pudu_ui


DEFAULT_THUMB_SIZE = 20
DEFAULT_BAR_HEIGHT = 12


@dataclass
class SliderParams(Params):
    width: int = 200
    height: int = DEFAULT_THUMB_SIZE
    bar_height: int = DEFAULT_BAR_HEIGHT
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
        self.bar_height = params.bar_height
        self.style = deepcopy(params.style)
        self.back_group = WidgetGroup(widget=self, order=0, parent=group)
        self.front_group = WidgetGroup(widget=self, order=1, parent=group)
        self.bar = self.create_bar()
        self.thumb = self.create_thumb()
        self.is_on_press = False

    def create_thumb(self) -> Frame:
        value_pos = self.get_value_pos()
        params = FrameParams(
            x=value_pos - self.height / 2.0,
            width=self.height, height=self.height, focusable=True,
            style=self.style.handle_style
        )
        frame = Frame(
            params, batch=self.batch, group=self.front_group, parent=self
        )
        return frame

    def create_bar(self) -> ProgressBar:
        params = ProgressBarParams(
            y=self.height / 2.0 - self.bar_height / 2.0,
            width=self.width, height=self.bar_height,
            min_value=self.min_value, max_value=self.max_value,
            value=self.value,
            style=self.style.bar_style
        )
        bar = ProgressBar(
            params, batch=self.batch, group=self.back_group, parent=self
        )
        return bar

    def get_value_pos(self) -> float:
        return (
            (self.value - self.min_value) / (self.max_value - self.min_value)
        ) * self.width

    def press(self):
        self.change_style(self.press_style)
        self.invalidate()
        self.is_on_press = True
        self.on_press(self)

    def release(self, is_inside: bool):
        self.is_on_press = False
        if not is_inside:
            self.change_style(self.style)
        else:
            self.change_style(self.hover_style)
        self.invalidate()

    def recompute(self):
        # Update bar
        self.bar.width = self.width
        self.bar.heigh = self.bar_height
        self.bar.value = self.value
        self.bar.invalidate()

        # Update thumb
        self.thumb.height = self.height
        self.thumb.width = self.width
        self.thumb.style.set_uniform_radius(self.height / 2.0)
        value_pos = self.get_value_pos()
        self.thumb.x = value_pos - self.thumb.width / 2.0
        self.thumb.invalidate()
