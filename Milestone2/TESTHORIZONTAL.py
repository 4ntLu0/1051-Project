
from L2_5_P5_horizontal import (flip_horizontal) 

def test_horizontal(image: Image):





    image = create_image( 4 , 1 )
    set_color(image, 0, 0, create_color(0, 0, 0))
    set_color(image, 1, 0, create_color(1, 1, 1))
    set_color(image, 2, 0, create_color(3, 5, 4))
    set_color(image, 3, 0, create_color(10, 30, 6))    
    
    
    flipped_image = create_image( 4 , 1 )
    set_color(image, 0, 0, create_color(10, 30, 6))
    set_color(image, 1, 0, create_color(3, 5, 4))
    set_color(image, 2, 0, create_color(1, 1, 1))
    set_color(image, 3, 0, create_color(0, 0, 0))              
  
    if flip_horizontal(image) = flipped_image:
        print('PASS')
    