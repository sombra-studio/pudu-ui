from dataclasses import dataclass


from pudu_ui.widget import Params, Widget


@dataclass
class ListLayoutParams(Params):
    item_width: int = 0
    item_height: int = 0
    inter_item_spacing: int = 0
    reversed: bool = False


class ListLayout(Widget):
    def __init__(
        self, params: ListLayoutParams
    ):
        super().__init__(params)
        self.item_width = params.item_width
        self.item_height = params.item_height
        self.inter_item_spacing = params.inter_item_spacing
        self.reversed = params.reversed
        self.items: list[Widget] = []

    def add(self, widget: Widget):
        self.items.append(widget)
        widget.index = len(self.items) - 1
        self.invalidate()

    def remove(self, index: int):
        count = len(self.items)
        if index >= count:
            raise IndexError(
                f"Index {index} is out of bounds for list layout with count "
                f"{count}"
            )
        reminder = self.items[index:]
        new_idx = index
        for elem in reminder:
            elem.index = new_idx
            new_idx += 1
        del self.items[index]
        self.invalidate()
