from collections.abc import Callable
from dataclasses import dataclass, field

from pyglet.graphics import Batch, Group

from pudu_ui import FrameParams, Frame, Label, LabelParams, Params, Widget
from pudu_ui.styles.fonts import h2
from pudu_ui.styles.popups import PopUpStyle, default_popup_style


TITLE_MARGIN_Y = 12


@dataclass
class PopUpParams(Params):
    title: str = ""
    description: str = ""
    opt1_text: str = ""
    opt2_text: str = ""
    opt1_callback: Callable[..., None] = lambda: None
    opt2_callback: Callable[..., None] | None = None
    style: PopUpStyle = field(default_factory=default_popup_style)


class PopUp(Widget):
    def __init__(
        self,
        params: PopUpParams | None = None,
        batch: Batch | None = None,
        group: Group | None = None
    ):
        super().__init__(params=params, batch=batch, group=group)
        if not params:
            params = PopUpParams()
        frame_params = FrameParams(
            x=params.x, y=params.y, width=params.width, height=params.height,
            style=params.style.background_style
        )
        self.frame = Frame(params=frame_params, batch=batch)
        title_params = LabelParams(
            x=params.width//2, y=TITLE_MARGIN_Y,
            anchor_x='center', anchor_y='center',
            style=h2()
        )
        self.title = Label(
            params=title_params, batch=batch, group=group, parent=self
        )
