from enum import Enum
from dataclasses import dataclass, field
from pyglet.image import AbstractImage
from pyglet.graphics import Batch, Group
from pyglet.sprite import Sprite
import pyglet


from pudu_ui import Color, Params, Widget
import pudu_ui


def default_color() -> Color:
    return pudu_ui.colors.WHITE


class ImageScaleType(Enum):
    CROP = 0
    FIT = 1
    FILL = 2


@dataclass
class ImageParams(Params):
    image_path: str = ""
    scale_type: ImageScaleType = ImageScaleType.FIT
    color: Color = field(default_factory=default_color)
    opacity: int = 255


def default_image_params():
    return ImageParams()

class Image(Widget):
    def __init__(
        self,
        params: ImageParams,
        batch: Batch = None,
        group: Group = None,
        parent: Widget | None = None
    ):
        super().__init__(params)
        self.image_path = params.image_path
        self.scale_type = params.scale_type
        self.color = params.color
        self.opacity = params.opacity
        self.parent = parent

        self.sprite_offset_x = 0.0
        self.sprite_offset_y = 0.0

        if params.image_path:
            self.img = pyglet.resource.image(params.image_path)
        else:
            self.img = pudu_ui.utils.create_gray_img(self.width, self.height)

        img = self.rescale()
        sprite_x, sprite_y = self.get_sprite_position()
        self.sprite = Sprite(
            img, x=sprite_x, y=sprite_y, batch=batch, group=group
        )
        self.sprite.color = (*self.color.as_tuple(), self.opacity)

    def copy_img(self) -> AbstractImage:
        img = self.img.get_region(0, 0, self.img.width, self.img.height)
        return img

    def crop(self) -> AbstractImage:
        center_x = int(self.img.width / 2.0)
        center_y = int(self.img.height / 2.0)

        diff_width = self.img.width - self.width
        diff_height = self.img.height - self.height
        if diff_width > 0 and diff_height > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return self.img.get_region(x, y, self.width, self.height)
        elif diff_width > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.img.height / 2.0)
            return self.img.get_region(x, y, self.width, self.img.height)
        elif diff_height > 0:
            x = int(center_x - self.img.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return self.img.get_region(x, y, self.img.width, self.height)
        return self.copy_img()

    def fit(self) -> AbstractImage:
        img = self.copy_img()
        if (
            (self.img.width - self.width) > 0 or
            (self.img.height - self.height) > 0
        ):
            w1, h1 = pudu_ui.utils.fit_screen(
                self.width, self.height, self.img.width, self.img.height
            )
            img.width = w1
            img.height = h1
            self.sprite_offset_x = (self.width - img.width) / 2.0
            self.sprite_offset_y = (self.height - img.height) / 2.0
        return img

    def fill(self) -> AbstractImage:
        img = self.copy_img()
        img.width = self.width
        img.height = self.height
        return img

    def get_sprite_position(self) -> [float, float]:
        x_offset = self.parent.x if self.parent else 0
        y_offset = self.parent.y if self.parent else 0
        return (
            self.x + x_offset + self.sprite_offset_x,
            self.y + y_offset + self.sprite_offset_y
        )

    def recompute(self):
        new_image = self.rescale()
        sprite_x, sprite_y = self.get_sprite_position()
        self.sprite.update(sprite_x, sprite_y)
        self.sprite.color = (*self.color.as_tuple(), self.opacity)
        self.sprite.image = new_image

    def rescale(self) -> AbstractImage:
        if self.scale_type == ImageScaleType.CROP:
            return self.crop()
        elif self.scale_type == ImageScaleType.FIT:
            return self.fit()
        else:
            return self.fill()
