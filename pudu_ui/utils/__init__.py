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
