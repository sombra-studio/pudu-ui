import pyglet


import pudu_ui
from pudu_ui import Label, LabelParams


class HelloScreen(pudu_ui.Screen):
    def __init__(self):
        params = LabelParams(x=50, y=100, )
        self.label = Label(params)

window = pyglet.window.Window(640, 480, "Test")
screen = pudu_ui.Screen



@window.event
def on_draw():
    window.clear()


if __name__ == '__main__':
    pyglet.app.run()
