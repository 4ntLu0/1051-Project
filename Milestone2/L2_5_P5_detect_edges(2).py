from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, create_image, show, save_as


def edgeDetect(image: Image, threshold: int = 0) -> Image:
    """ Using a selected image, this function alters the r, g, b components of an image to return a new image that looks like a pencil sketch (aka edge detected image). The pixels in the image are changed to either black or white depending on the threshold value inputed by the user. 
    
    Written by Alia Nichol. 
    
    >>> edgeDetect(image, 12)
    480 640 
    """
   
    height = get_height(image)
    width = get_width(image)
    new_image = create_image(width, height - 1) # subtract one because you lose one row***** of data
    print(height, width)
    
    black_colour = create_color(0, 0, 0)
    white_colour = create_color(255, 255, 255)

    for y in range(height - 1): # begins at the first row and moves down through each row in the image       
        
        for x in range(width):
            
            r, g, b = tuple(get_color(image, x, y)) 
            #print(r, g, b)
            brightness1 = ((r + g + b) / 3) # calculates the average of all the components in the image
            r, g, b = tuple(get_color(image, x, y + 1))
            brightness2 = ((r + g + b) / 3)
              
              
            if abs(brightness1 - brightness2) > threshold:
                set_color(new_image, x, y, black_colour)  
            else:
                set_color(new_image, x, y, white_colour) 
        
    show(new_image)  
    return new_image    

if __name__ == '__main__':
    edgeDetect(load_image(choose_file()), 12)
    
    
         