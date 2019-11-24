"""ECOR 1051 Fall 2019 Project. L2-5. Milestone 2, P6. Improved Edge Detection Test. This code has been attributed \
from given files on cuLearn. Submitted 22/11/2019"""

from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color,\
   create_image, show, save_as, copy

def detect_edges(image: Image, threshold: int) -> Image:
    """ Using a selected image, this function alters the r, g, b components of an image to return a new image\
    that looks like a pencil sketch (aka edge detected image). The pixels in the image are changed to either black\
    or white depending on the difference in contrast between the two pixels. 
    
    Written by Alia Nichol (#101143486).
    
    >>> detect_edges(choose_file(), 12)
    <Cimpl.Image object at 0x0000017986874A20>
    """    
    image = load_image(image)                                               # Loads an image of choice. 
    new_image = copy(image)    
    
    for y in range(get_height(new_image) - 1):                              # Begins at the first row and moves down through each row in the image.
        for x in range(get_width(new_image)): 

            r, g, b = (get_color(new_image, x, y))
            r1, g1, b1 = (get_color(new_image, x, y + 1))

            if abs(((r + g + b) // 3) - ((r1 + g1 + b1) // 3)) > threshold: # Changes the pixels to black if contrast between the two pixels is high.
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:                                                           # Changes the pixels to white is the contrast between the two pixels is low
                set_color(new_image, x, y, create_color(255, 255, 255))

    show(new_image)
    return new_image

if __name__ == '__main__':
    detect_edges(choose_file(), 12)





