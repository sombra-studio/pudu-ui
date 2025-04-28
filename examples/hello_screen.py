import pudu_ui
from pudu_ui import Label, LabelParams
import pyglet


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class HelloScreen(pudu_ui.Screen):
    def __init__(self):
        super().__init__("hello")
        params = LabelParams(x=50, y=100, text="Hello World")
        self.label = Label(params, batch=self.batch)

        fs = pudu_ui.styles.fonts.p2()
        fs.color = pudu_ui.colors.GRAY
        params = LabelParams(x=50, y=40, text="Trying something", style=fs)
        self.l2 = Label(params, batch=self.batch)

        self.label.set_debug_mode()
        # self.l2.set_debug_mode()
        self.l2.set_normal_mode()
        # self.label.set_normal_mode()
        print("stop")


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Test")
batch = pyglet.graphics.Batch()
screen = HelloScreen()


@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    screen.draw()


def update(dt: float):
    screen.label.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
