from collections.abc import Callable
from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group
from pyglet.window import mouse
import pyglet


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
    on_value_changed: Callable[[...], None] = lambda *args: None
    style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )
    hover_style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )
    focus_style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )


class Slider(Widget):
    def __init__(
        self,
        params: SliderParams | None = None,
        batch: Batch | None = None,
        group: Group | None = None,
        parent: Widget | None = None
    ):
        if not params:
            params = SliderParams()
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        self.min_value = params.min_value
        self.max_value = params.max_value
        self.value = params.value
        self.bar_height = params.bar_height
        self.on_value_changed = params.on_value_changed
        self.is_on_press = False
        self.style = deepcopy(params.style)
        self.hover_style = deepcopy(params.hover_style)
        self.focus_style = deepcopy(params.focus_style)
        self.back_group = WidgetGroup(widget=self, order=0, parent=group)
        self.front_group = WidgetGroup(widget=self, order=1, parent=group)
        self.bar = self.create_bar()
        self.children.append(self.bar)

        self.thumb = self.create_thumb()
        self.children.append(self.thumb)

    def change_style(self, style: SliderStyle):
        if style == self.style:
            return
        self.style = deepcopy(style)
        self.bar.change_style(style.bar_style)
        self.thumb.change_style(style.thumb_style)

    def create_thumb(self) -> Frame:
        value_pos = self.get_value_pos()
        style = self.style.thumb_style
        style.set_uniform_radius(self.height / 2.0)
        params = FrameParams(
            x=value_pos,
            width=self.height, height=self.height, focusable=True,
            style=style
        )
        frame = Frame(
            params, batch=self.batch, group=self.front_group, parent=self
        )
        return frame

    def create_bar(self) -> ProgressBar:
        bar_width = self.width - self.height
        style = self.style.bar_style
        style.set_uniform_radius(self.bar_height / 2.0)
        params = ProgressBarParams(
            x=self.height / 2.0,
            y=self.height / 2.0 - self.bar_height / 2.0,
            width=bar_width, height=self.bar_height,
            min_value=self.min_value, max_value=self.max_value,
            value=self.value,
            style=self.style.bar_style
        )
        bar = ProgressBar(
            params, batch=self.batch, group=self.back_group, parent=self
        )
        return bar

    def get_value_pos(self) -> float:
        value_t = (
            (self.value - self.min_value) / (self.max_value - self.min_value)
        )
        return value_t * self.bar.width

    def recompute(self):
        super().recompute()
        # Update bar
        self.bar.width = self.width - self.height
        self.bar.heigh = self.bar_height
        self.bar.value = self.value
        self.bar.invalidate()

        # Update thumb
        self.thumb.height = self.height
        self.thumb.width = self.height
        self.thumb.style.set_uniform_radius(self.height / 2.0)
        value_pos = self.get_value_pos()
        self.thumb.x = value_pos
        self.thumb.invalidate()

    # Event function
    def on_mouse_drag(self, _, __, dx, ___, buttons, ____) -> bool:
        if buttons & mouse.LEFT and self.is_on_press:
            value_delta = (dx / self.width) * (self.max_value - self.min_value)
            self.value += value_delta
            self.value = min(self.max_value, self.value)
            self.value = max(self.min_value, self.value)
            self.invalidate()
            self.on_value_changed(self)
            return pyglet.event.EVENT_HANDLED
        return pyglet.event.EVENT_UNHANDLED

    # Event function
    def on_mouse_press(self, x, y, buttons, _):
        if self.is_inside(x, y) and buttons & mouse.LEFT:
            self.is_on_press = True
            # reposition the thumb
            start_x, _ = self.get_position()
            relative_x = min(x - start_x - self.bar.x, self.bar.width)
            relative_x = max(0, relative_x)
            value_t = relative_x / self.bar.width
            self.value = self.min_value + value_t * self.max_value
            self.invalidate()
            self.on_value_changed(self)
            return pyglet.event.EVENT_HANDLED
        return pyglet.event.EVENT_UNHANDLED

    # Event function
    def on_mouse_release(self, _, __, buttons, ___):
        if not self.is_on_press or not (buttons & mouse.LEFT):
            return pyglet.event.EVENT_UNHANDLED
        self.is_on_press = False
        return pyglet.event.EVENT_HANDLED
