from dataclasses import dataclass, field
from pudu_ui.colors import PRIMARY_BTN_FONT_COLOR
from pudu_ui.styles.fonts import FontStyle, p1
from pudu_ui.styles.frames import FrameStyle, default_frame_style


DEFAULT_BTN_CORNER_RADIUS = 24


#------------------------------------------------------------------------------
# Factory functions

def default_button_style():
    style = ButtonStyle()
    style.frame_style.radius_top_left = DEFAULT_BTN_CORNER_RADIUS
    style.frame_style.radius_top_right = DEFAULT_BTN_CORNER_RADIUS
    style.frame_style.radius_bottom_left = DEFAULT_BTN_CORNER_RADIUS
    style.frame_style.radius_bottom_right = DEFAULT_BTN_CORNER_RADIUS
    style.font_style.color = PRIMARY_BTN_FONT_COLOR
    return style

#------------------------------------------------------------------------------


@dataclass
class ButtonStyle:
    frame_style: FrameStyle = field(default_factory=default_frame_style)
    font_style: FontStyle = field(default_factory=p1)
