import pyglet


class Screen:
    def __init__(self, name: str):
        self.name: str = name
        self.batch: pyglet.graphics.Batch = pyglet.graphics.Batch()

    def draw(self):
        self.batch.draw()
