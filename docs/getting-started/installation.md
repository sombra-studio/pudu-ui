# Installation

## Prerequisites

- **Python**: 3.11 or higher
- **OpenGL**: GPU with OpenGL 3.3+ support (required by pyglet 3.0)

---

## Using `uv` (Recommended)

`uv` is an extremely fast Python package and project manager.

### Add to an Existing Project

```bash
uv add pudu-ui
```

### Clone and Work Locally

If you are developing or contributing to `pudu-ui`:

```bash
git clone https://github.com/sombra-studio/pudu-ui.git
cd pudu-ui
uv sync
```

To run examples with `uv`:

```bash
uv run examples/hello_screen.py
```

---

## Using `pip`

You can also install `pudu-ui` using `pip`:

```bash
pip install pudu-ui
```

### Editable Install for Development

```bash
git clone https://github.com/sombra-studio/pudu-ui.git
cd pudu-ui
pip install -e .
```

To install development and documentation dependencies:

```bash
pip install -e ".[docs]"
```

---

## Verifying the Installation

Verify your setup by running a simple test in Python:

```python
import pudu_ui
from pudu_ui import App

app = App(caption="Pudu UI Test", width=400, height=300)
print(f"pudu-ui loaded successfully! App window: {app.caption}")
```
