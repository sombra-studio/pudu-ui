# Label

The `Label` widget renders text using Pyglet's text rendering engine with support for fonts, colors, anchoring, rotation, wrapping, and automatic text scaling.

---

## Basic Usage

```python
from pudu_ui import Label, LabelParams
import pudu_ui

params = LabelParams(
    x=100,
    y=300,
    text="Welcome to pudu-ui"
)
label = Label(params, batch=app.batch)
```

---

## LabelParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `str` | `""` | The string to display |
| `anchor_x` | `Literal['left', 'center', 'right']` | `'left'` | Horizontal anchor point |
| `anchor_y` | `Literal['top', 'bottom', 'center', 'baseline']` | `'baseline'` | Vertical anchor point |
| `multiline` | `bool` | `False` | Whether text wraps over multiple lines |
| `resize_type` | `LabelResizeType` | `NONE` | Scaling behavior (`FIT`, `FILL`, or `NONE`) |
| `rotation` | `float` | `0.0` | Rotation angle in degrees |
| `style` | `FontStyle` | `styles.fonts.p1` | Typography configuration |

---

## Anchors and Alignment

Anchors determine the reference origin for the label coordinates `(x, y)`:

```python
# Centered text horizontally and vertically
centered_params = LabelParams(
    x=320,
    y=240,
    text="Centered Text",
    anchor_x='center',
    anchor_y='center'
)
centered_label = Label(centered_params, batch=app.batch)
```

---

## Dynamic Resizing Modes

Using `LabelResizeType`, a label can automatically adapt its font size to fit within target bounding boxes (`width`, `height`):

```python
from pudu_ui.label import LabelResizeType

# Automatically shrinks font size if text exceeds bounding box
params = LabelParams(
    x=50,
    y=100,
    width=200,
    height=50,
    text="Long text that automatically scales down",
    resize_type=LabelResizeType.FIT
)
label = Label(params, batch=app.batch)
```

- `LabelResizeType.FIT`: Decreases `font_size` until the text fits inside `width` and `height`.
- `LabelResizeType.FILL`: Increases `font_size` to maximally fill the bounding box.
- `LabelResizeType.NONE`: Wraps dimensions to the natural text width and height.

---

## Updating Styles Dynamically

You can swap out typography on the fly using `change_style()`:

```python
new_style = pudu_ui.styles.fonts.h2()
new_style.color = pudu_ui.colors.RED
label.change_style(new_style)
```
