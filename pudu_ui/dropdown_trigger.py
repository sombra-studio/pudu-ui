from dataclasses import dataclass, field
from typing import Callable

from pyglet.event import EVENT_HANDLED, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group
from pyglet.window import key, mouse

from pudu_ui import Frame, FrameParams, Label, LabelParams, Params, Widget
from pudu_ui.arrow import Arrow, ArrowParams
from pudu_ui.enums import Direction
from pudu_ui.label import LabelResizeType
from pudu_ui.styles.dropdowns import (
    TriggerStyle, dft_trigger_focus_style, dft_trigger_hover_style,
    dft_trigger_style
)


DEFAULT_WIDTH = 150
DEFAULT_HEIGHT = 60
DEFAULT_LABEL_WIDTH = 80
DEFAULT_LABEL_CARET_MARGIN = 10
CARET_WIDTH = 20
CARET_HEIGHT = 12


@dataclass
class DropdownTriggerParams(Params):
    width: int = DEFAULT_WIDTH
    height: int = DEFAULT_HEIGHT
    focusable: bool = True
    text: str = "undefined"
    label_width: int = DEFAULT_LABEL_WIDTH
    label_caret_margin: int = DEFAULT_LABEL_CARET_MARGIN
    on_trigger: Callable[..., None] = lambda *args: None
    style: TriggerStyle = field(default_factory=dft_trigger_style)
    hover_style: TriggerStyle = field(default_factory=dft_trigger_hover_style)
    focus_style: TriggerStyle = field(default_factory=dft_trigger_focus_style)



def default_trigger_params():
    return DropdownTriggerParams()


class DropdownTrigger(Widget):
    def __init__(
        self,
        params: DropdownTriggerParams = DropdownTriggerParams(),
        batch: Batch = None,
        group: Group = None,
        parent: Widget | None = None
    ):
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        self.front_group = Group(order=1)
        self.back_group = Group()
        self.text = params.text
        self.label_width = params.label_width
        self.label_caret_margin = params.label_caret_margin
        self.on_trigger = params.on_trigger
        self.style = params.style
        self.hover_style = params.hover_style
        self.focus_style = params.focus_style
        self.background = self.create_background()
        self.label = self.create_label()
        self.caret = self.create_caret()

        self.children.append(self.background)
        self.children.append(self.label)
        self.children.append(self.caret)

    def create_background(self) -> Frame:
        params = FrameParams(
            width=self.width, height=self.height, style=self.style.frame_style
        )
        frame = Frame(
            params=params, batch=self.batch, group=self.back_group, parent=self
        )
        frame.visible = self.style.frame_visible
        return frame

    def create_label(self) -> Label:
        label_x = self.width / 2.0
        label_y = self.height / 2.0
        label_params = LabelParams(
            label_x,
            label_y,
            width=self.label_width,
            text=self.text,
            anchor_x='center',
            anchor_y='center',
            resize_type=LabelResizeType.FIT,
            style=self.style.font_style
        )
        label = Label(
            label_params, batch=self.batch, group=self.front_group, parent=self
        )
        return label

    def create_caret(self) -> Arrow:
        caret_x = (
            self.label.x + self.label.impl.content_width / 2.0 +
            self.label_caret_margin
        )
        params = ArrowParams(
            x=caret_x, width=CARET_WIDTH, height=CARET_HEIGHT,
            direction=Direction.DOWN
        )
        params.y = self.height / 2.0 - params.height / 2.0
        arrow = Arrow(
            params=params, batch=self.batch, group=self.front_group, parent=self
        )
        return arrow

    def trigger(self):
        self.on_trigger(self)

    def change_style(self, style: TriggerStyle):
        self.background.change_style(style.frame_style)
        self.label.change_style(style.font_style)
        self.caret.change_style(style.arrow_style)
        self.background.visible = style.frame_visible

    def on_hover(self):
        super().on_hover()
        self.change_style(self.hover_style)

    def on_unhover(self):
        super().on_unhover()
        if self.is_on_focus:
            self.change_style(self.focus_style)
        else:
            self.change_style(self.style)

    def on_focus(self):
        super().on_focus()
        self.change_style(self.focus_style)

    def on_unfocus(self):
        super().on_unfocus()
        self.change_style(self.style)

    def recompute(self):
        super().recompute()

        # Recompute background
        self.background.width = self.width
        self.background.height = self.height

        # Recompute label
        # This will keep the label centered in the button
        self.label.x = self.width / 2.0
        self.label.y = self.height / 2.0
        self.label.text = self.text
        self.label.width = self.label_width
        self.label.height = self.height

        # Recompute caret
        self.caret.x = (
            self.label.x + self.label_width / 2.0 + self.label_caret_margin
        )
        self.caret.y = self.height / 2.0 - self.caret.height / 2.0

    # Events

    # Override function
    def on_mouse_press(self, x, y, buttons, _):
        if self.is_inside(x, y) and buttons & mouse.LEFT:
            self.trigger()
            return EVENT_HANDLED
        return EVENT_UNHANDLED

    # Override function
    def on_key_press(self, symbol, _):
        if (
            self.is_on_focus and
            (symbol == key.ENTER or symbol == key.RETURN)
        ):
            self.trigger()
            return EVENT_HANDLED
        return EVENT_UNHANDLED