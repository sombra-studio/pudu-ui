# Widgets & Base Classes Reference

Core primitives and base classes from which all UI elements in `pudu-ui` are derived.

---

## Class: `Params`

::: pudu_ui.widget.Params
    options:
      show_root_heading: false
      show_source: false

The base dataclass for widget configuration.

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `x` | `float` | `0.0` | Base X coordinate |
| `y` | `float` | `0.0` | Base Y coordinate |
| `width` | `int` | `100` | Bounding box width |
| `height` | `int` | `100` | Bounding box height |
| `focusable` | `bool` | `True` | Whether widget can receive focus |
| `visible` | `bool` | `True` | Initial visibility |
| `debug_label_color`| `Color` | `DEBUG_TEXT_COLOR` | Color for debug wireframe label |

---

## Class: `Widget`

::: pudu_ui.widget.Widget
    options:
      show_root_heading: false
      show_source: false

The abstract base class for all UI components.

### Core Properties & Methods

- **`visible: bool`**: Gets or sets whether the widget and its group are currently drawn and responsive to inputs.
- **`get_position() -> tuple[float, float]`**: Returns absolute screen coordinates `(x, y)` accounting for parent hierarchy offsets and active animations.
- **`lerp_from_position(x: float, y: float, secs: float)`**: Smoothly interpolates the widget from an origin coordinate to its current position over a duration in seconds.
- **`contains(x: float, y: float) -> bool`**: Returns `True` if the screen coordinate lies within the bounding box of the widget.
- **`invalidate()`**: Flags the widget for recomputation and vertex rebuild.
- **`recompute()`**: Recalculates offsets, child positions, and updates debug geometry.
- **`update(dt: float)`**: Updates active animations and propagates ticks to children.

---

## Class: `CollectionWidget`

::: pudu_ui.collection_widget.CollectionWidget
    options:
      show_root_heading: false
      show_source: false

Base class for container and layout widgets managing collections of child items (`GridLayout`, `ListLayout`).

- **`add_child(widget: Widget)`**: Appends a widget to `self.children` and assigns its index.
- **`remove_child(widget: Widget)`**: Removes a widget and re-indexes remaining children.
- **`recompute()`**: Refreshes child layouts and positions according to container rules.
