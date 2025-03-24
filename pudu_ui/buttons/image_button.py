from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui.buttons import Button, ButtonParams
from pudu_ui.image import ImageParams, Image, default_image_params
from pudu_ui.styles.buttons import (
    dft_img_btn_style, dft_img_btn_hover_style, dft_img_btn_focus_style,
    dft_img_btn_press_style, ImageButtonStyle
)


@dataclass
class ImageButtonParams(ButtonParams):
    image_params: ImageParams = field(default_factory=default_image_params)
    style: ImageButtonStyle = field(default_factory=dft_img_btn_style)
    hover_style: ImageButtonStyle = field(
        default_factory=dft_img_btn_hover_style
    )
    focus_style: ImageButtonStyle = field(
        default_factory=dft_img_btn_focus_style
    )
    press_style: ImageButtonStyle = field(
        default_factory=dft_img_btn_press_style
    )


class ImageButton(Button):
    def __init__(
        self,
        params: ImageButtonParams,
        batch: Batch = None,
        group: Group = None
    ):
        super().__init__(params, batch=batch, group=group)
        params.image_params.color = params.style.color
        self.image = Image(
            params.image_params, batch=batch, group=self.front_group
        )
        self.children.append(self.image)

    def update(self, dt: float):
        super().update(dt)
        self.image.update(dt)

    def change_style(self, style: ImageButtonStyle):
        super().change_style(style)
        self.image.color = style.color
