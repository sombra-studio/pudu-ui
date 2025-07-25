from dataclasses import dataclass, field
from enum import Enum
from pyglet.event import EVENT_HANDLE_STATE, EVENT_HANDLED, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group
import pyglet

from pudu_ui import Color
from pudu_ui.colors import LIGHT_GRAY
from pudu_ui.primitives.quad import SolidBordersQuad


DEBUG_LABEL_OFFSET_X = 10
DEBUG_LABEL_OFFSET_Y = 20


def default_debug_label_color():
    return LIGHT_GRAY


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
    debug_label_color: Color = field(default_factory=default_debug_label_color)


class WidgetGroup(Group):
    def __init__(self, widget, order: int = 0, parent: Group | None = None) -> None:
        super().__init__(order, parent)
        self.widget = widget

    def __eq__(self, other: 'WidgetGroup') -> bool:
        return (
            self.__class__ is other.__class__ and
            self._order == other.order and
            self.parent == other.parent and
            self.widget == other.widget
        )

    def __hash__(self) -> int:
        return hash((self._order, self.parent, self.widget))


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
        self.batch: Batch = batch
        self.group: Group = group
        self.parent: Widget | None = parent
        self.focusable: bool = params.focusable
        self.is_on_focus: bool = False
        self.is_on_hover: bool = False
        self.index: int = 0
        self.is_valid: bool = True
        self.children: list[Widget] = []
        self.mode: Mode = Mode.NORMAL


        # Create borders to debug
        self.debug_front_group = WidgetGroup(self,4, parent=group)
        self.debug_background: SolidBordersQuad = SolidBordersQuad(
            0, 0, self.width, self.height,
            batch=batch, group=self.debug_front_group,
            parent=self
        )

        # Debug label
        debug_str = self.get_debug_string()
        x, y = self.get_position()
        label_x = x - DEBUG_LABEL_OFFSET_X
        label_y = y - DEBUG_LABEL_OFFSET_Y
        self.debug_label = pyglet.text.Label(
            debug_str, x=label_x, y=label_y, font_size=10,
            color=params.debug_label_color.as_tuple(),
            batch=self.batch, group=self.debug_front_group
        )

        self.set_normal_mode()

    def get_debug_string(self) -> str:
        return f"{self}"

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

    def on_unhover(self):
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

    def unhover(self):
        if self.focusable:
            self.is_on_hover = False
            self.on_unhover()
            for child in self.children:
                child.unhover()

    def invalidate(self):
        self.is_valid = False
        for child in self.children:
            child.invalidate()

    def recompute(self):
        # Debug borders
        self.debug_background.width = self.width
        self.debug_background.height = self.height
        self.debug_background.recompute()

        # Debug label
        debug_str = self.get_debug_string()
        x, y = self.get_position()
        label_x = x - DEBUG_LABEL_OFFSET_X
        label_y = y - DEBUG_LABEL_OFFSET_Y
        self.debug_label.text = debug_str
        self.debug_label.x = label_x
        self.debug_label.y = label_y

    def update(self, dt: float):
        if not self.is_valid:
            self.recompute()
            self.is_valid = True
            for child in self.children:
                child.update(dt)

    def is_inside(self, x: float, y: float) -> bool:
        x_pos, y_pos = self.get_position()
        left = x_pos
        right = left + self.width
        bottom = y_pos
        top = bottom + self.height

        return (
            (left <= x <= right) and (bottom <= y <= top)
        )

    def on_mouse_motion(self, x, y, _, __) -> bool:
        if self.is_inside(x, y):
            if not self.is_on_hover:
                self.hover()
        else:
            if self.is_on_hover:
                self.unhover()
        return pyglet.event.EVENT_UNHANDLED

    def set_normal_mode(self):
        self.mode = Mode.NORMAL
        self.debug_front_group.visible = False

    def set_debug_mode(self):
        self.mode = Mode.DEBUG
        self.debug_front_group.visible = True


    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(x: {self.x}, y: {self.y},"
            f" w: {self.width}, h: {self.height})"
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

    def handle_input_event(self, event_name: str, *args) -> EVENT_HANDLE_STATE:
        for widget in self.children:
            # The first widget that handles this event will return
            if hasattr(widget, event_name):
                widget_func = getattr(widget, event_name)
                if widget_func(*args) == EVENT_HANDLED:
                    return EVENT_HANDLED
        return EVENT_UNHANDLED

    def on_mouse_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_press', *args
        )

    def on_mouse_release(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_release', *args
        )

    def on_mouse_motion(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_motion', *args
        )

    def on_mouse_drag(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_drag', *args
        )