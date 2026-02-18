from pudu_ui import App, Frame, FrameParams, Slider, SliderParams
from pudu_ui.colors import WHITE
from pudu_ui.primitives import Quad
from pudu_ui.slider import DEFAULT_THUMB_SIZE
from pudu_ui.styles.sliders import default_thumb_style


app = App(background_color=WHITE)


if __name__ == '__main__':
    screen = app.current_screen
    # Slider
    # params = SliderParams(x=300, y=100)
    # for i in range(3):
    #     x = i * 300
    #     params.x = x
    #     new_slider = Slider(params, batch=app.batch)
    #     screen.widgets.append(new_slider)
    # slider = Slider(params, batch=screen.batch)
    # screen.widgets.append(slider)

    # Quad
    # quad = Quad(batch=app.batch)

    # Frame
    style = default_thumb_style()
    params = FrameParams(
        width=DEFAULT_THUMB_SIZE, height=DEFAULT_THUMB_SIZE, focusable=True,
        style=style
    )
    frame = Frame(params, batch=app.batch)

    app.run()
