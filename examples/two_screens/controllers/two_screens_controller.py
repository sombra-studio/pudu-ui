from pudu_ui.controller import Controller


from screens.first_screen import FirstScreen
from screens.second_screen import SecondScreen


class TwoScreensController(Controller):
    def __init__(self, batch):
        super().__init__(name="two screens controller")
        self.batch = batch
        self.current_screen = FirstScreen(batch=self.batch)
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.go

    def go(self):
        # continue to the next screen
        self.current_screen = SecondScreen(batch=self.batch)
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.back
        print("going")
        # self.batch.invalidate()

    def back(self):
        # go back to first screen
        self.current_screen = FirstScreen(batch=self.batch)
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.go
        print("backing")
        # self.batch.invalidate()

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
