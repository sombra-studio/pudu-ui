from dataclasses import dataclass
from pyglet.graphics import Batch, Group
import pyglet


from .styles import FontStyle
from . import styles
from .widget import Params, Widget


@dataclass
class LabelParams(Params):
    value: str = ""
    style: FontStyle = styles.P1


class Label(Widget):
    def __init__(
        self, params: LabelParams, batch: Batch = None, group: Group = None
    ):
        super().__init__(params)
        self.impl = pyglet.text.Label(
            text=params.value,
            x=params.x,
            y=params.y,
            width=params.width,
            height=params.height,
            font_name=params.style.font_name,
            font_size=params.style.font_size,
            bold=params.style.bold,
            italic=params.style.italic,
            color=params.style.color,
            batch=batch,
            group=group
        )

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.impl.x = value
