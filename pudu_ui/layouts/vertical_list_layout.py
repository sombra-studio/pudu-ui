from pudu_ui.layouts import ListLayout


class VerticalListLayout(ListLayout):
    def recompute(self):
        n = len(self.items)
        if not self.item_height:
            available_height = self.height - (n - 1) * self.inter_item_spacing
            item_height = available_height / n
        else:
            item_height = self.item_height

        curr_x = self.x
        if self.reversed:
            curr_y = self.y + self.height - self.item_height
        else:
            curr_y = self.y

        for item in self.items:
            item.x = curr_x
            item.y = curr_y
            offset = self.item_height + self.inter_item_spacing
            if self.reversed:
                offset *= -1
            curr_y -= offset
            item.height = item_height
            item.invalidate()
