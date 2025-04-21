from dataclasses import dataclass
from enum import Enum
import pyglet
from pyglet.graphics import Batch, Group

from pudu_ui.primitives.quad import SolidBordersQuad


class Mode(Enum):
    NORMAL = 0
    DEBUG = 1


@dataclass
class Params:
    x: float = 0.0
    y: float = 0.0
    width: int = 100
    height: int = 100
    focusable: bool = True


class Widget:
    def __init__(
        self, params: Params = None, batch: Batch = None, group: Group = None,
        parent=None
    ):
        if not params:
            params = Params()
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
        self.mode: Mode = Mode.NORMAL

        # Create borders to debug
        self.debug_front_group = Group(4, parent=group)
        self.debug_background: SolidBordersQuad = SolidBordersQuad(
            0, 0, self.width, self.height,
            batch=batch, group=self.debug_front_group,
            parent=self
        )
        self.set_normal_mode()

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
        self.debug_background.width = self.width
        self.debug_background.height = self.height
        self.debug_background.recompute()

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

    def set_normal_mode(self):
        self.mode = Mode.NORMAL
        # self.debug_front_group.visible = False

    def set_debug_mode(self):
        self.mode = Mode.DEBUG
        self.debug_front_group.visible = True


    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(x: {self.x}, y: {self.y}, width:"
            f" {self.width}, height: {self.height})"
        )


class CollectionWidget(Widget):
    def add(self, widget: Widget):
        widget.index = len(self.children)
        widget.parent = self
        self.children.append(widget)
        self.invalidate()

    def insert(self, index: int, widget: Widget):
        count = len(self.children)
        widget.index = index
        widget.parent = self
        self.children.insert(index, widget)
        # Update the rest of children
        for i in range(index + 1, count):
            self.children[i].index = i
        self.invalidate()

    def remove_at(self, index: int):
        count = len(self.children)
        if index >= count:
            raise IndexError(
                f"Index {index} is out of bounds for {self.__class__.__name__}"
                f" with count {count}"
            )
        reminder = self.children[index:]
        new_idx = index
        for elem in reminder:
            elem.index = new_idx
            new_idx += 1
        removed_widget = self.children[index]
        removed_widget.parent = None
        removed_widget.invalidate()
        del self.children[index]

        self.invalidate()
