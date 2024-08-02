import pyglet


class Screen:
    def __init__(
        self,
        name: str,
        batch: pyglet.graphics.Batch = pyglet.graphics.get_default_batch(),
        group: pyglet.graphics.Group = pyglet.graphics.Group()
    ):
        self.name: str = name
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
