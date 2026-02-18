import pyglet


def create_color_img(
    width: int, height: int, color: tuple[int, int, int, int]
):
    color_pattern = pyglet.image.SolidColorImagePattern(color)
    img = color_pattern.create_image(width, height)
    return img


def create_black_img(width: int, height: int):
    return create_color_img(width, height, (0, 0, 0, 255))


def create_white_img(width: int, height: int):
    return create_color_img(width, height, (255, 255, 255, 255))


def create_gray_img(width: int, height: int):
    return create_color_img(width, height, (123, 123, 123, 255))


def get_grid_pos_from_idx(index: int, columns: int) -> tuple[int, int]:
    j = index // columns
    i = index % columns
    return j, i


def fit_screen(
    screen_width: int, screen_height: int, w0: int, h0: int
) -> tuple[int, int]:
    """
    Fit the screen by returning new width and height. Calculate the width if the
    screen height is used, and the height if the screen width is used, and use
    the one that fits.
    """
    h1 = int((screen_width / w0) * h0)
    w1 = int((screen_height / h0) * w0)
    if h1 <= screen_height:
        return screen_width, h1
    return w1, screen_height
