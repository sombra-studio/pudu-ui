from . import Widget


class Screen:
    def __init__(self, name: str):
        self.name: str = name
        self.active: bool = True
        self.widgets: list[Widget]

    def load(self):
        pass

    def on_loaded(self, f, *args, **kwargs):
        f(*args, **kwargs)

    def close(self):
        pass

    def on_close(self, f, *args, **kwargs):
        f(*args, **kwargs)
