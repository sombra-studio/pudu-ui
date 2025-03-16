from copy import deepcopy
from enum import Enum
from dataclasses import dataclass
from pyglet.image import AbstractImage, ImageData
from pyglet.graphics import Batch, Group
from pyglet.sprite import Sprite
import pyglet


from pudu_ui import Params, Widget
import pudu_ui


class ImageScaleType(Enum):
    CROP = 0
    FIT = 1
    FILL = 2


@dataclass
class ImageParams(Params):
    image_path: str = ""
    scale_type: ImageScaleType = ImageScaleType.CROP
    color: tuple[int, int, int, int] = (255, 255, 255, 255)


def default_image_params():
    return ImageParams()

class Image(Widget):
    def __init__(
        self,
        params: ImageParams,
        batch: Batch = None,
        group: Group = None
    ):
        super().__init__(params)
        self.image_path = params.image_path
        self.scale_type = params.scale_type
        self.color = params.color
        self.sprite_offset_x = 0.0
        self.sprite_offset_y = 0.0

        if params.image_path:
            self.img = pyglet.resource.image(params.image_path)
        else:
            self.img = pudu_ui.utils.create_gray_img(self.width, self.height)

        img = self.rescale(self.img)

        self.sprite = Sprite(
            img, x=self.x, y=self.y, batch=batch, group=group
        )

    def crop(self) -> AbstractImage:
        center_x = int(self.img.width / 2.0)
        center_y = int(self.img.height / 2.0)

        diff_width = self.img.width - self.width
        diff_height = self.img.height - self.height
        if diff_width > 0 and diff_height > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return self.img.get_region(
                x, y, self.width, self.height
            )
        elif diff_width > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.img.height / 2.0)
            return self.img.get_region(
                x, y, self.width, self.img.height
            )
        elif diff_height > 0:
            x = int(center_x - self.img.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return self.img.get_region(
                x, y, self.img.width, self.height
            )
        return self.img

    def fit(self) -> AbstractImage:
        img = deepcopy(self.img)
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
            self.x += self.sprite_offset_x
            self.y += self.sprite_offset_y
        return img

    def fill(self) -> AbstractImage:
        img = deepcopy(self.img)
        img.width = self.width
        img.height = self.height
        return img

    def recompute(self):
        self.sprite.x = self.x + self.sprite_offset_x
        self.sprite.y = self.y + self.sprite_offset_y
        self.sprite.color = self.color
        self.sprite.width = self.width
        self.sprite.height = self.height
        # Not handling image change after init for now

    def rescale(self, img: AbstractImage) -> AbstractImage:
        # Handle image cropping
        if self.scale_type == ImageScaleType.CROP:
            return self.crop()
        # Handle image fitting
        elif self.scale_type == ImageScaleType.FIT:



                return img
        # Handle image filling
        else:
            return self.fill()
