from dataclasses import dataclass, field
from pudu_ui.colors import *
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


def dft_btn_hover_style():
    style = default_button_style()
    style.frame_style.start_color = PRIMARY_BTN_HOVER_BG_COLOR
    return style


def dft_btn_focus_style():
    style = default_button_style()
    style.frame_style.start_color = PRIMARY_BTN_FOCUS_BG_COLOR
    return style


def dft_btn_press_style():
    style = default_button_style()
    style.frame_style.start_color = PRIMARY_BTN_PRESS_BG_COLOR
    return style


#------------------------------------------------------------------------------


@dataclass
class ButtonStyle:
    frame_style: FrameStyle = field(default_factory=default_frame_style)
    font_style: FontStyle = field(default_factory=p1)

    def set_solid_color(self, color: Color):
        self.frame_style.set_solid_color(color)

    def set_uniform_radius(self, radius: float):
        self.frame_style.set_uniform_radius(radius)
