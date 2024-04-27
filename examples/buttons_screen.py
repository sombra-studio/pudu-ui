import pudu_ui
from pudu_ui import Button, ButtonParams, Label, LabelParams
import pyglet


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
DATA_UPDATE = 0


class ButtonsScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch = pyglet.graphics.get_default_batch()
    ):
        super().__init__(
            "hello",
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            batch=batch
        )
        label_params = LabelParams(x=SCREEN_WIDTH / 2, y=400)
        self.label = Label(label_params, batch=batch)
        button_params = ButtonParams(x=100, y=200, label="+")
        self.add_button = Button(button_params, batch=batch)
        button_params.x = 400
        button_params.label = "-"
        self.subtract_button = Button(button_params, batch=batch)

        # Register input event handlers
        # self.push_handlers(self.add_button, self.subtract_button)

    def handle_event(self, event_type: int, data: int):
        """
        The view should not do any logic work, and should not have reference
        to the model. So this is how we send changes to the view.

        Args:
            event_type: The type of the event
            data: the new number that will be displayed in the label
        """
        if event_type == DATA_UPDATE:
            self.label.value = str(data)


class NumberController(pudu_ui.controller.Controller):
    def __init__(self, name: str, batch: pyglet.graphics.Batch):
        super().__init__(name)
        self.number: int = 0
        self.screen = ButtonsScreen(batch=batch)
        self.screen.label.value = str(self.number)
        self.screen.add_button.on_press = self.add
        self.screen.subtract_button.on_press = self.subtract

        # self.push_handlers(self.screen)
    def add(self):
        self.number += 1
        self.screen.handle_event(DATA_UPDATE, self.number)

    def subtract(self):
        self.number -= 1
        self.screen.handle_event(DATA_UPDATE, self.number)


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Test")
batch = pyglet.graphics.Batch()
controller = NumberController(name="example controller", batch=batch)
window.push_handlers(
    controller.screen.add_button, controller.screen.subtract_button
)


@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
