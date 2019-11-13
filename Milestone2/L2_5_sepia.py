from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color #change this later please
from Utils.simple_Cimpl_filters import grayscale
from typing import NewType
Image = NewType('Image', str)


def sepia(sep_img):
    for x, y, (r, g, b) in sep_img:
        if r < 63:
            set_color(sep_img, x, y, create_color(r * 1.1, g, b * 0.9))
        elif r <= 191:
            set_color(sep_img, x, y, create_color(r * 1.15, g, b * 0.85))
        else:
            set_color(sep_img, x, y, create_color(r * 1.08, g, b * 0.93))
    show(sep_img)
    return sep_img

if __name__ == '__main__':
    working_img = grayscale(load_image(choose_file()))
    save_as(sepia(working_img), 'returns/sepia.jpg')