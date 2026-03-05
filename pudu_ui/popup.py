from collections.abc import Callable
from dataclasses import dataclass, field

from pudu_ui.styles.popups import PopUpStyle, default_popup_style
from pyglet.graphics import Batch


from pudu_ui import FrameParams, Frame, Params, Widget



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
        batch: Batch | None = None
    ):
        super().__init__(params=params, batch=batch)
        if not params:
            params = PopUpParams()
        frame_params = FrameParams(
            x=params.x, y=params.y, width=params.width, height=params.height,
            style=params.style.background_style
        )
        self.frame = Frame(params=frame_params, batch=batch)
