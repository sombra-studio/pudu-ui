#version 330

uniform float radius_v3; // top-left
uniform float radius_v2; // top-right
uniform float radius_v0; // bottom-left
uniform float radius_v1; // bottom-right
uniform int border_width;
uniform vec3 border_color;
uniform float opacity;
uniform float right_opacity;
uniform vec3 left_color;
uniform vec3 right_color;
uniform float limit_x;
uniform vec2 position;
uniform int width;
uniform int height;

in vec3 frag_color;
out vec4 final_color;

const int NUM_SAMPLES = 4;
const float SAMPLE_AREA_DISTANCE = 1;

vec4 progress_color(vec2 pos) {
    vec4 color;
    if (pos.x < position.x + limit_x) {
        color = vec4(frag_color * left_color, opacity);
    } else {
        color = vec4(frag_color * right_color, right_opacity);
    }
    return color;
}

vec4 color_rounded_corner(vec2 pos, vec2 center, float radius) {
    float dist = distance(pos, center);

    if (dist > radius + 2 * SAMPLE_AREA_DISTANCE) {
        discard;
    } else {
        vec4 color = vec4(0.0);
        int TOTAL_SAMPLES = NUM_SAMPLES * NUM_SAMPLES;
        vec4 sample_color = vec4(0.0);
        float sample_opacity = 0.0;
        for (int j = 0; j < NUM_SAMPLES; j++) {
            for (int i = 0; i < NUM_SAMPLES; i++) {
                vec2 sample_pos = pos + vec2(
                    (
                        -SAMPLE_AREA_DISTANCE / 2.0 +
                        SAMPLE_AREA_DISTANCE * i / NUM_SAMPLES
                    ),
                    (
                        -SAMPLE_AREA_DISTANCE / 2.0 +
                        SAMPLE_AREA_DISTANCE * j / NUM_SAMPLES
                    )
                );
                float sample_dist = distance(sample_pos, center);
                if (sample_dist > radius) {
                    // Out of the circle
                    continue;
                } else if (sample_dist > (radius - border_width)) {
                    // Inside the border
                    sample_color = vec4(border_color, opacity);
                    sample_opacity += 1.0 / TOTAL_SAMPLES;
                } else {
                    // Inside the circle
                    sample_color = progress_color(pos);
                    sample_opacity += 1.0 / TOTAL_SAMPLES;
                }

            }
        }
        sample_color.a = sample_opacity;
        color = sample_color;
        return color;
    }
}


void main() {
    vec4 color;
    vec2 pos_v0 = position + vec2(radius_v0, radius_v0);
    vec2 pos_v1 = position + vec2(width - radius_v1, radius_v1);
    vec2 pos_v2 = position + vec2(width - radius_v2, height - radius_v2);
    vec2 pos_v3 = position + vec2(radius_v3, height - radius_v3);
    float left = position.x;
    float right = position.x + width;
    float top = position.y + height;
    float bottom = position.y;
    vec2 pos = gl_FragCoord.xy;

    // Corner top left
    if (
        pos_v3.x - radius_v3 <= pos.x &&
        pos.x <= pos_v3.x &&
        pos_v3.y <= pos.y &&
        pos.y <= pos_v3.y + radius_v3
    ) {
        color = color_rounded_corner(pos, pos_v3, radius_v3);
    // Corner top right
    } else if (
        pos_v2.x <= pos.x &&
        pos.x <= pos_v2.x + radius_v2 &&
        pos_v2.y <= pos.y &&
        pos.y <= pos_v2.y + radius_v2
    ) {
        color = color_rounded_corner(pos, pos_v2, radius_v2);
    // Corner bottom left
    } else if (
        pos_v0.x - radius_v0 <= pos.x &&
        pos.x <= pos_v0.x &&
        pos_v0.y - radius_v0 <= pos.y &&
        pos.y <= pos_v0.y
    ) {
        color = color_rounded_corner(pos, pos_v0, radius_v0);
    // Corner bottom right
    } else if (
        pos_v1.x <= pos.x &&
        pos.x <= pos_v1.x + radius_v1 &&
        pos_v1.y - radius_v1 <= pos.y &&
        pos.y <= pos_v1.y
    ) {
        color = color_rounded_corner(pos, pos_v1, radius_v1);
    } else {
        // Inner rectangle
        if (
            pos.x > left + border_width &&
            pos.x < right - border_width &&
            pos.y > bottom + border_width &&
            pos.y < top - border_width
        ) {
            color = progress_color(pos);
        // outer rectangle
        } else {
            color = vec4(border_color, opacity);
        }
    }
    if (color.a == 0.0) discard;
    final_color = color;
}
