#version 330

uniform float thickness;
uniform vec3 color;
uniform float opacity;
uniform float width;
uniform float height;
uniform float scale_x;
uniform float scale_y;
uniform vec2 position;

const int NUM_SAMPLES = 3;

out vec4 final_color;

bool is_inside_triangle(float x, float y, float w, float h) {
    float triangle_ratio = h / w;
    float triangle_line = x * triangle_ratio;
    if (y < triangle_line) {
        return true;
    }
    return false;
}

void main() {
    vec2 pos = gl_FragCoord.xy;
    // Use positions relative to the widget local coordinates
    float x = (pos.x - position.x) * scale_x;
    float y = (pos.y - position.y) * scale_y;
    float TOTAL_SAMPLES = NUM_SAMPLES * NUM_SAMPLES;
    float total_opacity = 0.0;
    // h1 is the height of the smaller triangle
    float w0 = (width / 2.0) * scale_x;
    float h0 = height * scale_y;
    float w1 = (w0 - thickness) * scale_x;
    float h1 = (w1 * (h0 / w0)) * scale_y;

    for (int j = 0; j < NUM_SAMPLES; j++) {
        for (int i = 0; i < NUM_SAMPLES; i++) {
            float sample_x = -0.5 + x + float(i) / NUM_SAMPLES;
            float sample_y = -0.5 + y + float(j) / NUM_SAMPLES;

            if (sample_x < width / 2.0) {
                // Left half
                if (
                    is_inside_triangle(sample_x, sample_y, w0, h0) &&
                    !is_inside_triangle(
                        sample_x - thickness, sample_y, w1, h1
                    )
                ) {
                    total_opacity += 1.0 / TOTAL_SAMPLES;
                }
            } else {
                // Right half
                float local_x = sample_x - (width / 2.0);
                if (
                    !is_inside_triangle(
                        local_x, h0 - sample_y, w0, h0
                    ) &&
                    is_inside_triangle(local_x, h1 - sample_y, w1, h1)
                ) {
                    total_opacity += 1.0 / TOTAL_SAMPLES;
                }
            }
        } // For i
    } // For j

    vec4 calculated_color = vec4(color, total_opacity);
    if (calculated_color.a == 0.0)
        discard;
    final_color = calculated_color * vec4(1, 1, 1, opacity);
}
