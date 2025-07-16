from pudu_ui import (
    App, Button, ButtonParams, Frame, FrameParams, LabelParams, Label
)
from pudu_ui.label import LabelResizeType
from pudu_ui.layouts import GridLayout, GridLayoutParams
import pudu_ui
import pyglet


SYMBOLS = [
    ["C", "⌫", "%", "^"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "﹣", "="]
]
number_strs = [str(i) for i in range(10)]
WIDTH = 350
HEIGHT = 600
ITEM_GAP = 5
GRID_HEIGHT = (WIDTH // 4) * 5
DISPLAY_HEIGHT = HEIGHT - GRID_HEIGHT - 2 * ITEM_GAP
M = len(SYMBOLS[0])
N = len(SYMBOLS)
BUTTON_SIZE = int((WIDTH - 2 * M * ITEM_GAP) / M)


class Display(Frame):
    LABEL_X_MARGIN = 20
    def __init__(self, batch: pyglet.graphics.Batch):
        style = pudu_ui.styles.frames.FrameStyle()
        style.set_solid_color(pudu_ui.colors.DARK_GRAY)
        style.border_width = 2
        style.set_uniform_radius(8)
        params = FrameParams(height=DISPLAY_HEIGHT, style=style)
        super().__init__(params=params, batch=batch)

        fs = pudu_ui.styles.fonts.FontStyle(
            font_size=42, color=pudu_ui.colors.WHITE
        )
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


class OperationButton(Button):
    def __init__(
        self,
        text: str,
        batch: pyglet.graphics.Batch
    ):
        params = ButtonParams(
            text=text, on_press=lambda x: print(x.text)
        )
        super().__init__(params, batch=batch)


class NumberButton(Button):
    def __init__(
        self,
        text: str,
        batch: pyglet.graphics.Batch
    ):
        # unhover style
        style = pudu_ui.styles.buttons.default_button_style()
        style.set_solid_color(pudu_ui.colors.DARK_GRAY)

        # hover style
        hover_style = pudu_ui.styles.buttons.dft_btn_hover_style()
        hover_style.set_solid_color(pudu_ui.colors.GRAY)

        # focus style
        focus_style = pudu_ui.styles.buttons.dft_btn_focus_style()
        focus_style.set_solid_color(pudu_ui.colors.GRAY)

        # press style
        press_style = pudu_ui.styles.buttons.dft_btn_press_style()
        press_style.set_solid_color(pudu_ui.colors.DARKER_GRAY)

        params = ButtonParams(
            text=text, on_press=lambda x: print(x.text),
            style=style, hover_style=hover_style, focus_style=focus_style,
            press_style=press_style
        )
        super().__init__(params, batch=batch)


class Calculator(App):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, caption="Calculator")
        # Display
        display_width = self.width - 2 * ITEM_GAP
        display = Display(
            batch=self.batch
        )
        display.x = ITEM_GAP
        display.y = HEIGHT - ITEM_GAP - display.height
        display.width = display_width
        display.invalidate()

        # Grid
        params = GridLayoutParams(
            width=WIDTH, height=GRID_HEIGHT,
            rows=5, columns=4, item_gap=ITEM_GAP
        )
        grid = GridLayout(params, batch=self.batch)

        for row in SYMBOLS:
            for cell in row:
                if cell in number_strs:
                    button = NumberButton(cell, batch=self.batch)
                else:
                    params = ButtonParams(text=cell)
                    params.set_uniform_radius(BUTTON_SIZE * 0.25)
                    button = Button(params, batch=self.batch)
                # button.set_debug_mode()
                grid.add(button)
        # grid.set_debug_mode()

        self.current_screen.widgets.append(display)
        self.current_screen.widgets.append(grid)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
