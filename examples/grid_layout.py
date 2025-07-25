import pudu_ui
from pudu_ui import Button
from pudu_ui.layouts import GridLayout, GridLayoutParams



if __name__ == '__main__':
    app = pudu_ui.App()
    layout_params = GridLayoutParams(
        width=200, height=300,
        rows=3, columns=2, item_gap=10.0
    )
    grid = GridLayout(layout_params, batch=app.batch)
    num_items = 6
    for i in range(num_items):
        new_item = Button(batch=app.batch)
        grid.add(new_item)
        # Use the index given to the new item as the text of the button
        new_item.text = f"{new_item.index}"

    # Invalidate grid to apply text change in buttons
    grid.invalidate()

    app.current_screen.widgets.append(grid)

    app.run()
