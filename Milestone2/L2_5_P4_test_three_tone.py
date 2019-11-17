from Utils.Cimpl import create_color, create_image, copy, get_color, set_color
from typing import NewType
from L2_5_three_tone import threeTone

Image = NewType('Image', str)

# TODO: fix commenting

tones = ['black', 'white', 'red', 'lime', 'blue',
         'yellow', 'cyan', 'magenta', 'gray']
colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
           (255, 0, 255), (128, 128, 128)]


def testThreeTone():
    ''' Tests to ensure that three tone functions, that is: for any scenario, the lightest, middle, and darkest
    areas correspond to the assigned colours.
    Written by Anthony Luo
    :return:
    :rtype:
    '''

    img = create_image(3, 1)  # creates image

    # sets colours
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(128, 128, 128))
    set_color(img, 2, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for i in range(len(tones)):  # goes through all the tones, ensuring each one functions as expected
        image = copy(img)  # prevents loss of quality / information through repeated use of the same image
        print('\n--- testing', tones[i], tones[i - 1], tones[i - 2], '---')
        test_img = threeTone(image, tones[i], tones[i - 1], tones[i - 2])  # runs image through the function

        # set colours, to be compared with
        col1 = _setCol(colours[i])
        col2 = _setCol(colours[i - 1])
        col3 = _setCol(colours[i - 2])

        # compares colours and prints test results.
        if (get_color(test_img, 0, 0) == col1) and (get_color(test_img, 1, 0) == col2) and (get_color(test_img, 2,
                                                                                                      0) == col3):
            print('Passed')
        else:
            print('Fails at:', tones[i], tones[i - 1], tones[i - 2])


def _setCol( tone ):
    r = tone[0]
    g = tone[1]
    b = tone[2]
    return create_color(r, g, b)


testThreeTone()
