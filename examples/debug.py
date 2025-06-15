from pudu_ui import Frame, FrameParams, Screen, Slider, SliderParams
import pudu_ui
from pyglet.gl import (
    GL_BLEND, glClearColor, glEnable
)
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        n = 4
        size = 100
        # for i in range(n):
        #     style = pudu_ui.styles.frames.FrameStyle()
        #     style.set_uniform_radius(50.0)
        #     params = FrameParams(
        #         x=435, y=104 + i * 150, width=size, height=size,
        #         style=style
        #     )
        #     frame = Frame(params, batch=self.batch)
        #     self.widgets.append(frame)
        # params = SliderParams(x=300, y=100)
        # slider = Slider(params, batch=self.batch)
        # self.widgets.append(slider)

        num_objects = 4
        for i in range(num_objects):
            params = SliderParams(x=300, y=100 + i * 120)
            slider = Slider(params, batch=self.batch)
            self.widgets.append(slider)

        # self.quad = pudu_ui.primitives.quad.Quad(
        #     x=100, y=150,
        #     batch=self.batch
        # )





window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()


@window.event
def on_draw():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    window.clear()
    glEnable(GL_BLEND)
    screen.draw()


def update(dt: float):
    screen.update(dt)


if __name__ == '__main__':
    for widget in screen.widgets:
        if isinstance(widget, Slider):
            window.push_handlers(widget)
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
