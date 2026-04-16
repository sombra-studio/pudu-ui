from pudu_ui import App, DropdownParams, Dropdown
from pudu_ui.dropdown_trigger import DropdownTriggerParams


app = App()


def on_trigger_press(_):
    print("Trigger pressed")


def on_select(option: str):
    print(f"{option} selected")


if __name__ == '__main__':
    trigger_params = DropdownTriggerParams(
        text="English", on_trigger=on_trigger_press
    )
    params = DropdownParams(
        x=400, y=200,
        options=["English", "Spanish", "French"],
        on_select=on_select,
        trigger_params=trigger_params
    )
    widget = Dropdown(params=params, batch=app.batch)
    app.current_screen.widgets.append(widget)
    # widget.set_debug_mode()

    app.run()
