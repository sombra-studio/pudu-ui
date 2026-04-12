from pudu_ui import App, DropdownParams, Dropdown
from pudu_ui.colors import WHITE


app = App(background_color=WHITE)


if __name__ == '__main__':
    params = DropdownParams(
        x=400, y=200, width=160, height=300
    )
    widget = Dropdown(params=params, batch=app.batch)

    app.run()
