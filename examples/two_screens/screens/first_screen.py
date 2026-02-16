from pudu_ui import ButtonParams, Button, LabelParams, Label
import pudu_ui


from examples.two_screens.constants import WINDOW_WIDTH, WINDOW_HEIGHT


class FirstScreen(pudu_ui.Screen):
    def __init__(self):
        super().__init__(name="S1")

        font_style: pudu_ui.styles.fonts.FontStyle = pudu_ui.styles.fonts.p1()
        font_style.color = pudu_ui.colors.WHITE
        label_params = LabelParams(
            x=(WINDOW_WIDTH // 2), y=(WINDOW_HEIGHT // 4),
            text="First Screen",
            style=font_style
        )
        self.label = Label(label_params, batch=self.batch)

        button_params = ButtonParams(
            x=100, y=(3 * WINDOW_HEIGHT) // 4, text="Continue"
        )
        self.button = Button(button_params, batch=self.batch)

        self.widgets.append(self.button)
