# Batches and Groups

`pudu-ui` leverages Pyglet's graphics architecture—specifically **Batches** and **Groups**—to maximize GPU efficiency and manage rendering order.

---

## Pyglet Batches

In traditional naive rendering, each individual element issues its own draw call to OpenGL. With dozens or hundreds of UI elements, this causes severe CPU-to-GPU overhead.

A **`Batch`** pools geometry into shared vertex lists:
- All widgets attached to the same `batch` are consolidated and drawn together in a minimal number of GPU draw calls.
- When you pass `batch=app.batch` or `batch=screen.batch`, the widget registers its vertex arrays into that batch.

```python
# Create a dedicated batch for your screen or overlay
from pyglet.graphics import Batch

hud_batch = Batch()
label = Label(params, batch=hud_batch)
```

---

## Pyglet Groups and Z-Ordering

While a `Batch` combines draw calls, **`Group`** controls OpenGL state and drawing order (Z-index):

- Within a `Batch`, objects belonging to higher-ordered groups are drawn on top of objects in lower-ordered groups.
- `pudu-ui` uses groups to ensure dropdown menus, modal popups, and debug overlays render above background frames and buttons.

```python
from pyglet.graphics import Group

background_group = Group(order=0)
foreground_group = Group(order=1)
modal_group = Group(order=10)

# Pass group to widgets
background_frame = Frame(frame_params, batch=app.batch, group=background_group)
dialog_box = PopUp(popup_params, batch=app.batch, group=modal_group)
```

---

## Widget Hierarchy and Relative Positioning

Widgets support parent-child relationships via the `parent` parameter:

```python
# Outer container frame
parent_frame = Frame(frame_params, batch=app.batch)

# Child label positioned relative to parent_frame
child_params = LabelParams(x=10, y=10, text="Inside Frame")
child_label = Label(child_params, batch=app.batch, parent=parent_frame)
```

- When `parent` is provided, the child widget calculates its screen coordinates offset by its parent (`self.x + self.parent.x`, `self.y + self.parent.y`).
- Moving the parent automatically shifts the visual position of all children when recalculated.
