# Params and Styles

One common problem in UI frameworks is constructor pollution: initializing a single widget can require dozens of arguments (positions, sizes, margins, borders, fonts, colors, callbacks).

`pudu-ui` solves this by decoupling widget data into two types of dataclasses:
1. **Params**: Geometry, alignment, and functional configuration.
2. **Styles**: Aesthetic properties such as colors, borders, and typography.

---

## The `Params` Pattern

Every widget takes a corresponding `Params` object in its constructor. All widget-specific parameter classes inherit from the base `Params` dataclass.

### Base `Params`
Defined in `pudu_ui.widget`:

```python
from dataclasses import dataclass, field
from pudu_ui.colors import Color

@dataclass
class Params:
    x: float = 0.0
    y: float = 0.0
    width: int = 100
    height: int = 100
    focusable: bool = True
    visible: bool = True
    debug_label_color: Color = field(default_factory=default_debug_label_color)
```

### Extending `Params` for Specific Widgets
For example, `LabelParams` adds properties relevant to text rendering:

```python
from dataclasses import dataclass, field
from typing import Literal
from pudu_ui import Params
from pudu_ui.styles.fonts import FontStyle
import pudu_ui

@dataclass
class LabelParams(Params):
    text: str = ""
    anchor_x: Literal['left', 'center', 'right'] = 'left'
    anchor_y: Literal['top', 'bottom', 'center', 'baseline'] = 'baseline'
    multiline: bool = False
    resize_type: LabelResizeType = LabelResizeType.NONE
    rotation: float = 0.0
    style: FontStyle = field(default_factory=pudu_ui.styles.fonts.p1)
```

### Benefits of Params
- **Preset Configurations**: You can define reusable configuration presets and pass them to multiple widgets.
- **Clean Constructors**: Instantiating a widget is simply `Button(params, batch=batch)`.
- **Cloning & Mutation**: Dataclasses can be easily shallow-copied or modified before passing to a widget.

---

## The `Style` Pattern

Styles govern the visual appearance of components. Rather than setting individual hex colors on a widget, you configure or reuse dedicated style classes.

### Typography: `FontStyle`
Defined in `pudu_ui.styles.fonts`:

```python
from dataclasses import dataclass, field
from typing import Union
from pudu_ui.colors import Color

@dataclass
class FontStyle:
    font_size: Union[float, int, str] = 16
    font_name: str = "Arial"
    weight: str = 'normal'
    italic: bool = False
    color: Color = field(default_factory=lambda: Color(255, 255, 255))
    opacity: int = 255
```

Pre-configured font presets are available under `pudu_ui.styles.fonts`:
- `fonts.h1()`, `fonts.h2()`, `fonts.h3()`: Heading styles.
- `fonts.p1()`, `fonts.p2()`, `fonts.p3()`: Body text styles of varying scales.

```python
import pudu_ui

# Create and customize a font style
title_style = pudu_ui.styles.fonts.h1()
title_style.color = pudu_ui.colors.ORANGE
title_style.italic = True
```

---

## Working with `Color`

Colors in `pudu-ui` are represented with `pudu_ui.Color`:

```python
from pudu_ui.colors import Color, WHITE, BLACK, RED, GREEN, BLUE

# Create custom RGB or RGBA colors (values 0-255)
brand_primary = Color(41, 128, 185)
semi_transparent = Color(0, 0, 0, 128)

# Convert to normalized float tuples (0.0 - 1.0) for OpenGL shaders
vec4 = brand_primary.as_vec4() # (r, g, b, a)
```
