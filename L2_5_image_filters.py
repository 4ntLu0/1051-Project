"""Milestone 3. EAAA. L2_5 SIPE Image Filters. Release 1.0.0 December 1, 2019.
This code has been attributed from given files on cuLearn.
Authors: Alia Nichol, Anthony Luo, Emilio Lindia, Abdelrahman Alatoom.
Contact information may be obtained from Carleton University.
Group Leader: Anthony Luo"""

from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
from simple_Cimpl_filters import grayscale
from typing import Tuple, List
import os


def _adjust_component(comp: int)-> int: #Enters a red, green, or blue component
    
    if 0 <= comp <= 63:
        return 31    
    
    elif 63 < comp <= 127:
        return 95   
    
    elif 127 < comp <= 191:
        return 159    
    
    elif 191 < comp <= 255:
        return 223
    
    elif comp > 255:
        return 223
    
    elif comp < 0:
        return 31
#The midpoint of it's quadrant is returned
#This function is a helper function that will be called upon

def posterize(image: Image) -> Image:
    """ Posterizes the image by setting each r, g, b value to the midpoint of 
    it's quadrant.
    Written by: Emilio Lindia
    
    >>> posterize(miss_sullivan.jpg)
    """
    new_image = copy(image)  # assigns new image as a copy of original
    for pixel in image:  # examines all pixels in the new image
        x, y, (r, g, b) = pixel
        (r, g, b) = (_adjust_component(r), _adjust_component(g), _adjust_component(b))
        new_color = create_color(r, g, b)  
        # inserts rgb values into adjust component function to change rgb values
        set_color(new_image, x, y, new_color)
    show(new_image)
    return image

def extreme_contrast(new_image: str or Image) -> Image:
    """ Given an image, the r, g, b components are altered to be extremely contrasted. 
    Written by Alia Nichol (#101143486).
    
    >>> extreme_contrast("miss_sullivan.jpg")
    """   

    for x, y, (r, g, b) in new_image: # Reads through each pixel in the chosen image
       
        if 0 < r <= 127:
            r = 0
        else:
            r = 255
            
        if 0 < g <= 127:
            g = 0
        else:
            g = 255
            
        if 0 < b <= 127:
            b = 0
        else:
            b = 255
            
        set_color(new_image, x, y, create_color(r, g, b))
    show(new_image)
    return new_image

def sepia(img: Image, disp: bool = True, save: bool = False) -> Image:
    """ Adjusts the r, g, b values of an image to create a sepia image.
    Written by Anthony Luo. 
    
    >>> sepia(miss_sullivan.jpg, True, False)
    """
    sep_img = grayscale(img)
    for x, y, (r, g, b) in sep_img:
        if r < 63:
            set_color(sep_img, x, y, create_color(r * 1.1, g, b * 0.9))
        elif r <= 191:
            set_color(sep_img, x, y, create_color(r * 1.15, g, b * 0.85))
        else:
            set_color(sep_img, x, y, create_color(r * 1.08, g, b * 0.93))
    if disp:
        show(sep_img)
    if save:
        save_as(sep_img, "returns/sepia.jpg")
    return sep_img


tones = {"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0),
         "lime": (0, 255, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0),
         "cyan": (0, 255, 255), "magenta": (255, 0, 255),
         "gray": (128, 128, 128)}

def two_tone(image: Image, CR1: str, CR2: str) -> Image:
    """Adjusts the r, g, b components so that the image consists of two tones 
    chosen by the user. CR1 should be brighter than CR2.

    Colour inputs should be chosen from the dictionary above. 

    By: Abdelrahman Alatoom
    
    >>> two_tone(miss_sullivan.jpg, yellow, black) """
    
    image = copy(image)

    tone1r, tone1g, tone1b = tones[CR1]
    tone2r, tone2g, tone2b = tones[CR2]

    tone1 = create_color(tone1r, tone1g, tone1b)
    tone2 = create_color(tone2r, tone2g, tone2b)

    for x, y, (r, g, b) in image:
        average = ((r + g + b) / 3)

        if average <= 200:
            set_color(image, x, y, tone1)

        else:
            set_color(image, x, y, tone2)

    show(image)
    return image


def three_tone(image, CR1, CR2, CR3: str):
    """Adjusts the r, g, b components so that the image consists of three
    tones chosen by the user. Colour inputs should be chosen from the
    dictionary above.
    
    By: Abdelrahman Alatoom

    >>> three_tone(miss_sullivan.jpg, black, blue, red)"""

    image = copy(image)

    tone1r, tone1g, tone1b = tones[CR1]
    tone2r, tone2g, tone2b = tones[CR2]
    tone3r, tone3g, tone3b = tones[CR3]

    tone1 = create_color(tone1r, tone1g, tone1b)
    tone2 = create_color(tone2r, tone2g, tone2b)
    tone3 = create_color(tone3r, tone3g, tone3b)

    for x, y, (r, g, b) in image:
        average = ((r + g + b) / 3)

        if average < 84:
            set_color(image, x, y, tone1)

        elif average <= 170:
            set_color(image, x, y, tone2)

        else:
            set_color(image, x, y, tone3)

    show(image)
    return image


def detect_edges(image: Image, threshold: int) -> Image:
    """ Alters the r, g, b components of an image and returns a pencil sketch 
    (aka edge detected) image. The pixels in the image are changed to either 
    black or white depending on the difference in contrast between two pixels.

    Written by Alia Nichol (#101143486).

    >>> detect_edges(miss_sullivan.jpg, 12)
    
    """
    new_image = copy(image)

    # Begins at the first row and moves down through each row in the image.
    for y in range(get_height(new_image) - 1):  
        for x in range(get_width(new_image)):

            r, g, b = (get_color(new_image, x, y))
            r1, g1, b1 = (get_color(new_image, x, y + 1))
            
            # Changes the pixels to black as contrast between pixels is high. 
            if abs(((r + g + b) // 3) - ((r1 + g1 + b1) // 3)) > threshold:  
                # contrast between the two pixels is high.
                set_color(new_image, x, y, create_color(0, 0, 0))
            # Pixels changed to white as contrast between pixels is low.    
            else:  
                set_color(new_image, x, y, create_color(255, 255, 255))

    show(new_image)
    return new_image


def _avg_bright(colour: Tuple[int]) -> int:
    """Returns avg brightness of three colours
    Written by Anthony Luo.
    
    """
    r, g, b = colour
    return (r + g + b) / 3


def _new_col(colour: Tuple[int]) -> int:
    """ Returns a colour type from a colour
    written by Anthony Luo
    """
    r, g, b = tuple(colour)
    return create_color(r, g, b)


def detect_edges_better(img: Image, thresh: int = 0,
    disp: bool = True, save: bool = False):
    """ Return an image with the edge detects.
    Written by Anthony Luo (#101145222)
    :param img: Image to detect edges on
    :param thresh: Threshold value for detection
    :param disp: Whether or not to display the image, True by default
    :param save: Whether or not ot save the image. True by default.
    :return: edge detected image.
    >>> detect_edges_better(load_image(choose_file()), 13)
    >>> detect_edges_better(load_image(choose_file()), 15, True, False)
    """

    # functional definitions
    width = get_width(img)
    height = get_height(img)
    new_img = create_image(width, height)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)

    for y in range(height - 1):  # starts at the first row, then moves down
        for x in range(width - 1): #starts at left column, and moves right
            # compares brightness between two images and then resets colours.
            if abs(_avg_bright(tuple(get_color(img, x, y))) - _avg_bright(
                    tuple(get_color(img, x, y + 1)))) > thresh or abs(
                    _avg_bright(tuple(get_color(img, x, y))) -
                    _avg_bright(tuple(get_color(img, x + 1, y)))) > thresh:
                # sets colour to black (edge detected)
                set_color(new_img, x, y, black)
            else:
                # sets colour to white (no edge)
                set_color(new_img, x, y, white)

    for x in range(width):
        # sets the last row of pixels to be equal to the one right above
        set_color(new_img, x, height - 1,
                  _new_col(get_color(new_img, x, height - 2)))

    for y in range(height):
        # sets last column of pixels to be equal to the ones to the left
        set_color(new_img, width - 1, y,
                  _new_col(get_color(new_img, width - 2, y)))

    # sets the colour for the last pixel
    if get_color(new_img, width - 2, height - 1) == create_color(0, 0, 0) or \
            get_color(new_img, width - 1, height - 2) == create_color(0, 0, 0):
        set_color(new_img, width - 1, height - 1, create_color(0, 0, 0))
    else:
        set_color(new_img, width - 1, height -
                  1, create_color(255, 255, 255))
    
    if disp:
        show(new_img)  # shows image
    if save:
        # saves to returns/
        save_as(new_img, "returns/better_edge_detect.png")
    return new_img


def flip_horizontal(image: Image) -> Image:
    """Adjusts the r, g, b components so that the image is flipped along the 
    horizontal axis. 

    Written by Abdelrahman Alatoom

    >>> flip_horizontal(miss_sullivan.jpg)
    
    """    
    h = get_height(image)
    w = get_width(image)
    new_image = create_image(w, h)
    for pixel in image:
        x, y, (r, g, b) = pixel

        new_color = create_color(r, g, b)
        set_color(new_image, x - 1, h - y - 1, new_color)
    show(new_image)
    return new_image


def flip_vertical(img: Image) -> Image:
    """Adjusts the r, g, b components so that the image is flipped along the 
    vertical axis. 

    "Written by Emilio Lindia: 101143244"

    >>> flip_vertical(miss_sullivan.jpg)
    """
    image = copy(img)  # Creates the copy to prevent it from/
    # Being overwritten

    h = get_height(image)  # Interprets the height of the image

    w = get_width(image)  # Interprets the width of the image

    new_image = create_image(w, h)  # Creates an image with the same values/
    # As h,w

    # (Essentially creating an image of the/
    # Same dimensions)

    for pixel in image:  # Examines all pixels in the new image
        x, y, (r, g, b) = pixel
        # Print(r,g,b)                   #Prints the r g b values of every pixel
        new_color = create_color(r, g, b)
        set_color(new_image, w - x - 1, y - 1, new_color)
    show(new_image)
    return new_image


# Adjust pixels along x axis(width of image) ex: one pixel has a particular/
# Distance from one edge of the image, to flip the image, the pixel's distance/
# From the edge is now the same distance but from the other edge


if __name__ == "__main__":
    new_path = os.getcwd() + "/returns"  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
