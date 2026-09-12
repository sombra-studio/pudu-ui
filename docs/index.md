# pudu-ui

A lightweight, modern UI library and framework for building games and desktop applications in Python, powered by [pyglet](https://pyglet.org/).

---

## Highlights

- **Retained Mode & Imperative**: Object-oriented widget model that manages internal state and renders performantly.
- **GLSL Shaders**: Components use GLSL shaders for high-performance rendering and pixel-level control.
- **Platform Agnostic**: Does not rely on native OS controls, ensuring your UI looks and behaves consistently across Windows, macOS, and Linux.
- **Built-in MVC Architecture**: Includes `Controller`, `Screen`, and `Navigation` classes to cleanly separate business logic from UI layouts.
- **Dataclass-Driven Configuration**: Clean `Params` and `Style` dataclasses eliminate constructor bloat and make UI components reusable and themeable.
- **Developer & Performance Tools**: Built-in `Stats` widget monitors real-time FPS, RAM usage (via `psutil`), and triangle counts.

---

## Live Example: 10 de 10

**pudu-ui** powers [10 de 10](https://github.com/sombra-studio/10-de-10), an open-source puzzle game made at Sombra Studio:

![10 de 10 Game](imgs/10-de-10.png)

---

## Quick Example

```python
from pudu_ui import App, Label, LabelParams
import pudu_ui

# Create application window
app = App(caption="My First App", background_color=pudu_ui.colors.WHITE)

if __name__ == "__main__":
    # Create a styled label
    params = LabelParams(x=100, y=200, text="Hello, pudu-ui!")
    label = Label(params, batch=app.batch)

    # Start the event loop
    app.run()
```

---

## Component Gallery

| Component | Description |
| :--- | :--- |
| **[Button](components/buttons.md)** | Interactive text and image push buttons with hover, pressed, and disabled states |
| **[Label](components/labels.md)** | Text display with rich font styling, anchoring, and alignment |
| **[Frame](components/frames.md)** | Container widget for grouping and nesting child elements with border and background styling |
| **[GridLayout](components/layouts.md)** | Multi-column, multi-row grid layout for orderly widget placement |
| **[ListLayout](components/layouts.md)** | Vertical or horizontal linear container layout |
| **[Slider](components/controls.md)** | Continuous or stepped slider control with callbacks |
| **[Toggle](components/controls.md)** | Binary switch toggle with on/off states |
| **[ProgressBar](components/controls.md)** | Visual progress and status indicator bar |
| **[Dropdown](components/controls.md)** | Selection dropdown menu with trigger button |
| **[PopUp](components/popups.md)** | Modal dialog overlay with title, message, and action buttons |
| **[Image](components/images.md)** | Shader-rendered image element with texture mapping |

---

## Next Steps

- Check out the **[Installation Guide](getting-started/installation.md)** to add `pudu-ui` to your environment.
- Follow the step-by-step **[Quickstart](getting-started/quickstart.md)** tutorial.
- Explore **[Core Concepts](core-concepts/architecture.md)** to learn about the MVC framework, Params, and pyglet batches.
