from enum import Enum, auto


from pudu_ui import App


class State(Enum):
    LOADING = auto()
    ACTIVE = auto()
    PAUSED = auto()
    CLOSING = auto()


class Controller:
    def __init__(
        self, app: App, name: str
    ):
        self.app: App = app
        self.name: str = name
        self.state: State = State.LOADING

    def on_load(self):
        self.state = State.LOADING

    def on_close(self):
        self.state = State.CLOSING
