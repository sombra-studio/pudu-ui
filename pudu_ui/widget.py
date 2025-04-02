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
        self.parent: Widget | None = parent
        self.is_valid: bool = True
        self.children: list[Widget] = []

    def get_position(self) -> tuple[float, float]:
        if self.parent:
            x_offset, y_offset = self.parent.get_position()
        else:
            x_offset = 0.0
            y_offset = 0.0
        x = self.x + x_offset
        y = self.y + y_offset
        return x, y

    def on_focus(self):
        self.invalidate()

    def on_unfocus(self):
        self.invalidate()

    def on_hover(self):
        self.invalidate()

    def focus(self):
        if self.focusable:
            self.is_on_focus = True
            self.on_focus()
            for child in self.children:
                child.focus()

    def unfocus(self):
        if self.focusable:
            self.is_on_focus = False
            self.on_unfocus()
            for child in self.children:
                child.unfocus()

    def hover(self):
        if self.focusable:
            self.is_on_hover = True
            self.on_hover()
            for child in self.children:
                child.hover()

    def invalidate(self):
        self.is_valid = False
        for child in self.children:
            child.invalidate()

    def recompute(self):
        pass

    def update(self, dt: float):
        if not self.is_valid:
            self.recompute()
            self.is_valid = True
            for child in self.children:
                child.update(dt)

    def is_inside(self, x: float, y: float) -> bool:
        x_offset = self.parent.x if self.parent else 0
        y_offset = self.parent.y if self.parent else 0
        left = self.x + x_offset
        right = left + self.width
        bottom = self.y + y_offset
        top = bottom + self.height

        return (
            (left <= x <= right) and (bottom <= y <= top)
        )

    def on_mouse_motion(self, x, y, dx, dy) -> bool:
        if self.is_inside(x, y):
            if not self.is_on_hover:
                self.hover()
        else:
            if self.is_on_hover and not self.is_on_focus:
                self.is_on_hover = False
                for child in self.children:
                    child.is_on_hover = False
                self.unfocus()
        return pyglet.event.EVENT_UNHANDLED

    def __repr__(self) -> str:
        return f"Widget(x: {self.x}, y: {self.y}. width: {self.width}, height:"\
            f" {self.height})"
