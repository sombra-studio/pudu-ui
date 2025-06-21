from pyglet.gl import glEnable, GL_BLEND
from pyglet.graphics import Batch
from pyglet.window import Window


from pudu_ui.screen import Screen


class App(Window):
    def __init__(
        self,
        width: int | None = None,
        height: int | None = None,
        caption: str = "Pudu UI"
    ):
        super().__init__(width=width, height=height, caption=caption)
        self.screens: list[Screen] = []
        default_screen = Screen("default screen")
        self.screens.append(default_screen)
        self.current_screen = default_screen

    @property
    def batch(self):
        return self.current_screen.batch

    @batch.setter
    def batch(self, new_batch: Batch):
        self.current_screen.batch = new_batch

    def set_screen(self, screen: Screen):
        self.current_screen = screen

    def on_draw(self):
        glEnable(GL_BLEND)
        self.clear()
        self.current_screen.draw()

    def update(self, dt):
        self.current_screen.update(dt)
