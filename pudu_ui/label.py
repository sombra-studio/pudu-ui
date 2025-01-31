from dataclasses import dataclass, field
from enum import Enum, auto
from pyglet.graphics import Batch, Group
import pyglet
from typing import Literal


from pudu_ui.styles.fonts import FontStyle
from pudu_ui import styles
from pudu_ui.widget import Params, Widget


class LabelResizeType(Enum):
    WRAP = auto()
    FIT = auto()
    NONE = auto()


@dataclass
class LabelParams(Params):
    text: str = ""
    anchor_x: Literal['left', 'center', 'right'] = 'left'
    anchor_y: Literal['top', 'bottom', 'center', 'baseline'] = 'baseline'
    width: int = None
    height: int = None
    resize_type: LabelResizeType = LabelResizeType.NONE
    rotation: float = 0.0
    style: FontStyle = field(default_factory=styles.fonts.p1)


class Label(Widget):
    def __init__(
        self, params: LabelParams, batch: Batch = None, group: Group = None
    ):
        super().__init__(params)
        self.impl = pyglet.text.Label(
            text=params.text,
            x=params.x,
            y=params.y,
            width=params.width,
            height=params.height,
            anchor_x=params.anchor_x,
            anchor_y=params.anchor_y,
            rotation=params.rotation,
            font_name=params.style.font_name,
            font_size=params.style.font_size,
            weight=params.style.weight,
            italic=params.style.italic,
            color=params.style.color,
            batch=batch,
            group=group
        )
        self.text = params.text
        self.resize_type = params.resize_type
        if self.resize_type == LabelResizeType.WRAP:
            self.resize()

    def recompute(self):
        self.impl.x = self.x
        self.impl.y = self.y
        self.impl.text = self.text

    def resize(self):
        while self.width and self.impl.content_width > self.width:
            self.impl.font_size -= 1
        while self.height and self.impl.content_height > self.height:
            self.impl.font_size -= 1