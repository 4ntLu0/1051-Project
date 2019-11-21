"""ECOR 1051 Fall 2019 Project - Improved Edge Detection Test from group L2-5. This code has been attributed from given files on cuLearn"""

from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color,\
   create_image, show, save_as, copy
from L2_5_P5_detect_edges_better import detect_edges_better

def detect_edges_better_test(image:Image) -> str:
    """Test function that checks if the r, g, b components have been correctly altered by the Improved Edge Detection filter. If the pixels are correctly changed to either white or black, the test function returns "PASS" to the user. If this is not the case, test function returns "FAIL".
    
    Written by Alia Nichol (#101143486). 
    >>> edgeTest(image)
    PASS
    
    >>> edgeTest(image)
    FAIL
    """
    
    image = create_image(3, 4)  # Creates image that is 
    set_color(image, 0, 0, create_color(10, 20, 50))
    set_color(image, 1, 0, create_color(80, 100, 180))
    set_color(image, 2, 0, create_color(200, 240, 243))  
    set_color(image, 2, 1, create_color(200, 240, 243))  
    set_color(image, 2, 2, create_clor(200, 240, 243))   
      
    
    width = (get_width(image) - 1)
    height = (get_height(image) - 1)  

    pixel_count = 0 #Creating a counter to count the number of pixels in the image. 
    correct = 0  #Creating a counter to count the number of pixels that have been correctly changed. 
    
    new_img = detect_edges_better(image)

    for y in range(height):
        for x in range(width):
            pixel_count += 1 

            r, g, b = tuple(get_color(image, x, y))
            r1, g1, b1 = tuple(get_color(image, x, y + 1))  # Accounting for the pixels below
            r2, g2, b2 = tuple(get_color(image, x + 1, y))  # Accounting for the pixels to the right
            r3, g3, b3 = tuple(get_color(new_image, x, y))

            if int(abs(((r + g + b) / 3) - ((r1 + g1 + b1) / 3))) > threshold and int(abs(((r + g + b) / 3) - ((r2 + g2 + b2) / 3))) > threshold and r3 == 0 and g3 ==0 and b3 ==0:
                correct += 1
 
            elif int(abs(((r + g + b) / 3) - ((r1 + g1 + b1) / 3))) <= threshold \
                 and int(abs(((r + g + b) / 3) - ((r2 + g2 + b2) / 3))) <= threshold and r3 == 255 and g3 == 255 and b3 == 255:
                correct += 1

    if pixel_count == correct:
        return print("PASS")
    
    else:
        return print("FAIL")
    
    #show(new_img)
    
    


    
