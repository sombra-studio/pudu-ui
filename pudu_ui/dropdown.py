from dataclasses import dataclass, field

from pyglet.graphics import Batch, Group

from pudu_ui import Params, Widget
from pudu_ui.styles.dropdowns import (
    DropdownItemStyle, DropdownStyle,
    default_dropdown_item_style, default_dropdown_style
)


DEFAULT_LABEL_CARET_MARGIN = 20


def default_options() -> list[str]:
    return ["undefined"]


@dataclass
class DropdownItem(Params):
    text: str = "undefined"
    style: DropdownItemStyle = field(
        default_factory=default_dropdown_item_style
    )
    hover_style: DropdownItemStyle = field(
        default_factory=dft_dpdwn_item_hvr_style
    )
    focus_style: DropdownItemStyle = field(
        default_factory=dft_dpdwn_item_focus_style
    )


@dataclass
class DropdownParams(Params):
    options: list[str] = field(default_factory=default_options)
    label_caret_margin: int = DEFAULT_LABEL_CARET_MARGIN
    style: DropdownStyle = field(default_factory=default_dropdown_style)
    hover_style: DropdownStyle = field(default_factory=dft_dpdwn_hvr_style)
    focus_style: DropdownStyle = field(default_factory=dft_dpdwn_focus_style)


class Dropdown(Widget):
    def __init__(
        self,
        params: DropdownParams=DropdownParams(),
        batch: Batch | None = None,
        group: Group | None = None,
        parent=None
    ):
        super().__init__(params=params, batch=batch, group=group, parent=parent)

