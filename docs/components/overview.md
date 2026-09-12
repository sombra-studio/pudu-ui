# Component Overview

`pudu-ui` provides a rich set of retained-mode UI widgets designed for 2D game menus, HUDs, and desktop applications.

---

## Component Index

### Display & Containers
- **[Label](labels.md)**: Text display with rich font styling, anchoring (`anchor_x`, `anchor_y`), multiline text, and rotation.
- **[Frame](frames.md)**: Visual container with border, background shaders, and child widget nesting.
- **[Image](images.md)**: Texture and sprite display with support for custom GLSL shaders.

### Interactive Controls
- **[Button & ImageButton](buttons.md)**: Standard and textured push buttons with hover, pressed, and disabled states.
- **[Slider](controls.md#slider)**: Horizontal draggable value slider with min/max ranges and value-changed callbacks.
- **[Toggle](controls.md#toggle)**: Binary on/off switch with smooth visual transition.
- **[ProgressBar](controls.md#progressbar)**: Linear progress bar indicating completion percentage.
- **[Dropdown](controls.md#dropdown)**: Expandable option selection menu with trigger button.
- **[PopUp](popups.md)**: Modal dialog box with title, message, and customizable action buttons.

### Layouts & Organization
- **[GridLayout](layouts.md#gridlayout)**: Automatically arranges child widgets into rows and columns with configurable cell dimensions and padding.
- **[ListLayout](layouts.md#listlayout)**: Arranges widgets in a single linear column or row with dynamic spacing.

---

## Universal Widget Parameters

All widgets inherit from the base `Params` dataclass and share these common properties:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `x` | `float` | `0.0` | X coordinate in pixels from the left origin |
| `y` | `float` | `0.0` | Y coordinate in pixels from the bottom origin |
| `width` | `int` | `100` | Width of the widget bounding box |
| `height` | `int` | `100` | Height of the widget bounding box |
| `focusable` | `bool` | `True` | Whether the widget can receive keyboard/input focus |
| `visible` | `bool` | `True` | Whether the widget is rendered and receives events |
| `debug_label_color`| `Color` | `(255, 0, 0)` | Debug boundary color for testing |
