from pudu_ui.layouts import ListLayout


class VerticalListLayout(ListLayout):
    def recompute(self):
        super().recompute()
        # Compute item_width and item_height
        n = len(self.children)
        if not self.item_height:
            available_height = self.height - (n - 1) * self.inter_item_spacing
            item_height = available_height / n
        else:
            item_height = self.item_height
        if not self.item_width:
            item_width = self.width
        else:
            item_width = self.item_width

        # Compute position for each child
        curr_x = 0
        if self.reversed:
            curr_y = 0
        else:
            curr_y = self.height - item_height

        for item in self.children:
            item.x = curr_x
            item.y = curr_y
            offset = item_height + self.inter_item_spacing
            if self.reversed:
                offset *= -1
            curr_y -= offset
            item.width = int(item_width)
            item.height = int(item_height)
            item.invalidate()
