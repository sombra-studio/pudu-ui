from pudu_ui import Screen
import pudu_ui
import pyglet


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        height = 6
        radius = height // 2
        self.progress = pudu_ui.primitives.quad.ProgressQuad(
            x=300, y=200, width=200, height=height,
            radius_top_left=radius, radius_top_right=radius,
            radius_bottom_left=radius, radius_bottom_right=radius,
            batch=self.batch
        )
        self.progress.limit_x = self.progress.x + 2 * self.progress.width / 3
        self.progress.recompute()

    def update(self, dt: float):
        pass


window = pyglet.window.Window(caption="Pudu UI")
screen = DebugScreen()


@window.event
def on_draw():
    window.clear()
    screen.draw()


def update(dt: float):
    screen.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
