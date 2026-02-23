from pyglet.event import EVENT_HANDLE_STATE, EVENT_HANDLED, EVENT_UNHANDLED
from pyglet.gl import glClearColor, glEnable, GL_BLEND
from pyglet.graphics import Batch
from pyglet.window import Window
import pyglet


from pudu_ui.colors import Color, BLACK
from pudu_ui.screen import Screen


class App(Window):
    def __init__(
        self,
        width: int | None = None,
        height: int | None = None,
        caption: str = "Pudu UI",
        update_rate: float = 1.0 / 60.0,
        background_color: Color = BLACK
    ):
        super().__init__(width=width, height=height, caption=caption)
        self.screens: list[Screen] = []
        default_screen = Screen("default screen")
        self.screens.append(default_screen)
        self.current_screen = default_screen
        self.update_rate = update_rate
        self.background_color = background_color
        pyglet.clock.schedule_interval(self.update, update_rate)


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
        glClearColor(*self.background_color.as_vec4())
        self.clear()
        self.current_screen.draw()

    def on_mouse_press(
        self, x: int, y: int, button: int, modifiers: int
    ) -> EVENT_HANDLE_STATE:
        return self.current_screen.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(
        self, x: int, y: int, button: int, modifiers: int
    ) -> EVENT_HANDLE_STATE:
        return self.current_screen.on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(
        self, x: int, y: int, dx: int, dy: int
    ) -> EVENT_HANDLE_STATE:
        return self.current_screen.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(
        self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
    ) -> EVENT_HANDLE_STATE:
        return self.current_screen.on_mouse_drag(
            x, y, dx, dy, buttons, modifiers
        )

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if super().on_key_press(symbol, modifiers) == EVENT_UNHANDLED:
            return self.current_screen.on_key_press(symbol, modifiers)
        return EVENT_HANDLED

    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        return self.current_screen.on_key_release(symbol, modifiers)

    def update(self, dt: float):
        self.current_screen.update(dt)

    def run(self):
        pyglet.app.run(self.update_rate)
