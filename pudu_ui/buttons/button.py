from dataclasses import dataclass, field
import pyglet


from pudu_ui import Widget
from pudu_ui.primitives import Frame, FrameParams
from pudu_ui.label import Label, LabelParams, LabelResizeType
from pudu_ui.styles.buttons import ButtonStyle, default_button_style
from pudu_ui.colors import Color, PRIMARY_BTN_PRESS_BG_COLOR


#------------------------------------------------------------------------------
# Factory functions

def default_press_color():
    return PRIMARY_BTN_PRESS_BG_COLOR

#------------------------------------------------------------------------------


@dataclass
class ButtonParams(FrameParams):
    """
    Here you can define parameters for initialising a button. It inherits all
    parameters from FrameParams

    Args:
        text: The text that will be displayed in the button (optional)
        on_press: The callback function for when the button is pressed
        style: The style for the button
    """
    text: str = ""
    on_press: object = lambda: None
    style: ButtonStyle = field(default_factory=default_button_style)
    press_color: Color = field(default_factory=default_press_color)



class Button(Widget):
    def __init__(
        self,
        params: ButtonParams,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None
    ):
        # TODO: Add focus
        super().__init__(params)
        self.text: str = params.text
        self.on_press = params.on_press
        self.is_on_press = False
        self.batch: pyglet.graphics.Batch = batch
        self.front_group: pyglet.graphics.Group = pyglet.graphics.Group(
            1, parent=group
        )
        self.back_group: pyglet.graphics.Group = pyglet.graphics.Group(
            parent=group
        )

        self.background: Frame = self.create_background()
        # define label params
        label_x = self.x + self.width / 2.0
        label_y = self.y + self.height / 2.0
        label_params = LabelParams(
            label_x,
            label_y,
            width=self.width,
            text=self.text,
            anchor_x='center',
            anchor_y='center',
            resize_type=LabelResizeType.FIT,
            style=params.style.font_style
        )
        self.label: Label = Label(
            label_params, batch=batch, group=self.front_group
        )

    def change_background_color(self, new_color: Color):
        self.background.change_quad_colors(
            (new_color, new_color, new_color, new_color)
        )

    def create_background(self, params: FrameParams) -> Frame:
        frame = Frame(params, batch=self.batch, group=self.back_group)
        return frame

    def recompute(self):
        # Recompute background
        self.background.x = self.x
        self.background.y = self.y
        self.background.width = self.width
        self.background.height = self.height
        self.background.invalidate()

        # Recompute label
        label_x = self.x + self.width / 2.0
        label_y = self.y + self.height / 2.0
        self.label.x = label_x
        self.label.y = label_y
        self.label.width = self.width
        self.label.invalidate()

    def set_data(self, data: dict):
        self.text = data['text']
        self.invalidate()

    def update(self, dt: float):
        self.background.update(dt)
        self.label.update(dt)
        super().update(dt)

    # Override function
    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.is_inside(x, y):
            self.change_background_color(self.press_color)
            self.is_on_press = True
            self.on_press()
            return pyglet.event.EVENT_HANDLED
        return pyglet.event.EVENT_UNHANDLED

    # Override function
    def on_mouse_release(self, x, y, buttons, modifiers):
        if not self.is_on_press:
            return pyglet.event.EVENT_UNHANDLED
        self.is_on_press = False
        if not self.is_inside(x, y):
            self.change_background_color(self.background_color)
            return pyglet.event.EVENT_HANDLED
        else:
            self.change_background_color(self.hover_color)
            return pyglet.event.EVENT_HANDLED
