from pudu_ui import App
from pudu_ui.arrow import Arrow, ArrowParams
from pudu_ui.colors import WHITE
from pudu_ui.enums import Direction

app = App(background_color=WHITE)


if __name__ == '__main__':
    params = ArrowParams(
        x=400, y=200, width=240, height=160,
        direction=Direction.DOWN
    )
    params.style.thickness = 20
    arrow = Arrow(params=params, batch=app.batch)
    arrow.set_debug_mode()

    app.run()
