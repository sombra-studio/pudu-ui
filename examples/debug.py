from pudu_ui import Screen
from pudu_ui.layouts import GridLayout, GridLayoutParams
from pudu_ui import Button, ButtonParams
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__("home")
        layout_params = GridLayoutParams(
            width=200, height=300,
            rows=3, columns=2, item_gap=10.0
        )
        self.grid = GridLayout(layout_params)
        num_items = 6
        for i in range(num_items):
            params = ButtonParams(text=f"{i}")
            new_item = Button(params, batch=self.batch)
            self.grid.add(new_item)

    def update(self, dt: float):
        self.grid.update(dt)


window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()

@window.event
def on_draw():
    window.clear()
    screen.draw()


def update(dt: float):
    screen.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
