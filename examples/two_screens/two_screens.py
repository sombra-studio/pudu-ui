import pyglet


from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from controllers.two_screens_controller import TwoScreensController


class App(pyglet.window.Window):
    def __init__(self):
        super().__init__(
            width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption="two screens"
        )

    def on_draw(self):
        self.clear()
        controller.current_screen.draw()


if __name__ == '__main__':
    app = App()
    controller = TwoScreensController()
    app.push_handlers(controller)
    pyglet.app.run()
