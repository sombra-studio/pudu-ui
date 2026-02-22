from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch, Group
from pyglet.window import key


from pudu_ui import Params, Widget


class CollectionWidget(Widget):
    def __init__(
        self, params: Params, batch: Batch, group: Group, parent: Widget
    ):
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        self.current_item = -1


    def add(self, widget: Widget):
        widget.index = len(self.children)
        widget.parent = self
        self.children.append(widget)
        self.invalidate()

    def insert(self, index: int, widget: Widget):
        count = len(self.children)
        widget.index = index
        widget.parent = self
        self.children.insert(index, widget)
        # Update the rest of children
        for i in range(index + 1, count):
            self.children[i].index = i
        self.invalidate()

    def remove_at(self, index: int):
        count = len(self.children)
        if index >= count:
            raise IndexError(
                f"Index {index} is out of bounds for {self.__class__.__name__}"
                f" with count {count}"
            )
        reminder = self.children[index:]
        new_idx = index
        for elem in reminder:
            elem.index = new_idx
            new_idx += 1
        removed_widget = self.children[index]
        removed_widget.parent = None
        removed_widget.invalidate()
        del self.children[index]

        self.invalidate()

    def recompute(self):
        super().recompute()
        for i, item in enumerate(self.children):
            # Recompute item index in case children have changed order
            item.index = i

    def on_focus(self):
        if self.children:
            self.children[0].focus()
            self.current_item = 0

    def get_current_item(self) -> Widget | None:
        if 0 <= self.current_item < len(self.children):
            return self.children[self.current_item]
        return None

    def move_focus(self, amount: int):
        item = self.get_current_item()
        item.unfocus()

        self.current_item += amount
        new_item = self.get_current_item()
        if new_item:
            new_item.focus()
        else:
            # the focus was moved out of the collection
            self.current_item = -1
            self.unfocus()

    def handle_input_event(self, event_name: str, *args) -> EVENT_HANDLE_STATE:
        for widget in self.children:
            # The first widget that handles this event will return
            if hasattr(widget, event_name):
                widget_func = getattr(widget, event_name)
                if widget_func(*args) == EVENT_HANDLED:
                    return True
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

    def on_key_press(self, symbol, modifiers) -> EVENT_HANDLE_STATE:
        if not self.is_on_focus:
            return EVENT_UNHANDLED

        # Enter
        if symbol == key.ENTER or symbol == key.RETURN:
            item = self.get_current_item()
            if hasattr(item, 'on_key_press'):
                return item.on_key_press(symbol, modifiers)
        return EVENT_UNHANDLED

    def on_key_release(self, symbol, modifiers) -> EVENT_HANDLE_STATE:
        if not self.is_on_focus:
            return EVENT_UNHANDLED

        # Enter
        if symbol == key.ENTER or symbol == key.RETURN:
            item = self.get_current_item()
            if hasattr(item, 'on_key_release'):
                return item.on_key_release(symbol, modifiers)
        return EVENT_UNHANDLED
