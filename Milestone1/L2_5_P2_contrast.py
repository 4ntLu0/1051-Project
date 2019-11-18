from Cimpl import *

image = load_image(choose_file())  # loads the desired image from a given file
show(image) # displays the image to the user

image1 = copy(image) #creates a copy of the image so it is not overrided when the new image is returned



def extreme_contrast(image: Image) -> Image:
    
    """ Using a given image, the this function alters the r, g and b components to create a new contrasted image. 
    Written by Alia Nichol. 
    >>> extreme_contrast(IMAGE)
    IMAGE comes out with all pixels being extremely contrasted. 
    <Cimpl.Image object at 0x00000278831087B8>
    """   
    
    for x, y, (r, g, b) in image1:
        
        if 0 < r < 127:
            r = 0 
        else: 
            r = 255
        
        if 0 < g < 127:
            g = 0
        else:
            g = 255
        
        if 0 < b < 127:
            b = 0
        else:
            b = 255
    
    
        set_color(image1, x, y, create_color(r, g, b))
    
    show(image1)  
    return image1
    

