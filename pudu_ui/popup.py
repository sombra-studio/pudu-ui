from collections.abc import Callable
from dataclasses import dataclass, field

from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group

from pudu_ui import (
    Button, ButtonParams, FrameParams, Frame, Label, LabelParams,
    Params, Widget
)
from pudu_ui.label import LabelResizeType
from pudu_ui.styles.fonts import h2, p1
from pudu_ui.styles.popups import PopUpStyle, default_popup_style


DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 380
TITLE_MARGIN_Y = 12
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 64
BUTTON_MARGIN_Y = 12
BUTTON_MARGIN_X = 32
POPUP_GROUP_ORDER = 100     # Arbitrarily large number


@dataclass
class PopUpParams(Params):
    width: int = DEFAULT_WIDTH
    height: int = DEFAULT_HEIGHT
    visible: bool = False
    title: str = ""
    description: str = ""
    opt1_text: str = ""
    opt2_text: str = ""
    opt1_callback: Callable[..., ...] | None = None
    opt2_callback: Callable[..., ...] | None = None
    style: PopUpStyle = field(default_factory=default_popup_style)


class PopUp(Widget):
    def __init__(
        self,
        params: PopUpParams | None = None,
        batch: Batch | None = None,
        group: Group | None = None
    ):
        self.is_opened = False
        # This should make the popup be on top of everything
        group = Group(order=POPUP_GROUP_ORDER, parent=group)
        super().__init__(params=params, batch=batch, group=group)
        if not params:
            params = PopUpParams()
        frame_params = FrameParams(
            x=params.x, y=params.y, width=params.width, height=params.height,
            style=params.style.background_style
        )
        self.frame = Frame(params=frame_params, batch=batch, group=self.group)

        title_params = LabelParams(
            x=params.width//2, y=params.height - TITLE_MARGIN_Y,
            width=int(params.width * 0.8),  # Max. width set to 80%
            text=params.title,
            anchor_x='center', anchor_y='top',
            resize_type=LabelResizeType.FIT,
            style=h2()
        )
        self.title = Label(
            params=title_params, batch=batch, group=self.group, parent=self
        )

        desc_height = (
            params.height -
            self.title.impl.content_height - 2 * TITLE_MARGIN_Y -
            BUTTON_HEIGHT - 2 * BUTTON_MARGIN_Y
        )
        desc_params = LabelParams(
            x=params.width//2, y=params.height//2,
            width=int(params.width * 0.8),  # Max. width set to 80%
            height=desc_height,
            text=params.description,
            anchor_x='center', anchor_y='center', multiline=True,
            resize_type=LabelResizeType.FIT,
            style=p1()
        )
        self.description = Label(
            params=desc_params, batch=batch, group=self.group, parent=self
        )

        if params.opt1_callback:
            if params.opt2_callback:
                # Make two buttons
                left_x = (
                    params.width // 2 - BUTTON_MARGIN_X // 2 - BUTTON_WIDTH
                )
                btn_params = ButtonParams(
                    x=left_x, y=BUTTON_MARGIN_Y,
                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                    text=params.opt1_text, on_press=params.opt1_callback
                    # TODO: Add styles
                )
                btn_left = Button(
                    params=btn_params, batch=batch, group=self.group,
                    parent=self
                )
                self.children.append(btn_left)

                right_x = (
                    params.width // 2 + BUTTON_MARGIN_X // 2
                )
                btn_params.x = right_x
                btn_params.text = params.opt2_text
                btn_params.on_press = params.opt2_callback
                # TODO: Add styles
                btn_right = Button(
                    params=btn_params, batch=batch, group=self.group,
                    parent=self
                )
                self.children.append(btn_right)
            else:
                # Make one button
                btn_params = ButtonParams(
                    x=params.width // 2 - BUTTON_WIDTH // 2, y=BUTTON_MARGIN_Y,
                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                    text=params.opt1_text, on_press=params.opt1_callback
                    # TODO: Add styles
                )
                btn = Button(
                    params=btn_params, batch=batch, group=self.group,
                    parent=self
                )
                self.children.append(btn)

    def open(self):
        self.is_opened = True
        self.visible = True

    def dismiss(self):
        self.is_opened = False
        self.visible = False

    def handle_input_event(self, event_name: str, *args) -> EVENT_HANDLE_STATE:
        if not self.is_opened:
            return EVENT_UNHANDLED

        for widget in self.children:
            # The first widget that handles this event will return
            if hasattr(widget, event_name):
                widget_func = getattr(widget, event_name)
                if widget_func(*args) == EVENT_HANDLED:
                    return True
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

    def on_key_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_key_press', *args
        )

    def on_key_release(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_key_release', *args
        )
