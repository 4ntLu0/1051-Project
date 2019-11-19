from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, \
    create_image, show, save_as
import os


def betterEdgeDetect( image: Image, thresh: int = 0, disp: bool = True, save: bool = True ):
    """
    Written by Anthony Luo
    :param image: Image to detect edges on
    :param thresh: Threshold value for detection
    :return: edge-y boi image.
    """
    # functional definitions
    width = get_width(image)
    height = get_height(image)
    new_image = create_image(width, height)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)

    for y in range(height - 1):  # starts at the first level, then moves down
        for x in range(width - 1):
            # compares brightness between two images and then resets colours.
            if abs(_avgBright(tuple(get_color(image, x, y))) - _avgBright(tuple(get_color(image, x, y + 1)))) > thresh \
                    or abs(_avgBright(tuple(get_color(image, x, y))) - _avgBright(
                tuple(get_color(image, x + 1, y)))) > thresh:
                set_color(new_image, x, y, black)  # sets colour to black (edge detected)
            else:
                set_color(new_image, x, y, white)  # sets colour to white (no edge)

    for x in range(width):
        # sets the last row of pixels to be equal to the one right above
        set_color(new_image, x, height - 1, _newCol(get_color(new_image, x, height - 2)))

    for y in range(height):
        # sets last column of pixels to be equal to the ones to the left
        set_color(new_image, width - 1, y, _newCol(get_color(new_image, width - 2, y)))

    # sets the colour for the last pixel
    if get_color(new_image, width - 2, height - 1) == create_color(0, 0, 0) or \
            get_color(new_image, width - 1, height - 2) == create_color(0, 0, 0):
        set_color(new_image, width - 1, height - 1, create_color(0, 0, 0))
    else:
        set_color(new_image, width - 1, height - 1, create_color(255, 255, 255))
    if disp:
        show(new_image)  # shows image
    if save:
        save_as(new_image, 'returns/better_edge_detect.png')  # saves to returns/
    return new_image


def _avgBright( colour ):
    '''Returns avg brightness of things
    written by anthony luo'''
    r, g, b = colour
    return (r + g + b) / 3


def _newCol( colour ):
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
    ret_img = betterEdgeDetect(load_image(choose_file()), 15)
