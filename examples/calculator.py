from pudu_ui import (
    App, Button, ButtonParams, Frame, FrameParams, Label, LabelParams
)
from pudu_ui.layouts import GridLayout, GridLayoutParams
import pudu_ui
import pyglet


WIDTH = 800
HEIGHT = 600
BUTTON_SIZE = 40


class Calculator(App):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, caption="Calculator")
        symbols = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "x"],
            [".", "0", "﹣", "/"],
            ["C", "⌫", "="]
        ]
        grid_width = len(symbols[0]) * BUTTON_SIZE
        grid_height = (len(symbols) - 1) * BUTTON_SIZE
        params = GridLayoutParams(
            x=100, y=20+10+BUTTON_SIZE, width=grid_width, height=grid_height,
            rows=4, columns=4, item_gap=5
        )
        self.grid = GridLayout(params, batch=self.batch)

        for row in symbols[:-1]:
            for cell in row:
                params = ButtonParams(text=cell)
                params.set_uniform_radius(4)
                button = Button(params, batch=self.batch)
                self.push_handlers(button)
                # button.set_debug_mode()
                self.grid.add(button)

        self.grid.set_debug_mode()

    def update(self, dt):
        self.grid.update(dt)


if __name__ == '__main__':
    calculator = Calculator()
    pyglet.clock.schedule_interval(calculator.update, 1.0 / 60.0)
    pyglet.app.run()
