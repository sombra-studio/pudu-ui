from pudu_ui import App
from pudu_ui.enums import Direction
from pudu_ui.layouts import ListLayoutParams
from pudu_ui.layouts.list_layout import ListLayout
from pudu_ui.arrow import ArrowParams, Arrow


if __name__ == '__main__':
    app = App()
    layout = ListLayout(
        params=ListLayoutParams(width=400, height=60, inter_item_spacing=20),
        batch=app.batch
    )
    layout.invalidate()

    layout.add(
        Arrow(
            params=ArrowParams(direction=Direction.LEFT),
            batch=app.batch
        )
    )
    layout.add(
        Arrow(
            params=ArrowParams(direction=Direction.RIGHT),
            batch=app.batch
        )
    )
    layout.add(
        Arrow(
            params=ArrowParams(direction=Direction.DOWN),
            batch=app.batch
        )
    )
    layout.add(
        Arrow(
            params=ArrowParams(direction=Direction.UP),
            batch=app.batch
        )
    )

    app.current_screen.widgets.append(layout)

    app.run()
