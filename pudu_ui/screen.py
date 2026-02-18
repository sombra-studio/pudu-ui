from pyglet.event import EVENT_HANDLE_STATE, EVENT_HANDLED, EVENT_UNHANDLED
import pyglet

from pudu_ui import Widget

class Screen:
    def __init__(self, name: str):
        self.name: str = name
        self.batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
        self.widgets: list[Widget] = []

    def update(self, dt):
        for widget in self.widgets:
            widget.update(dt)

    def draw(self):
        self.batch.draw()

    def handle_input_event(self, event_name: str, *args) -> EVENT_HANDLE_STATE:
        for widget in self.widgets:
            # The first widget that handles this event will return
            if hasattr(widget, event_name):
                widget_func = getattr(widget, event_name)
                if widget_func(*args) == EVENT_HANDLED:
                    return EVENT_HANDLED
        return EVENT_UNHANDLED

    def on_mouse_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_press', *args
        )

    def on_mouse_release(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_release', *args
        )

    def on_mouse_motion(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_motion', *args
        )

    def on_mouse_drag(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_mouse_drag', *args
        )

    def on_key_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_key_press', *args
        )

    def on_key_release(self, *args) -> EVENT_HANDLE_STATE:
        return self.handle_input_event(
            'on_key_release', *args
        )
