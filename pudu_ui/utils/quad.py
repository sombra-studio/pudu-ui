import pyglet


class Quad:
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
