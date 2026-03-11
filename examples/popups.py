from pudu_ui import App, Controller, PopUpParams, PopUp, Screen
from pudu_ui.navigation import Navigator


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


FIRST = "First"
SECOND = "Second"
THIRD = "Third"


class FirstController(Controller):
    def on_load(self, navigator: Navigator):
        self.screen = Screen(FIRST)
        params = PopUpParams(
            title="Pause",
            description="Choose resume to continue playing or go back to "
                        "return to the menu",
            opt1_text="Continue",
            opt2_text="Go back",
            opt1_callback=lambda: self.screen.widgets.pop(),
            opt2_callback=lambda: navigator.change(SECOND)
        )
        params.x = SCREEN_WIDTH // 2 - params.width // 2
        params.y = SCREEN_HEIGHT // 2 - params.height // 2
        popup = PopUp(params=params, batch=self.screen.batch)
        self.screen.widgets.append(popup)
        popup.open()


class SecondController(Controller):
    def on_load(self, navigator: Navigator):
        self.screen = Screen(SECOND)
        params = PopUpParams(
            width=250,
            title="Menu",
            description=(
                "Does this actually wrap? Yes! If the width is set to 200, "
                "this sentence is guaranteed to take up several lines."
                "Now, what about line breaks?\n"
                "Let's test it out:\n"
                "Brrr..\n"
                "wow"
            ),
            opt1_text="Continue",
            opt1_callback=lambda: navigator.change(THIRD),
        )
        params.x = SCREEN_WIDTH // 2 - params.width // 2
        params.y = SCREEN_HEIGHT // 2 - params.height // 2
        popup = PopUp(params=params, batch=self.screen.batch)
        self.screen.widgets.append(popup)
        popup.open()


class ThirdController(Controller):
    def on_load(self, navigator: Navigator):
        self.screen = Screen(THIRD)
        params = PopUpParams(
            height=250,
            description="This is the last one",
            opt1_text="Continue",
            opt1_callback=lambda: self.popup.dismiss(),
        )
        params.x = SCREEN_WIDTH // 2 - params.width // 2
        params.y = SCREEN_HEIGHT // 2 - params.height // 2
        self.popup = PopUp(params=params, batch=self.screen.batch)
        self.screen.widgets.append(self.popup)
        self.popup.open()

if __name__ == '__main__':
    app = App()
