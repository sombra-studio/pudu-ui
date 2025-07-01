import pudu_ui
import pyglet

from pudu_ui.layouts import ListLayoutParams

IMG_SIZE = 25
BTN_SIZE = 50
RADIUS = BTN_SIZE / 2.0

app = pudu_ui.App()
img_paths = [
    "resources/play-solid.png",
    "resources/plus-solid.png",
    "resources/thumbs-up-solid.png",
]


def on_press(button: pudu_ui.Button):
    print(f"pressed button {button.index}")


if __name__ == '__main__':
    # Create list layout
    list_params = ListLayoutParams(
        x=50.0, y=100.0, width=400, item_width=BTN_SIZE, item_height=BTN_SIZE,
        inter_item_spacing=25
    )
    list_layout = pudu_ui.layouts.HorizontalListLayout(list_params)
    app.current_screen.widgets.append(list_layout)

    # Create button params
    params = pudu_ui.ImageButtonParams(on_press=on_press)
    params.set_uniform_radius(RADIUS)
    params.image_params.width = IMG_SIZE
    params.image_params.height = IMG_SIZE
    # center the image inside the button
    params.image_params.x = BTN_SIZE / 2.0 - IMG_SIZE / 2.0
    params.image_params.y = BTN_SIZE / 2.0 - IMG_SIZE / 2.0

    for img_path in img_paths:
        params.image_params.texture = pyglet.resource.image(img_path)
        img_button = pudu_ui.ImageButton(params, batch=app.batch)
        list_layout.add(img_button)

    list_layout.children[0].focus()

    app.run()
