from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui import Widget
from pudu_ui.buttons.button import Button, ButtonParams
from pudu_ui.styles.dropdowns import TriggerStyle, dft_trigger_style


DEFAULT_LABEL_CARET_MARGIN = 20


@dataclass
class DropdownTriggerParams(ButtonParams):
    style: TriggerStyle = field(default_factory=dft_trigger_style)
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
