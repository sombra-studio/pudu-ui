import pudu_ui
import pyglet


class FirstScreen(pudu_ui.Screen):
    def __init__(
        self,
        batch: pyglet.graphics.Batch,
        group: pyglet.graphics.Group
    ):
        super().__init__(
            name="First Screen", width=640, height=480, batch=batch,
            group=group
        )
        button_params = pudu_ui.ButtonParams(
            x=100, y=(3 * self.height) // 4,
            label="Continue",
            on_press=lambda: None
        )
        self.button = pudu_ui.Button(
            params=button_params, batch=batch, group=group
        )


def main():
    # create first screen

    # create second screen

    # add mapping s1 - s2

    # add nav s2 - s1
    pass


if __name__ == '__main__':
    main()
