from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color, create_image, copy  # change
# this
# later please
from Utils.simple_Cimpl_filters import grayscale
from typing import NewType
# from L2_5_two_tone import twoTone
from L2_5_three_tone import threeTone

Image = NewType('Image', str)
from datetime import datetime

# TODO: write the rest of this code :(

tones = ['black', 'white', 'red', 'lime', 'blue',
         'yellow', 'cyan', 'magenta', 'gray']
colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
           (255, 0, 255), (128, 128, 128)]


def testTwoTone():
    ''' Tests to ensure that two tone creates an image with the colours specified.
    Tests both ranges, both High (255, 255, 255) and Low (0, 0, 0)
    Written by Anthony Luo
    :return:
    :rtype:
    '''
    img = create_image(2, 1)  # creates image
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for i in range(len(tones)):
        print('\n testing', tones[i])
        test_img = twoTone(img, tones[i], tones[i])
        for x , y, (r, g, b) in test_img:
            if (r, g, b) == colours[i]:
                print('pass', end = '')
            else:
                print('fails at', tones[i], r, g, b)


def testThreeTone():
    ''' Tests to ensure that three tone functions
    Written by Anthony Luo
    :return:
    :rtype:
    '''

    img = create_image(3, 1)  # creates image
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(128, 128, 128))
    set_color(img, 2, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for i in range(len(tones)):
        print('\n testing', tones[i])
        test_img = threeTone(img, tones[i], tones[i], tones[i])
        for x , y, (r, g, b) in test_img:
            if (r, g, b) == colours[i]:
                print('pass', end = '')
            else:
                print('fails at', tones[i], r, g, b)


testThreeTone()
