# L2-5, Milestone 2, Submitted: 11/22/2019
from Cimpl import set_color, create_image, create_color, get_color

from L2_5_P5_horizontal import (flip_horizontal)    #import the filter function

def test_horizontal() :
    """
    Test function which tests the functionality of the filtwr which flips
    images horizontally. 
    After importing the filter function, the test function creates an image
    of size 1,4 (in terms of x,y).
    The colours are retrieved from this new image and they are compared with
    that of another image of equal size, except reversed y order.(horizontally
    flipped)
    If the pixels match, the function has flipped the image properly
    
     ' Written by Emilio Lindia: 101143244 '
    
    DOCSTRING TESTING (How to run the code)
    Code is run
    image of size (1,4) is displayed somewhere on screen
    Close the image
    Refer to shell
    If test was run correctly and the filter passed all tests, PASS should be
    printed
    END OF CODE
  
    
    CODE HAS BEEN ATTRIBUTED FROM GIVEN FILES FOUND ON CULEARN
    """
    image = create_image( 1 , 4 )                 #Creates image of size (1,4)
    set_color(image, 0, 0, create_color(0, 0, 0)) 
    set_color(image, 0, 1, create_color(1, 1, 1))
    set_color(image, 0, 2, create_color(3, 5, 4))
    set_color(image, 0, 3, create_color(10, 30, 6))    
    
    
    flipped_image = create_image( 1 , 4 )         #Creates image of size (1,4)
    set_color(flipped_image, 0, 0, create_color(10, 30, 6))
    set_color(flipped_image, 0, 1, create_color(3, 5, 4))
    set_color(flipped_image, 0, 2, create_color(1, 1, 1))
    set_color(flipped_image, 0, 3, create_color(0, 0, 0))  
#Notice this second image that is created possesses opposite RGB values
#This accounts for the images to be identical, except for the fact that \
#he flipped_image is the upside-down version

    result_image = flip_horizontal(image)
    
    for x, y, (r, g, b) in result_image:        
        if (r, g, b) == tuple(get_color(flipped_image, x, y)):
            print("PASS")     
        else:
            print("FAIL")
#If the images are equal, then the filter has properly flipped the image
#printing PASS will be an indication that this is the case
#Otherwise, FAIL would be printed
   
  
test_horizontal()       
        
        
