from dataclasses import dataclass


from . import Widget
from .widget import Params


@dataclass
class ButtonParams(Params):
    """
    Here you can define parameters for initialising a button.

    Args:
        label: The label that will be displayed in the button (optional)
        on_press: The callback function for when the button is pressed
    """
    label: str = ""
    on_press: object = lambda: None


class Button(Widget):
    def __init__(
        self, params: ButtonParams
    ):
        super().__init__(params)
        self.label = params.label
        self.on_press = params.on_press
