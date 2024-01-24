from enum import Enum, auto

from . import Widget


class State(Enum):
    LOADING = auto()
    ACTIVE = auto()
    PAUSED = auto()
    CLOSING = auto()


class Screen:
    def __init__(
        self, name: str, on_load=lambda: None, on_close=lambda: None
    ):
        self.name: str = name
        self.state: State = State.LOADING
        self.widgets: list[Widget] = []
        self.on_load = on_load
        self.on_close = on_close

    def load(self):
        self.state = State.LOADING
        self.on_load()

    def close(self):
        self.state = State.CLOSING
        self.on_close()
