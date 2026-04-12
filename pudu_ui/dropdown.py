from dataclasses import dataclass, field

from pyglet.graphics import Batch, Group

from pudu_ui import Params, Widget
from pudu_ui.buttons import (
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

        # create menu container
            # create each item

    def expand(self):
        pass

    def collapse(self):
        pass

    def change_style(self, style: DropdownStyle):
        pass
    
    def recompute(self):
        super().recompute()
