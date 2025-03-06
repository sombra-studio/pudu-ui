from dataclasses import dataclass
import pyglet


@dataclass
class Params:
    x: float = 0.0
    y: float = 0.0
    width: int = 100
    height: int = 100
    focusable: bool = True


class Widget:
    def __init__(self, params: Params = Params(), parent=None):
        self.x: float = params.x
        self.y: float = params.y
        self.width: int = params.width
        self.height: int = params.height
        self._visible: bool = True
        self.focusable: bool = params.focusable
        self.is_on_focus: bool = False
        self.is_on_hover: bool = False
        self.index: int = 0
        self.parent: Widget = parent
        self.is_valid: bool = True

    def on_focus(self):
        pass

    def on_unfocus(self):
        pass

    def on_hover(self):
        pass

    def focus(self):
        if self.focusable:
            self.is_on_focus = True
            self.on_focus()

    def unfocus(self):
        if self.focusable:
            self.is_on_focus = False
            self.is_on_hover = False
            self.on_unfocus()

    def hover(self):
        if self.focusable:
            self.is_on_hover = True
            self.on_hover()

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

    def on_mouse_motion(self, x, y, dx, dy) -> bool:
        if self.is_inside(x, y):
            if not self.is_on_hover:
                self.hover()
        else:
            if self.is_on_hover and not self.is_on_focus:
                self.unfocus()
        return pyglet.event.EVENT_UNHANDLED

    def __repr__(self) -> str:
        return f"Widget(x: {self.x}, y: {self.y}. width: {self.width}, height:"\
            f" {self.height})"
