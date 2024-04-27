from dataclasses import dataclass


@dataclass
class Params:
    x: float = 0.0
    y: float = 0.0
    width: float = 100.0
    height: float = 100.0
    scale_x: float = 1.0
    scale_y: float = 1.0
    focusable: bool = False


class Widget:
    def __init__(self, params: Params = Params(), parent=None):
        self._x: float = params.x
        self._y: float = params.y
        self.width: float = params.width
        self.height: float = params.height
        self._scale_x: float = params.scale_x
        self._scale_y: float = params.scale_y
        self._visible: bool = True
        self.focusable: bool = params.focusable
        self.is_on_focus: bool = False
        self.parent: Widget = parent

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value
        if self.parent is not None:
            self._x += self.parent.x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value
        if self.parent is not None:
            self._y += self.parent.y

    def focus(self):
        if self.focusable:
            self.is_on_focus = True

    def unfocus(self):
        if self.focusable:
            self.is_on_focus = False

    def is_inside(self, x: float, y: float) -> bool:
        print(f"x: {x}, self.x: {self.x}, y: {y}, self.y: {self.y}, "
              f"w: {self.width} , h: {self.height}")
        return (
            (self.x <= x <= self.x + self.width) and
            (self.y <= y <= self.y + self.height)
        )

    def __repr__(self):
        return f"Widget(x: {self.x}, y: {self.y}. width: {self.width}, height:"\
            f" {self.height})"
