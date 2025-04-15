from dataclasses import dataclass


from pudu_ui.widget import Params, CollectionWidget


@dataclass
class ListLayoutParams(Params):
    item_width: int = 0
    item_height: int = 0
    inter_item_spacing: int = 0
    reversed: bool = False


class ListLayout(CollectionWidget):
    def __init__(
        self, params: ListLayoutParams = None
    ):
        if not params:
            params = ListLayoutParams()
        super().__init__(params)
        self.item_width = params.item_width
        self.item_height = params.item_height
        self.inter_item_spacing = params.inter_item_spacing
        self.reversed = params.reversed
