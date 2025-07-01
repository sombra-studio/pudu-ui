from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from controllers.two_screens_controller import TwoScreensController
import pudu_ui


app = pudu_ui.App(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
controller = TwoScreensController(app)


if __name__ == '__main__':
    app.run()
