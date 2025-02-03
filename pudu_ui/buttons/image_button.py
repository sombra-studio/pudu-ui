from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from button import Button, ButtonParams
from pudu_ui.image import ImageParams, Image, default_image_params


@dataclass
class ImageButtonParams(ButtonParams):
    image_params: ImageParams = field(default_factory=default_image_params)



class ImageButton(Button):
    def __init__(
        self, params: ImageButtonParams, batch: Batch, group: Group
    ):
        super().__init__(params, batch=batch, group=group)
        self.image = Image(params.image_params, batch=batch, group=group)