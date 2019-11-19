from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, \
    create_image, show, save_as

def testPosterize():
    '''
    Tests the posterize function: which basically sets each rgb to the midpoint?
              x <= 63  :   31         Case1
        63  < x <= 127 :   95         Case2
        127 < x <= 191 :  159         Case3
        191 < x <= 255 :  223         Case4
        255 < x        :  223         Case5
    Different test scenarios:
    --- Make sure that for each RGB component, they are set to the right values? ---
        5 cases, with RGB offset slightly so as to not create a grayscale image.
              P1    P2    P3    P4    P5
        R:    C1    C2    C3    C4    C5
        G:    C2    C3    C4    C5    C1
        B:    C3    C4    C5    C1    C2
    This creates a row of five pixels, shown above.

    Memefied by Anthony Luo
    '''

    create_image