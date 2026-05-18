#version 330 core

uniform WindowBlock {
    mat4 projection;
    mat4 view;
} window;

in vec2 position;
in vec4 vertex_color;

out vec3 frag_color;
out float opacity;

void main() {
    frag_color = vertex_color.rgb;
    opacity = vertex_color.a;
    gl_Position = window.projection * window.view * vec4(position, 1, 1);
}
