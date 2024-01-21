from dataclasses import dataclass


@dataclass
class Params:
    x: float = 0.0
    y: float = 0.0
    width: float = 100.0
    height: float = 100.0
    focusable: bool = False


class Widget:
    def __init__(self, params: Params = Params()):
        self.x: float = params.x
        self.y: float = params.y
        self.width: float = params.width
        self.height: float = params.height
        self.focusable: bool = params.focusable
        self.is_on_focus: bool = False

    def focus(self):
        if self.focusable:
            self.is_on_focus = True

    def unfocus(self):
        if self.focusable:
            self.is_on_focus = False
