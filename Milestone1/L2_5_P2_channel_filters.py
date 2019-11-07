from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height
from L2_5_P2_red import createRed
from L2_5_P2_green import green_filter
#from L2_5_P2_blue import createBlue

original_img = 'p2-original.jpg'

if __name__ == '__main__':
    """main function to run all the things!
    Written by Anthony Luo
    """
    print('running red')
    createRed(original_img, True)
    print('done red')
    green_filter(original_img)
    #createBlue(original_img)
