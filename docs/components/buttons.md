# Buttons

Buttons provide interactive triggers for actions in your UI. `pudu-ui` offers standard text `Button` and textured `ImageButton` with distinct visual states.

---

## Basic Text Button

```python
from pudu_ui import Button, ButtonParams

def handle_click():
    print("Button clicked!")

params = ButtonParams(
    x=100,
    y=200,
    width=140,
    height=45,
    text="Click Me",
    on_press=handle_click
)
button = Button(params, batch=app.batch)
```

---

## Button States & Styling

A button transitions through four visual states:
1. **Normal (`style`)**: Default appearance when idle.
2. **Hover (`hover_style`)**: Cursor is hovered over the button.
3. **Focus (`focus_style`)**: Button has received keyboard focus (via Tab navigation).
4. **Press (`press_style`)**: Mouse button is pressed down on the widget.

Each state uses a `ButtonStyle` object defining the background color, border color, border radius, and font style:

```python
from pudu_ui.styles.buttons import ButtonStyle
import pudu_ui

params = ButtonParams(
    x=100,
    y=100,
    text="Custom Style",
    on_press=handle_click
)

# Customize normal style
params.style.background_color = pudu_ui.colors.BLUE
params.style.border_radius = 8.0

# Customize hover style
params.hover_style.background_color = pudu_ui.colors.LIGHT_BLUE

# Helper method to set corner radii across all states
params.set_uniform_radius(8.0)

button = Button(params, batch=app.batch)
```

---

## ImageButton

`ImageButton` displays an image or icon on the button surface:

```python
import pyglet
from pudu_ui import ImageButton, ImageButtonParams
from pudu_ui.image import ImageParams

# Load icon texture
icon_texture = pyglet.resource.image("resources/icons/play.png").get_texture()

img_params = ImageParams(
    x=10,
    y=10,
    width=32,
    height=32,
    texture=icon_texture
)

btn_params = ImageButtonParams(
    x=50,
    y=50,
    width=60,
    height=60,
    image_params=img_params,
    on_press=lambda: print("Play clicked")
)

image_button = ImageButton(btn_params, batch=app.batch)
```
