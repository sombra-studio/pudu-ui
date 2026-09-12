# Examples Catalog

The repository includes a diverse collection of runnable examples in the `examples/` directory demonstrating each component, complex layouts, and multi-screen workflows.

You can run any example directly from the repository root using `uv run`:

```bash
uv run examples/<example_script>.py
```

---

## Starter Examples

### Hello Screen
- **File**: `examples/hello_screen.py`
- **Command**: `uv run examples/hello_screen.py`
- **Highlights**: Demonstrates creating an `App` window, defining `Label` widgets with different text alignments, custom font styles, and rendering to `app.batch`.

### Simple Menu
- **File**: `examples/simple_menu.py`
- **Command**: `uv run examples/simple_menu.py`
- **Highlights**: Creates an interactive main menu screen using styled buttons with click callbacks.

---

## Interactive Applications

### Calculator
- **File**: `examples/calculator.py`
- **Command**: `uv run examples/calculator.py`
- **Highlights**: A complete, working desktop calculator application demonstrating grid-based layout composition, dynamic label updates, and button event handling.

### Two Screens (MVC & Navigation)
- **Directory**: `examples/two_screens/`
- **Command**: `uv run examples/two_screens/main.py`
- **Highlights**: Shows how to structure multi-screen projects using `Controller`, `Screen`, and `Navigator` to transition between different views.

---

## Component Showcases

| Example | Command | Features Demonstrated |
| :--- | :--- | :--- |
| **Buttons** | `uv run examples/buttons_screen.py` | Normal, hover, focus, and pressed button states |
| **Image Buttons** | `uv run examples/image_buttons.py` | Texture loading, custom icons, and button styling |
| **Sliders** | `uv run examples/sliders.py` | Value changes, thumb positioning, and callbacks |
| **Toggles** | `uv run examples/toggle.py` | Binary switch states and animations |
| **Progress Bars**| `uv run examples/progress_bars.py` | Progress fill styling and status updates |
| **Popups** | `uv run examples/popups.py` | Modal dialogs, action callbacks, and group layering |
| **Frames** | `uv run examples/frames.py` | Rounded corners, borders, and gradient backgrounds |
| **Grid Layout** | `uv run examples/grid_layout.py` | Auto-arranging widgets in rows and columns |
| **Image List** | `uv run examples/image_list.py` | ListLayout combined with Image widgets |
| **Debug Stats** | `uv run examples/debug.py` | Performance monitoring (FPS, RAM usage, triangle count) |
| **Arrows** | `uv run examples/arrows.py` | Primitive arrow drawing and orientation |
