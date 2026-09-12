# Controls & Inputs

This page covers interactive input controls: `Slider`, `Toggle`, `ProgressBar`, and `Dropdown`.

---

## Slider

The `Slider` widget allows users to select a numeric value within a range by dragging a thumb or clicking the track.

```python
from pudu_ui import Slider, SliderParams

def on_volume_change(value: float):
    print(f"Volume adjusted to: {value:.1f}")

params = SliderParams(
    x=100,
    y=250,
    width=240,
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    on_value_changed=on_volume_change
)
slider = Slider(params, batch=app.batch)
```

### SliderParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min_value` | `float` | `0.0` | Minimum selectable bound |
| `max_value` | `float` | `100.0` | Maximum selectable bound |
| `value` | `float` | `75.0` | Initial starting value |
| `bar_height` | `int` | `12` | Height of the slider track bar |
| `on_value_changed` | `Callable[[float], None]` | `lambda *args: None` | Callback triggered on value updates |

---

## Toggle

The `Toggle` widget represents a binary on/off switch with smooth animated state transitions.

```python
from pudu_ui import Toggle, ToggleParams

def on_toggle_change(widget, is_on: bool):
    print(f"Feature enabled: {is_on}")

params = ToggleParams(
    x=100,
    y=180,
    is_on=True
)
toggle = Toggle(params, batch=app.batch)
```

### ToggleParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `is_on` | `bool` | `True` | Initial switch state |
| `on_style` | `ToggleStyle` | Default ON style | Colors and radii when active |
| `off_style` | `ToggleStyle` | Default OFF style | Colors and radii when inactive |

---

## ProgressBar

The `ProgressBar` visually represents completion percentage or metrics like health, energy, or loading.

```python
from pudu_ui import ProgressBar, ProgressBarParams

params = ProgressBarParams(
    x=100,
    y=120,
    width=300,
    height=24,
    min_value=0.0,
    max_value=100.0,
    value=65.0
)
progress = ProgressBar(params, batch=app.batch)

# Update dynamically
progress.value = 85.0
progress.invalidate()
```

---

## Dropdown

The `Dropdown` displays a collapsed trigger button that expands into a selectable menu list when clicked.

```python
from pudu_ui import Dropdown, DropdownParams

def on_resolution_selected(selected_item: str):
    print(f"Selected resolution: {selected_item}")

params = DropdownParams(
    x=100,
    y=50,
    width=180,
    options=["1280x720", "1920x1080", "2560x1440", "3840x2160"],
    on_select=on_resolution_selected
)
dropdown = Dropdown(params, batch=app.batch)
```
