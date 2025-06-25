from pudu_ui import App
from pudu_ui.controller import Controller


from examples.two_screens.screens.first_screen import FirstScreen
from examples.two_screens.screens.second_screen import SecondScreen


class TwoScreensController(Controller):
    def __init__(self, app: App):
        super().__init__(app=app, name="two screens controller")
        first_screen = FirstScreen()
        self.app.set_screen(first_screen)
        self.app.push_handlers(first_screen.button)
        # Map screen buttons to controller actions
        self.app.current_screen.button.on_press = self.go

    def go(self, _):
        # continue to the next screen
        self.app.pop_handlers()
        second_screen = SecondScreen()
        self.app.set_screen(second_screen)
        self.app.push_handlers(second_screen.button)
        # Map screen buttons to controller actions
        self.app.current_screen.button.on_press = self.back
        print("going")

    def back(self, _):
        # go back to first screen
        self.app.pop_handlers()
        first_screen = FirstScreen()
        self.app.set_screen(first_screen)
        self.app.push_handlers(first_screen.button)
        # Map screen buttons to controller actions
        self.app.current_screen.button.on_press = self.go
        print("backing")
