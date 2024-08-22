from pudu_ui.controller import Controller


from ..screens.first_screen import FirstScreen
from ..screens.second_screen import SecondScreen


class TwoScreensController(Controller):
    def __init__(self, batch, group):
        super().__init__(name="two screens controller")
        self.batch = batch
        self.group = group
        self.current_screen = FirstScreen(batch=self.batch, group=self.group)
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.go

    def go(self):
        # continue to the next screen
        self.current_screen = SecondScreen(batch=self.batch, group=self.group)
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.back

    def back(self):
        # go back to first screen
        self.current_screen = FirstScreen(batch=self.batch, group=self.group)
        # Map screen buttons to controller actions
        self.current_screen.button.on_press = self.go
