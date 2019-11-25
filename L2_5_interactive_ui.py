from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy


def prompt():
    """
    Prompts the user for an input. Checks validity before returning an
    """


def is_valid():
    """
    checks the validity of the input
    :return:
    :rtype:
    """


def apply_filter(selection: str, image: Image) -> Image:
    """
    Applies the selected filter
    """


def main():
    image = load_image(choose_file())
    while True:
        image = apply_filter(prompt(), image)


if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
    main()
