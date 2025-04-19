#version 330

uniform float border_width;
uniform vec3 color;
uniform float x;
uniform float y;
uniform int width;
uniform int height;

out vec4 final_color;


bool in_top_row(vec2 pos) {
    return ((height - border_width) <= pos.y && pos.y <= height);
}

bool in_left_col(vec2 pos) {
    return (0 <= pos.x && pos.x <= border_width);
}

bool in_bottom_row(vec2 pos) {
    return (0 <= pos.y && pos.y <= border_width);
}

bool in_right_col(vec2 pos) {
    return (width - border_width <= pos.x && pos.x <= width);
}


void main() {
    vec2 pos = vec2(gl_FragCoord.x - x, gl_FragCoord.y - y);

    if (in_left_col(pos) || in_right_col(pos)) {
        final_color = vec4(color, 1.0);
    } else {
        if (in_top_row(pos) || in_bottom_row(pos)) {
            final_color = vec4(color, 1.0);
        } else {
            discard;
        }
    }
}
