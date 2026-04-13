from pudu_ui import App, DropdownParams, Dropdown
from pudu_ui.buttons import DropdownTriggerParams


app = App()


def on_trigger_press(_):
    print("Trigger pressed")


if __name__ == '__main__':
    trigger_params = DropdownTriggerParams(
        text="English", on_press=on_trigger_press
    )
    params = DropdownParams(
        x=400, y=200, width=160, height=300, trigger_params=trigger_params
    )
    widget = Dropdown(params=params, batch=app.batch)
    app.current_screen.widgets.append(widget)
    # widget.set_debug_mode()

    app.run()
