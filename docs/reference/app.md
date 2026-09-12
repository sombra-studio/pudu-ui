# App & Window Reference

The `App` class is the central entry point for running a `pudu-ui` application, extending Pyglet's `Window`.

---

## Class: `App`

::: pudu_ui.app.App
    options:
      show_root_heading: false
      show_source: false

### Constructor Parameters

```python
App(
    width: int | None = None,
    height: int | None = None,
    caption: str = "Pudu UI",
    resizable: bool = False,
    fullscreen: bool = False,
    visible: bool = True,
    update_rate: float = 1.0 / 60.0,
    background_color: Color = BLACK,
    vsync: bool = True,
    is_debug: bool = False
)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `width` | `int \| None` | `None` | Window width in pixels |
| `height` | `int \| None` | `None` | Window height in pixels |
| `caption` | `str` | `"Pudu UI"` | Window title bar text |
| `resizable` | `bool` | `False` | Allows the user to manually resize the window |
| `fullscreen` | `bool` | `False` | Launches window in fullscreen mode |
| `visible` | `bool` | `True` | Controls whether the window is visible on launch |
| `update_rate` | `float` | `1.0 / 60.0` | Target frame interval for the `update(dt)` loop |
| `background_color` | `Color` | `BLACK` | Background color fill |
| `vsync` | `bool` | `True` | Sync buffer swap with monitor refresh rate |
| `is_debug` | `bool` | `False` | Enables performance overlay (FPS, RAM, triangles) and disables vsync |

---

### Methods

- **`set_screen(screen: Screen)`**: Sets the currently active screen to be rendered and updated.
- **`run()`**: Starts the Pyglet application loop at `self.update_rate`.
- **`update(dt: float)`**: Called every tick to update the active screen and performance stats.
- **`on_draw()`**: Clears the framebuffer with `background_color` and draws the current screen batch.
