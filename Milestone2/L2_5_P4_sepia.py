from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color #change this later please
from Utils.simple_Cimpl_filters import grayscale
from typing import NewType
Image = NewType('Image', str)
from datetime import datetime


def sepia(img, disp = True, save = True):
    """ Adjusts the r, g, and b values of an image to create a sepia image.
    Written by Anthony Luo
    :param img:
    :type img:
    :return:
    :rtype:
    """
    sep_img = grayscale(img)
    for x, y, (r, g, b) in sep_img:
        if r < 63:
            set_color(sep_img, x, y, create_color(r * 1.1, g, b * 0.9))
        elif r <= 191:
            set_color(sep_img, x, y, create_color(r * 1.15, g, b * 0.85))
        else:
            set_color(sep_img, x, y, create_color(r * 1.08, g, b * 0.93))
    if disp:
        show(sep_img)
    if save:
        save_as(sepia(image), 'returns/sepia.jpg')
    return sep_img

if __name__ == '__main__':
    """Runs sepia program
    written by Anthony Luo
    """
    #TODO: work on saving things better
    image = load_image(choose_file())
    print('image loaded, program starting')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string.strip()
    print("start time =", dt_string)
    sepia(image)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string.strip()
    print("end time =", dt_string)