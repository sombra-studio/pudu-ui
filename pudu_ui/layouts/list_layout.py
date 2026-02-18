from dataclasses import dataclass
from enum import Enum
from pyglet.graphics import Batch, Group
from pyglet.window import key


from pudu_ui import CollectionWidget, Params, Widget


class ListDirection(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


@dataclass
class ListLayoutParams(Params):
    item_width: int = 0
    item_height: int = 0
    inter_item_spacing: int = 0
    reversed: bool = False
    resizes_item_width: bool = True
    resizes_item_height: bool = True
    direction: ListDirection = ListDirection.HORIZONTAL


class ListLayout(CollectionWidget):
    def __init__(
        self, params: ListLayoutParams = None,
        batch: Batch = None, group: Group = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ListLayoutParams()
        super().__init__(params, batch=batch, group=group, parent=parent)
        self.item_width = params.item_width
        self.item_height = params.item_height
        self.inter_item_spacing = params.inter_item_spacing
        self.reversed = params.reversed
        self.resizes_item_width = params.resizes_item_width
        self.resizes_item_height = params.resizes_item_height
        self.direction = params.direction
        self.current_item = -1

    def calculate_item_height(self) -> int:
        n = len(self.children)
        if not self.item_height:
            if self.direction == ListDirection.VERTICAL:
                available_height = (
                    self.height - (n - 1) * self.inter_item_spacing
                )
                item_height = available_height / n
            else:
                item_height = self.height
        else:
            item_height = self.item_height
        return item_height

    def calculate_item_width(self) -> int:
        n = len(self.children)
        if not self.item_width:
            if self.direction == ListDirection.HORIZONTAL:
                available_width = (
                    self.width - (n - 1) * self.inter_item_spacing
                )
                item_width = available_width / n
            else:
                item_width = self.width
        else:
            item_width = self.item_width
        return item_width

    def recompute(self):
        super().recompute()
        # Compute item_width and item_height
        n = len(self.children)
        if not n:
            return

        item_height = self.calculate_item_height()
        item_width = self.calculate_item_width()

        # Compute position for each child

        if self.direction == ListDirection.HORIZONTAL:
            curr_pos = 0
            if self.reversed:
                curr_pos = self.width
        else:
            curr_pos = self.height
            if self.reversed:
                curr_pos = 0

        for item in self.children:
            if self.resizes_item_height:
                item.height = int(item_height)

            if self.resizes_item_width:
                item.width = int(item_width)

            if self.direction == ListDirection.HORIZONTAL:
                item.x = curr_pos
                if self.reversed:
                    item.x -= item.width
                item.y = 0
                offset = item.width + self.inter_item_spacing
            else:
                item.y = curr_pos - item.height
                if self.reversed:
                    item.y += item.height
                item.x = 0
                offset = item.height + self.inter_item_spacing
            if self.reversed:
                offset *= -1
            if self.direction == ListDirection.VERTICAL:
                offset *= -1    # Since list goes from top to bottom which is -y
            curr_pos += offset

            item.invalidate()

    def on_focus(self):
        if self.children:
            self.children[0].focus()
            self.current_item = 0

    def get_current_item(self) -> Widget | None:
        if self.current_item >= 0 and self.current_item < len(self.children):
            return self.children[self.current_item]
        return None

    def on_key_press(self, symbol, modifiers):
        if not self.is_on_focus:
            return

        if self.direction == ListDirection.HORIZONTAL:
            if (symbol == key.LEFT or symbol == key.A) and not modifiers:
                item = self.get_current_item()
                item.unfocus()

                self.current_item -= 1
                new_item = self.get_current_item()
                if new_item:
                    new_item.focus()

            elif (symbol == key.RIGHT or symbol == key.D) and not modifiers:
                item = self.get_current_item()
                item.unfocus()

                self.current_item += 1
                new_item = self.get_current_item()
                if new_item:
                    new_item.focus()

        if self.direction == ListDirection.VERTICAL:
            if (symbol == key.UP or symbol == key.W) and not modifiers:
                item = self.get_current_item()
                item.unfocus()

                self.current_item -= 1
                new_item = self.get_current_item()
                if new_item:
                    new_item.focus()

            elif (symbol == key.DOWN or symbol == key.S) and not modifiers:
                item = self.get_current_item()
                item.unfocus()

                self.current_item += 1
                new_item = self.get_current_item()
                if new_item:
                    new_item.focus()

        if self.current_item < 0 or self.current_item >= len(self.children):
            self.current_item = -1
            self.unfocus()
