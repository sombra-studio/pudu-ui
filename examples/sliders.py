from pudu_ui import App, Label, LabelParams, Screen, Slider, SliderParams
import pudu_ui


def format_slider_value(slider: Slider) -> str:
    return f"{round(slider.value, 2):.2f}"


def create_on_value_change(label: Label):
    def on_value_change(slider: Slider):
        label.text = format_slider_value(slider)
        label.invalidate()

    return on_value_change


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")

        values = [0.0, 75, 33.3, 100.0]
        for i in range(len(values)):
            params = SliderParams(x=300, y=100 + i * 120, value=values[i])
            slider = Slider(params=params, batch=self.batch)
            # slider.set_debug_mode()

            label_style = pudu_ui.styles.fonts.p2()
            label_style.color = pudu_ui.colors.DARK_GRAY
            label_params = LabelParams(
                x=550, y=(slider.y + slider.height / 2.0),
                text=format_slider_value(slider), anchor_y='center',
                style=label_style
            )
            label = Label(
                label_params, batch=self.batch
            )
            slider.on_value_changed = create_on_value_change(label)

            self.widgets.append(slider)
            self.widgets.append(label)


app = App(background_color=pudu_ui.colors.WHITE)
screen = DebugScreen()
app.current_screen = screen


if __name__ == '__main__':
    app.run()
