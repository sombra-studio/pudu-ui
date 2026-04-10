from dataclasses import dataclass, field

from pyglet.graphics import Batch, Group

from pudu_ui import Params, Widget
from pudu_ui.popup import POPUP_GROUP_ORDER
from pudu_ui.styles.dropdowns import (
    DropdownStyle, default_dropdown_style,
    dft_dropdown_focus_style, dft_dropdown_hover_style
)


DEFAULT_LABEL_CARET_MARGIN = 20


def default_options() -> list[str]:
    return ["undefined"]


@dataclass
class DropdownParams(Params):
    options: list[str] = field(default_factory=default_options)
    label_caret_margin: int = DEFAULT_LABEL_CARET_MARGIN
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
        group = Group(order=POPUP_GROUP_ORDER, parent=group)
        super().__init__(params=params, batch=batch, group=group, parent=parent)

        # create trigger

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
