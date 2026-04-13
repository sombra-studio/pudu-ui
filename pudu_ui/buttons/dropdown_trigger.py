from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui import Widget
from pudu_ui.buttons.button import Button, ButtonParams
from pudu_ui.styles.dropdowns import (
    TriggerStyle, dft_trigger_focus_style, dft_trigger_hover_style,
    dft_trigger_style
)


DEFAULT_LABEL_CARET_MARGIN = 20


@dataclass
class DropdownTriggerParams(ButtonParams):
    style: TriggerStyle = field(default_factory=dft_trigger_style)
    hover_style: TriggerStyle = field(default_factory=dft_trigger_hover_style)
    focus_style: TriggerStyle = field(default_factory=dft_trigger_focus_style)
    press_style: TriggerStyle = field(default_factory=dft_trigger_hover_style)
    label_caret_margin: int = DEFAULT_LABEL_CARET_MARGIN


def default_trigger_params():
    return DropdownTriggerParams()


class DropdownTrigger(Button):
    def __init__(
        self,
        params: DropdownTriggerParams = DropdownTriggerParams(),
        batch: Batch = None,
        group: Group = None,
        parent: Widget | None = None
    ):
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        self.set_debug_mode()
