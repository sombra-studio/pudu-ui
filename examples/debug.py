from pudu_ui import Screen, Slider, SliderParams
from pyglet.gl import *
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        params = SliderParams(x=300, y=100)
        self.slider = Slider(params=params, batch=self.batch)

    def update(self, dt: float):
        self.slider.update(dt)


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
