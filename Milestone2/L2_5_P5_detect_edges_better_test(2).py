"""ECOR 1051 Fall 2019 Project - Improved Edge Detection Test from group L2-5. This code has been attributed from given files on cuLearn"""

from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color,\
   create_image, show, save_as, copy
from L2_5_P5_detect_edges_better import detect_edges_better

def detect_edges_better_test() -> str:
    """Test function that checks if the r, g, b components have been correctly altered by the Improved Edge Detection filter. If the pixels are correctly changed to either white or black, the test function returns "PASS" to the user. If this is not the case, test function returns "FAIL".
    
    Written by Alia Nichol (#101143486). 
    >>> edgeTest(image)
    PASS
    
    >>> edgeTest(image)
    FAIL
    """
    
    original_image = create_image(7, 3, color = create_color(10, 10, 10))  # Creates image that is width 6 and height 2
    bright = create_color(250, 250, 250)
    set_color(original_image, 1, 0, bright)
    set_color(original_image, 2, 1, bright)
    set_color(original_image, 2, 2, bright)
    set_color(original_image, 3, 0, bright)
    set_color(original_image, 3, 1, bright)
    set_color(original_image, 3, 2, bright)
    set_color(original_image, 4, 1, bright)
                
    
    
    expected_image =  create_image(7, 3, color = create_color(255, 255, 255))
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
    
    actual_image = detect_edges_better(original_image, 100, False)
    
    #width = (get_width(image) - 1)
    #height = (get_height(image) - 1)  
       
    for x, y, (r, g, b) in actual_image:
        if (r, g, b) == tuple(get_color(expected_image, x, y)):
            print('PASS')
        else:
            print('FAIL')
    #if expected_image == actual_image:
        #print("PASS") 
    #else:
        #print("FAIL") 
        
detect_edges_better_test()
                
                