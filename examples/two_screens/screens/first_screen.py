from examples.two_screens.two_screens import WINDOW_HEIGHT, WINDOW_WIDTH
from pudu_ui import ButtonParams, Button, LabelParams, Label
import pudu_ui
import pyglet


class FirstScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch,
        group: pyglet.graphics.Group
    ):
        super().__init__(name="S1", batch=batch, group=group)

        label_params = LabelParams(
            x=(WINDOW_WIDTH // 2), y=(WINDOW_HEIGHT // 4), value="First Screen"
        )
        self.label = Label(label_params, batch=batch, group=group)

        button_params = ButtonParams(
            x=100, y=(3 * WINDOW_HEIGHT) // 4, label="Continue"
        )
        self.button = Button(
            params=button_params, batch=batch, group=group
        )