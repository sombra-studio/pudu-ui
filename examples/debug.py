import pudu_ui
import pyglet


IMG_SIZE = 25
BTN_SIZE = 50

window = pyglet.window.Window(caption="Pudu UI")
batch = pyglet.graphics.Batch()

img_paths = [
    "resources/play-solid.png",
    "resources/plus-solid.png",
    "resources/thumbs-up-solid.png",
]

params = pudu_ui.ImageButtonParams(x=50, y=100, width=BTN_SIZE, height=BTN_SIZE)
params.style.set_uniform_radius(params.width / 2.0)
params.hover_style.set_uniform_radius(params.width / 2.0)
params.focus_style.set_uniform_radius(params.width / 2.0)
params.press_style.set_uniform_radius(params.width / 2.0)
params.image_params.width = IMG_SIZE
params.image_params.height = IMG_SIZE
buttons = []

for img_path in img_paths:
    params.image_params.image_path = img_path
    img_button = pudu_ui.ImageButton(params, batch=batch)
    img_button.image.x = img_button.x + img_button.width / 2.0 - IMG_SIZE / 2.0
    img_button.image.y = img_button.y + img_button.height / 2.0 - IMG_SIZE / 2.0
    img_button.invalidate()
    params.x += 25 + BTN_SIZE
    buttons.append(img_button)

# Add mouse events to buttons
for btn in buttons:
    window.push_handlers(btn)


@window.event
def on_draw():
    window.clear()
    batch.draw()


def update(dt: float):
    for button in buttons:
        button.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
