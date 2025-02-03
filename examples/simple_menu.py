import pudu_ui
from pudu_ui import Button, ButtonParams
from pudu_ui.layouts import ListLayoutParams, VerticalListLayout
import pyglet


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class SimpleMenuScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch = pyglet.graphics.get_default_batch()
    ):
        super().__init__(
            "menu",
            batch=batch
        )
        vertical_margin = 50
        width = 250
        height = SCREEN_HEIGHT - 2 * vertical_margin

        list_params = ListLayoutParams(
            x=SCREEN_WIDTH / 2.0 - (width / 2.0),
            y=vertical_margin,
            width=width,
            height=height,
            inter_item_spacing=25
        )
        self.layout = VerticalListLayout(list_params)

        button_names = ["New Game", "Continue", "Load Game", "Settings", "Quit"]
        button_params = ButtonParams()

        self.buttons = []

        for name in button_names:
            button_params.text = name
            button = Button(button_params, batch=batch)
            self.buttons.append(button)
            self.layout.add(button)
            window.push_handlers(button)

    def update(self, dt: float):
        self.layout.update(dt)
        for button in self.buttons:
            button.update(dt)

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption="example")
batch = pyglet.graphics.Batch()
screen = SimpleMenuScreen(batch=batch)


@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    batch.draw()



def update(dt: float):
    screen.update(dt)



if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0 / 60.0)
    pyglet.app.run()