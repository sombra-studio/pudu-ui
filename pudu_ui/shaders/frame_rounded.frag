#version 330

uniform float radius_v3; // top-left
uniform float radius_v2; // top-right
uniform float radius_v0; // bottom-left
uniform float radius_v1; // bottom-right
uniform vec2 pos_v3;
uniform vec2 pos_v2;
uniform vec2 pos_v0;
uniform vec2 pos_v1;

uniform float opacity;

in vec3 frag_color;
out vec4 final_color;


void main() {
    vec2 pos = gl_FragCoord.xy;
    if (pos_v3.x - radius_v3 <= pos.x && pos.x <= pos_v3.x) {
        if (pos_v3.y <= pos.y && pos.y <= pos_v3.y + radius_v3) {
            // check outside of top-left circle
            if (distance(pos, pos_v3) > radius_v3) {
                discard;
            }
        }
    }

    if (pos_v2.x <= pos.x && pos.x <= pos_v2.x + radius_v2) {
        if (pos_v2.y <= pos.y && pos.y <= pos_v2.y + radius_v2) {
            // check outside of top-right circle
            if (distance(pos, pos_v2) > radius_v2) {
                discard;
            }
        }
    }

    if (pos_v0.x - radius_v0 <= pos.x && pos.x <= pos_v0.x) {
        if (pos_v0.y - radius_v0 <= pos.y && pos.y <= pos_v0.y) {
            // check outside of bottom-left circle
            if (distance(pos, pos_v0) > radius_v0) {
                discard;
            }
        }
    }

    if (pos_v1.x <= pos.x && pos.x <= pos_v1.x + radius_v1) {
        if (pos_v1.y - radius_v1 <= pos.y && pos.y <= pos_v1.y) {
            // check outside of bottom-right circle
            if (distance(pos, pos_v1) > radius_v1) {
                discard;
            }
        }
    }

    final_color = vec4(frag_color, opacity);
}
