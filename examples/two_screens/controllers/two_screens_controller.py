from pudu_ui.controller import Controller


from examples.two_screens.screens.first_screen import FirstScreen
from examples.two_screens.screens.second_screen import SecondScreen


class TwoScreensController(Controller):
    def __init__(self):
        super().__init__(name="two screens controller")
        self.current_screen = FirstScreen()
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.go

    def go(self, _):
        # continue to the next screen
        self.current_screen = SecondScreen()
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.back
        print("going")

    def back(self, _):
        # go back to first screen
        self.current_screen = FirstScreen()
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.go
        print("backing")

    # Override function
    def on_mouse_press(self, x, y, buttons, modifiers):
        return self.current_screen.button.on_mouse_press(
            x, y, buttons, modifiers
        )

    # Override function
    def on_mouse_release(self, x, y, buttons, modifiers):
        return self.current_screen.button.on_mouse_release(
            x, y, buttons, modifiers
        )

    # Override function
    def on_mouse_motion(self, x, y, dx, dy):
        return self.current_screen.button.on_mouse_motion(x, y, dx, dy)
