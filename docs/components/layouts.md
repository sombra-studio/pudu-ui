# Layouts

Layout widgets automate positioning and sizing of child widgets, saving you from manually calculating absolute pixel offsets.

---

## GridLayout

`GridLayout` divides its bounding box into a grid of rows and columns, applying a uniform gap between items.

```python
from pudu_ui.layouts.grid_layout import GridLayout, GridLayoutParams
from pudu_ui import Button, ButtonParams

params = GridLayoutParams(
    x=50,
    y=50,
    width=400,
    height=300,
    rows=3,
    columns=3,
    item_gap=8.0
)
grid = GridLayout(params, batch=app.batch)

# Add widgets to the grid
for i in range(9):
    btn_params = ButtonParams(text=f"Item {i + 1}")
    btn = Button(btn_params, batch=app.batch)
    grid.add_child(btn)

# Recalculate item positions
grid.recompute()
```

### GridLayoutParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `rows` | `int` | `2` | Number of rows in the grid |
| `columns` | `int` | `3` | Number of columns in the grid |
| `item_gap` | `float` | `10.0` | Margin around each cell item |

---

## ListLayout

`ListLayout` organizes child widgets along a single linear axis (horizontal or vertical).

```python
from pudu_ui.layouts.list_layout import ListLayout, ListLayoutParams, ListDirection
from pudu_ui import Button, ButtonParams

params = ListLayoutParams(
    x=50,
    y=100,
    width=200,
    height=300,
    direction=ListDirection.VERTICAL,
    inter_item_spacing=12,
    resizes_item_width=True,
    resizes_item_height=False,
    item_height=40
)
list_layout = ListLayout(params, batch=app.batch)

for label_text in ["Profile", "Settings", "Audio", "Quit"]:
    btn = Button(ButtonParams(text=label_text), batch=app.batch)
    list_layout.add_child(btn)

list_layout.recompute()
```

### ListLayoutParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `direction` | `ListDirection` | `HORIZONTAL` | Axis orientation (`HORIZONTAL` or `VERTICAL`) |
| `inter_item_spacing` | `int` | `0` | Spacing in pixels between adjacent items |
| `item_width` | `int` | `0` | Fixed item width (or `0` to auto-calculate) |
| `item_height` | `int` | `0` | Fixed item height (or `0` to auto-calculate) |
| `reversed` | `bool` | `False` | Reverse insertion order |
| `resizes_item_width` | `bool` | `True` | Whether to stretch child widths |
| `resizes_item_height` | `bool` | `True` | Whether to stretch child heights |
