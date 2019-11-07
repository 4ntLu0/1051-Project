from Cimpl import load_image, create_color, set_color, show, Image, save_as
from typing import NewType
import os

Image = NewType('Image')

def createRed(original_img: Image, verify: bool, log: bool):
    """ Takes an original img and saves a new image with only the red channel.
    Written by Anthony Luo
    """
    if log:
        try:
            os.remove('redImgLog.txt')
        except:
            pass
        red_log = open('redImgLog.txt')  # creates a NEW log file
    if verify:
        show(image)  # shows the original image
    for x, y, (r, g, b) in image:  # reads through the image pixel by pixel
        red = create_color(r, 0, 0)  # creates new 'colour' tuple
        
        # remaps each x,y coordinate to new colour
        set_color(image, x, y, red)

        # creates a string to write to log
        str1 = 'X: ' + str(x) + ' Y: ' + str(y) + ' WITH ORIGINAL R: ' + str(r) + \
            ' G: ' + str(g) + ' B: ' + str(b) + ' | WITH NEW: R: ' + str(red[0]) + \
            ' G: ' + str(red[1]) + ' B: ' + str(red[2]) + '\n'  # compiles string
        if log:
                red_log.write(str1)  # saves string

    save_as(image, 'red_channel.jpg')  # saves as a new image
    if verify:
        show(load_image('red_channel.jpg'))  # shows the image to double check
    
    print('red_channel created')
    exit()
