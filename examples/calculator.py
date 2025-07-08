from pudu_ui import (
    App, Button, ButtonParams, Frame, FrameParams, LabelParams, Label
)
from pudu_ui.label import LabelResizeType
from pudu_ui.layouts import (
    GridLayout, GridLayoutParams, ListDirection, ListLayout,
    ListLayoutParams
)
import pudu_ui
import pyglet


SYMBOLS = [
    ["C", "⌫", "%", "^"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "﹣", "="]
]
WIDTH = 350
HEIGHT = 600
GRID_HEIGHT = (WIDTH // 4) * 5
DISPLAY_HEIGHT = HEIGHT - GRID_HEIGHT
ITEM_GAP = 5
M = len(SYMBOLS[0])
N = len(SYMBOLS)
BUTTON_SIZE = int((WIDTH - 2 * M * ITEM_GAP) / M)


class Display(Frame):
    LABEL_X_MARGIN = 20
    def __init__(self, batch: pyglet.graphics.Batch):
        style = pudu_ui.styles.frames.FrameStyle()
        style.set_solid_color(pudu_ui.colors.LIGHTER_GRAY)
        params = FrameParams(height=DISPLAY_HEIGHT, style=style)
        super().__init__(params=params, batch=batch)

        fs = pudu_ui.styles.fonts.FontStyle(font_size=42)
        params = LabelParams(
            x=self.width - self.LABEL_X_MARGIN,
            y=self.height // 2,
            width=self.width - 2 * self.LABEL_X_MARGIN,
            text="0", anchor_x='right',
            anchor_y='center', resize_type=LabelResizeType.FIT, style=fs
        )
        self.label = Label(params, batch=batch, parent=self)
        self.label.set_debug_mode()
        self.children.append(self.label)

    def recompute(self):
        super().recompute()
        self.label.x = self.width - self.LABEL_X_MARGIN
        self.label.y = self.height // 2
        self.label.width = self.width - 2 * self.LABEL_X_MARGIN
        self.label.invalidate()

    def set_number(self, number: int):
        self.label.text = f"{number}"
        self.label.invalidate()


class Calculator(App):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, caption="Calculator")
        # Container
        params = ListLayoutParams(
            width=WIDTH, height=HEIGHT, focusable=False,
            resizes_item_height=False, direction=ListDirection.VERTICAL
        )
        container = ListLayout(params, batch=self.batch)

        # Display
        display = Display(batch=self.batch)
        container.add(display)

        # Grid
        params = GridLayoutParams(
            width=WIDTH, height=GRID_HEIGHT,
            rows=5, columns=4, item_gap=ITEM_GAP
        )
        grid = GridLayout(params, batch=self.batch)

        for row in SYMBOLS:
            for cell in row:
                params = ButtonParams(text=cell)
                params.set_uniform_radius(BUTTON_SIZE * 0.25)
                button = Button(params, batch=self.batch)
                # button.set_debug_mode()
                grid.add(button)
        # grid.set_debug_mode()

        container.add(grid)
        self.current_screen.widgets.append(container)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
