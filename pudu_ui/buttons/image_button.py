from dataclasses import dataclass, field
from pyglet.graphics import Batch, Group


from pudu_ui.buttons import Button, ButtonParams
from pudu_ui.image import ImageParams, Image, default_image_params


@dataclass
class ImageButtonParams(ButtonParams):
    image_params: ImageParams = field(default_factory=default_image_params)


class ImageButton(Button):
    def __init__(
        self,
        params: ImageButtonParams,
        batch: Batch = None,
        group: Group = None
    ):
        super().__init__(params, batch=batch, group=group)
        self.image = Image(
            params.image_params, batch=batch, group=self.front_group
        )

    def update(self, dt: float):
        super().update(dt)
        self.image.update(dt)
