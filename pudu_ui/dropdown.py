from collections.abc import Callable
from dataclasses import dataclass, field

from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group

from pudu_ui import Button, ButtonParams, Frame, FrameParams, Params, Widget
from pudu_ui.dropdown_trigger import (
    default_trigger_params, DropdownTrigger, DropdownTriggerParams
)
from pudu_ui.layouts import ListDirection, ListLayout, ListLayoutParams
from pudu_ui.styles.dropdowns import (
    DropdownStyle, default_dropdown_style,
    dft_dropdown_focus_style, dft_dropdown_hover_style
)


LIST_INTER_ITEM_SPACING = 5
CONTAINER_PADDING = 6
DEFAULT_TRIGGER_CONTAINER_MARGIN = 8


def default_options() -> list[str]:
    return ["undefined", "undefined", "undefined"]


@dataclass
class DropdownParams(Params):
    width: int = 160
    height: int = 200
    options: list[str] = field(default_factory=default_options)
    on_select: Callable[[str], None] = lambda s: None
    trigger_container_margin: int = DEFAULT_TRIGGER_CONTAINER_MARGIN
    trigger_params: DropdownTriggerParams = field(
        default_factory=default_trigger_params
    )
    style: DropdownStyle = field(default_factory=default_dropdown_style)
    hover_style: DropdownStyle = field(default_factory=dft_dropdown_hover_style)
    focus_style: DropdownStyle = field(default_factory=dft_dropdown_focus_style)


class Dropdown(Widget):
    def __init__(
        self,
        params: DropdownParams=DropdownParams(),
        batch: Batch | None = None,
        group: Group | None = None,
        parent=None
    ):
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        self.on_select = params.on_select
        self.trigger_container_margin = params.trigger_container_margin
        self.is_expanded = False

        self.back_group = Group(parent=self.group)
        self.front_group = Group(order=1, parent=self.group)

        # create trigger
        params.trigger_params.y = (
            self.height - params.trigger_params.height
            + params.trigger_container_margin
        )
        params.trigger_params.on_trigger = self.on_trigger
        params.trigger_params.style = params.style.trigger_style
        self.trigger = DropdownTrigger(
            params=params.trigger_params,
            batch=batch, group=self.front_group, parent=self
        )
        self.children.append(self.trigger)

        # create menu container
        container_height = self.height - (
            self.trigger.height + params.trigger_container_margin
        )
        container_bg_params = FrameParams(
            width=self.width, height=container_height, visible=False,
            style=params.style.menu_container_style
        )
        self.container_bg = Frame(
            params=container_bg_params, batch=batch, group=self.back_group,
            parent=self
        )
        list_width = self.container_bg.width - 2 * CONTAINER_PADDING
        list_height = self.container_bg.height - 2 * CONTAINER_PADDING
        list_params = ListLayoutParams(
            x=CONTAINER_PADDING, y=CONTAINER_PADDING,
            width=list_width, height=list_height,
            visible=False,
            inter_item_spacing=LIST_INTER_ITEM_SPACING,
            resizes_item_width=True, resizes_item_height=True,
            direction=ListDirection.VERTICAL
        )
        self.list_layout = ListLayout(
            params=list_params, batch=batch, group=self.front_group, parent=self
        )
        for option in params.options:
            # create each item
            button_params = ButtonParams(
                text=option,
                on_press=self.on_option_press,
                style=params.style.items_style,
                hover_style=params.hover_style.items_style,
                focus_style=params.focus_style.items_style,
                press_style=params.hover_style.items_style,
            )
            button = Button(
                params=button_params, batch=batch, group=self.list_layout.group
            )
            self.list_layout.add(button)

        self.children.append(self.list_layout)


    def on_trigger(self, _):
        if self.is_expanded:
            self.collapse()
        else:
            self.expand()

    def on_option_press(self, option: Button):
        self.on_select(option.text)
        self.collapse()

    def expand(self):
        self.container_bg.visible = True
        self.list_layout.visible = True
        self.list_layout.is_focusable = True
        self.is_expanded = True

    def collapse(self):
        self.container_bg.visible = False
        self.list_layout.visible = False
        self.list_layout.is_focusable = False
        self.is_expanded = False
    
    def recompute(self):
        super().recompute()
        self.trigger.y = (
            self.height - self.trigger.height + self.trigger_container_margin
        )

        # create menu container
        self.container_bg.width = self.width
        self.container_bg.height = (
            self.height - self.trigger.height - self.trigger_container_margin
        )

        list_width = self.container_bg.width - 2 * CONTAINER_PADDING
        list_height = self.container_bg.height - 2 * CONTAINER_PADDING
        self.list_layout.width = list_width
        self.list_layout.height = list_height

    # Events

    def handle_input_event(self, event_name: str, *args) -> EVENT_HANDLE_STATE:
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

    def on_key_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_key_press', *args
        )

    def on_key_release(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_key_release', *args
        )
