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
        cell_width = int(self.width / self.columns)
        cell_height = int(self.height / self.rows)
        item_width = int(cell_width - 2 * self.item_gap)
        item_height = int(cell_height - 2 * self.item_gap)

        for item in self.children:
            j, i = utils.get_grid_pos_from_idx(item.index, self.columns)
            # Reposition each item
            item.x = i * cell_width + self.item_gap
            item.y = self.height - j * cell_height - cell_height + self.item_gap
            item.width = item_width
            item.height = item_height
            item.invalidate()
