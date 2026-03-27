from dataclasses import dataclass, field
from copy import deepcopy
from pyglet.event import EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group
from pyglet.window import key, mouse


from pudu_ui import Frame, FrameParams, Params, Widget, WidgetGroup
from pudu_ui.styles.toggles import (
    ToggleStyle, DEFAULT_TOGGLE_THUMB_RADIUS, dft_off_focus_toggle_style,
    dft_off_toggle_style, dft_on_focus_toggle_style, dft_on_toggle_style,
)


DEFAULT_TOGGLE_WIDTH = 56
TOGGLE_MARGIN_X = 2
TOGGLE_MARGIN_Y = 2
DEFAULT_TOGGLE_HEIGHT = 2 * TOGGLE_MARGIN_Y + 2 * DEFAULT_TOGGLE_THUMB_RADIUS
TOGGLE_ANIMATION_TIME = 0.15


@dataclass
class ToggleParams(Params):
    width: int = DEFAULT_TOGGLE_WIDTH
    height: int = DEFAULT_TOGGLE_HEIGHT
    is_on: bool = True
    on_style: ToggleStyle = field(default_factory=dft_on_toggle_style)
    off_style:  ToggleStyle = field(default_factory=dft_off_toggle_style)
    on_focus_style: ToggleStyle = field(
        default_factory=dft_on_focus_toggle_style
    )
    off_focus_style: ToggleStyle = field(
        default_factory=dft_off_focus_toggle_style
    )


class Toggle(Widget):
    def __init__(
        self,
        params: ToggleParams | None = None,
        batch: Batch | None = None,
        group: Group | None = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ToggleParams()
        super().__init__(params=params, batch=batch, group=group, parent=parent)

        self.is_on = params.is_on

        self.style = deepcopy(
            params.on_style if self.is_on else params.off_style
        )
        self.on_style = deepcopy(params.on_style)
        self.off_style = deepcopy(params.off_style)
        self.on_focus_style = deepcopy(params.on_focus_style)
        self.off_focus_style = deepcopy(params.off_focus_style)

        self.back_group = WidgetGroup(widget=self, order=0, parent=self.group)
        self.front_group = WidgetGroup(widget=self, order=1, parent=self.group)

        self.background = self.create_background()
        self.thumb = self.create_thumb()

        self.children.append(self.background)
        self.children.append(self.thumb)

    def create_background(self) -> Frame:
        frame_params = FrameParams(
            width=self.width, height=self.height,
            style=self.style.background_style
        )
        frame = Frame(
            params=frame_params, batch=self.batch, group=self.back_group,
            parent=self
        )
        return frame

    def create_thumb(self) -> Frame:
        thumb_size = self.height - 2 * TOGGLE_MARGIN_Y
        thumb_x = self.width - thumb_size - TOGGLE_MARGIN_X
        frame_params = FrameParams(
            x=thumb_x, y=TOGGLE_MARGIN_Y,
            width=thumb_size, height=thumb_size,
            style=self.style.thumb_style
        )
        frame = Frame(
            params=frame_params, batch=self.batch, group=self.front_group,
            parent=self
        )
        return frame

    def change_style(self, style: ToggleStyle):
        self.style = deepcopy(style)
        self.background.change_style(style.background_style)
        self.thumb.change_style(style.thumb_style)

    def on(self):
        self.is_on = True
        new_style = self.on_focus_style if self.is_on_focus else self.on_style
        self.change_style(new_style)
        previous_x = self.thumb.x
        # Move thumb to the right
        self.thumb.x = self.width - TOGGLE_MARGIN_X - self.thumb.width
        self.thumb.invalidate()
        self.thumb.lerp_from_position(
            previous_x, self.thumb.y, TOGGLE_ANIMATION_TIME
        )

    def off(self):
        self.is_on = False
        new_style = self.off_focus_style if self.is_on_focus else self.off_style
        self.change_style(new_style)
        previous_x = self.thumb.x
        # Move thumb to the right
        self.thumb.x = TOGGLE_MARGIN_X
        self.thumb.invalidate()
        self.thumb.lerp_from_position(
            previous_x, self.thumb.y, TOGGLE_ANIMATION_TIME
        )

    def press(self):
        if self.is_on:
            self.off()
        else:
            self.on()

    def recompute(self):
        super().recompute()
        self.background.width = self.width
        self.background.height = self.height

        thumb_size = self.height - 2 * TOGGLE_MARGIN_Y
        thumb_x = self.width - TOGGLE_MARGIN_X - self.thumb.width if \
            self.is_on else TOGGLE_MARGIN_X
        self.thumb.x = thumb_x
        self.thumb.width = thumb_size
        self.thumb.height = thumb_size
        self.thumb.style.set_uniform_radius(thumb_size / 2.0)

    # Events

    def on_focus(self):
        super().on_focus()
        style = self.on_focus_style if self.is_on else self.off_focus_style
        self.change_style(style)

    def on_unfocus(self):
        super().on_unfocus()
        style = self.on_style if self.is_on else self.off_style
        self.change_style(style)

    def on_mouse_press(self, x, y, buttons, _) -> EVENT_HANDLE_STATE:
        if self.is_inside(x, y) and buttons & mouse.LEFT:
            self.press()
            return True
        return EVENT_UNHANDLED

    def on_key_press(self, symbol, _) -> EVENT_HANDLE_STATE:
        if (
            self.is_on_focus and
            (symbol == key.ENTER or symbol == key.RETURN)
        ):
            self.press()
            return True
        return EVENT_UNHANDLED
