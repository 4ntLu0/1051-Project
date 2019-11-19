from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, \
    create_image, show, save_as
import os


def edgeDetect( image: Image, thresh: int = 0, disp: bool = True, save: bool = True ):
    """
    Written by Anthony Luo
    :param image:
    :param thresh:
    :return:
    """
    # TODO: create padded image.
    # TODO: efficiency TMTM
    # functional definitions
    width = get_width(image)
    height = get_height(image)
    new_image = create_image(width, height)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    '''
    for x, y, (r, g, b) in image:
        if abs(_avgBright( (r,g,b) ) - _avgBright(tuple(get_color(image, x ,y + 1)))) > thresh \ 
            or abs(_avgBright (r, g, b)  - _avgBright(tuple(get_color(image, x + 1, y)))) > thresh:
            set_color(new_image, x, y, black)
        else: set_color(new_image, x, y, white)
    '''
    for y in range(height - 1):  # starts at the first level, then moves down
        for x in range(width - 1):
            # compares brightness between two images and then resets colours.
            if abs(_avgBright(tuple(get_color(image, x, y))) - _avgBright(tuple(get_color(image, x, y + 1)))) > thresh \
                    or \
                    abs(_avgBright(tuple(get_color(image, x, y))) - _avgBright(
                        tuple(get_color(image, x + 1, y)))) > thresh:
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)

    for x in range(width):
        # sets the last row of pixels.
        set_color(new_image, x, height - 1, _newCol(get_color(new_image, x, height - 2)))
    for y in range(height):
        set_color(new_image, width - 1, y, _newCol(get_color(new_image, width - 2, y)))
    if disp:
        show(new_image)  # shows image
    if save:
        save_as(new_image, 'returns/better_edge_detect.png')  # saves to returns/
    return new_image


def _avgBright( colour ):
    r, g, b = colour
    return (r + g + b) / 3


def _newCol( colour ):
    r, g, b = tuple(colour)
    return create_color(r, g, b)


if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
    ret_img = edgeDetect(load_image(choose_file()), 15)