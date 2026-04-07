from copy import deepcopy
from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui.enums import Direction
from pudu_ui.primitives import ArrowQuad
from pudu_ui.primitives.quad import arrow_left_program
from pudu_ui.styles.arrows import ArrowStyle, default_arrow_style
from pudu_ui import Params, Widget


@dataclass
class ArrowParams(Params):
    direction: Direction = Direction.LEFT
    style: ArrowStyle = field(default_factory=default_arrow_style)


class Arrow(Widget):
    def __init__(
        self,
        params: ArrowParams = ArrowParams(),
        batch: Batch | None = None,
        group: Group | None = None,
        parent = None
    ):
        super().__init__(params=params, batch=batch, group=group, parent=parent)
        match params.direction:
            case _:
                program = arrow_left_program()
        self.style = deepcopy(params.style)

        self.quad = ArrowQuad(
            x=params.x, y=params.y, width=params.width, height=params.height,
            color=params.style.color, opacity=params.style.opacity,
            thickness=params.style.thickness,
            program=program,
            batch=batch,
            group=group,
            parent=parent
        )

    def change_style(self, style: ArrowStyle):
        if self.style == style:
            return
        self.style = deepcopy(style)

        self.quad.color = style.color
        self.quad.opacity = style.opacity
        self.quad.thickness = style.thickness

        self.invalidate()

    def recompute(self):
        super().recompute()
        self.quad.width = self.width
        self.quad.height = self.height
        self.quad.recompute()
