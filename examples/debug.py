import pudu_ui
import pyglet


window = pyglet.window.Window()
window.projection = pyglet.math.Mat4.orthogonal_projection(
    0, window.width, 0, window.height, 0.1, 100
)
batch = pyglet.graphics.Batch()
# quad = pudu_ui.primitives.quad.RoundedSolidColorQuad(
quad = pudu_ui.primitives.quad.RoundedQuad(
    x=50, y=100,
    width=300,
    height=120,
    batch=batch
)


@window.event
def on_draw():
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
