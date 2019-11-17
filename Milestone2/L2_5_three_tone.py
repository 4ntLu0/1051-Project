from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color, get_width, get_height  # change
# this later please
from Utils.simple_Cimpl_filters import grayscale
from typing import NewType, List
import numpy as np

Image = NewType('Image', str)
from datetime import datetime

tones = {'black' : (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'lime': (0, 255, 0), 'blue': (0, 0, 255),
         'yellow': (255, 255, 0), 'cyan': (0, 255, 255), 'magenta': (255, 0, 255), 'gray': (128, 128, 128)}
brightness = []


def threeTone( image: Image, col1: str, col2: str, col3: str , show = False, txt = True) -> Image:
    """ Returns an image with three tones, with the darkest being the first tone, and brightest being the third tone.
    Written by Anthony Luo.
    :param image:
    :type image:
    :param col1:
    :type col1:
    :param col2:
    :type col2:
    :param col3:
    :type col3:
    :return:
    :rtype:
    """
    if txt:
        tone1r, tone1g, tone1b = tones[col1]
        tone2r, tone2g, tone2b = tones[col2]
        tone3r, tone3g, tone3b = tones[col3]
    else:
        tone1r, tone1g, tone1b = col1
        tone2r, tone2g, tone2b = col2
        tone3r, tone3g, tone3b = col3
    tone1 = create_color(tone1r, tone1g, tone1b)
    tone2 = create_color(tone2r, tone2g, tone2b)
    tone3 = create_color(tone3r, tone3g, tone3b)
    for x, y, (r, g, b) in image:
        avg = (r + g + b) / 3
        if avg < 84:
            set_color(image, x, y, tone1)
        elif avg <= 170:
            set_color(image, x, y, tone2)
        else:
            set_color(image, x, y, tone3)
    if show:
        show(image)
    return image


if __name__ == '__main__':
    image = load_image(choose_file())
    print('image loaded, starting conversion')
    save_as(threeTone(image, 'white', 'gray', 'black'), 'returns/three_tone.jpg')
    print('conversion finished.')
    if input(' would you like to view the image? [Y/N]') == 'Y':
        show(image)
    else:
        print('ok, exiting code. byebye!')
