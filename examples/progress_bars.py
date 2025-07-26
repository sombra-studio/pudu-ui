from pudu_ui import ProgressBar, ProgressBarParams, Screen
import pudu_ui


class DebugScreen(Screen):
    def __init__(self):
        super().__init__(name="home")
        self.bars = []
        values = [0, 30, 50, 75, 100]
        # Health bars
        for i, value in enumerate(values):
            bar = ProgressBar(batch=self.batch)
            bar.x = 200
            bar.y = 500 - i * 100
            bar.value = value
            bar.invalidate()
            self.bars.append(bar)

        # Video bars
        height = 12
        style = pudu_ui.styles.progress_bars.ProgressBarStyle(
            left_color=pudu_ui.colors.PURPLE,
            right_color=pudu_ui.colors.DARK_GRAY,
            border_width=0
        )
        style.set_uniform_radius(height / 2.0)
        params = ProgressBarParams(height=height, style=style)

        for i, value in enumerate(values):
            params.x = 500
            params.y = 500 - i * 100
            params.value = value
            bar = ProgressBar(params=params, batch=self.batch)
            self.bars.append(bar)

        for bar in self.bars:
            self.widgets.append(bar)


app = pudu_ui.App()
screen = DebugScreen()
app.current_screen = screen


if __name__ == '__main__':
    app.run()
