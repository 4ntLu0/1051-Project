from Utils.Cimpl import *
from Utils.simple_Cimpl_filters import grayscale
from L2_5_P4_sepia import sepia


def sepiaTest() -> None:
    """Test function for the sepia filter that checks if all the r, g, b components have gotten the sepia filter
    applied to them. The function returns "PASS" if all the pixels are successfully changed. If "PASS" is returned,
    this indicates that the red component has increased by the correct percentage and the blue component has
    decreased by the correct percentage, ultimately applying the sepia filter. If not, the function returns "FAIL".

    Written by Alia Nichol.
    """
    img = create_image(3, 1)  # creates image
    set_color(img, 0, 0, create_color(10, 20, 50))
    set_color(img, 1, 0, create_color(80, 100, 180))
    set_color(img, 2, 0, create_color(200, 240, 243))

    test_img = sepia(img, disp = False, save = True)
    #check to see if worked    
    #print(get_color(test_img, 0, 0))
    #print(get_color(test_img, 1, 0))
    #print(get_color(test_img, 2, 0))

    if (get_color(test_img, 0, 0) == create_color(28, 26, 23)) and \
            (get_color(test_img, 1, 0) == create_color(138, 120, 102)) and \
            (get_color(test_img, 2, 0) == create_color(245, 227, 211)):
        print('pass')
    else:
        print('fails')

sepiaTest()









