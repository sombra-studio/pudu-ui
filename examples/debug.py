import pudu_ui
import pyglet


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
with open("../pudu_ui/shaders/default.vert") as vf:
    with open("../pudu_ui/shaders/frame.frag") as ff:
        vertex_source = vf.read()
        fragment_source = ff.read()
        vs = pyglet.graphics.shader.Shader(vertex_source, 'vertex')
        fs = pyglet.graphics.shader.Shader(fragment_source, 'fragment')
        program = pyglet.graphics.shader.ShaderProgram(vs, fs)

quad = pudu_ui.primitives.Quad(
    x=50, y=100,
    width=300,
    height=120,
    color=pudu_ui.colors.PURPLE,
    program=program,
    batch=batch,
    group=None
)


@window.event
def on_draw():
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
