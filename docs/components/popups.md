# PopUp

The `PopUp` widget creates a modal dialog overlay on top of all other interface elements. It features a title, description text, and up to two customizable action buttons.

---

## Basic Usage

```python
from pudu_ui import PopUp, PopUpParams

def on_confirm():
    print("User confirmed action")
    popup.close()

def on_cancel():
    print("Action canceled")
    popup.close()

params = PopUpParams(
    x=120,
    y=80,
    width=400,
    height=320,
    title="Confirm Exit",
    description="Are you sure you want to exit without saving?",
    opt1_text="Confirm",
    opt1_callback=on_confirm,
    opt2_text="Cancel",
    opt2_callback=on_cancel,
    visible=False  # Start closed
)
popup = PopUp(params, batch=app.batch)

# Open the dialog when needed
popup.open()
```

---

## PopUpParams Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `str` | `""` | Heading text displayed at the top of the modal |
| `description` | `str` | `""` | Body message or explanation text |
| `opt1_text` | `str` | `""` | Label for the primary action button |
| `opt1_callback` | `Callable` | `None` | Callback executed when the primary button is clicked |
| `opt2_text` | `str` | `""` | Label for the secondary action button |
| `opt2_callback` | `Callable` | `None` | Callback executed when the secondary button is clicked |
| `visible` | `bool` | `False` | Initial visibility state |
| `style` | `PopUpStyle` | Default popup style | Container and typography styles |

---

## Group Layering

The `PopUp` widget internally assigns its graphics elements to a high Pyglet group order (`order=100`), ensuring it always renders in front of other screens, layouts, and controls.
