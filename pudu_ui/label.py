from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum, auto
from pyglet.graphics import Batch, Group
import pyglet
from typing import Literal


from pudu_ui.styles.fonts import FontStyle
from pudu_ui import styles, Params, Widget


class LabelResizeType(Enum):
    FIT = auto()
    FILL = auto()
    NONE = auto()


@dataclass
class LabelParams(Params):
    text: str = ""
    anchor_x: Literal['left', 'center', 'right'] = 'left'
    anchor_y: Literal['top', 'bottom', 'center', 'baseline'] = 'baseline'
    resize_type: LabelResizeType = LabelResizeType.NONE
    rotation: float = 0.0
    style: FontStyle = field(default_factory=styles.fonts.p1)


class Label(Widget):
    def __init__(
        self, params: LabelParams = None,
        batch: Batch = None, group: Group = None,
        parent: Widget | None = None
    ):
        if not params:
            params = LabelParams()
        super().__init__(params, batch=batch, group=group)
        self.style = deepcopy(params.style)
        self.color = params.style.color
        self.opacity = params.style.opacity
        self.parent = parent
        self.text = params.text
        self.resize_type = params.resize_type
        self.anchor_x = params.anchor_x
        self.anchor_y = params.anchor_y

        x, y = self.get_position()
        self.impl = pyglet.text.Label(
            text=params.text,
            x=x,
            y=y,
            width=params.width,
            # pyglet has this weird thing that if you pass a height value to
            # Label it will not center it if you give an anchor_x, so we only
            # pass the width and the font_size and that determines everything
            # height=params.height,
            anchor_x=params.anchor_x,
            anchor_y=params.anchor_y,
            rotation=params.rotation,
            font_name=params.style.font_name,
            font_size=params.style.font_size,
            weight=params.style.weight,
            italic=params.style.italic,
            color=self.get_color_tuple(),
            batch=batch,
            group=group
        )
        self.recompute()

    def change_style(self, style: FontStyle):
        if self.style == style:
            return
        self.style = deepcopy(style)
        self.color = style.color
        self.opacity = style.opacity
        self.impl.font_name = style.font_name
        self.impl.font_size = style.font_size
        self.impl.width = style.weight
        self.impl.italic = style.italic
        self.impl.color = self.get_color_tuple()
        self.recompute()

    def get_color_tuple(self)-> tuple[int, int, int, int]:
        color = self.color
        return color.r, color.g, color.b, self.opacity

    def recompute(self):
        x, y = self.get_position()
        self.impl.x = x
        self.impl.y = y
        self.impl.text = self.text
        # in case width or height was changed, we use the target style
        self.impl.font_size = self.style.font_size
        self.rescale()

        super().recompute()

        if self.anchor_x == 'center':
            self.debug_background.x = -(self.width / 2.0)
            self.debug_label.x += -(self.width / 2.0)
        if self.anchor_y == 'center':
            self.debug_background.y = -(self.height / 2.0)
            self.debug_label.y += -(self.height / 2.0)
        if self.anchor_x == 'right':
            self.debug_background.x = -self.width
            self.debug_label.x += -self.width
        if self.anchor_y == 'right':
            self.debug_background.y = -self.height
            self.debug_label.x += -self.height
        self.debug_background.recompute()

    def rescale(self):
        if self.resize_type == LabelResizeType.FIT:
            self.fit()
        elif self.resize_type == LabelResizeType.FILL:
            self.fill()
        else:
            self.wrap()

    def fill(self):
        while (
            self.width and self.height and
            not (
                self.impl.content_width >= self.width or
                self.impl.content_height >= self.height
            )
        ):
            self.impl.font_size += 1

    def fit(self):
        while self.width and self.impl.content_width > self.width:
            self.impl.font_size -= 1
        while self.height and self.impl.content_height > self.height:
            self.impl.font_size -= 1

    def wrap(self):
        self.width = int(self.impl.content_width)
        self.height = int(self.impl.content_height)
