from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, create_image, show, save_as


def edgeDetect(image: Image, thresh: int = 0, disp: bool = True, save: bool = True):
    """
    Written by Anthony Luo (tentatively)
    :param image:
    :param thresh:
    :return:
    """
    width = get_width(image)
    height = get_height(image)
    new_image = create_image(width, height - 1)  # you lose one row of data.
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    for y in range(height - 1):  # starts at the first level, then moves down
        for x in range(width):
            if abs(avgBright(tuple(get_color(image, x, y))) - avgBright(tuple(get_color(image, x, y + 1)))) > thresh:
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)
    if disp:
        show(new_image)
    if save:
        save_as(new_image, 'returns/edge_detect.png')
    return new_image


def avgBright(colour):
    r, g, b = colour
    return (r + g + b) / 3


if __name__ == '__main__':
    edgeDetect(load_image(choose_file()), 12)
