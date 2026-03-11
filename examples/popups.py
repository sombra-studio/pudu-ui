from pudu_ui import App, Controller, PopUpParams, PopUp, Screen
from pudu_ui.navigation import Navigator


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


FIRST = "First"
SECOND = "Second"
THIRD = "Third"


class FirstController(Controller):
    def on_load(self, navigator: Navigator):
        super().on_load()
        self.screen = Screen(FIRST)
        params = PopUpParams(
            title="Pause",
            description="Choose resume to continue playing or go back to "
                        "return to the menu",
            opt1_text="Continue",
            opt2_text="Go back",
            opt1_callback=lambda l: navigator.change(SECOND, navigator),
            opt2_callback=lambda l: print("Going back")
        )
        params.x = SCREEN_WIDTH // 2 - params.width // 2
        params.y = SCREEN_HEIGHT // 2 - params.height // 2
        popup = PopUp(params=params, batch=self.screen.batch)
        self.screen.widgets.append(popup)
        popup.open()
        app.set_screen(self.screen)


class SecondController(Controller):
    def on_load(self, navigator: Navigator):
        super().on_load()
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
            opt1_callback=lambda l: navigator.change(THIRD, navigator),
        )
        params.x = SCREEN_WIDTH // 2 - params.width // 2
        params.y = SCREEN_HEIGHT // 2 - params.height // 2
        popup = PopUp(params=params, batch=self.screen.batch)
        self.screen.widgets.append(popup)
        popup.open()
        app.set_screen(self.screen)


class ThirdController(Controller):
    def on_load(self, navigator: Navigator):
        super().on_load()
        self.screen = Screen(THIRD)
        params = PopUpParams(
            height=250,
            description="This is the last one",
            opt1_text="Continue",
            opt1_callback=self.on_popup_btn_press,
        )
        params.x = SCREEN_WIDTH // 2 - params.width // 2
        params.y = SCREEN_HEIGHT // 2 - params.height // 2

        self.popup = PopUp(params=params, batch=self.screen.batch)
        self.screen.widgets.append(self.popup)
        self.popup.open()
        app.set_screen(self.screen)

    def on_popup_btn_press(self, _):
        self.popup.dismiss()

if __name__ == '__main__':
    app = App()
    nav = Navigator()
    first_controller = FirstController(app, FIRST)
    second_controller = SecondController(app, SECOND)
    third_controller = ThirdController(app, THIRD)
    nav.add_controller(first_controller)
    nav.add_controller(second_controller)
    nav.add_controller(third_controller)
    nav.change(FIRST, nav)
    app.run()
