# Image

The `Image` widget renders textures and graphics with precise scaling modes (`FIT`, `FILL`, `CROP`, `WRAP`), color tints, and opacity.

---

## Basic Usage

```python
import pyglet
from pudu_ui import Image, ImageParams
from pudu_ui.image import ImageScaleType

# Load texture via pyglet resource loader
avatar_texture = pyglet.resource.image("resources/avatar.png").get_texture()

params = ImageParams(
    x=50,
    y=100,
    width=128,
    height=128,
    texture=avatar_texture,
    scale_type=ImageScaleType.FIT
)
image_widget = Image(params, batch=app.batch)
```

---

## ImageParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `texture` | `Texture` | Placeholder gray texture | Pyglet texture to draw |
| `scale_type` | `ImageScaleType` | `ImageScaleType.FIT` | Scaling rule inside the widget bounds |
| `color` | `Color` | `WHITE` | Tint color applied to the sprite |
| `opacity` | `int` | `255` | Alpha transparency (0–255) |

---

## Scaling Modes (`ImageScaleType`)

- `ImageScaleType.FIT`: Scales uniformly so the entire image is visible within the bounding box without distortion.
- `ImageScaleType.FILL`: Scales uniformly to completely fill the box; excess area is cropped.
- `ImageScaleType.CROP`: Retains 1:1 pixel scale and clips outside the widget bounding box.
- `ImageScaleType.WRAP`: Sets widget width and height to match the image's original dimensions.
