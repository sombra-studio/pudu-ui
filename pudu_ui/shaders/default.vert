#version 330 core

in vec2 position;

uniform WindowBlock {
    mat4 projection;
    mat4 view;
} window;

void main() {
    gl_Position = window.projection * window.view * vec4(position, 1, 1);
}
