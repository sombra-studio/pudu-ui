from pudu_ui import ButtonParams, Button, LabelParams, Label
from pudu_ui import styles
import pudu_ui
import pyglet


from constants import WINDOW_WIDTH, WINDOW_HEIGHT


class FirstScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch
    ):
        super().__init__(name="S1", batch=batch)

        front_group = pyglet.graphics.Group(1)
        back_group = pyglet.graphics.Group()

        font_style: styles.fonts.FontStyle = styles.fonts.p1()
        font_style.color = styles.colors.WHITE
        label_params = LabelParams(
            x=(WINDOW_WIDTH // 2), y=(WINDOW_HEIGHT // 4),
            text="First Screen",
            style=font_style
        )
        self.label = Label(label_params, batch=batch, group=front_group)

        button_params = ButtonParams(
            x=100, y=(3 * WINDOW_HEIGHT) // 4, text="Continue"
        )
        self.button = Button(
            button_params, batch, front_group, back_group
        )
