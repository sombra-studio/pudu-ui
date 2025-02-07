from pudu_ui.layouts import ListLayout


class HorizontalListLayout(ListLayout):
    def recompute(self):
        n = len(self.items)
        if not self.item_height:
            item_height = self.height
        else:
            item_height = self.item_height

        if not self.item_width:
            available_width = self.width - (n - 1) * self.inter_item_spacing
            item_width = available_width / n
        else:
            item_width = self.item_width

        curr_y = self.y
        if self.reversed:
            curr_x = self.x + self.width - item_width
        else:
            curr_x = self.x

        for item in self.items:
            item.x = curr_x
            item.y = curr_y
            offset = item_width + self.inter_item_spacing
            if self.reversed:
                offset *= -1
            curr_x += offset
            item.width = item_width
            item.height = item_height
            item.invalidate()
