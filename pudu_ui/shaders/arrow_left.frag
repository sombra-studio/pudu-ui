#version 330


uniform float thickness;
uniform vec3 color;
uniform float opacity;
uniform float width;
uniform float height;
uniform vec2 position;


out vec4 final_color;


bool is_inside_top_triangle(float x, float y) {
    float triangle_ratio = (height / 2) / width;
    float triangle_line = x * triangle_ratio;
    if (height / 2 - y > triangle_line) {
        return false;
    }
    return true;
}

bool is_inside_bottom_triangle(float x, float y) {
    float triangle_ratio = (height / 2) / width;
    float triangle_line = x * triangle_ratio;
    if (y > triangle_line) {
        return true;
    }
    return false;
}

void main() {
    vec2 pos = gl_FragCoord.xy;
    // Use positions relative to the widget local coordinates
    float x = pos.x - position.x;
    float y = pos.y - position.y;
    if (y > height / 2.0) {
        // Top half
        if (is_inside_bottom_triangle(x, y)) {
            final_color = vec4(color, opacity);
        } else {
            final_color = vec4(0.0, 0.0, 1.0, 1.0);
        }

    } else {
        // Bottom half
        if (is_inside_bottom_triangle(x, y)) {
            final_color = vec4(color, opacity);
        } else {
            final_color = vec4(0.0, 0.0, 1.0, 1.0);
        }
    }
}
