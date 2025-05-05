from pudu_ui import Button, Screen
from pudu_ui.layouts import GridLayout, GridLayoutParams
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        layout_params = GridLayoutParams(
            width=200, height=300,
            rows=3, columns=2, item_gap=10.0
        )
        self.grid = GridLayout(layout_params, batch=self.batch)
        num_items = 6
        for i in range(num_items):
            new_item = Button(batch=self.batch)
            self.grid.add(new_item)
            # Use the index given to the new item as the text of the button
            new_item.text = f"{new_item.index}"

        # Invalidate grid to apply text change in buttons
        self.grid.invalidate()
        self.grid.set_debug_mode()
        #for item in self.grid.children:
            #item.set_debug_mode()

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
