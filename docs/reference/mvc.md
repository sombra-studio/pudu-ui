# MVC & Architecture Reference

Reference for architecture classes that structure your views, controllers, data providers, and screen transitions.

---

## Screen

::: pudu_ui.screen.Screen
    options:
      show_root_heading: false
      show_source: false

Represents a complete visual view. Holds a dedicated `pyglet.graphics.Batch` and a list of registered widgets, routing input events down the widget tree.

---

## Controller

::: pudu_ui.controller.Controller
    options:
      show_root_heading: false
      show_source: false

Coordinates business logic, receives UI callbacks, and populates `Screen` views.

### Lifecycle Methods

- **`on_load(*args, **kwargs)`**: Called when the controller is loaded and becomes active. Initialize your screen and widgets here.
- **`on_pause()`**: Called when the controller loses focus or is suspended.
- **`on_resume()`**: Called when returning to an active state.
- **`on_close()`**: Called before transition to a new controller; cleans up references and prepares for garbage collection.

---

## Navigator

::: pudu_ui.navigation.Navigator
    options:
      show_root_heading: false
      show_source: false

Router for switching between screens and controllers.

- **`add_controller(controller: Controller)`**: Registers a named controller instance.
- **`change(name: str, *args, **kwargs)`**: Closes the current controller and activates the new controller with the provided arguments.
