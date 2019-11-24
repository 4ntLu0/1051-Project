"""ECOR 1051 Fall 2019 Project - Extreme Contrast from group L2-5. This code has been attributed from given files on cuLearn"""

from Cimpl import create_color, set_color, save_as, show, load_image, Image, choose_file, copy

def extreme_contrast(image: str or Image) -> Image:
    """ Given an image, the r, g, b components are altered to be extremely contrasted. 
    Written by Alia Nichol (#101143486).
    
    >>> extreme_contrast("miss_sullivan.jpg")
    """   
    if type(image) == str:
        photo = load_image(image)
    else:
        photo = image
        
    new_image = copy(image)

    for x, y, (r, g, b) in new_image: # Reads through each pixel in the chosen image
       
        if 0 < r <= 127:
                r = 0
        else:r = 255
            
        if 0 < g <= 127:
                g = 0
        else:g = 255
            
        if 0 < b <= 127:
            b = 0
        else:b = 255
            
        set_color(new_image, x, y, create_color(r, g, b))
    show(new_image)
    return new_image
    

        #if 0 < r < 127:
            #contrast = create_color(0, g, b)
            #set_color(image, x, y, contrast)            
        #elif 0 < g < 127:
            #contrast = create_color(r, 0, b)
            #set_color(image, x, y, contrast)              
        #elif 0 < b < 127:
            #contrast = create_color(r, g, 0)
            #set_color(image, x, y, contrast)              
        #elif 128 < r < 255:
            #contrast = create_color(255, g, b)
            #set_color(image, x, y, contrast)              
        #elif 128 < g < 255:
            #contrast = create_color(r, 255, b)
            #set_color(image, x, y, contrast)             
        #elif 128 < b < 255:
            #contrast = create_color(r, g, 255)
            #set_color(image, x, y, contrast)                 

    #save_as(image, 'returns/contrast_channel.png') 
    #show(load_image('returns/contrast_channel.png'))
    #print('contrast_channel saved as new image')

#if __name__ == '__main__':
    #image = load_image(choose_file())  # Loads the desired image from a given file.
    #show(image)
    #new_image = copy(image)  
    ### Creates a copy of the image so it is not overrided when the new image is returned.
    #extreme_contrast(image)