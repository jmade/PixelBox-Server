# Color Helpers
RESET="\x1b[0;0m"
GREEN="\x1b[1;32m"
BOLD="\x1b[1m"
BLUE="\x1b[34m"
YELLOW="\x1b[93m"

# from colors import lighter, darker

from colorsys import rgb_to_hls, hls_to_rgb

def lighter(rgb,percentage=0.10):
    return lighten_color(rgb[0], rgb[1], rgb[2],percentage)

def darker(rgb,percentage=0.10):
    return darken_color(rgb[0], rgb[1], rgb[2],percentage)

def lighten_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 + factor)

def darken_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 - factor)

def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

