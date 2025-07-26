from pudu_ui import App, Button, ButtonParams, Label, LabelParams
import pudu_ui


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
DATA_UPDATE = 0


class ButtonsScreen(pudu_ui.Screen):
    def __init__(self):
        super().__init__("buttons")
        button_params = ButtonParams(text="+")
        button_params.x = SCREEN_WIDTH / 4 - button_params.width / 2
        button_params.y = SCREEN_HEIGHT / 2 - button_params.height / 2
        self.add_button = Button(button_params, batch=self.batch)

        y = button_params.y + button_params.height / 2.0
        label_params = LabelParams(
            x=SCREEN_WIDTH / 2, y=y,
            anchor_x='center', anchor_y='center'
        )
        label_params.style.color = pudu_ui.colors.GRAY
        self.label = Label(label_params, batch=self.batch)

        button_params.x = SCREEN_WIDTH - button_params.x - button_params.width
        button_params.text = "-"
        self.subtract_button = Button(button_params, batch=self.batch)

        # Add widgets
        self.widgets.append(self.add_button)
        self.widgets.append(self.label)
        self.widgets.append(self.subtract_button)

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
    def __init__(self, app: pudu_ui.App, name: str):
        super().__init__(app, name)
        self.number: int = 0
        self.screen = self.app.current_screen
        self.screen.label.text = str(self.number)
        self.screen.label.invalidate()
        self.screen.add_button.on_press = self.add
        self.screen.subtract_button.on_press = self.subtract

    def add(self, _):
        self.number += 1
        self.screen.handle_event(DATA_UPDATE, self.number)

    def subtract(self, _):
        self.number -= 1
        self.screen.handle_event(DATA_UPDATE, self.number)


app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
app.current_screen = ButtonsScreen()
controller = NumberController(app, name="example controller")


if __name__ == '__main__':
    app.run()
