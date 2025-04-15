from dataclasses import dataclass


from pudu_ui import CollectionWidget, Params
from pudu_ui import utils


@dataclass
class GridLayoutParams(Params):
    width: int = 300
    height: int = 200
    rows: int = 2
    columns: int = 3
    # Item gap is a uniform gap applied to the top, left, right and bottom of
    # every item in the grid
    item_gap: float = 10.0


class GridLayout(CollectionWidget):
    def __init__(self, params: GridLayoutParams = None):
        if not params:
            params = GridLayoutParams()
        super().__init__(params)

        self.rows = params.rows
        self.columns = params.columns
        self.item_gap = params.item_gap

    def recompute(self):
        item_width = int((self.width / self.columns) - 2 * self.item_gap)
        item_height = int((self.height / self.rows) - 2 * self.item_gap)

        for item in self.children:
            j, i = utils.get_grid_pos_from_idx(item.index, self.columns)
            # Reposition each item
            item.x = i * (item_width) + self.item_gap
            item.y = self.height - j * item_height - self.item_gap
            item.width = int(item_width - 2 * self.item_gap)
            item.height = int(item_height - 2 * self.item_gap)
            item.invalidate()
