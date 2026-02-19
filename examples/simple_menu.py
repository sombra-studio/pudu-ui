from pudu_ui import App, Button, ButtonParams
from pudu_ui.colors import WHITE
from pudu_ui.layouts import ListDirection, ListLayoutParams, ListLayout
import pudu_ui


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SimpleMenuScreen(pudu_ui.Screen):
    def __init__(self):
        super().__init__("menu")
        vertical_margin = 50
        width = 250
        height = SCREEN_HEIGHT - 2 * vertical_margin

        list_params = ListLayoutParams(
            x=SCREEN_WIDTH / 2.0 - (width / 2.0),
            y=vertical_margin,
            width=width,
            height=height,
            inter_item_spacing=25,
            direction=ListDirection.VERTICAL

        )
        self.layout = ListLayout(list_params, batch=self.batch)

        button_names = ["New Game", "Continue", "Load Game", "Settings", "Quit"]
        button_params = ButtonParams()

        self.buttons = []

        for name in button_names:
            button_params.text = name
            button = Button(button_params, batch=self.batch)
            self.buttons.append(button)
            self.layout.add(button)

        self.widgets.append(self.layout)
        self.layout.focus()



app = App(
    SCREEN_WIDTH, SCREEN_HEIGHT, caption="example"
)
screen = SimpleMenuScreen()
app.current_screen = screen


if __name__ == '__main__':
    app.run()