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
        (WIDTH - (M + 1) * ITEM_GAP) / M
    )
)


class Calculator(App):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, caption="Calculator")
        # Grid
        grid_width = WIDTH
        grid_height = grid_width
        params = GridLayoutParams(
            x=0, y=0, width=grid_width, height=grid_height,
            rows=4, columns=4, item_gap=5
        )
        self.grid = GridLayout(params, batch=self.batch)

        for row in SYMBOLS[:-1]:
            for cell in row:
                params = ButtonParams(text=cell)
                params.set_uniform_radius(BUTTON_SIZE * 0.25)
                button = Button(params, batch=self.batch)
                self.push_handlers(button)
                # button.set_debug_mode()
                self.grid.add(button)

        params = ListLayoutParams()
        list_layout = ListLayout()

        self.grid.set_debug_mode()
        self.current_screen.widgets.append(self.grid)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
