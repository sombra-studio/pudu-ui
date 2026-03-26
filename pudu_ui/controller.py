from enum import Enum, auto


from pudu_ui import App


class State(Enum):
    INITIALIZING = auto()
    INITIALIZED = auto()
    LOADING = auto()
    ACTIVE = auto()
    PAUSED = auto()
    CLOSING = auto()


class Controller:
    def __init__(
        self, app: App, name: str | None = None
    ):
        self.state = State.INITIALIZING
        self.app: App = app
        if not name:
            name = self.__class__.__name__
        self.name: str = name
        self.state = State.INITIALIZED
        self.screen = None

    def load(self, *args, **kwargs):
        self.on_load(*args, **kwargs)
        self.resume()

    def pause(self):
        self.on_pause()

    def resume(self):
        self.on_resume()

    def close(self):
        self.on_close()
        # Removing the reference to the screen at the end should make the
        # garbage collector delete it
        self.screen = None

    def on_load(self, *_, **__):
        self.state = State.LOADING

    def on_pause(self):
        self.state = State.PAUSED

    def on_resume(self):
        self.state = State.ACTIVE

    def on_close(self):
        self.state = State.CLOSING
