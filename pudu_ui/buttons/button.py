from collections.abc import Callable
from copy import deepcopy
from dataclasses import dataclass, field
import pyglet
from pyglet.window import mouse


from pudu_ui import Params, Widget
from pudu_ui import Frame, FrameParams
from pudu_ui.label import Label, LabelParams, LabelResizeType
from pudu_ui.styles.buttons import (
    ButtonStyle, default_button_style, dft_btn_hover_style,
    dft_btn_focus_style, dft_btn_press_style
)


@dataclass
class ButtonParams(Params):
    """
    Here you can define parameters for initialising a button.

    Args:
        text: The text that will be displayed in the button (optional)
        on_press: The callback function for when the button is pressed
        style: The style for the button when unfocused
        hover_style: The style for the button when hovered
        focus_style: The style for the button when focused
        press_style: The style for the button when pressed
    """
    text: str = ""
    on_press: Callable[[...], None] = lambda *args: None
    style: ButtonStyle = field(default_factory=default_button_style)
    hover_style: ButtonStyle = field(default_factory=dft_btn_hover_style)
    focus_style: ButtonStyle = field(default_factory=dft_btn_focus_style)
    press_style: ButtonStyle = field(default_factory=dft_btn_press_style)
    focusable: bool = True

    def set_uniform_radius(self, radius: float):
        self.style.set_uniform_radius(radius)
        self.hover_style.set_uniform_radius(radius)
        self.focus_style.set_uniform_radius(radius)
        self.press_style.set_uniform_radius(radius)


class Button(Widget):
    def __init__(
        self,
        params: ButtonParams = None,
        batch: pyglet.graphics.Batch | None = None,
        group: pyglet.graphics.Group | None = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ButtonParams()
        super().__init__(params, batch=batch, group=group, parent=parent)
        self.text: str = params.text
        self.on_press = params.on_press
        self.is_on_press = False
        self.front_group: pyglet.graphics.Group = pyglet.graphics.Group(
            1, parent=group
        )
        self.back_group: pyglet.graphics.Group = pyglet.graphics.Group(
            parent=group
        )
        self.style = deepcopy(params.style)
        self.hover_style = deepcopy(params.hover_style)
        self.focus_style = deepcopy(params.focus_style)
        self.press_style = deepcopy(params.press_style)

        # Create background Frame
        self.background = self.create_background()
        self.children.append(self.background)

        # Create Label
        self.label = self.create_label()
        self.children.append(self.label)

    def change_style(self, style: ButtonStyle):
        self.background.change_style(style.frame_style)
        self.label.change_style(style.font_style)

    def create_background(self) -> Frame:
        frame_params = FrameParams(
            0.0, 0.0, self.width, self.height, style=self.style.frame_style
        )
        frame = Frame(
            frame_params, batch=self.batch, group=self.back_group, parent=self
        )
        return frame

    def create_label(self) -> Label:
        label_x = self.width / 2.0
        label_y = self.height / 2.0
        label_params = LabelParams(
            label_x,
            label_y,
            width=self.width,
            text=self.text,
            anchor_x='center',
            anchor_y='center',
            resize_type=LabelResizeType.FIT,
            style=self.style.font_style
        )
        label = Label(
            label_params, batch=self.batch, group=self.front_group, parent=self
        )
        return label

    def on_hover(self):
        super().on_hover()
        self.change_style(self.hover_style)

    def on_unhover(self):
        super().on_unhover()
        if self.is_on_focus:
            self.change_style(self.focus_style)
        else:
            self.change_style(self.style)

    def on_focus(self):
        super().on_focus()
        self.change_style(self.focus_style)

    def on_unfocus(self):
        super().on_unfocus()
        self.change_style(self.style)

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
        super().recompute()
        # Recompute background
        self.background.width = self.width
        self.background.height = self.height
        self.background.invalidate()

        # Recompute label
        # This will keep the label centered in the button
        self.label.x = self.width / 2.0
        self.label.y = self.height / 2.0
        self.label.text = self.text
        self.label.width = self.width
        self.label.height = self.height
        self.label.invalidate()

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
