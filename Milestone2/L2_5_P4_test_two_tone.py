from Cimpl import set_color, create_color, create_image, copy, get_color
from typing import NewType, Tuple
from L2_5_two_tone import twoTone

Image = NewType('Image', str)
from datetime import datetime

tones = ['black', 'white', 'red', 'lime', 'blue',
         'yellow', 'cyan', 'magenta', 'gray']
colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
           (255, 0, 255), (128, 128, 128)]


def testTwoTone():
    ''' Tests to ensure that two tone creates an image with the colours specified.
    Tests both ranges, both High (255, 255, 255) and Low (0, 0, 0), with all tones in all positions.
    Written by Anthony Luo
    :return:
    :rtype:
    '''

    img = create_image(2, 1)  # creates image

    # sets two ranges for the colours ( low / high )
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for i in range(len(tones)):  # iterates through to ensure all tones are tested
        image = copy(img)
        print('\n--- testing', tones[i], tones[i - 1], '---')
        test_img = twoTone(image, tones[i], tones[i - 1])

        col1 = _setCol(colours[i])
        col2 = _setCol(colours[i - 1])
        if (get_color(test_img, 0, 0) == col1) and (get_color(test_img, 1, 0) == col2):
            print('Passed')
        else:
            print('Fails at:', tones[i], tones[i - 1])


def _setCol(tone: Tuple[int]):
    """ returns a colour created from a tuple with three integers.
    Written by Anthony Luo
    :param tone:
    :return: Colour
    """
    r = tone[0]
    g = tone[1]
    b = tone[2]
    return create_color(r, g, b)


if __name__ == '__main__':
    testTwoTone()
