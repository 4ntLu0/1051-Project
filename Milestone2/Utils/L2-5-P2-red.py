from Cimpl import load_image, create_color, set_color, show, Image, save_as, copy
from typing import NewType
import os

Image = NewType('Image', str)


def createRed( img: Image, verify: bool = True, log: bool = False ):
    """ Saves a new image which constitutes only the red channel of an image img
    Written by Anthony Luo
    :param img: Original image
    :type img: Image
    :param verify: Whether or not to verify the image (ie, show it to the user)
    :type verify: bool
    :param log: whether or not to save image data to log files
    :type log: bool
    :return: None
    :rtype: NoneType
    >>> image = load_image(choose_image())
    >>> createRed(image)
    >>> show(image)
    """
    image = copy(img)
    if verify:
        show(image)  # shows the original image

    # checks if you are logging or not (once, at the start, instead of everytime)
    if log:
        try:
            os.remove('redImgLog.txt')
        except:
            pass
        red_log = open('redImgLog.txt', 'a')  # creates a NEW log file
        for x, y, (r, g, b) in image:  # reads through the image pixel by pixel
            red = create_color(r, 0, 0)  # creates new 'colour' tuple

            # remaps each x,y coordinate to new colour
            set_color(image, x, y, red)
        str1 = f'{x:03}' + f'{y:03}' + f'{r:03}' + f'{g:03}' + f'{b:03}' + f'{red[0]:03}' + \
               f'{red[1]:03}' + f'{red[2]:03}' + '\n'  # creates logger string
        red_log.write(str1)  # saves string
    else:
        for x, y, (r, g, b) in image:  # reads through the image pixel by pixel
            red = create_color(r, 0, 0)  # creates new 'colour' tuple

            # remaps each x,y coordinate to new colour
            set_color(image, x, y, red)

    save_as(image, 'red_channel.png')  # saves as a new image
    if verify:
        show(load_image('red_channel.png'))  # shows the image to double check

    print('red_channel created')  # notifies user


def testRed( ori_img: Image ):
    """ Tests the red image to ensure there are no traces of blue or green in the image.
    written by Anthony Luo
    :param ori_img: Original image
    :type ori_img: load_image('')
    >>> test_red( load_image(choose_image()))
    'Red PASSES'
    """
    createRed(ori_img, False, True)  # runs the red function in debugging mode.
    show(ori_img)  # shows the original image, to ensure that it is correct
    show(load_image('red_channel.png'))  # shows the red image, to ensure that it's correct.
    log = open('redImgLog.txt', 'r')  # opens logger
    fail = False
    for line in log:
        if line[18:24] == str('000000'):  # double checks that last 6 digits (ggg,bbb) are all 0
            pass
        else:
            print('fails with log line: ', line, '\n')  # notifies user of fail
            print(line[18:24])
            fail = True  # has failed tests
    if fail:
        return ('1')  # error code 1
    else:
        print('Red PASSES')
