import pyglet
from pyglet.gl import glClearColor

from pudu_ui.image import ImageParams, Image, ImageScaleType
from pudu_ui.layouts import HorizontalListLayout, ListLayoutParams

ITEM_WIDTH = 250
ITEM_HEIGHT = 250
INTER_ITEM_SPACING = 50
LAYOUTS_VERTICAL_SPACING = 80 + ITEM_HEIGHT

window = pyglet.window.Window(height=1000)
batch = pyglet.graphics.Batch()
glClearColor(1.0, 1.0, 1.0, 1.0)

# Define Pudu Widgets
img_paths = [
    "examples/resources/mummy3.jpg",
    "examples/resources/nationaltreasure.jpg",
    "examples/resources/Pirates-of-the-Caribbean-Chest-Fight.png"
]
img_textures = []
for img_path in img_paths:
    img = pyglet.image.load(img_path).get_texture()
    img_textures.append(img)

imgs = []
list_layouts = []

# Use images with FIT
imgs.append([])
img_params = ImageParams(scale_type=ImageScaleType.FIT)
for img in img_textures:
    img_params.texture = img
    new_img = Image(img_params, batch=batch)
    imgs[-1].append(new_img)

list_params = ListLayoutParams(
    x=80, y=50,
    width=3 * ITEM_WIDTH, height=ITEM_HEIGHT,
    item_width=ITEM_WIDTH, item_height=ITEM_HEIGHT,
    inter_item_spacing=INTER_ITEM_SPACING
)

new_list_layout = HorizontalListLayout(list_params)
list_layouts.append(new_list_layout)
for img in imgs[-1]:
    list_layouts[-1].add(img)

# Use images with FILL
imgs.append([])
img_params = ImageParams(scale_type=ImageScaleType.FILL)
for img in img_textures:
    img_params.texture = img
    new_img = Image(img_params, batch=batch)
    imgs[-1].append(new_img)

list_params.y += LAYOUTS_VERTICAL_SPACING
new_list_layout = HorizontalListLayout(list_params)
list_layouts.append(new_list_layout)
for img in imgs[-1]:
    list_layouts[-1].add(img)


# Use images with CROP
imgs.append([])
img_params = ImageParams(scale_type=ImageScaleType.CROP)
for img in img_textures:
    img_params.texture = img
    new_img = Image(img_params, batch=batch)
    imgs[-1].append(new_img)

list_params.y += LAYOUTS_VERTICAL_SPACING
new_list_layout = HorizontalListLayout(list_params)
list_layouts.append(new_list_layout)
for img in imgs[-1]:
    list_layouts[-1].add(img)

def update(dt: float):
    for list_layout in list_layouts:
        list_layout.update(dt)
    for img_list in imgs:
        for img_widget in img_list:
            img_widget.update(dt)


@window.event
def on_draw():
    window.clear()
    batch.draw()


def main():
    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()


if __name__ == '__main__':
    main()
