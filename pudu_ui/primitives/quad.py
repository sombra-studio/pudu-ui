from pyglet.graphics.vertexdomain import IndexedVertexList
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.math import Vec2
import pyglet


import pudu_ui


DEFAULT_BORDER_RADIUS = 12


with open("shaders/default.vert") as f:
    default_vertex_src = f.read()

with open("shaders/frame.frag") as f:
    default_fragment_src = f.read()

with open("shaders/frame_rounded.frag") as f:
    rounded_fragment_src = f.read()

default_vs = Shader(default_vertex_src, 'vertex')
default_fs = Shader(default_fragment_src, 'fragment')
rounded_fs = Shader(rounded_fragment_src, 'fragment')
default_program = ShaderProgram(default_vs, default_fs)
rounded_program = ShaderProgram(default_vs, rounded_fs)


class Quad:
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        program: pyglet.graphics.shader.ShaderProgram = default_program,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None
    ):
        self.x: float = x
        self.y: float = y
        self.width: int = width
        self.height: int = height
        x2 = x + width
        y2 = y + height
        self.positions = (x, y, x2, y, x2, y2, x, y2)
        indices = (0, 1, 2, 0, 2, 3)
        self.program: pyglet.graphics.shader.ShaderProgram = program
        self.data = {}
        self.set_data()
        self.set_uniforms()
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
        self.vertex_list = self.create_vertex_list(indices, **self.data)

    def set_data(self):
        self.data["position"] = ('f', self.positions)

    def create_vertex_list(self, indices, **data) -> IndexedVertexList:
        vertex_list = self.program.vertex_list_indexed(
            count=4,
            mode=pyglet.gl.GL_TRIANGLES,
            indices=indices,
            batch=self.batch,
            group=self.group,
            **data
        )
        return vertex_list

    def set_uniforms(self):
        pass


class SolidColorQuad(Quad):
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        color: pudu_ui.Color = pudu_ui.colors.PURPLE,
        opacity: float = 255,
        program: pyglet.graphics.shader.ShaderProgram = default_program,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None
    ):
        self.color = color
        self.opacity = opacity
        super().__init__(x, y, width, height, program, batch, group)

    def set_uniforms(self):
        color = self.color
        self.program['color'] = (
            color.r / 255.0, color.g / 255.0, color.b / 255.0,
            self.opacity / 255.0
        )


class RoundedSolidColorQuad(SolidColorQuad):
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        color: pudu_ui.Color = pudu_ui.colors.PURPLE,
        opacity: float = 255,
        radius_top_left: float = DEFAULT_BORDER_RADIUS,
        radius_top_right: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_left: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_right: float = DEFAULT_BORDER_RADIUS,
        program: pyglet.graphics.shader.ShaderProgram = rounded_program,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None
    ):
        self.radius_top_left = radius_top_left
        self.radius_top_right = radius_top_right
        self.radius_bottom_left = radius_bottom_left
        self.radius_bottom_right = radius_bottom_right
        super().__init__(
            x, y, width, height, color, opacity, program, batch, group
        )

    def set_uniforms(self):
        super().set_uniforms()
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

class TexturedQuad:
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        program: pyglet.graphics.shader.ShaderProgram,
        batch: pyglet.graphics.Batch,
        group: pyglet.graphics.Group
    ):
        self.x: float = x
        self.y: float = y
        self.width: int = width
        self.height: int = height
        x2 = x + width
        y2 = y + height
        positions = (x, y, x2, y, x2, y2, x, y2)
        tex_coords = (0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0)
        self.program: pyglet.graphics.shader.ShaderProgram = program
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
        self.vertex_list = self.program.vertex_list(
            count=4,
            mode=pyglet.gl.GL_TRIANGLES,
            batch=batch,
            group=group,
            positions=('f', positions),
            tex_coords=('f', tex_coords)
        )
