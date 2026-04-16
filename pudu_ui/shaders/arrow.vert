#version 330 core

uniform WindowBlock {
    mat4 projection;
    mat4 view;
} window;

in vec2 position;

void main() {
    gl_Position = window.projection * window.view * vec4(position, 1, 1);
}
