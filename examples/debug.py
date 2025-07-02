import pudu_ui
import pyglet


if __name__ == '__main__':
    app = pudu_ui.App()
    params = pudu_ui.layouts.ListLayoutParams(
        width=app.width, height=app.height, item_width=app.width,
        resizes_item_height=False
    )
    container = pudu_ui.layouts.VerticalListLayout(params, batch=app.batch)

    # First frame
    style = pudu_ui.styles.frames.FrameStyle()
    style.set_solid_color(pudu_ui.colors.WHITE)
    params = pudu_ui.FrameParams(height=200, style=style)
    container.add(pudu_ui.Frame(params, batch=app.batch))

    # Second frame
    style = pudu_ui.styles.frames.FrameStyle()
    style.set_solid_color(pudu_ui.colors.MEDIUM_BLUE)
    params = pudu_ui.FrameParams(height=350, style=style)
    container.add(pudu_ui.Frame(params, batch=app.batch))

    # Third frame
    container.add(pudu_ui.Frame(batch=app.batch))

    app.current_screen.widgets.append(container)
    app.run()
