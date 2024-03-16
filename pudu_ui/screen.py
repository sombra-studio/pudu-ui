import pyglet


class Screen:
    def __init__(
        self,
        name: str,
        width: int,
        height: int,
        batch: pyglet.graphics.Batch = pyglet.graphics.get_default_batch(),
        group: pyglet.graphics.Group = pyglet.graphics.Group()
    ):
        self.name: str = name
        self.width: int = width
        self.height: int = height
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
