from pudu_ui import App
from pudu_ui.image import ImageParams, Image, ImageScaleType
from pudu_ui.layouts import ListLayout, ListLayoutParams
import pudu_ui
import pyglet


ITEM_WIDTH = 250
ITEM_HEIGHT = 250
INTER_ITEM_SPACING = 50
LAYOUTS_VERTICAL_SPACING = 80 + ITEM_HEIGHT


app = App(height=1000, background_color=pudu_ui.colors.WHITE)


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
    new_img = Image(img_params, batch=app.batch)
    # new_img.set_debug_mode()
    imgs[-1].append(new_img)

list_params = ListLayoutParams(
    x=80, y=50,
    width=3 * ITEM_WIDTH + 2 * INTER_ITEM_SPACING, height=ITEM_HEIGHT,
    item_width=ITEM_WIDTH, item_height=ITEM_HEIGHT,
    inter_item_spacing=INTER_ITEM_SPACING
)

new_list_layout = ListLayout(list_params, batch=app.batch)
new_list_layout.set_debug_mode()
list_layouts.append(new_list_layout)
for img in imgs[-1]:
    list_layouts[-1].add(img)

# Use images with FILL
imgs.append([])
img_params = ImageParams(scale_type=ImageScaleType.FILL)
for img in img_textures:
    img_params.texture = img
    new_img = Image(img_params, batch=app.batch)
    # new_img.set_debug_mode()
    imgs[-1].append(new_img)

list_params.y += LAYOUTS_VERTICAL_SPACING
new_list_layout = ListLayout(list_params, batch=app.batch)
list_layouts.append(new_list_layout)
for img in imgs[-1]:
    list_layouts[-1].add(img)


# Use images with CROP
imgs.append([])
img_params = ImageParams(scale_type=ImageScaleType.CROP)
for img in img_textures:
    img_params.texture = img
    new_img = Image(img_params, batch=app.batch)
    # new_img.set_debug_mode()
    imgs[-1].append(new_img)

list_params.y += LAYOUTS_VERTICAL_SPACING
new_list_layout = ListLayout(list_params, batch=app.batch)
list_layouts.append(new_list_layout)
for img in imgs[-1]:
    list_layouts[-1].add(img)


for list_layout in list_layouts:
    app.current_screen.widgets.append(list_layout)


def on_key_press(symbol, _):
    if symbol == pyglet.window.key.S:
        pyglet.image.get_buffer_manager().get_color_buffer().save(
            'screenshot.png'
        )


app.push_handlers(on_key_press)


if __name__ == '__main__':
    app.run()
