#version 330

uniform float thickness;
uniform vec3 color;
uniform float opacity;
uniform float width;
uniform float height;
uniform vec2 position;

const int NUM_SAMPLES = 3;

out vec4 final_color;

void main() {
    vec2 pos = gl_FragCoord.xy;

    // Use positions relative to the widget local coordinates
    float x = pos.x - position.x;
    float y = pos.y - position.y;

    float TOTAL_SAMPLES = float(NUM_SAMPLES * NUM_SAMPLES);
    float total_opacity = 0.0;

    float w0 = width / 2.0;
    float h0 = height;
    float w1 = (w0 + thickness);
    float h1 = (h0 / w0) * w1;

    for (int j = 0; j < NUM_SAMPLES; j++) {
        for (int i = 0; i < NUM_SAMPLES; i++) {
            float sample_x = -0.5 + x + float(i) / float(NUM_SAMPLES);
            float sample_y = -0.5 + y + float(j) / float(NUM_SAMPLES);

            if (sample_x < w0) {
                // Left
                vec2 pa = vec2(0.0, h0);
                vec2 pb = vec2(w0, 0.0);
                vec2 d = pb - pa;
                vec2 n = normalize(vec2(-d.y, d.x));
                vec2 pap = vec2(0.0, h1);

                vec2 p = vec2(sample_x, sample_y);

                if (dot(n, p - pa) > 0.0 && dot(n, p - pap) <= 0.0) {
                    total_opacity += 1.0 / TOTAL_SAMPLES;
                }
            } else {
                // Right
                vec2 pa = vec2(0.0, 0.0);
                vec2 pb = vec2(w0, h0);
                vec2 d = pb - pa;
                vec2 n = normalize(vec2(-d.y, d.x));
                vec2 pap = vec2(-thickness, 0.0);

                vec2 p = vec2(sample_x - w0, sample_y);

                if (dot(n, p - pa) > 0.0 && dot(n, p - pap) <= 0.0) {
                    total_opacity += 1.0 / TOTAL_SAMPLES;
                }
            }
        }
    }

    vec4 calculated_color = vec4(color, total_opacity);
    if (calculated_color.a == 0.0) {
        discard;
    }

    final_color = calculated_color * vec4(1.0, 1.0, 1.0, opacity);
}