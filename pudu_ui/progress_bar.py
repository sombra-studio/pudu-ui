from dataclasses import dataclass, field


from pudu_ui import Params, Widget
from pudu_ui.styles.progress_bars import ProgressBarStyle
import pudu_ui


@dataclass
class ProgressBarParams(Params):
    min_value: float = 0.0
    max_value: float = 100.0
    value: float = 50.0
    style: ProgressBarStyle = field(
        default_factory=pudu_ui.styles.progress_bars.default_progress_bar_style
    )


class ProgressBar(Widget):
    pass
