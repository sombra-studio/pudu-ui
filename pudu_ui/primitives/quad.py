from pyglet.graphics.shader import Shader, ShaderProgram
import pyglet


import pudu_ui


with open("shaders/default.vert") as f:
    default_vertex_src = f.read()

with open("shaders/frame.frag") as f:
    default_fragment_src = f.read()

with open("shaders/frame_rounded.frag") as f:
    rounded_fragment_src = f.read()

default_vs = Shader(default_vertex_src, 'vertex')
default_fs = Shader(default_fragment_src, 'fragment')
# rounded_fs = Shader(rounded_fragment_src, 'fragment')
default_program = ShaderProgram(default_vs, default_fs)
# rounded_program = ShaderProgram(default_vs, rounded_fs)


class Quad:
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        color: pudu_ui.Color,
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
        positions = (x, y, x2, y, x2, y2, x, y2)
        indices = (0, 1, 2, 0, 2, 3)
        self.program: pyglet.graphics.shader.ShaderProgram = program
        self.program['color'] = (
            color.r / 255.0, color.g / 255.0, color.b / 255.0, color.a / 255.0
        )
        self.batch: pyglet.graphics.Batch = batch
        self.group: pyglet.graphics.Group = group
        self.vertex_list = self.program.vertex_list_indexed(
            count=4,
            mode=pyglet.gl.GL_TRIANGLES,
            indices=indices,
            batch=batch,
            group=group,
            position=('f', positions)
        )

class RoundedQuad(Quad):
    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        color: pudu_ui.Color,
        radius_top_left: float,
        radius_top_right: float,
        radius_bottom_left: float,
        radius_bottom_right: float,
        program: pyglet.graphics.shader.ShaderProgram,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None
    ):
        pass



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
