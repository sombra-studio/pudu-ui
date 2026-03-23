from dataclasses import dataclass, field
from pudu_ui import Frame, FrameParams, Params, Widget, WidgetGroup
from pyglet.graphics import Batch, Group

from pudu_ui.styles.toggles import ToggleStyle, dft_toggle_style


@dataclass
class ToggleParams(Params):
    width: int = 120
    height: int = 20
    is_on: bool = False
    style: ToggleStyle = field(default_factory=dft_toggle_style)
    focus_style: ToggleStyle = field(default_factory=dft_toggle_style)


class Toggle(Widget):
    def __init__(
        self,
        params: ToggleParams | None = None,
        batch: Batch | None = None,
        group: Group | None = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ToggleParams()
        super().__init__(params=params, batch=batch, group=group, parent=parent)

        self.style = params.style
        self.focus_style = params.focus_style

        self.back_group = WidgetGroup(widget=self, order=0, parent=self.group)
        self.front_group = WidgetGroup(widget=self, order=1, parent=self.group)

        self.background = self.create_background()
        self.thumb = self.create_thumb()

        self.children.append(self.background)
        self.children.append(self.thumb)

    def create_background(self) -> Frame:
        frame_params = FrameParams(
            width=self.width, height=self.height,
            style=self.style.background_style
        )
        frame = Frame(params=frame_params)
        return frame

    def create_thumb(self) -> Frame:
        pass

    def change_style(self, style: ToggleStyle):
        self.background.change_style(style.background_style)
        self.thumb.change_style(style.thumb_style)
