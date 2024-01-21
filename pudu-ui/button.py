from dataclasses import dataclass


from . import Widget
from .widget import Params


@dataclass
class ButtonParams(Params):
    label: str = ""
    on_press: object = lambda: None


class Button(Widget):
    def __init__(
        self, params: ButtonParams
    ):
        super().__init__(params)
        self.label = params.label
        self.on_press = params.on_press
