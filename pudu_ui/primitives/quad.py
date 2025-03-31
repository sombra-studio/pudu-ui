from pyglet.graphics.vertexdomain import IndexedVertexList
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.math import Vec2
import pyglet
from collections.abc import Sequence


from pudu_ui import Color, Widget
import pudu_ui


DEFAULT_BORDER_RADIUS = 24
NUM_VERTICES = 4


with open("pudu_ui/shaders/quad.vert") as f:
    default_vertex_src = f.read()

with open("pudu_ui/shaders/textured.vert") as f:
    textured_vertex_src = f.read()

with open("pudu_ui/shaders/frame_rounded.frag") as f:
    rounded_fragment_src = f.read()

with open("pudu_ui/shaders/frame_textured.frag") as f:
    textured_fragment_src = f.read()

default_vs = Shader(default_vertex_src, 'vertex')
textured_vs = Shader(textured_vertex_src, 'vertex')
rounded_fs = Shader(rounded_fragment_src, 'fragment')
textured_fs = Shader(textured_fragment_src, 'fragment')


def rounded_program():
    return ShaderProgram(default_vs, rounded_fs)

def textured_program():
    return ShaderProgram(textured_vs, textured_fs)


default_colors = (
    pudu_ui.colors.BLACK, pudu_ui.colors.BLACK,
    pudu_ui.colors.PURPLE, pudu_ui.colors.PURPLE
)


default_textured_colors = (
    pudu_ui.colors.WHITE, pudu_ui.colors.WHITE,
    pudu_ui.colors.WHITE, pudu_ui.colors.WHITE
)


class Quad:
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        colors: tuple[Color, Color, Color, Color] = default_colors,
        opacity: float = 255,
        radius_top_left: float = DEFAULT_BORDER_RADIUS,
        radius_top_right: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_left: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_right: float = DEFAULT_BORDER_RADIUS,
        program: pyglet.graphics.shader.ShaderProgram = None,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None,
        parent: Widget | None = None
    ):
        self.x: float = x
        self.y: float = y
        self.width: int = width
        self.height: int = height
        self.indices = (0, 1, 2, 0, 2, 3)
        self.opacity = opacity
        self.colors = colors
        self.radius_top_left = radius_top_left
        self.radius_top_right = radius_top_right
        self.radius_bottom_left = radius_bottom_left
        self.radius_bottom_right = radius_bottom_right
        if not program:
            program = rounded_program()
        self.program: pyglet.graphics.shader.ShaderProgram = program
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
        self.parent = parent

        self.attributes = {}
        self.set_attributes()
        self.set_uniforms()

        self.vertex_list = self.create_vertex_list(
            self.indices, **self.attributes
        )

    def create_vertex_list(self, indices, **attributes) -> IndexedVertexList:
        group = pyglet.graphics.ShaderGroup(
            self.program, parent=self.group
        )
        vertex_list = self.program.vertex_list_indexed(
            count=NUM_VERTICES,
            mode=pyglet.gl.GL_TRIANGLES,
            indices=indices,
            batch=self.batch,
            group=group,
            **attributes
        )
        return vertex_list

    def get_position(self)  -> tuple[float, float]:
        if self.parent:
            x_offset, y_offset = self.parent.get_position()
        else:
            x_offset = 0.0
            y_offset = 0.0
        x = self.x + x_offset
        y = self.y + y_offset
        return x, y

    def get_vertices(self) -> Sequence[float]:
        x, y = self.get_position()
        x2 = x + self.width
        y2 = y + self.height
        vertices = (x, y, x2, y, x2, y2, x, y2)
        return vertices

    def recompute(self):
        self.set_attributes()
        self.set_uniforms()
        self.vertex_list.position[:] = self.attributes['position'][1]
        self.vertex_list.vertex_color[:] = self.attributes['vertex_color'][1]

    def set_attributes(self):
        # Set position
        self.attributes['position'] = ('f', self.get_vertices())

        # Set vertex color
        vertex_color = []
        for color in self.colors:
            vertex_color += [color.r, color.g, color.b]
        self.attributes['vertex_color'] = ('Bn', vertex_color)

    def set_uniforms(self):
        self.program['opacity'] = self.opacity / 255.0
        self.program['radius_v3'] = self.radius_top_left
        self.program['radius_v2'] = self.radius_top_right
        self.program['radius_v0'] = self.radius_bottom_left
        self.program['radius_v1'] = self.radius_bottom_right

        x, y = self.get_position()

        left = x
        right = left + self.width
        bottom = y
        top = bottom + self.height

        self.program['pos_v3'] = Vec2(
            left + self.radius_top_left,
            top - self.radius_top_left
        )
        self.program['pos_v2'] = Vec2(
            right - self.radius_top_right,
            top - self.radius_top_right
        )
        self.program['pos_v0'] = Vec2(
            left + self.radius_bottom_left,
            bottom + self.radius_bottom_left
        )
        self.program['pos_v1'] = Vec2(
            right - self.radius_bottom_right,
            bottom + self.radius_bottom_right
        )


class TexturedQuad(Quad):
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        colors: tuple[Color, Color, Color, Color] = default_textured_colors,
        opacity: float = 255,
        radius_top_left: float = 0,
        radius_top_right: float = 0,
        radius_bottom_left: float = 0,
        radius_bottom_right: float = 0,
        program: pyglet.graphics.shader.ShaderProgram = None,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None
    ):
        if not program:
            program = textured_program()
        self.program: pyglet.graphics.shader.ShaderProgram = program
        super().__init__(
            x, y, width, height,
            colors=colors, opacity=opacity, radius_top_left=radius_top_left,
            radius_top_right=radius_top_right,
            radius_bottom_left=radius_bottom_left,
            radius_bottom_right=radius_bottom_right,
            program=program,
            batch=batch,
            group=group
        )

    def set_attributes(self):
        super().set_attributes()
        tex_coords = (0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0)
        self.attributes['tex_coords'] = ('f', tex_coords)

    def recompute(self):
        super().recompute()
        self.vertex_list.tex_coords[:] = self.attributes['tex_coords'][1]
