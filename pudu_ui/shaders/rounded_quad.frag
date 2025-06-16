#version 330

uniform float radius_v3; // top-left
uniform float radius_v2; // top-right
uniform float radius_v0; // bottom-left
uniform float radius_v1; // bottom-right
uniform int border_width;
uniform vec3 border_color;
uniform float opacity;
uniform vec2 position;
uniform int width;
uniform int height;

in vec3 frag_color;
out vec4 final_color;

const int NUM_SAMPLES = 4;

bool is_inside_box(vec2 box_origin, vec2 pos, float side) {
    return (
        pos.x >= box_origin.x &&
        pos.x - box_origin.x <= side &&
        pos.y >= box_origin.y &&
        pos.y - box_origin.y <= side
    );
}

vec4 color_rounded_corner(vec2 pos, vec2 center, float radius) {
    vec2 pixel_center = pos + vec2(0.5, 0.5);
    float dist = distance(pixel_center, center);

    if (dist > radius + 2.0) {
        discard;
    } else {
        bool is_border = false;
        if (dist > (radius - border_width)) {
            is_border = true;
        }

        // Use multi sample anti-aliasing to calculate opacity
        const int TOTAL_SAMPLES = NUM_SAMPLES * NUM_SAMPLES;
        vec4 color = vec4(0.0);

        for (int j = 0; j < NUM_SAMPLES; j++) {
            for (int i = 0; i < NUM_SAMPLES; i++) {
                vec2 sample_pos = pos + vec2(
                    (i / NUM_SAMPLES), (j / NUM_SAMPLES)
                );
                float sample_dist = distance(sample_pos, center);
                if (sample_dist > radius) {
                    // Out of the circle
                    continue;
                } else {
                    // Inside the circle
                    if (sample_dist > (radius - border_width)) {
                        // Inside the border
                        color += vec4(border_color, 1.0) / TOTAL_SAMPLES;
                    } else {
                        // Inside the circle
                        color += vec4(frag_color, 1.0) / TOTAL_SAMPLES;
                    }
                }
            }   // for each sample column
        }   // for each sample row

        return color;
    }
}


void main() {
    vec4 color;
    float left = position.x;
    float right = position.x + width;
    float top = position.y + height;
    float bottom = position.y;
    vec2 box3_origin = vec2(left, top - radius_v3);
    vec2 box2_origin = vec2(right - radius_v2, top - radius_v2);
    vec2 box1_origin = vec2(right - radius_v0, bottom);
    vec2 box0_origin = vec2(left, bottom);
    vec2 pos = gl_FragCoord.xy;

    // Corner top left
    if (is_inside_box(box3_origin, pos, radius_v3)) {
        vec2 center = vec2(box3_origin.x + radius_v3, box3_origin.y);
        color = color_rounded_corner(pos, center, radius_v3);
    // Corner top right
    } else if (is_inside_box(box2_origin, pos, radius_v2)) {
        vec2 center = box2_origin;
        color = color_rounded_corner(pos, center, radius_v2);
    // Corner bottom left
    } else if (is_inside_box(box0_origin, pos, radius_v0)) {
        vec2 center = vec2(
            box0_origin.x + radius_v0, box0_origin.y + radius_v0
        );
        color = color_rounded_corner(pos, center, radius_v0);
    // Corner bottom right
    } else if (is_inside_box(box1_origin, pos, radius_v1)) {
        vec2 center = vec2(box1_origin.x, box1_origin.y + radius_v1);
        color = color_rounded_corner(pos, center, radius_v1);
    } else {
        // Inner rectangle
        if (
            pos.x > left + border_width &&
            pos.x < right - border_width &&
            pos.y > bottom + border_width &&
            pos.y < top - border_width
        ) {
            color = vec4(frag_color, 1.0);
        // outer rectangle
        } else {
            color = vec4(border_color, 1.0);
        }
    }

    if (color.a == 0.0) discard;
    final_color = color * vec4(1.0, 1.0, 1.0, opacity);
}
