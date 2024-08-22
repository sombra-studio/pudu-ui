from controllers.two_screens_controller import TwoScreensController
import pyglet


WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640


class App(pyglet.window.Window):
    def __init__(self):
        super().__init__(
            width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption="two screens"
        )
        self.batch = pyglet.graphics.Batch()

    def on_draw(self):
        self.clear()
        self.batch.draw()


if __name__ == '__main__':
    app = App()
    controller = TwoScreensController(app.batch, None)
    pyglet.app.run()
