from enum import Enum, auto


from pudu_ui import App


class State(Enum):
    LOADING = auto()
    ACTIVE = auto()
    PAUSED = auto()
    CLOSING = auto()


class Controller:
    def __init__(
        self, app: App, name: str | None = None
    ):
        self.app: App = app
        if not name:
            name = self.__class__.__name__
        self.name: str = name
        self.load()

    def load(self):
        self.on_load()
        self.state = State.ACTIVE

    def pause(self):
        self.on_pause()

    def close(self):
        self.on_close()

    def on_load(self):
        self.state = State.LOADING

    def on_close(self):
        self.state = State.CLOSING
