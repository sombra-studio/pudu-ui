from collections.abc import Callable
from enum import StrEnum
from pudu_ui import (
    App, Button, ButtonParams, Frame, FrameParams, LabelParams, Label
)
from pudu_ui.label import LabelResizeType
from pudu_ui.layouts import GridLayout, GridLayoutParams
import pudu_ui
import pyglet


class Operators(StrEnum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"


SYMBOLS = [
    ["C", "⌫", "%", "^"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "﹣", "="]
]
number_strs = [str(i) for i in range(10)]
secondary_strs = [".", "﹣"] + number_strs
operator_strs = ["+", "-", "*", "/", "%"]
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
        self.children.append(self.label)

    def recompute(self):
        super().recompute()
        self.label.x = self.width - self.LABEL_X_MARGIN
        self.label.y = self.height // 2
        self.label.width = self.width - 2 * self.LABEL_X_MARGIN
        self.label.invalidate()

    def set_number(self, number: float):
        self.label.text = f"{number}"
        self.invalidate()


class OperationButton(Button):
    def __init__(
        self,
        text: str,
        on_press: Callable[[...], None],
        batch: pyglet.graphics.Batch
    ):
        params = ButtonParams(text=text, on_press=on_press)
        super().__init__(params, batch=batch)


class SecondaryButton(Button):
    def __init__(
        self,
        text: str,
        on_press: Callable[[...], None],
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
            text=text, on_press=on_press,
            style=style, hover_style=hover_style, focus_style=focus_style,
            press_style=press_style
        )
        super().__init__(params, batch=batch)


class Calculator(App):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, caption="Calculator")
        self.current_number = 0
        self.previous_number = 0
        self.current_digit = 0
        self.is_second_number = False
        self.current_operator = None


        # Display
        display_width = self.width - 2 * ITEM_GAP
        self.number_display = Display(
            batch=self.batch
        )
        self.number_display.x = ITEM_GAP
        self.number_display.y = HEIGHT - ITEM_GAP - self.number_display.height
        self.number_display.width = display_width
        self.number_display.invalidate()

        # Grid
        params = GridLayoutParams(
            width=WIDTH, height=GRID_HEIGHT,
            rows=5, columns=4, item_gap=ITEM_GAP
        )
        grid = GridLayout(params, batch=self.batch)

        for row in SYMBOLS:
            for cell in row:
                if cell in secondary_strs:
                    button = SecondaryButton(
                        cell,
                        on_press=self.on_button_press,
                        batch=self.batch
                    )
                else:
                    button = OperationButton(
                        cell,
                        on_press=self.on_button_press,
                        batch=self.batch
                    )
                # button.set_debug_mode()
                grid.add(button)
        # grid.set_debug_mode()

        self.current_screen.widgets.append(self.number_display)
        self.current_screen.widgets.append(grid)

    def set_number(self):
        self.number_display.set_number(self.current_number)

    def on_button_press(self, button: Button):
        if button.text in number_strs:
            # Pressed a number
            new_digit = int(button.text)
            self.current_number = self.current_number * 10 + new_digit
            self.current_digit += 1
            if self.current_digit > -1:
                self.set_number()
        elif button.text in operator_strs:
            if self.current_operator:
                # we already have an operator
                if self.is_second_number:
                    # let's calculate the result for now and put it in the
                    # number
                    if self.current_operator == Operators.ADD:
                        self.current_number += self.previous_number
                    elif self.current_operator == Operators.SUBTRACT:
                        self.current_number = (
                            self.previous_number - self.current_number
                        )
                    elif self.current_operator == Operators.MULTIPLY:
                        self.current_number *= self.previous_number
                    elif self.current_operator == Operators.DIVIDE:
                        self.current_number = (
                            self.previous_number / self.current_number
                        )
                else:
                    self.is_second_number = True
                    self.current_number = 0

                self.previous_number = self.current_number

                self.set_number()
            else:
                # we are just adding this operator
                self.is_second_number = True
                self.current_number = 0
                self.set_number()
            self.current_operator = button.text
        print(button.text)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
