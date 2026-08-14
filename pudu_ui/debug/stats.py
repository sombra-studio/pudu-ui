import os
import psutil
from pudu_ui import Label, LabelParams, Params, Widget
from pudu_ui.styles.fonts import FontStyle
import pudu_ui
from pyglet.graphics import Batch, Group
from pyglet.window import FPSDisplay, Window


DEBUG_FONT_SIZE = 14
TIME_TO_UPDATE_DEBUG = 0.5
LABEL_Y_MARGIN = 22


class Stats(Widget):
    def __init__(
        self, window: Window, params: Params, batch: Batch, group: Group
    ):
        super().__init__(params=params, batch=batch, group=group)
        self.fps_display = FPSDisplay(
            window=window, color=(0, 127, 0, 127), batch=batch
        )
        self.fps_label = self.fps_display.label
        self.fps_label.position = (self.x, self.y, 0.0)
        self.fps_label.font_size = DEBUG_FONT_SIZE
        debug_label_style = FontStyle(
            font_size=DEBUG_FONT_SIZE,
            weight="bold",
            color=pudu_ui.colors.Color(0, 127, 0),
            opacity=127
        )

        label_params = LabelParams(
            x=0.0,
            y=LABEL_Y_MARGIN,
            text="hola",
            style=debug_label_style
        )
        self.memory_label = Label(
            params=label_params,
            batch=batch,
            group=group,
            parent=self
        )
        label_params.y += LABEL_Y_MARGIN
        self.tri_count_label = Label(
            params=label_params,
            batch=batch,
            group=group,
            parent=self
        )

        # Add children widgets
        self.children.append(self.memory_label)
        self.children.append(self.tri_count_label)

        self.batch = batch
        self.time_to_update_debug = TIME_TO_UPDATE_DEBUG
        self.process = psutil.Process(os.getpid())

    def draw(self):
        self.fps_display.draw()
        self.batch.draw()

    def update(self, dt: float):
        self.time_to_update_debug -= dt
        if self.time_to_update_debug <= 0:
            self.time_to_update_debug = TIME_TO_UPDATE_DEBUG
            ram_used = self.process.memory_info().rss / (1024 * 1024)  # in MB
            self.memory_label.text = f"{round(ram_used, 2)} MB"
            self.memory_label.invalidate()
            self.invalidate()

        super().update(dt)

    def set_tri_counts(self, tri_count: int):
        self.tri_count_label.text = f"{tri_count:,} triangles"
        self.tri_count_label.invalidate()
        self.invalidate()
