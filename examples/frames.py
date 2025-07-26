import pudu_ui

app = pudu_ui.App(background_color=pudu_ui.colors.DARK_GRAY)
params = pudu_ui.FrameParams(
    x=50, y=100,
    width=300,
    height=120
)
frames = [pudu_ui.Frame(params, batch=app.batch)]

params.x += 400
params.style.end_color = pudu_ui.colors.DARK_PURPLE
frames.append(pudu_ui.Frame(params, batch=app.batch))

params.y += 200
params.style.radius_top_left = 24
params.style.radius_bottom_left = 24
params.style.start_color = pudu_ui.colors.MEDIUM_BLUE
params.style.end_color = pudu_ui.colors.MEDIUM_BLUE
frames.append(pudu_ui.Frame(params, batch=app.batch))

params.x -= 400
params.style.radius_top_right = 24
params.style.radius_bottom_right = 24
params.style.gradient_direction = pudu_ui.colors.GradientDirection.HORIZONTAL
params.style.start_color = pudu_ui.colors.LIGHT_BLUE_GREEN
params.style.end_color = pudu_ui.colors.MEDIUM_BLUE
frames.append(pudu_ui.Frame(params, batch=app.batch))


if __name__ == '__main__':
    app.run()
