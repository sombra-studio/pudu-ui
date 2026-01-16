from enum import Enum
from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group, Texture
from pyglet.sprite import Sprite

from pudu_ui import Color, Params, Widget
import pudu_ui


def default_color() -> Color:
    return pudu_ui.colors.WHITE


class ImageScaleType(Enum):
    CROP = 0
    FIT = 1
    FILL = 2
    WRAP = 3


@dataclass
class ImageParams(Params):
    texture: Texture | None = None
    scale_type: ImageScaleType = ImageScaleType.FIT
    color: Color = field(default_factory=default_color)
    opacity: int = 255


def default_image_params():
    return ImageParams()

class Image(Widget):
    def __init__(
        self,
        params: ImageParams = None,
        batch: Batch = None,
        group: Group = None,
        parent: Widget | None = None
    ):
        if not params:
            params = ImageParams()
        super().__init__(params, batch=batch, group=group, parent=parent)
        self.scale_type = params.scale_type
        self.color = params.color
        self.opacity = params.opacity
        self.parent = parent

        self.sprite_offset_x = 0.0
        self.sprite_offset_y = 0.0

        if params.texture:
            self.texture = params.texture
        else:
            self.texture = pudu_ui.utils.create_gray_img(self.width,
                self.height
            ).get_texture()

        img = self.rescale()
        sprite_x, sprite_y = self.get_sprite_position()
        self.sprite = Sprite(
            img, x=sprite_x, y=sprite_y, batch=batch, group=group
        )
        self.sprite.color = (*self.color.as_tuple(), self.opacity)

    def copy_img(self) -> Texture:
        img = self.texture.get_region(
            0, 0, self.texture.width, self.texture.height
        )
        return img

    def crop(self) -> Texture:
        center_x = int(self.texture.width / 2.0)
        center_y = int(self.texture.height / 2.0)

        diff_width = self.texture.width - self.width
        diff_height = self.texture.height - self.height
        if diff_width > 0 and diff_height > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return self.texture.get_region(x, y, self.width, self.height)
        elif diff_width > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.texture.height / 2.0)
            return self.texture.get_region(x, y, self.width, self.texture.height)
        elif diff_height > 0:
            x = int(center_x - self.texture.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return self.texture.get_region(x, y, self.texture.width, self.height)
        return self.copy_img()

    def fit(self) -> Texture:
        img = self.copy_img()
        if (
            (self.texture.width - self.width) > 0 or
            (self.texture.height - self.height) > 0
        ):
            w1, h1 = pudu_ui.utils.fit_screen(
                self.width, self.height, self.texture.width, self.texture.height
            )
            img.width = w1
            img.height = h1
            self.sprite_offset_x = (self.width - img.width) / 2.0
            self.sprite_offset_y = (self.height - img.height) / 2.0
        return img

    def fill(self) -> Texture:
        img = self.copy_img()
        img.width = self.width
        img.height = self.height
        return img

    def wrap(self) -> Texture:
        self.sprite_offset_x = 0
        self.sprite_offset_y = 0
        img = self.copy_img()
        if self.width != img.width or self.height != img.height:
            self.width = img.width
            self.height = img.height
            self.recompute()
        return img

    def get_sprite_position(self) -> tuple[float, float]:
        x, y = self.get_position()
        return (
            x + self.sprite_offset_x, y + self.sprite_offset_y
        )

    def recompute(self):
        super().recompute()
        new_image = self.rescale()
        sprite_x, sprite_y = self.get_sprite_position()
        self.sprite.update(sprite_x, sprite_y)
        self.sprite.color = (*self.color.as_tuple(), self.opacity)
        self.sprite.image = new_image

    def rescale(self) -> Texture:
        if self.scale_type == ImageScaleType.CROP:
            return self.crop()
        elif self.scale_type == ImageScaleType.FIT:
            return self.fit()
        elif self.scale_type == ImageScaleType.FILL:
            return self.fill()
        else:
            return self.wrap()
