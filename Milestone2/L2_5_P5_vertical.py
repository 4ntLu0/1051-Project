from Cimpl import *
"""
creates a function which mirrors the inputed image vertically... ex: photo 
facing left, creates photo facing right

Written by Emilio Lindia
"""


image = load_image(choose_file())        #allows you to choose a file
show(image)
new_image = copy(image)                  #creates the copy to prevent it from being overwritten


def flip_vertical(image):
    
    h= get_height(image)                 #interprets the height of the image
    w = get_width(image)                 #interprets the width of the image
    
    new_image = create_image(w, h )      #creates an image with the same values as h,w
                                         #essentially creating an image of the same dimensions
    for pixel in image:                  #examines all pixels in the new image
        x,y,(r,g,b) = pixel
        print(r,g,b)                     # prints the r g b values of every pixel
        new_color = create_color(r,g,b)  #
        set_color(new_image, w-x-1, y-1, new_color)
    show(new_image)
        
        
        
flip_vertical(new_image)
    





    

