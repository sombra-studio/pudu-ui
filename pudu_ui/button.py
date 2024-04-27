from dataclasses import dataclass, field
from pyglet.shapes import Rectangle
import pyglet

from pudu_ui import Widget
from pudu_ui.label import Label, LabelParams
from pudu_ui.widget import Params
from pudu_ui.styles import FontStyle, p1


@dataclass
class ButtonParams(Params):
    """
    Here you can define parameters for initialising a button.

    Args:
        label: The label that will be displayed in the button (optional)
        on_press: The callback function for when the button is pressed
        color: The RGBA 8bit color for the background
        hover_color: The color when hovering the button
        press_color: The color when the button is pressed
        style: The font style for the label
    """
    label: str = ""
    on_press: object = lambda: None
    color: [int, int, int, int] = (36, 36, 36, 255)
    hover_color: [int, int, int, int] = (72, 72, 72, 255)
    press_color: [int, int, int, int] = (107, 107, 107, 255)
    style: FontStyle = field(default_factory=p1)


class Button(Widget):
    def __init__(
        self,
        params: ButtonParams,
        batch: pyglet.graphics.Batch,
        group: pyglet.graphics.Group = None
    ):
        # TODO: Add focus
        super().__init__(params)
        self.label_value: str = params.label
        self.on_press = params.on_press
        self.color: [int, int, int, int] = params.color
        self.hover_color: [int, int, int, int] = params.hover_color
        self.press_color: [int, int, int, int] = params.press_color
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
        self.background: Rectangle = self.create_background()
        # define label params
        label_x = self.x + self.width / 2.0
        label_y = self.y + self.height / 2.0
        label_params = LabelParams(
            label_x,
            label_y,
            self.width,
            self.height,
            value=self.label_value,
            style=params.style
        )
        self.label: Label = Label(label_params, batch=batch, group=group)

    def create_background(self) -> Rectangle:
        rect: Rectangle = Rectangle(
            x=self.x * self._scale_x,
            y=self.y * self._scale_y,
            width=self.width * self._scale_x,
            height=self.height * self._scale_y,
            color=self.color,
            batch=self.batch,
            group=self.group
        )
        return rect

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.is_inside(x, y):
            self.background.color = self.press_color
            self.on_press()
            return pyglet.event.EVENT_HANDLED

    def on_mouse_release(self, x, y, buttons, modifiers):
        if not self.is_inside(x, y):
            self.background.color = self.color
            return pyglet.event.EVENT_HANDLED
        else:
            self.background.color = self.hover_color

    def on_mouse_motion(self, x, y, dx, dy):
        if self.is_inside(x, y):
            self.background.color = self.hover_color
        else:
            self.background.color = self.color
