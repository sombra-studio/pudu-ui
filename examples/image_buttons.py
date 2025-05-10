import pudu_ui
import pyglet


IMG_SIZE = 25
BTN_SIZE = 50
RADIUS = BTN_SIZE / 2.0

window = pyglet.window.Window(caption="Pudu UI")
batch = pyglet.graphics.Batch()

img_paths = [
    "resources/play-solid.png",
    "resources/plus-solid.png",
    "resources/thumbs-up-solid.png",
]
buttons = []


@window.event
def on_draw():
    window.clear()
    batch.draw()


def on_press(caller: pudu_ui.Button):
    if caller.y == 100:
        caller.y = 200
        caller.recompute()
    else:
        caller.y = 100


def update(dt: float):
    for button in buttons:
        button.update(dt)


if __name__ == '__main__':
    params = pudu_ui.ImageButtonParams(
        x=50, y=100, width=BTN_SIZE, height=BTN_SIZE,
        on_press=on_press
    )
    params.style.set_uniform_radius(RADIUS)
    params.hover_style.set_uniform_radius(RADIUS)
    params.focus_style.set_uniform_radius(RADIUS)
    params.press_style.set_uniform_radius(RADIUS)
    params.image_params.width = IMG_SIZE
    params.image_params.height = IMG_SIZE
    # center the image inside the button
    params.image_params.x = params.width / 2.0 - IMG_SIZE / 2.0
    params.image_params.y = params.height / 2.0 - IMG_SIZE / 2.0

    for img_path in img_paths:
        params.image_params.texture = pyglet.resource.image(img_path)
        img_button = pudu_ui.ImageButton(params, batch=batch)
        params.x += 25 + BTN_SIZE
        buttons.append(img_button)

    buttons[0].focus()

    # Add mouse events to buttons
    for btn in buttons:
        window.push_handlers(btn)

    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
