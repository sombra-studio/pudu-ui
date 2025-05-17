from pudu_ui import ProgressBar, Screen
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        self.progress_bar = ProgressBar(batch=self.batch)
        self.progress_bar.x = 200
        self.progress_bar.y = 150
        self.progress_bar.value = 75
        self.progress_bar.invalidate()

    def update(self, dt: float):
        self.progress_bar.update(dt)


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
