from pudu_ui import Screen
from pudu_ui.layouts import ListLayoutParams, VerticalListLayout
from pudu_ui.primitives import Frame, FrameParams
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__("home")
        list_params = ListLayoutParams(
            x=200.0, y=200.0, width=200, height=400,
            inter_item_spacing=25
        )
        self.list = VerticalListLayout(list_params)
        num_frames = 4
        params = FrameParams()
        for i in range(num_frames):
            new_frame = Frame(params, batch=self.batch)
            self.list.add(new_frame)

    def update(self, dt: float):
        self.list.update(dt)


window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()

@window.event
def on_draw():
    window.clear()
    screen.draw()


def update(dt: float):
    screen.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
