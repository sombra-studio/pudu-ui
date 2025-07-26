from pudu_ui import App, Label, LabelParams
import pudu_ui


app = App(background_color=pudu_ui.colors.WHITE)


if __name__ == '__main__':
    # Regular text
    params = LabelParams(x=50, y=200, text="Hello World")
    label = Label(params, batch=app.batch)

    # Text anchored right
    fs = pudu_ui.styles.fonts.p2()
    fs.color = pudu_ui.colors.GRAY
    params = LabelParams(
        x=200, y=150, text="Trying something", anchor_x='right', style=fs
    )
    l2 = Label(params, batch=app.batch)

    # Centered text
    fs = pudu_ui.styles.fonts.p3()
    params = LabelParams(
        x=(50 + 150 // 2), y=100, text="Centered text", anchor_x='center',
        anchor_y='center', style=fs
    )
    l3 = Label(params, batch=app.batch)

    label.set_debug_mode()
    l2.set_debug_mode()
    l3.set_debug_mode()

    app.run()
