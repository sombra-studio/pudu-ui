from pudu_ui import Label, LabelParams, Screen, Slider, SliderParams
import pudu_ui
from pyglet.gl import (
    GL_BLEND, glClearColor, glEnable
)
import pyglet


def create_on_value_change(label: Label):
    def on_value_change(slider: Slider):
        label.text = f"{slider.value}"
        label.invalidate()

    return on_value_change


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")

        num_objects = 4
        for i in range(num_objects):
            params = SliderParams(x=300, y=100 + i * 120)
            slider = Slider(params=params, batch=self.batch)
            # slider.set_debug_mode()

            label_style = pudu_ui.styles.fonts.p2()
            label_style.color = pudu_ui.colors.LIGHTER_GRAY
            label_params = LabelParams(
                x=550, y=(slider.y + slider.height / 2.0),
                text=f"{slider.value}", anchor_y='center',
                style=label_style
            )
            label = Label(
                label_params, batch=self.batch
            )
            slider.on_value_changed = create_on_value_change(label)

            self.widgets.append(slider)
            self.widgets.append(label)


window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()


@window.event
def on_draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
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
