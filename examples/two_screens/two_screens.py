from pudu_ui import ButtonParams, Button, LabelParams, Label
import pudu_ui
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
    # create first screen

    # create second screen

    # add mapping s1 - s2

    # add nav s2 - s1
    pyglet.app.run()
