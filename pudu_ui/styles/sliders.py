from dataclasses import dataclass, field


from pudu_ui import Color
import pudu_ui


def default_handle_color():
    return pudu_ui.colors.PURPLE


def default_left_color():
    return pudu_ui.colors.LIGHT_PURPLE


def default_right_color():
    return pudu_ui.colors.LIGHTER_GRAY


def default_slider_style():
    return SliderStyle()


@dataclass
class SliderStyle:
    left_color: Color = field(default_factory=default_left_color)
    right_color: Color = field(default_factory=default_left_color)
    handle_color: Color = field(default_factory=default_handle_color)
