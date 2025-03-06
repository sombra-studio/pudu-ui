import pudu_ui
import pyglet


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

params = pudu_ui.primitives.FrameParams(
    x=50, y=100,
    width=300,
    height=120,
    color_type=pudu_ui.colors.ColorType.GRADIENT
)
frames = [pudu_ui.primitives.Frame(params, batch=batch)]

params.x += 400
params.color_type = pudu_ui.colors.ColorType.SOLID
frames.append(pudu_ui.primitives.Frame(params, batch=batch))

params.y += 200
params.radius_top_left = 24
params.radius_bottom_left = 24
params.background_color = pudu_ui.colors.MEDIUM_BLUE
frames.append(pudu_ui.primitives.Frame(params, batch=batch))

params.x -= 400
params.radius_top_right = 24
params.radius_bottom_right = 24
params.color_type = pudu_ui.colors.ColorType.GRADIENT
params.gradient_direction = pudu_ui.colors.GradientDirection.HORIZONTAL
bg_gradient = pudu_ui.colors.ColorGradient(
    pudu_ui.colors.MEDIUM_BLUE, pudu_ui.colors.LIGHT_BLUE_GREEN
)
params.background_gradient = bg_gradient
frames.append(pudu_ui.primitives.Frame(params, batch=batch))


@window.event
def on_draw():
    pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
