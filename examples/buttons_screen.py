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
            batch=batch
        )

        button_params = ButtonParams(x=100, y=200, text="+")
        self.add_button = Button(button_params, batch=batch)

        y = self.add_button.y + self.add_button.height / 2.0
        label_params = LabelParams(
            x=SCREEN_WIDTH / 2, y=y,
            anchor_x='center', anchor_y='center'
        )
        self.label = Label(label_params, batch=batch)

        button_params.x = 400
        button_params.text = "-"
        self.subtract_button = Button(button_params, batch=batch)

    def handle_event(self, event_type: int, data: int):
        """
        The view should not do any logic work, and should not have reference
        to the model. So this is how we send changes to the view.

        Args:
            event_type: The type of the event
            data: the new number that will be displayed in the label
        """
        if event_type == DATA_UPDATE:
            self.label.text = str(data)
            self.label.invalidate()


class NumberController(pudu_ui.controller.Controller):
    def __init__(self, name: str, batch: pyglet.graphics.Batch):
        super().__init__(name)
        self.number: int = 0
        self.screen = ButtonsScreen(batch=batch)
        self.screen.label.text = str(self.number)
        self.screen.label.invalidate()
        self.screen.add_button.on_press = self.add
        self.screen.subtract_button.on_press = self.subtract

    def add(self):
        self.number += 1
        self.screen.handle_event(DATA_UPDATE, self.number)

    def subtract(self):
        self.number -= 1
        self.screen.handle_event(DATA_UPDATE, self.number)


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Test")
batch = pyglet.graphics.Batch()
controller = NumberController(name="example controller", batch=batch)
window.push_handlers(controller.screen.add_button)
window.push_handlers(controller.screen.subtract_button)

@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    batch.draw()


def update(dt):
    # need to call update on label, so that it's value is recomputed after
    # invalidating
    controller.screen.label.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0 / 60.0)
    pyglet.app.run()
