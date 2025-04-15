from pudu_ui import Screen
from pudu_ui.layouts import GridLayout
from pudu_ui.primitives import Frame
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__("home")
        self.grid = GridLayout()
        num_frames = 4
        for i in range(num_frames):
            new_frame = Frame(batch=self.batch)
            self.grid.add(new_frame)

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
