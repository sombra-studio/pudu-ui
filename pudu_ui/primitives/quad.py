from pyglet.graphics.vertexdomain import IndexedVertexList
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.math import Vec2, Vec3
import pyglet
from collections.abc import Sequence
from importlib.resources import files

from pudu_ui import Color
import pudu_ui


NUM_VERTICES = 4
DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 50
DEFAULT_BORDER_RADIUS = DEFAULT_HEIGHT / 2.0

default_vertex_src = files('pudu_ui.shaders').joinpath('quad.vert').read_text()
textured_vertex_src = files('pudu_ui.shaders').joinpath(
    'textured.vert'
).read_text()
rounded_fragment_src = files('pudu_ui.shaders').joinpath(
    'rounded_quad.frag'
).read_text()
progress_fragment_src = files('pudu_ui.shaders').joinpath(
    'progress_quad.frag'
).read_text()
textured_fragment_src = files('pudu_ui.shaders').joinpath(
    'textured_quad.frag'
).read_text()

default_vs = Shader(default_vertex_src, 'vertex')
textured_vs = Shader(textured_vertex_src, 'vertex')
rounded_fs = Shader(rounded_fragment_src, 'fragment')
progress_fs = Shader(progress_fragment_src, 'fragment')
textured_fs = Shader(textured_fragment_src, 'fragment')


def rounded_program():
    return ShaderProgram(default_vs, rounded_fs)

def progress_program():
    return ShaderProgram(default_vs, progress_fs)

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


class SolidBordersQuad:
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        color: Color = pudu_ui.colors.DEBUG_BORDER_COLOR,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None,
        parent = None
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.parent = parent
        indices = (0, 1, 2, 0, 2, 3)

        vertex_src = files('pudu_ui.shaders').joinpath(
            'solid_borders.vert'
        ).read_text()
        fragment_src = files('pudu_ui.shaders').joinpath(
            'solid_borders.frag'
        ).read_text()
        vs = Shader(vertex_src, 'vertex')
        fs = Shader(fragment_src, 'fragment')
        self.program = pyglet.graphics.shader.ShaderProgram(
            vs, fs
        )
        self.attributes = {}
        self.set_attributes()
        self.set_uniforms()

        shader_group = pyglet.graphics.ShaderGroup(
           program=self.program, parent=group
        )
        self.vertex_list = self.program.vertex_list_indexed(
            count=NUM_VERTICES,
            mode=pyglet.gl.GL_TRIANGLES,
            indices=indices,
            batch=batch,
            group=shader_group,
            position=('f', self.get_vertices())
        )

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

    def set_attributes(self):
        # Set position
        self.attributes['position'] = ('f', self.get_vertices())

    def set_uniforms(self):
        self.program['border_width'] = 2.0
        self.program['color'] = Vec3(
            self.color.r / 255.0, self.color.g / 255.0, self.color.b / 255.0
        )
        x, y = self.get_position()
        self.program['x'] = x
        self.program['y'] = y
        self.program['width'] = self.width
        self.program['height'] = self.height


class Quad:
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        colors: tuple[Color, Color, Color, Color] = default_colors,
        opacity: float = 255,
        radius_top_left: float = DEFAULT_BORDER_RADIUS,
        radius_top_right: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_left: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_right: float = DEFAULT_BORDER_RADIUS,
        border_width: int = 3,
        border_color: Color = pudu_ui.colors.WHITE,
        program: pyglet.graphics.shader.ShaderProgram = None,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None,
        parent = None
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
        self.border_width = border_width
        self.border_color = border_color
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
        self.program['position'] = Vec2(x, y)
        self.program['width'] = self.width
        self.program['height'] = self.height

        # Set highlight
        self.program['border_width'] = self.border_width
        border_color = Vec3(
            self.border_color.r,
            self.border_color.g,
            self.border_color.b
        )
        border_color /= 255
        self.program['border_color'] = border_color


class ProgressQuad(Quad):
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        left_color: Color = pudu_ui.colors.LIGHT_PURPLE,
        right_color: Color = pudu_ui.colors.LIGHTER_GRAY,
        opacity: float = 255,
        right_opacity: float = 255,
        radius_top_left: float = DEFAULT_BORDER_RADIUS,
        radius_top_right: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_left: float = DEFAULT_BORDER_RADIUS,
        radius_bottom_right: float = DEFAULT_BORDER_RADIUS,
        border_width: int = 0,
        border_color: Color = pudu_ui.colors.WHITE,
        limit_x: int = DEFAULT_WIDTH,
        program: pyglet.graphics.shader.ShaderProgram = None,
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None,
        parent=None
    ):
        if not program:
            program = progress_program()
        colors = (
            pudu_ui.colors.WHITE, pudu_ui.colors.WHITE,
            pudu_ui.colors.WHITE, pudu_ui.colors.WHITE
        )
        self.left_color = left_color
        self.right_color = right_color
        self.limit_x = x + limit_x
        self.right_opacity = right_opacity
        super().__init__(
            x=x, y=y, width=width, height=height,
            colors=colors, opacity=opacity,
            radius_top_left=radius_top_left,
            radius_top_right=radius_top_right,
            radius_bottom_left=radius_bottom_left,
            radius_bottom_right=radius_bottom_right,
            border_width=border_width,
            border_color=border_color,
            program=program,
            batch=batch,
            group=group,
            parent=parent
        )

    def set_uniforms(self):
        super().set_uniforms()
        self.program['left_color'] = self.left_color.as_vec3()
        self.program['right_color'] = self.right_color.as_vec3()
        self.program['limit_x'] = self.limit_x
        self.program['right_opacity'] = self.right_opacity / 255.0


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
        group: pyglet.graphics.Group = None,
        parent = None
    ):
        if not program:
            program = textured_program()
        self.program: pyglet.graphics.shader.ShaderProgram = program
        super().__init__(
            x=x, y=y, width=width, height=height,
            colors=colors, opacity=opacity,
            radius_top_left=radius_top_left,
            radius_top_right=radius_top_right,
            radius_bottom_left=radius_bottom_left,
            radius_bottom_right=radius_bottom_right,
            program=program,
            batch=batch,
            group=group,
            parent=parent
        )

    def set_attributes(self):
        super().set_attributes()
        tex_coords = (0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0)
        self.attributes['tex_coords'] = ('f', tex_coords)

    def recompute(self):
        super().recompute()
        self.vertex_list.tex_coords[:] = self.attributes['tex_coords'][1]
