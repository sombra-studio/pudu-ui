from dataclasses import dataclass


@dataclass
class Params:
    x: float = 0.0
    y: float = 0.0
    width: int = 100
    height: int = 100
    scale_x: float = 1.0
    scale_y: float = 1.0
    focusable: bool = False


class Widget:
    def __init__(self, params: Params = Params(), parent=None):
        self.x: float = params.x
        self.y: float = params.y
        self.width: int = params.width
        self.height: int = params.height
        self._scale_x: float = params.scale_x
        self._scale_y: float = params.scale_y
        self._visible: bool = True
        self.focusable: bool = params.focusable
        self.is_on_focus: bool = False
        self.index: int = 0
        self.parent: Widget = parent
        self.is_valid: bool = True

    def on_focus(self):
        pass

    def on_unfocus(self):
        pass

    def focus(self):
        if self.focusable:
            self.is_on_focus = True
            self.on_focus()

    def unfocus(self):
        if self.focusable:
            self.is_on_focus = False
            self.on_unfocus()

    def invalidate(self):
        self.is_valid = False

    def recompute(self):
        pass

    def update(self, dt: float):
        if not self.is_valid:
            self.recompute()
            self.is_valid = True

    def is_inside(self, x: float, y: float) -> bool:
        return (
            (self.x <= x <= self.x + self.width) and
            (self.y <= y <= self.y + self.height)
        )

    def __repr__(self) -> str:
        return f"Widget(x: {self.x}, y: {self.y}. width: {self.width}, height:"\
            f" {self.height})"
