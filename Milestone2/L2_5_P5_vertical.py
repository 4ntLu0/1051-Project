# L2-5, Milestone 2, Submitted: 11/22/2019
from Cimpl import *



def flip_vertical(img):
    """
    A photo is displayed. The function is called and the rgb values for each /
    pixel is printed. ... 
    ex: 
    photo facing left, creates photo facing right
    
    'Written by Emilio Lindia: 101143244'
    
    DOCSTRING TESTING (How to run the code)
    Code is run
    File explorer appears
    Choose a file, an image you wish to flip
    Image will appear when opened
    Close the image
    The height and width of this image is recorded and the rgb values for each 
    pixel are changed
    New flipped image is returned with changed applied to it
    Close the new image
    
    
    
    CODE HAS BEEN ATTRIBUTED FROM GIVEN FILES FOUND ON CULEARN
    """
    show(img)
    image = copy(img)                  #creates the copy to prevent it from/
                                             #being overwritten    
    
    h= get_height(image)                 #interprets the height of the image
    
    w = get_width(image)                 #interprets the width of the image
    
    new_image = create_image(w, h )      #creates an image with the same values/
                                         #as h,w
                                         
                                         #(essentially creating an image of the/
                                         #same dimensions)
                                         
                                         
    for pixel in image:                  #examines all pixels in the new image
        x,y,(r,g,b) = pixel
        print(r,g,b)                     #prints the r g b values of every pixel
        new_color = create_color(r,g,b)  
        set_color(new_image, w-x-1, y-1, new_color)  
    show(new_image)                                  

#adjust pixels along x axis(width of image) ex: one pixel has a particular/
#distance from one edge of the image, to flip the image, the pixel's distance/
#from the edge is now the same distance but from the other edge   


if __name__ == '__main__':
    new_image = load_image(choose_file())
    flip_vertical(new_image)



    

