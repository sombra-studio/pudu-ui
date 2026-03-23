from dataclasses import dataclass, field
from enum import Enum
from pyglet.graphics import Batch, Group
import pyglet
from pyglet.math import Vec2


from pudu_ui import Color
from pudu_ui.primitives.quad import SolidBordersQuad
import pudu_ui


DEBUG_LABEL_OFFSET_X = 0
DEBUG_LABEL_OFFSET_Y = 20


def default_debug_label_color():
    return pudu_ui.colors.DEBUG_TEXT_COLOR


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
    visible: bool = True
    debug_label_color: Color = field(default_factory=default_debug_label_color)


class WidgetGroup(Group):
    def __init__(
        self, widget, order: int = 0, parent: Group | None = None
    ) -> None:
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
        self,
        params: Params | None = None,
        batch: Batch | None = None,
        group: Group | None = None,
        parent=None
    ):
        if not params:
            params = Params()
        self.x: float = params.x
        self.y: float = params.y
        self.width: int = params.width
        self.height: int = params.height
        self.animation_offset_x: float = 0.0
        self.animation_offset_y: float = 0.0
        self.animation_velocity: Vec2 = Vec2()
        self.animation_timer: float = 0.0
        self.batch: Batch = batch
        self.group: WidgetGroup = WidgetGroup(self, parent=group)
        self.parent: Widget | None = parent
        self.is_focusable: bool = params.focusable
        self.is_on_focus: bool = False
        self.is_on_hover: bool = False
        self.is_in_animation: bool = False
        self.is_valid: bool = True
        self.index: int = 0
        self.children: list[Widget] = []
        self.mode: Mode = Mode.NORMAL
        self.group.visible = params.visible

        # Create borders to debug
        self.debug_front_group = WidgetGroup(self, order=4, parent=group)
        self.debug_background: SolidBordersQuad = SolidBordersQuad(
            0, 0, self.width, self.height,
            batch=batch, group=self.debug_front_group,
            parent=self
        )

        # Debug label
        debug_str = self.get_debug_string()
        x, y = self.get_position()
        label_x = x + DEBUG_LABEL_OFFSET_X
        label_y = y + DEBUG_LABEL_OFFSET_Y
        self.debug_label = pyglet.text.Label(
            debug_str, x=label_x, y=label_y, font_size=10,
            color=params.debug_label_color.as_tuple(),
            weight=pyglet.text.Weight.BOLD,
            batch=self.batch, group=self.debug_front_group
        )

        self.set_normal_mode()

    @property
    def visible(self):
        return self.group.visible

    @visible.setter
    def visible(self, value):
        self.group.visible = value

    def get_debug_string(self) -> str:
        return f"{self}"

    def get_position(self) -> tuple[float, float]:
        if self.parent:
            x_offset, y_offset = self.parent.get_position()
        else:
            x_offset = 0.0
            y_offset = 0.0

        if self.is_in_animation:
            x_offset += self.animation_offset_x
            y_offset += self.animation_offset_y

        x = self.x + x_offset
        y = self.y + y_offset
        return x, y

    def lerp_from_position(self, x: float, y: float, secs: float):
        curr_x, curr_y = self.get_position()
        dx = curr_x - x
        dy = curr_y - y
        v = Vec2(dx / secs, dy / secs)
        self.animation_velocity = v
        self.is_in_animation = True
        self.animation_offset_x = -dx
        self.animation_offset_y = -dy
        self.animation_timer = secs

    def on_focus(self):
        self.invalidate()

    def on_unfocus(self):
        self.invalidate()

    def on_hover(self):
        self.invalidate()

    def on_unhover(self):
        self.invalidate()

    def focus(self):
        if self.is_focusable and not self.is_on_focus:
            self.is_on_focus = True
            self.on_focus()

    def unfocus(self):
        if self.is_focusable and self.is_on_focus:
            self.is_on_focus = False
            self.on_unfocus()

    def hover(self):
        if self.is_focusable and not self.is_on_hover and not self.is_on_focus:
            self.is_on_hover = True
            self.on_hover()

    def unhover(self):
        if self.is_focusable and self.is_on_hover:
            self.is_on_hover = False
            self.on_unhover()

    def invalidate(self):
        self.is_valid = False

        if self.parent:
            # Invalidate the parent so that it will update and recompute
            # recursively
            self.parent.invalidate()

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

        for child in self.children:
            child.invalidate()

    def update(self, dt: float):
        # Animate
        if self.is_in_animation:
            self.animation_timer -= dt
            if self.animation_timer <= 0.0:
                # Animation finished, reset everything
                self.animation_timer = 0.0
                self.is_in_animation = False
                self.animation_offset_x = 0.0
                self.animation_offset_y = 0.0

            self.animation_offset_x += self.animation_velocity.x * dt
            self.animation_offset_y += self.animation_velocity.y * dt
            self.recompute()

        elif not self.is_valid:
            self.recompute()
            self.is_valid = True

        # Always call update on every child
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
