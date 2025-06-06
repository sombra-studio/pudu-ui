from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch
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
        self.height_offset = params.height * 0.1
        self.style = deepcopy(params.style)
        self.hover_style = deepcopy(params.hover_style)
        self.focus_style = deepcopy(params.focus_style)
        self.press_style = deepcopy(params.press_style)
        self.back_group = WidgetGroup(widget=self, order=0, parent=group)
        self.front_group = WidgetGroup(widget=self, order=1, parent=group)
        self.bar = self.create_bar()
        self.children.append(self.bar)

        self.thumb = self.create_thumb()
        self.children.append(self.thumb)

        self.is_on_press = False

    def change_style(self, style: SliderStyle):
        if style == self.style:
            return
        self.style = deepcopy(style)
        self.bar.change_style(style.bar_style)
        self.thumb.change_style(style.thumb_style)

    def create_thumb(self) -> Frame:
        value_pos = self.get_value_pos()
        params = FrameParams(
            x=value_pos - self.height / 2.0,
            width=self.height, height=self.height, focusable=True,
            style=self.style.thumb_style
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

    def is_inside(self, x: float, y: float) -> bool:
        left, bottom = self.thumb.get_position()
        radius = self.thumb.width / 2.0
        center_x = left + radius
        center_y = bottom + radius

        return (
            ((x - center_x) ** 2 <= radius ** 2) and
            ((y - center_y) ** 2 <= radius ** 2)
        )

    def press(self):
        self.change_style(self.press_style)
        self.invalidate()
        self.is_on_press = True

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
        self.thumb.width = self.height
        self.thumb.style.set_uniform_radius(self.height / 2.0)
        value_pos = self.get_value_pos()
        self.thumb.x = value_pos - self.thumb.width / 2.0
        self.thumb.invalidate()


    # Override function
    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.is_inside(x, y) and buttons & mouse.LEFT:
            self.press()
            return pyglet.event.EVENT_HANDLED
        return pyglet.event.EVENT_UNHANDLED

    # Override function
    def on_mouse_release(self, x, y, buttons, modifiers):
        if not self.is_on_press or not (buttons & mouse.LEFT):
            return pyglet.event.EVENT_UNHANDLED
        self.release(self.is_inside(x, y))
        return pyglet.event.EVENT_HANDLED

    def on_mouse_motion(self, x, y, dx, dy) -> bool:
        if self.is_on_press:
            value_delta = (dx / self.width) * (self.max_value - self.min_value)
            self.value += value_delta
            self.value = min(self.max_value, self.value)
            self.value = max(self.min_value, self.value)
            self.invalidate()
            return pyglet.event.EVENT_HANDLED
        else:
            if self.is_inside(x, y):
                if not self.is_on_hover:
                    self.hover()
            else:
                if self.is_on_hover:
                    self.unhover()
            return pyglet.event.EVENT_UNHANDLED
