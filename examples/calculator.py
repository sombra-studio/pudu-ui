from pudu_ui import (
    App, Button, ButtonParams
)
from pudu_ui.layouts import (
    GridLayout, GridLayoutParams, ListLayout,
    ListLayoutParams
)

SYMBOLS = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "x"],
    [".", "0", "﹣", "/"],
    ["C", "⌫", "="]
]
WIDTH = 350
HEIGHT = 600
ITEM_GAP = 5
M = len(SYMBOLS[0])
N = len(SYMBOLS)
BUTTON_SIZE = int(
    round(
        (WIDTH - 2 * M * ITEM_GAP) / M
    )
)


class Calculator(App):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, caption="Calculator")
        # Container

        # List
        list_height = 2 * ITEM_GAP + BUTTON_SIZE
        params = ListLayoutParams(
            x=ITEM_GAP, y=ITEM_GAP, width=WIDTH, height=list_height,
            item_height=BUTTON_SIZE, inter_item_spacing=(2 * ITEM_GAP),
            resizes_item_width=False
        )
        list_layout = ListLayout(params, batch=self.batch)
        for i, cell in enumerate(SYMBOLS[-1]):
            button_size = BUTTON_SIZE
            if i == (len(SYMBOLS[-1]) - 1):
                button_size = 2 * BUTTON_SIZE
            params = ButtonParams(width=button_size, text=cell)
            params.set_uniform_radius(BUTTON_SIZE * 0.25)
            button = Button(params, batch=self.batch)
            list_layout.add(button)
        list_layout.set_debug_mode()
        self.current_screen.widgets.append(list_layout)

        # Grid
        grid_width = WIDTH
        grid_height = grid_width
        params = GridLayoutParams(
            x=0, y=list_height, width=grid_width, height=grid_height,
            rows=4, columns=4, item_gap=ITEM_GAP
        )
        grid = GridLayout(params, batch=self.batch)

        for row in SYMBOLS[:-1]:
            for cell in row:
                params = ButtonParams(text=cell)
                params.set_uniform_radius(BUTTON_SIZE * 0.25)
                button = Button(params, batch=self.batch)
                # button.set_debug_mode()
                grid.add(button)
        # grid.set_debug_mode()
        self.current_screen.widgets.append(grid)




if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
