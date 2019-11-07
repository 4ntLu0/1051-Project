from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height
from L2_5_P2_red import createRed
original_img = load_image('p-2-original.jpg')

if __name__ == '__main__':
    createRed(original_img, True, False)