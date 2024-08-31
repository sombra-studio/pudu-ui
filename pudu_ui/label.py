from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group
import pyglet
from typing import Literal


from pudu_ui.styles.fonts import FontStyle
from pudu_ui import styles
from pudu_ui.widget import Params, Widget


@dataclass
class LabelParams(Params):
    value: str = ""
    anchor_x: Literal['left', 'center', 'right'] = 'left'
    anchor_y: Literal['top', 'bottom', 'center', 'baseline'] = 'baseline'
    width: float = None
    height: float = None
    rotation: float = 0.0
    style: FontStyle = field(default_factory=styles.fonts.p1)


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
            anchor_x=params.anchor_x,
            anchor_y=params.anchor_y,
            rotation=params.rotation,
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
        return self.impl.x

    @x.setter
    def x(self, value):
        self.impl.x = value

    @property
    def y(self):
        return self.impl.y

    @y.setter
    def y(self, value):
        self.impl.y = value

    @property
    def value(self):
        return self.impl.text

    @value.setter
    def value(self, text):
        self.impl.text = text
