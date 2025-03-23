from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group

from pudu_ui import Color
from pudu_ui.buttons import Button, ButtonParams
import pudu_ui.colors
from pudu_ui.image import ImageParams, Image, default_image_params


def default_color() -> Color:
    return pudu_ui.colors.GRAY


def default_hover_color() -> Color:
    # return pudu_ui.colors.LIGHT_GRAY
    return pudu_ui.colors.MEDIUM_BLUE

def default_focus_color() -> Color:
    return pudu_ui.colors.LIGHT_GRAY


def default_press_color() -> Color:
    return pudu_ui.colors.LIGHTER_GRAY


@dataclass
class ImageButtonParams(ButtonParams):
    image_params: ImageParams = field(default_factory=default_image_params)
    color: Color = field(default_factory=default_color)
    hover_color: Color = field(default_factory=default_hover_color)
    focus_color: Color = field(default_factory=default_focus_color)
    press_color: Color = field(default_factory=default_press_color)


class ImageButton(Button):
    def __init__(
        self,
        params: ImageButtonParams,
        batch: Batch = None,
        group: Group = None
    ):
        super().__init__(params, batch=batch, group=group)
        self.image = Image(
            params.image_params, batch=batch, group=self.front_group
        )
        self.color = params.color
        self.hover_color = params.hover_color
        self.focus_color = params.focus_color
        self.press_color = params.press_color

    def update(self, dt: float):
        super().update(dt)
        self.image.update(dt)

    def on_unfocus(self):
        super().on_unfocus()
        self.image.color = self.color

    def on_hover(self):
        print("on_hover")
        super().on_hover()
        self.image.color = self.hover_color

    def on_focus(self):
        super().on_focus()
        self.image.color = self.focus_color

    def press(self):
        super().press()
        self.image.color = self.press_color
