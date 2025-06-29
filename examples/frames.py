from pyglet.gl import GL_BLEND, glEnable

import pudu_ui
import pyglet


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

params = pudu_ui.FrameParams(
    x=50, y=100,
    width=300,
    height=120
)
frames = [pudu_ui.Frame(params, batch=batch)]

params.x += 400
params.style.end_color = pudu_ui.colors.DARK_PURPLE
frames.append(pudu_ui.Frame(params, batch=batch))

params.y += 200
params.style.radius_top_left = 24
params.style.radius_bottom_left = 24
params.style.start_color = pudu_ui.colors.MEDIUM_BLUE
params.style.end_color = pudu_ui.colors.MEDIUM_BLUE
frames.append(pudu_ui.Frame(params, batch=batch))

params.x -= 400
params.style.radius_top_right = 24
params.style.radius_bottom_right = 24
params.style.gradient_direction = pudu_ui.colors.GradientDirection.HORIZONTAL
params.style.start_color = pudu_ui.colors.LIGHT_BLUE_GREEN
params.style.end_color = pudu_ui.colors.MEDIUM_BLUE
frames.append(pudu_ui.Frame(params, batch=batch))


@window.event
def on_draw():
    glEnable(GL_BLEND)
    pyglet.gl.glClearColor(0.3, 0.3, 0.3, 1.0)
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
