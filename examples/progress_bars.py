from pudu_ui import ProgressBar, ProgressBarParams, Screen
import pudu_ui
from pyglet.gl import *
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        self.bars = []
        values = [0, 30, 50, 75, 100]
        # Health bars
        for i, value in enumerate(values):
            bar = ProgressBar(batch=self.batch)
            bar.x = 200
            bar.y = 500 - i * 100
            bar.value = value
            bar.invalidate()
            self.bars.append(bar)

        # Video bars
        height = 12
        style = pudu_ui.styles.progress_bars.ProgressBarStyle(
            left_color=pudu_ui.colors.PURPLE,
            right_color=pudu_ui.colors.DARK_GRAY,
            border_width=0
        )
        style.set_uniform_radius(height / 2.0)
        params = ProgressBarParams(height=height, style=style)

        for i, value in enumerate(values):
            params.x = 500
            params.y = 500 - i * 100
            params.value = value
            bar = ProgressBar(params=params, batch=self.batch)
            self.bars.append(bar)

    def update(self, dt: float):
        for bar in self.bars:
            bar.update(dt)


window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()


@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    screen.draw()


def update(dt: float):
    screen.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
