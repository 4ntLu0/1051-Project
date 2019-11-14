from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color #change this later please
from Utils.simple_Cimpl_filters import grayscale
from typing import NewType
Image = NewType('Image', str)
from datetime import datetime



def sepia(sep_img):
    """ Adjusts the r, g, and b values of a grayscale image to create a sepia image.
    Written by Anthony Luo
    :param sep_img:
    :type sep_img:
    :return:
    :rtype:
    """
    for x, y, (r, g, b) in sep_img:
        if r < 63:
            set_color(sep_img, x, y, create_color(r * 1.1, g, b * 0.9))
        elif r <= 191:
            set_color(sep_img, x, y, create_color(r * 1.15, g, b * 0.85))
        else:
            set_color(sep_img, x, y, create_color(r * 1.08, g, b * 0.93))
    #show(sep_img)
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
    working_img = grayscale(image)
    save_as(sepia(working_img), 'returns/sepia.jpg')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string.strip()
    print("end time =", dt_string)