import pudu_ui
from pudu_ui.button import Button, ButtonParams
from pudu_ui.layouts import ListLayoutParams, VerticalListLayout
import pyglet


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class SimpleMenuScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch = pyglet.graphics.get_default_batch(),
        group: pyglet.graphics.Group = pyglet.graphics.Group()
    ):
        super().__init__(
            "menu",
            batch=batch,
            group=group
        )
        list_params = ListLayoutParams(
            x=300.0,
            y=200.0,
            width=250,
            height=500,
            item_height=80,
            inter_item_spacing=25
        )
        self.layout = VerticalListLayout(list_params)

        button_names = ["New Game", "Continue", "Load Game", "Settings", "Quit"]
        button_params = ButtonParams()

        self.buttons = []

        for name in button_names:
            button_params.label = name
            button = Button(button_params, batch, group)
            self.buttons.append(button)
            self.layout.add(button)

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