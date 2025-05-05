#version 330

uniform float left;
uniform float right;
uniform float bottom;
uniform float top;
uniform float radius_v3; // top-left
uniform float radius_v2; // top-right
uniform float radius_v0; // bottom-left
uniform float radius_v1; // bottom-right
uniform int highlight_width;
uniform vec3 highlight_color;
uniform vec2 pos_v3;
uniform vec2 pos_v2;
uniform vec2 pos_v0;
uniform vec2 pos_v1;

uniform float opacity;

in vec3 frag_color;
out vec4 final_color;

const float MAX_DIFF = 1.414213;

vec3 color_rounded_corner(vec2 pos, vec2 center, float radius) {
    float dist = distance(pos, center);
    if (dist > radius) {
        discard;
    } else if (dist > (radius - highlight_width)) {
        return highlight_color;
    } else {
        return frag_color;
    }
}


void main() {
    vec2 pos = gl_FragCoord.xy;
    vec3 color;
    float middle_y = max(radius_v0, radius_v1);
    float middle_left = max(radius_v0, radius_v3);
    float middle_right = max(radius_v1, radius_v2);

    // Segment top left
    if (
        pos_v3.x - radius_v3 <= pos.x &&
        pos.x <= pos_v3.x &&
        pos_v3.y <= pos.y &&
        pos.y <= pos_v3.y + radius_v3
    ) {
        color = color_rounded_corner(pos, pos_v3, radius_v3);
    // Segment top center
    } else if (
        pos.x > pos_v3.x && pos.x < pos_v2.x && pos.y > (top - highlight_width)
    ) {
        color = highlight_color;
    // Segment top right
    } else if (
        pos_v2.x <= pos.x &&
        pos.x <= pos_v2.x + radius_v2 &&
        pos_v2.y <= pos.y &&
        pos.y <= pos_v2.y + radius_v2
    ) {
        color = color_rounded_corner(pos, pos_v2, radius_v2);
    // Segment middle left
    } else if (
        pos.y > middle_y &&
        pos.x <= middle_left
    ) {
        if (pos.x - left <= highlight_width) {
            color = highlight_color;
        } else {
            color = frag_color;
        }
    } else if (pos_v0.x - radius_v0 <= pos.x && pos.x <= pos_v0.x) {
        if (pos_v0.y - radius_v0 <= pos.y && pos.y <= pos_v0.y) {
            color = color_rounded_corner(pos, pos_v0, radius_v0);
        }
    } else if (pos_v1.x <= pos.x && pos.x <= pos_v1.x + radius_v1) {
        if (pos_v1.y - radius_v1 <= pos.y && pos.y <= pos_v1.y) {
            color = color_rounded_corner(pos, pos_v1, radius_v1);
        }
    }

    final_color = vec4(color, opacity);
}
