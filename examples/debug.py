from pudu_ui import ProgressBar, Screen
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        self.bars = []
        values = [0, 30, 50, 75, 100]
        for i, value in enumerate(values):
            bar = ProgressBar(batch=self.batch)
            bar.x = 200
            bar.y = 500 - i * 100
            bar.value = value
            bar.invalidate()
            self.bars.append(bar)

    def update(self, dt: float):
        for bar in self.bars:
            bar.update(dt)


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
