import pyglet
from pyglet.gl import glClearColor

from pudu_ui.image import ImageParams, Image, ImageScaleType
from pudu_ui.layouts import HorizontalListLayout, ListLayoutParams

ITEM_WIDTH = 300
ITEM_HEIGHT = 300

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
glClearColor(1.0, 1.0, 1.0, 1.0)

# Define Pudu Widgets
img_params = ImageParams(
    width=ITEM_WIDTH, height=ITEM_HEIGHT, scale_type=ImageScaleType.FIT
)
img_params.image_path = "resources/mummy3.jpg"
img1 = Image(img_params, batch=batch)

img_params.image_path = "resources/nationaltreasure.jpg"
img2 = Image(img_params, batch=batch)

img_params.image_path = "resources/Pirates-of-the-Caribbean-Chest-Fight.png"
img3 = Image(img_params, batch=batch)

list_params = ListLayoutParams(
    x=100, y=540 / 2 - ITEM_HEIGHT / 2,
    width=3 * ITEM_WIDTH, height=ITEM_HEIGHT
)
list_layout = HorizontalListLayout(list_params)


def update(dt: float):
    list_layout.update(dt)
    img1.update(dt)
    img2.update(dt)
    img3.update(dt)


@window.event
def on_draw():
    window.clear()
    batch.draw()


def main():
    list_layout.add(img1)
    list_layout.add(img2)
    list_layout.add(img3)

    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()


if __name__ == '__main__':
    main()
