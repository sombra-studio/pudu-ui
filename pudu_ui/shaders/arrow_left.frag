#version 330


uniform float thickness;
uniform float opacity;
uniform int width;
uniform int height;


in vec3 frag_color;
out vec4 final_color;


bool is_inside_top_triangle(float x, float y) {
    float triangle_ratio = (height / 2.0) / width;
    float triangle_line = x * triangle_ratio;
    if (y - height / 2.0 > triangle_line) {
        return false;
    }
    return true;
}

bool is_inside_bottom_triangle(float x, float y) {
    float triangle_ratio = (height / 2.0) / width;
    float triangle_line = x * triangle_ratio;
    if (y > triangle_line) {
        return true;
    }
    return false;
}

void main() {

    vec2 pos = gl_FragCoord.xy;
    if (pos.y > height / 2.0) {
        // Top half
        if (is_inside_bottom_triangle(pos.x, pos.y)) {

        }

    } else {
        // Bottom half
    }


    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
