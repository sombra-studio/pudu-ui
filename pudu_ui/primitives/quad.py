from pyglet.graphics.vertexdomain import IndexedVertexList
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.math import Vec2
import pyglet
from collections.abc import Sequence


from pudu_ui import Color
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
        group: pyglet.graphics.Group = None
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

        self.data = {}
        self.set_data()
        self.set_uniforms()

        self.vertex_list = self.create_vertex_list(self.indices, **self.data)

    def create_vertex_list(self, indices, **data) -> IndexedVertexList:
        group = pyglet.graphics.ShaderGroup(
            self.program, parent=self.group
        )
        vertex_list = self.program.vertex_list_indexed(
            count=NUM_VERTICES,
            mode=pyglet.gl.GL_TRIANGLES,
            indices=indices,
            batch=self.batch,
            # TODO: FIX ERROR WITH GIVING A GROUP
            group=group,
            **data
        )
        return vertex_list

    def get_vertices(self) -> Sequence[float]:
        x = self.x
        y = self.y
        x2 = x + self.width
        y2 = y + self.height
        vertices = (x, y, x2, y, x2, y2, x, y2)
        return vertices

    def recompute(self):
        self.set_data()
        self.set_uniforms()
        self.vertex_list.position[:] = self.data['position'][1]
        self.vertex_list.vertex_color[:] = self.data['vertex_color'][1]

    def set_data(self):
        # Set position
        self.data['position'] = ('f', self.get_vertices())

        # Set vertex color
        vertex_color = []
        for color in self.colors:
            vertex_color += [color.r, color.g, color.b]
        self.data['vertex_color'] = ('Bn', vertex_color)

    def set_uniforms(self):
        self.program['opacity'] = self.opacity / 255.0
        self.program['radius_v3'] = self.radius_top_left
        self.program['radius_v2'] = self.radius_top_right
        self.program['radius_v0'] = self.radius_bottom_left
        self.program['radius_v1'] = self.radius_bottom_right
        self.program['pos_v3'] = Vec2(
            self.x + self.radius_top_left,
            self.y + self.height - self.radius_top_left
        )
        self.program['pos_v2'] = Vec2(
            self.x + self.width - self.radius_top_right,
            self.y + self.height - self.radius_top_right
        )
        self.program['pos_v0'] = Vec2(
            self.x + self.radius_bottom_left,
            self.y + self.radius_bottom_left
        )
        self.program['pos_v1'] = Vec2(
            self.x + self.width - self.radius_bottom_right,
            self.y + self.radius_bottom_right
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

    def set_data(self):
        super().set_data()
        tex_coords = (0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0)
        self.data['tex_coords'] = ('f', tex_coords)

    def recompute(self):
        super().recompute()
        self.vertex_list.tex_coords[:] = self.data['tex_coords'][1]
