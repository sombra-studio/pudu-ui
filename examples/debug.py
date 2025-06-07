from pudu_ui import Label, LabelParams, Screen, Slider, SliderParams
import pudu_ui
from pyglet.gl import *
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        params = SliderParams(
            x=300, y=100, on_value_changed=self.on_value_changed
        )
        self.slider = Slider(params=params, batch=self.batch)
        # self.slider.set_debug_mode()

        label_style = pudu_ui.styles.fonts.p2()
        label_style.color = pudu_ui.colors.LIGHTER_GRAY
        label_params = LabelParams(
            x=550, y=(100 + self.slider.height / 2.0),
            text=f"{self.slider.value}", anchor_y='center',
            style=label_style
        )
        self.label = Label(
            label_params, batch=self.batch
        )

    def on_value_changed(self, widgets):
        self.label.text = f"{self.slider.value}"
        self.label.invalidate()

    def update(self, dt: float):
        self.slider.update(dt)
        self.label.update(dt)


window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()
window.push_handlers(screen.slider.on_mouse_drag)


@window.event
def on_draw():
    # glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    screen.draw()


def update(dt: float):
    screen.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
