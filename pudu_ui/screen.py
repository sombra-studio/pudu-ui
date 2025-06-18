import pyglet


from pudu_ui import Widget

class Screen:
    def __init__(self, name: str):
        self.name: str = name
        self.batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
        self.widgets: list[Widget] = []

    def update(self, dt):
        for widget in self.widgets:
            widget.update(dt)

    def draw(self):
        self.batch.draw()
