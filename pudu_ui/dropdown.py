from dataclasses import dataclass, field

from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group

from pudu_ui import Params, Widget
from pudu_ui.dropdown_trigger import (
    default_trigger_params, DropdownTrigger, DropdownTriggerParams
)
from pudu_ui.styles.dropdowns import (
    DropdownStyle, default_dropdown_style,
    dft_dropdown_focus_style, dft_dropdown_hover_style
)


def default_options() -> list[str]:
    return ["undefined"]


@dataclass
class DropdownParams(Params):
    options: list[str] = field(default_factory=default_options)
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

        # create trigger
        self.trigger = DropdownTrigger(
            params=params.trigger_params,
            batch=batch, group=self.group, parent=self
        )
        self.children.append(self.trigger)

        # create menu container
            # create each item

    def expand(self):
        pass

    def collapse(self):
        pass
    
    def recompute(self):
        super().recompute()

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
