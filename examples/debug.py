from pudu_ui import App
from pudu_ui.colors import WHITE
from pudu_ui.primitives import Arrow


app = App(background_color=WHITE)


if __name__ == '__main__':
    # Quad
    quad = Arrow(
        x=400,
        y=100,
        width=100,
        height=300,
        batch=app.batch
    )

    app.run()
