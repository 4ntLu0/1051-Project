from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height
L2_5_P2_red = __import__('L2-5-P2-red')
L2_5_P2_green = __import__('L2-5-P2-green')
L2_5_P2_blue = __import__('blueTEST')
#

original_img = 'p2-original.jpg'

if __name__ == '__main__':
    """main function to run all the things!
    Written by Anthony Luo
    """
    print('running red')
    L2_5_P2_red.createRed(original_img, False)
    print('done red')
    #L2_5_P2_green.createGreen(original_img)
    L2_5_P2_blue.createBlue(original_img)
