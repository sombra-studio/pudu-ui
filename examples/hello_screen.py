import pudu_ui
from pudu_ui import Label, LabelParams
import pyglet


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class HelloScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch = pyglet.graphics.get_default_batch()
    ):
        super().__init__(
            "hello",
            batch=batch
        )
        params = LabelParams(x=50, y=100, text="Hello World")
        self.label = Label(params, batch=batch)


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Test")
batch = pyglet.graphics.Batch()
screen = HelloScreen(batch=batch)


@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
