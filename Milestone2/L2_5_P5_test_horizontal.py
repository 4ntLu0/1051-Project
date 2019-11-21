# L2-5, Milestone 2, Submitted: 11/22/2019
from Cimpl import *

from L2_5_P5_horizontal import (flip_horizontal)    #import the filter function

def test_horizontal() :

    image = create_image( 1 , 4 )
    set_color(image, 0, 0, create_color(0, 0, 0))
    set_color(image, 0, 1, create_color(1, 1, 1))
    set_color(image, 0, 2, create_color(3, 5, 4))
    set_color(image, 0, 3, create_color(10, 30, 6))    
    
    
    flipped_image = create_image( 1 , 4 )
    set_color(flipped_image, 0, 0, create_color(10, 30, 6))
    set_color(flipped_image, 0, 1, create_color(3, 5, 4))
    set_color(flipped_image, 0, 2, create_color(1, 1, 1))
    set_color(flipped_image, 0, 3, create_color(0, 0, 0))  


    result_image = flip_horizontal(image)
    
    for x, y, (r, g, b) in result_image:
        if (r, g, b) == tuple(get_color(flipped_image, x, y)):
            print("PASS")
        else:
            print("FAIL")
            
   
  
test_horizontal()       
        
        

          
  