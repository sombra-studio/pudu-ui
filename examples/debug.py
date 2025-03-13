import pudu_ui
import pyglet


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

params = pudu_ui.ButtonParams(x=50, y=100)
buttons = [pudu_ui.Button(params, batch=batch)]
# params = pudu_ui.primitives.FrameParams(x=50, y=100)
# buttons = [pudu_ui.primitives.Frame(params, batch=batch)]

@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
