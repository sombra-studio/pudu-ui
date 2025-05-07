#version 330

uniform sampler2D texture_map;
uniform float opacity;

in vec3 frag_color;
in vec2 frag_tex_coords;
out vec4 final_color;


void main() {
    vec4 tex_color = texture(texture_map, frag_tex_coords);
    vec4 final_color = tex_color * vec4(frag_color, opacity);
}
