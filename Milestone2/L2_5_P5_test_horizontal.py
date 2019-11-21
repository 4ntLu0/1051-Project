# L2-5, Milestone 2, Submitted: 11/22/2019
from Cimpl import *

#from L2_5_P5_horizontal import (flip_horizontal) 


from Cimpl import *
image = load_image(choose_file())     
show(image)
new_image = copy(image)

def flip_horizontal(image):
    h= get_height(image)      
    w = get_width(image)    
    new_image = create_image(w, h )
    for pixel in image:                  
        x,y,(r,g,b) = pixel
                        
        new_color = create_color(r,g,b)  
        set_color(new_image,x-1, h- y-1, new_color)  
    show(new_image)           
    
flip_horizontal(new_image)





def test_horizontal(image: Image):

    flip_image = flip_horizontal(new_image)
    
   
    for x in range(get_width(image)):
        horizontal_factor = flip_image.get_width() - 1
       
        for y in range(get_height(image)):
            
            original_color = get_color(image, x, y )
            
            print('found color pattern of original image')
            
            flipped_color = get_color(flip_image, x, horizontal_factor)
            
            print('found color pattern of flipped image')
            
            if (original_color != flipped_color):
                return False
          
            else:
                pass
            
            horizontal_factor -= 1
           
          
    return print('test passed') 
  
     
        #make changes to vertical code too!!!!!!
        
        

          
  # def test_filter(original_image):

# filtered_image = filter(original_image)

# then compare pixels of each image
      