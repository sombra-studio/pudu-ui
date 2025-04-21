from dataclasses import dataclass, field
from pudu_ui.colors import *
from pudu_ui.styles.fonts import FontStyle, p1
from pudu_ui.styles.frames import FrameStyle, default_frame_style


DEFAULT_BTN_CORNER_RADIUS = 24


#------------------------------------------------------------------------------
# Factory functions

def default_button_style():
    style = ButtonStyle()
    style.frame_style.set_uniform_radius(DEFAULT_BTN_CORNER_RADIUS)
    style.font_style.color = PRIMARY_BTN_FONT_COLOR
    return style


def dft_btn_hover_style():
    style = default_button_style()
    style.frame_style.start_color = PRIMARY_BTN_HOVER_BG_COLOR
    style.font_style.color = PRIMARY_BTN_HOVER_FONT_COLOR
    return style


def dft_btn_focus_style():
    style = default_button_style()
    style.font_style.color = PRIMARY_BTN_FOCUS_FONT_COLOR
    style.font_style.color = PRIMARY_BTN_FOCUS_FONT_COLOR
    return style


def dft_btn_press_style():
    style = default_button_style()
    style.frame_style.start_color = PRIMARY_BTN_PRESS_BG_COLOR
    style.font_style.color = PRIMARY_BTN_PRESS_FONT_COLOR
    return style


# Image Buttons

def dft_img_btn_style():
    style = ImageButtonStyle()
    return style


def dft_img_btn_hover_style():
    style = ImageButtonStyle()
    style.frame_style.start_color = PRIMARY_BTN_HOVER_BG_COLOR
    style.color = LIGHTER_GRAY
    return style


def dft_img_btn_focus_style():
    style = dft_img_btn_style()
    style.frame_style.start_color = PRIMARY_BTN_FOCUS_BG_COLOR
    style.color = LIGHTER_GRAY
    return style


def dft_img_btn_press_style():
    style = dft_img_btn_style()
    style.frame_style.start_color = PRIMARY_BTN_PRESS_BG_COLOR
    style.color = WHITE
    return style


def default_image_color() -> Color:
    return LIGHT_GRAY

#------------------------------------------------------------------------------


@dataclass
class ButtonStyle:
    frame_style: FrameStyle = field(default_factory=default_frame_style)
    font_style: FontStyle = field(default_factory=p1)

    def set_solid_color(self, color: Color):
        self.frame_style.set_solid_color(color)

    def set_uniform_radius(self, radius: float):
        self.frame_style.set_uniform_radius(radius)


@dataclass
class ImageButtonStyle(ButtonStyle):
    color: Color = field(default_factory=default_image_color)
