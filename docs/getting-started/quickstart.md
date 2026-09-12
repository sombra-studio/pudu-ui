# Quickstart

In this guide, we'll build your first interactive window with `pudu-ui` and explain the core building blocks.

---

## Hello World Example

Create a file named `main.py`:

```python
import pudu_ui
from pudu_ui import App, Label, LabelParams

# 1. Initialize the application window
app = App(
    width=640,
    height=480,
    caption="Pudu UI - Quickstart",
    background_color=pudu_ui.colors.WHITE,
    is_debug=False
)

if __name__ == "__main__":
    # 2. Configure a basic Label
    params = LabelParams(
        x=50,
        y=400,
        text="Hello World from pudu-ui!"
    )
    label = Label(params, batch=app.batch)

    # 3. Create a styled label
    font_style = pudu_ui.styles.fonts.p2()
    font_style.color = pudu_ui.colors.GRAY
    
    styled_params = LabelParams(
        x=50,
        y=350,
        text="A secondary label with custom font style",
        style=font_style
    )
    secondary_label = Label(styled_params, batch=app.batch)

    # 4. Start the application loop
    app.run()
```

Run the application:

```bash
uv run main.py
```

---

## How It Works

### 1. `App`
`App` inherits from `pyglet.window.Window`. It initializes OpenGL rendering contexts, sets up the application icon, handles default window inputs, and manages the main rendering loop.

Key parameters:
- `width` / `height`: Dimensions of the application window.
- `caption`: Window title text.
- `background_color`: Background fill color as a `Color` object (e.g. `pudu_ui.colors.WHITE`, `pudu_ui.colors.BLACK`).
- `is_debug`: When set to `True`, displays real-time FPS, RAM usage, and triangle count in the lower-left corner.
- `resizable`: Whether the window allows manual resizing.
- `fullscreen`: Whether the window opens in fullscreen mode.

### 2. `LabelParams`
Instead of long constructor signatures, `pudu-ui` uses **Params dataclasses** to define widget properties. `LabelParams` specifies the coordinate positions (`x`, `y`), text, alignment anchors, and font styles.

### 3. `app.batch`
Pyglet draws graphics in high-performance **Batches**. Passing `batch=app.batch` attaches the widget to the window's main rendering batch so it is automatically drawn on each frame.

### 4. `app.run()`
Starts the Pyglet event loop. This manages mouse clicks, keyboard input, animations, and calls the `update(dt)` loop at the configured refresh rate (default 60 FPS).
