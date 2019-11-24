"""ECOR 1051 Fall 2019 Project - Improved Edge Detection Test from group L2-5. This code has been attributed from given files on cuLearn"""

from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color,\
   create_image, show, save_as, copy
from L2_5_P5_detect_edges_better import detect_edges_better      #Imports the Improved Edge Detection function so it can later be called. 

def detect_edges_better_test() -> None:
    """Test function that checks if the r, g, b components have been correctly altered by the Improved Edge Detection filter. \
    If the pixels are correctly changed to either white or black, the test function returns "PASS" to the user. If this is not the case, \
    the test function returns "FAIL".
    
    Written by Alia Nichol (#101143486). 
    >>> detect_edges_better_test(image)
    PASS
    
    >>> detect_edges_better_test(image)
    FAIL
    """
    
    original_image = create_image(7, 3, color = create_color(10, 10, 10))       # Creates image that is width 6 and height 2 set to a dark colour. 
    bright = create_color(250, 250, 250)
    set_color(original_image, 1, 0, bright)
    set_color(original_image, 2, 1, bright)
    set_color(original_image, 2, 2, bright)
    set_color(original_image, 3, 0, bright)
    set_color(original_image, 3, 1, bright)
    set_color(original_image, 3, 2, bright)
    set_color(original_image, 4, 1, bright)         
    
    expected_image =  create_image(7, 3, color = create_color(255, 255, 255))   # Creates image that is width 6 and height 2 set to a bright colour.
    black = create_color(0, 0, 0)
    set_color(expected_image, 0, 0, black)
    set_color(expected_image, 1, 0, black)
    set_color(expected_image, 1, 1, black)  
    set_color(expected_image, 1, 2, black)    
    set_color(expected_image, 2, 0, black)
    set_color(expected_image, 3, 0, black)
    set_color(expected_image, 4, 0, black)  
    set_color(expected_image, 4, 1, black)    
    set_color(expected_image, 4, 2, black)    
    
    actual_image = detect_edges_better(original_image, 100, False)              # The Improved Edge Detection filter is applied to original_image. 
       
    for x, y, (r, g, b) in actual_image:
        if (r, g, b) == tuple(get_color(expected_image, x, y)):                 # Checks if the pixels in the actual image equal the ones in the expected image.
            print('PASS')
        else:
            print('FAIL')
        
detect_edges_better_test()                                                      # Calls the test function.
                
                