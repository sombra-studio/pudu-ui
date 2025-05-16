from dataclasses import dataclass, field


from pudu_ui import Params, Widget
from pudu_ui.styles.sliders import SliderStyle
import pudu_ui


@dataclass
class SliderParams(Params):
    min_value: float = 0.0
    max_value: float = 100.0
    value: float = 50.0
    style: SliderStyle = field(
        default_factory=pudu_ui.styles.sliders.default_slider_style
    )


class Slider(Widget):
    pass
