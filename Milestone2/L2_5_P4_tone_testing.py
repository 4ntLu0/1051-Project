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

tones = {'black' : (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'lime': (0, 255, 0), 'blue': (0, 0, 255),
         'yellow': (255, 255, 0), 'cyan': (0, 255, 255), 'magenta': (255, 0, 255), 'gray': (128, 128, 128)}
colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
           (255, 0, 255), (128, 128, 128)]


def testTwoTone():
    ''' Tests to ensure that two tone functions
    Written by Anthony Luo
    :return:
    :rtype:
    '''
    img = create_image(2, 1)  # creates image
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(128, 128, 128))
    test_img = copy(img)
    for count in range(len(tone_list) - 1):
        set_color(test_img, 0, 0, create_color(tone_list[count]))
        set_color(test_img, 1, 0, create_color(tone_list[count + 1]))
        if twoTone(tone_list[count], tone_list[count + 1]) == test_img:
            print('yote')
        else:
            print('fails')


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

    for col in colours:
        print('\n testing', col)
        test_img = threeTone(test_img, col, col, col, txt = False)
        for x, y, (r, g, b) in test_img:
            if (r, g, b) == col:
                print('pass ', end = '')
            else:
                print('fails at', col, r, g, b)


testThreeTone()
