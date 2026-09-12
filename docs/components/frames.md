# Frame

The `Frame` widget acts as a visual panel or container. It is rendered using a GPU shader quad supporting gradients, borders, and independent corner border radii.

---

## Basic Usage

```python
from pudu_ui import Frame, FrameParams
import pudu_ui

params = FrameParams(
    x=50,
    y=50,
    width=400,
    height=300
)
frame = Frame(params, batch=app.batch)
```

---

## Styling Frames

`FrameStyle` (in `pudu_ui.styles.frames`) provides comprehensive styling properties:

```python
from pudu_ui.styles.frames import FrameStyle
import pudu_ui

style = FrameStyle(
    start_color=pudu_ui.colors.DARK_GRAY,
    end_color=pudu_ui.colors.BLACK,        # Set different end_color for vertical gradient
    border_width=2.0,
    border_color=pudu_ui.colors.WHITE,
    radius_top_left=12.0,
    radius_top_right=12.0,
    radius_bottom_left=0.0,
    radius_bottom_right=0.0,
    opacity=240
)

params = FrameParams(
    x=100,
    y=100,
    width=350,
    height=200,
    style=style
)
card_frame = Frame(params, batch=app.batch)
```

---

## Nesting Child Widgets

Frames are commonly used as container backdrops for other widgets. By passing `parent=card_frame`, child widgets are positioned relative to the frame:

```python
from pudu_ui import Label, LabelParams, Button, ButtonParams

# Title label inside card_frame
title_params = LabelParams(x=20, y=150, text="Card Title")
title = Label(title_params, batch=app.batch, parent=card_frame)

# Button inside card_frame
btn_params = ButtonParams(x=20, y=30, width=100, height=35, text="Submit")
button = Button(btn_params, batch=app.batch, parent=card_frame)
```
