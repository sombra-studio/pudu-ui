from pudu_ui import App
from pudu_ui.arrow import Arrow, ArrowParams
from pudu_ui.colors import WHITE
from pudu_ui.enums import Direction

app = App(background_color=WHITE)


if __name__ == '__main__':
    params = ArrowParams(
        x=400, y=200, width=16, height=8,
        direction=Direction.UP
    )
    arrow = Arrow(params=params, batch=app.batch)
    #arrow.set_debug_mode()

    app.run()
