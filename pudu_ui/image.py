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
    def __init__(self, params: ImageParams, batch: Batch, group: Group):
        super().__init__(params)
        img = pyglet.resource.image(params.image_path)
        img.anchor_x = 'center'
        img.anchor_y = 'center'
        center_x = img.width / 2.0
        center_y = img.height / 2.0
        diff_width = img.width - params.width
        diff_height = img.height - params.height
        self.image_path = params.image_path
        self.color = params.color

        if params.scale_type == ImageScaleType.CROP:
            # Handle image cropping
            if diff_width > 0 and diff_height > 0:
                img = img.get_region(
                    center_x, center_y, params.width, params.height
                )
            elif diff_width > 0:
                img = img.get_region(
                    center_x, center_y, params.width, img.height
                )
            elif diff_height > 0:
                img = img.get_region(
                    center_x, center_y, img.width, params.height
                )
        elif params.scale_type == ImageScaleType.FIT:
            # Handle image fitting
            if diff_width > 0 or diff_height > 0:
                pudu_ui.utils.fit_screen(
                    params.width, params.height, img.width, img.height
                )
        else:
            # Handle image filling
            img.width = params.width
            img.height = params.height

        self.sprite = Sprite(
            img, x=params.x, y=params.y, batch=batch, group=group
        )

    def recompute(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.color = self.color
        # Not handling image change after init for now
