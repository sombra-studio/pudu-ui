#version 330 core

uniform WindowBlock {
    mat4 projection;
    mat4 view;
} window;

in vec2 position;
in vec4 vertex_color;
in vec2 tex_coords;

out vec3 frag_color;
out float opacity;
out vec2 frag_tex_coords;

void main() {
    frag_color = vertex_color.rgb;
    opacity = vertex_color.a;
    frag_tex_coords = tex_coords;
    gl_Position = window.projection * window.view * vec4(position, 1, 1);
}
