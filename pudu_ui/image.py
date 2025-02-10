from enum import Enum
from dataclasses import dataclass
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
        self.color = params.color
        sprite_x = params.x
        sprite_y = params.y
        self.sprite_offset_x = 0.0
        self.sprite_offset_y = 0.0

        if params.image_path:
            img = pyglet.resource.image(params.image_path)
            # Handle image cropping
            if params.scale_type == ImageScaleType.CROP:
                img = self.crop(img)
            # Handle image fitting
            elif params.scale_type == ImageScaleType.FIT:
                if (
                    (img.width - self.width) > 0 or
                    (img.height - self.height) > 0
                ):
                    img = self.fit(img)
                    self.sprite_offset_x = (self.width - img.width) / 2.0
                    self.sprite_offset_y = (self.height - img.height) / 2.0
                    sprite_x += self.sprite_offset_x
                    sprite_y += self.sprite_offset_y
            # Handle image filling
            else:
                img.width = self.width
                img.height = self.height
        else:
            img = pudu_ui.utils.create_gray_img(self.width, self.height)

        self.sprite = Sprite(
            img, x=sprite_x, y=sprite_y, batch=batch, group=group
        )

    def crop(self, img: pyglet.image.ImageData) -> pyglet.image.ImageData:
        center_x = int(img.width / 2.0)
        center_y = int(img.height / 2.0)

        diff_width = img.width - self.width
        diff_height = img.height - self.height
        if diff_width > 0 and diff_height > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return img.get_region(
                x, y, self.width, self.height
            )
        elif diff_width > 0:
            x = int(center_x - self.width / 2.0)
            y = int(center_y - img.height / 2.0)
            return img.get_region(
                x, y, self.width, img.height
            )
        elif diff_height > 0:
            x = int(center_x - img.width / 2.0)
            y = int(center_y - self.height / 2.0)
            return img.get_region(
                x, y, img.width, self.height
            )
        return img

    def fit(self, img: pyglet.image.ImageData) -> pyglet.image.ImageData:
        w1, h1 = pudu_ui.utils.fit_screen(
            self.width, self.height, img.width, img.height
        )
        img.width = w1
        img.height = h1
        return img

    def recompute(self):
        self.sprite.x = self.x + self.sprite_offset_x
        self.sprite.y = self.y + self.sprite_offset_y
        self.sprite.color = self.color
        # Not handling image change after init for now
