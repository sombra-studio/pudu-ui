from pudu_ui import Color, Params, Widget
import pudu_ui


class FrameParams(Params):
    background_color:Color = pudu_ui.colors.PURPLE
    focus_color:Color = pudu_ui.colors.LIGHT_PURPLE
    hover_color:Color = pudu_ui.colors.LIGHTER_PURPLE


class Frame(Widget):
    def __init__(self, params: FrameParams):
        super().__init__(params)

