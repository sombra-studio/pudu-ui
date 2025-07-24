from collections.abc import Callable
from enum import StrEnum
from pudu_ui import (
    App, Button, ButtonParams, Frame, FrameParams, LabelParams, Label
)
from pudu_ui.label import LabelResizeType
from pudu_ui.layouts import GridLayout, GridLayoutParams
import pudu_ui
from pyglet.event import EVENT_HANDLE_STATE, EVENT_HANDLED, EVENT_UNHANDLED
from pyglet.window import key
import pyglet


class Operators(StrEnum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "x"
    DIVIDE = "/"
    POWER = "^"


SYMBOLS = [
    ["C", "⌫", "^", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "﹣", "="]
]
number_strs = [str(i) for i in range(10)]
secondary_strs = [".", "﹣"] + number_strs
operator_strs = ["+", "-", "x", "/", "^"]
WIDTH = 350
HEIGHT = 600
ITEM_GAP = 5
GRID_HEIGHT = (WIDTH // 4) * 5
DISPLAY_HEIGHT = HEIGHT - GRID_HEIGHT - 2 * ITEM_GAP
M = len(SYMBOLS[0])
N = len(SYMBOLS)
BUTTON_SIZE = int((WIDTH - 2 * M * ITEM_GAP) / M)
KEY_MAP = {
    key.C: "C",
    key.BACKSPACE: "⌫",
    key.X: "x",
    key.ASTERISK: "x",
    key.NUM_MULTIPLY: "x",
    key.SLASH: "/",
    key.NUM_DIVIDE: "/",
    key.MINUS: "-",
    key.NUM_SUBTRACT: "-",
    key.PLUS: "+",
    key.NUM_ADD: "+",
    key.EQUAL: "=",
    key.NUM_EQUAL: "=",
    key.NUM_ENTER: "=",
    key.ENTER: "=",
    key.RETURN: "=",
    key.PERIOD: ".",
    key.NUM_DECIMAL: "."
}

for i in range(10):
    key_val = key._0 + i
    num_key_val = key.NUM_0 + i
    value = chr(ord('0') + i)
    KEY_MAP[key_val] = value
    KEY_MAP[num_key_val] = value


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
        self.previous_digit = 0
        self.is_second_number = False
        self.current_operator = None
        self.buttons_map = {}

        # Display
        self.number_display = self.create_number_display()

        # Grid
        self.grid = self.create_grid()

        self.current_screen.widgets.append(self.number_display)
        self.current_screen.widgets.append(self.grid)

    def create_grid(self) -> GridLayout:
        params = GridLayoutParams(
            width=WIDTH, height=GRID_HEIGHT,
            rows=5, columns=4, item_gap=ITEM_GAP
        )
        grid = GridLayout(params, batch=self.batch)

        for row in SYMBOLS:
            for cell in row:
                # use the index of the button in the grid as the value in the
                # map
                self.buttons_map[cell] = len(grid.children)
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
                grid.add(button)
        return grid

    def create_number_display(self) -> Display:
        display_width = self.width - 2 * ITEM_GAP
        number_display = Display(batch=self.batch)
        number_display.x = ITEM_GAP
        number_display.y = HEIGHT - ITEM_GAP - number_display.height
        number_display.width = display_width
        number_display.invalidate()
        return number_display

    def set_number(self):
        if self.current_digit < 0:
            decimal_digits = abs(self.current_digit) - 1
            self.current_number = round(self.current_number, decimal_digits)
            decimals_format = f".{decimal_digits}f"
            self.number_display.label.text = (
                f"{self.current_number:{decimals_format}}"
            )
        else:
            self.number_display.label.text = f"{self.current_number}"
        self.number_display.invalidate()

    def use_operator(self, operator: str):
        temp = self.current_number
        match operator:
            case Operators.ADD:
                self.current_number += self.previous_number
            case Operators.SUBTRACT:
                self.current_number = (
                    self.previous_number - self.current_number
                )
            case Operators.MULTIPLY:
                self.current_number *= self.previous_number
            case Operators.DIVIDE:
                self.current_number = (
                    self.previous_number / self.current_number
                )
            case Operators.POWER:
                self.current_number = (
                    self.previous_number ** self.current_number
                )
            case _:
                raise Exception(f"{operator} is not valid")

        self.previous_number = temp
        self.current_digit = min(self.previous_digit, self.current_digit)
        self.set_number()
        self.current_operator = None

    def clear_result(self):
        self.current_number = 0
        self.previous_number = 0
        self.current_digit = 0
        self.is_second_number = False
        self.current_operator = None
        self.set_number()

    def delete(self):
        if self.current_digit > 0:
            self.current_number = self.current_number // 10
        elif self.current_digit == -1:
            self.current_number = int(self.current_number)
        elif self.current_digit < -1:
            self.current_digit += 1
            self.current_number -= self.current_number % (
                10 ** self.current_digit
            )
        self.set_number()

    def enter_digit(self, new_digit_str: str):
        new_digit = int(new_digit_str)
        if self.current_number < 0:
            new_digit *= -1

        if self.current_digit > 0:
            self.current_number = self.current_number * 10 + new_digit
            self.current_digit += 1
        elif self.current_digit == 0:
            self.current_number = new_digit
            self.current_digit += 1
        else:
            decimal_part = new_digit * (10 ** self.current_digit)
            self.current_number = self.current_number + decimal_part
            self.current_digit -= 1
        self.set_number()

    def enter_operator(self, operator_str: str):
        if self.current_operator:
            # we already have an operator
            if self.is_second_number:
                # let's calculate the result for now and put it in the
                # number
                self.use_operator(self.current_operator)
                self.previous_number = self.current_number
            else:
                self.is_second_number = True

        else:
            # we are just adding this operator
            self.is_second_number = True
            self.previous_number = self.current_number
            self.current_number = 0

        self.previous_digit = self.current_digit
        self.current_digit = 0
        self.current_operator = operator_str

    def floating_point(self):
        if self.current_digit > - 1:
            self.current_digit = -1

    def negative(self):
        if self.current_number > 0:
            self.current_number *= -1
        self.set_number()

    def result(self):
        if not self.current_operator:
            return
        self.use_operator(self.current_operator)
        self.previous_number = 0
        self.current_digit = 0
        self.is_second_number = False
        self.current_operator = None

    def map_button_str(self, button_str: str):
        if button_str in number_strs:
            self.enter_digit(button_str)
        elif button_str in operator_strs:
            self.enter_operator(button_str)
        elif button_str == '⌫':
            self.delete()
        elif button_str == 'C':
            self.clear_result()
        elif button_str == '﹣':
            self.negative()
        elif button_str == '.':
            self.floating_point()
        else:
            self.result()

    def on_button_press(self, button: Button):
        self.map_button_str(button.text)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        super().on_key_press(symbol, modifiers)
        if symbol in KEY_MAP:
            button_text = KEY_MAP[symbol]
            button_idx = self.buttons_map[button_text]
            button = self.grid.children[button_idx]
            if isinstance(button, Button):
                button.press()
                return EVENT_HANDLED
        return EVENT_UNHANDLED

    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol in KEY_MAP:
            button_text = KEY_MAP[symbol]
            button_idx = self.buttons_map[button_text]
            button = self.grid.children[button_idx]
            if isinstance(button, Button):
                button.release(False)
                return EVENT_HANDLED
        return EVENT_UNHANDLED

    def __repr__(self):
        return (
            f"prev: {self.previous_number} "
            f"curr: {self.current_number} "
            f"is_second: {self.is_second_number} "
            f"curr_op: {self.current_operator} "
            f"curr_digit: {self.current_digit}"
        )


if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
