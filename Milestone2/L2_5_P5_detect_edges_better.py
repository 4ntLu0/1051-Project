from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, \
    create_image, show, save_as
import os

'''
Written by Anthony Luo, Nov 20, 2019
Cimpl attributed from CuLearn, 2019.
'''

def detect_edges_better(img: Image, thresh: int = 0, disp: bool = True, save: bool = True):
    """ return an image with the edge detects.
    Written by Anthony Luo (#101145222)
    :param image: Image to detect edges on
    :param thresh: Threshold value for detection
    :return: edge detected image.
    >>> detect_edges_better(load_image(choose_file()), 13)
    >>> detect_edges_better(load_image(choose_file()), 15, False, True)
    """

    # functional definitions
    width = get_width(img)
    height = get_height(img)
    new_img = create_image(width, height)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)

    for y in range(height - 1):  # starts at the first level, then moves down
        for x in range(width - 1):
            # compares brightness between two images and then resets colours.
            if abs(_avg_bright(tuple(get_color(img, x, y))) - _avg_bright(tuple(get_color(img, x, y + 1)))) > thresh \
                    or abs(
                _avg_bright(tuple(get_color(img, x, y))) - _avg_bright(tuple(get_color(img, x + 1, y)))) > thresh:
                # sets colour to black (edge detected)
                set_color(new_img, x, y, black)
            else:
                # sets colour to white (no edge)
                set_color(new_img, x, y, white)

    for x in range(width):
        # sets the last row of pixels to be equal to the one right above
        set_color(new_img, x, height - 1,
                  _new_col(get_color(new_img, x, height - 2)))

    for y in range(height):
        # sets last column of pixels to be equal to the ones to the left
        set_color(new_img, width - 1, y,
                  _new_col(get_color(new_img, width - 2, y)))

    # sets the colour for the last pixel
    if get_color(new_img, width - 2, height - 1) == create_color(0, 0, 0) or \
            get_color(new_img, width - 1, height - 2) == create_color(0, 0, 0):
        set_color(new_img, width - 1, height - 1, create_color(0, 0, 0))
    else:
        set_color(new_img, width - 1, height -
                  1, create_color(255, 255, 255))
    if disp:
        show(new_img)  # shows image
    if save:
        # saves to returns/
        save_as(new_img, 'returns/better_edge_detect.png')
    return new_img


def _avg_bright(colour):
    '''Returns avg brightness of things
    written by anthony luo'''
    r, g, b = colour
    return (r + g + b) / 3


def _new_col(colour):
    ''' Returns a colour type from a colour
    written by Anthony Luo
    '''
    # TODO: try to see if there's a way to integrate this directly into the program
    r, g, b = tuple(colour)
    return create_color(r, g, b)


if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
    ret_img = detect_edges_better(load_image(choose_file()), 15)
