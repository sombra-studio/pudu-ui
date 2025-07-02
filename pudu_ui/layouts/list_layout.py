from dataclasses import dataclass
from pyglet.graphics import Batch, Group


from pudu_ui import CollectionWidget, Params, Widget


@dataclass
class ListLayoutParams(Params):
    item_width: int = 0
    item_height: int = 0
    inter_item_spacing: int = 0
    reversed: bool = False
    resizes_item_width: bool = True
    resizes_item_height: bool = True


class ListLayout(CollectionWidget):
    def __init__(
        self, params: ListLayoutParams = None,
        batch: Batch = None, group: Group = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ListLayoutParams()
        super().__init__(params, batch=batch, group=group, parent=parent)
        self.item_width = params.item_width
        self.item_height = params.item_height
        self.inter_item_spacing = params.inter_item_spacing
        self.reversed = params.reversed
        self.resizes_item_width = params.resizes_item_width
        self.resizes_item_height = params.resizes_item_height
