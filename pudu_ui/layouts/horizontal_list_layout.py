from pudu_ui.layouts import ListLayout


class HorizontalListLayout(ListLayout):
    def recompute(self):
        super().recompute()
        # Compute item_height and item_width
        n = len(self.children)
        if not self.item_height:
            item_height = self.height
        else:
            item_height = self.item_height

        if not self.item_width:
            available_width = self.width - (n - 1) * self.inter_item_spacing
            item_width = available_width / n
        else:
            item_width = self.item_width

        # Compute new positions for each child
        curr_y = 0
        if self.reversed:
            curr_x = 0 + self.width - item_width
        else:
            curr_x = 0

        for item in self.children:
            item.x = curr_x
            item.y = curr_y
            offset = item_width + self.inter_item_spacing
            if self.reversed:
                offset *= -1
            curr_x += offset
            item.width = int(item_width)
            item.height = int(item_height)
            item.invalidate()
