"""L2_5 SIPE Image Filters. Release 1.0.0 December 1, 2019.
This code has been attributed from given files on cuLearn.
Contact information may be obtained from carleton university
Group Leader: Anthony Luo"""

from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
from simple_Cimpl_filters import grayscale
from typing import Tuple, List
import os


def create_red(img: Image, verify: bool = True, log: bool = False) -> Image:
    """ Saves a new image which constitutes only the red channel of an image img
    Written by Anthony Luo (#101145222)
    >>> image = load_image(choose_image())
    >>> create_red(image)
    >>> show(image)
    """
    image = copy(img)

    # checks if you are logging or not (once, at the start, instead of everytime)
    if log:
        try:
            os.remove("redImgLog.txt")

        except:
            pass
        red_log = open("redImgLog.txt", "a")  # creates a NEW log file

        for x, y, (r, g, b) in image:
            red = create_color(r, 0, 0)
            set_color(image, x, y, red)

        str1 = f"{x:03}" + f"{y:03}" + f"{r:03}" + f"{g:03}" + f"{b:03}" + f"{red[0]:03}" + \
               f"{red[1]:03}" + f"{red[2]:03}" + "\n"  # creates logger string
        red_log.write(str1)  # saves string

    else:
        for x, y, (r, g, b) in image:
            red = create_color(r, 0, 0)
            set_color(image, x, y, red)

    save_as(image, "returns/red_channel.png")  # saves as a new image

    if verify:
        show(load_image("red_channel.png"))  # shows the image to double check

    print("red_channel created")  # notifies user

    return image


def create_blue(img):
    """ the function createBlue displays the original image, once closed it displays the image with a blue filter

    -Emilio Lindia
    """
    image = copy(img)
    # image = load_image("p2-original.jpg")  # loads the original colourless picture

    new_image = image

    for x, y, (r, g, b) in image:  # examines all pixels
        blue = create_color(0, 0, b)  # creates a 100% blue filter

        set_color(new_image, x, y, blue)

    save_as(new_image, "returns/blue_channel.png")  # saves the blue filter as a new image
    show(load_image("blue_channel.png"))  # shows image

    print("blue_channel saved as new_image")
    return new_image


def green_filter(image1: Image) -> Image:
    """Alia Nichol

    """
    image = copy(image1)  # creates a copy of the image so it is not overrided

    for x, y, (r, g, b) in image:  # reads through the image
        green = create_color(0, g, 0)
        set_color(image, x, y, green)  # sets all the pixels of defined locations in that image to the color

    save_as(image, "returns/green_channel.png")
    show(load_image("green_channel.png"))
    print("green_channel saved as new image")

    return image


def combine(log: Tuple = False) -> Tuple[Image, List[int], List[int], List[int], List[Tuple]]:
    """ Combines three single-colour images (red, green, and blue) into a final image.
    Written by Anthony Luo
    >>> combine()
    >>> show(load_image("combined_image.png"))
    """
    # loads images in
    r_img = load_image("red_channel.png")
    g_img = load_image("green_channel.png")
    b_img = load_image("blue_channel.png")

    # creates new image with hard dimensions.
    new_img = create_image(640, 480)

    # creates the different channels for RGB
    r_chan = []
    g_chan = []
    b_chan = []
    rgb = []

    for x, y, (r, g, b) in r_img:  # grabs r value
        r_chan.append(r)

    for x, y, (r, g, b) in g_img:  # grabs g value
        g_chan.append(g)

    for x, y, (r, g, b) in b_img:  # grabs b value
        b_chan.append(b)

    counter = 0
    if not log:  # checks whether or not we should be logging (once, instead of every time the loop runs)
        for x, y, (r, g, b) in new_img:
            colour = create_color(r_chan[counter], g_chan[counter], b_chan[counter])  # create colour from constituents
            set_color(new_img, x, y, colour)  # set colour
            counter += 1

        show(new_img)
        show(load_image("combined_image.png"))
        return new_img
    else:  # this is the same as above, except it saves all the files.
        for x, y, (r, g, b) in new_img:
            colour = create_color(r_chan[counter], g_chan[counter], b_chan[counter])
            rgb.append(colour)
            set_color(new_img, x, y, colour)
            counter += 1

        save_as(new_img, "returns/combined_image.png")
        show(load_image("combined_image.png"))
        return (r_chan, g_chan, b_chan, rgb)


def extreme_contrast(image: Image):
    """ Given an image, the r, g, b components are altered to be extremely contrasted.
    Written by Alia Nichol (#101143486).
    >>> extreme_contrast("miss_sullivan.jpg")
    """
    new_image = copy(image)

    for x, y, (r, g, b) in new_image:  # Reads through each pixel in the chosen image

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


def _adjust_component(comp: int) -> int:  # enters a red, green, or blue component
    """ Returns the midpoint of a component
    """
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

def posterize(image: Image) -> Image:
    """ posterizes the image by setting each r, g, b value to the midpoint of it's quadrant
    Written by: Emilio Lindia
    """
    new_image = copy(image)  # assigns new image as a copy of original
    for pixel in image:  # examines all pixels in the new image
        x, y, (r, g, b) = pixel
        (r, g, b) = (_adjust_component(r), _adjust_component(g), _adjust_component(b))
        new_color = create_color(r, g, b)  # inserts rgb values into adjust component function to change rgb values
        set_color(new_image, x, y, new_color)
    show(new_image)
    return image


def sepia(img: Image, disp: bool = True, save: bool = False) -> Image:
    """ Adjusts the r, g, and b values of an image to create a sepia image.
    Written by Anthony Luo
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


"""code for two and three tone below"""
tones = {"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0), "lime": (0, 255, 0), "blue": (0, 0, 255),
         "yellow": (255, 255, 0), "cyan": (0, 255, 255), "magenta": (255, 0, 255), "gray": (128, 128, 128)}


def two_tone(image: Image, CR1, CR2: str) -> Image:
    """
    Returns a copy of the loaded image with only the chosen two pixel colours

    Preconditions:

    colour_1 must be brighter than colour_2

    The only recognized colour inputs (for colour_1 and colour_2) are the
    the following:

    black
    white
    red
    lime
    blue
    cyan
    magenta
    gray

    By: Abdelrahman Alatoom

    """
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
    """

    Returns a copy of the loaded image with only the three chosen pixel colours

    Preconditions:

    The only recognized colour inputs (for colour_1, colour_2, colour_3) are the the following:

    black
    white
    red
    lime
    blue
    cyan
    magenta
    gray

    >>>three_tone(image,black,blue,red)

    By: Abdelrahman Alatoom
    """

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
    """ Using a selected image, this function alters the r, g, b components of an image to return a new image\
    that looks like a pencil sketch (aka edge detected image). The pixels in the image are changed to either black\
    or white depending on the difference in contrast between the two pixels.

    Written by Alia Nichol (#101143486).

    >>> detect_edges(choose_file(), 12)
    <Cimpl.Image object at 0x0000017986874A20>
    """
    new_image = copy(image)

    for y in range(get_height(new_image) - 1):  # Begins at the first row and moves down through each row in the image.
        for x in range(get_width(new_image)):

            r, g, b = (get_color(new_image, x, y))
            r1, g1, b1 = (get_color(new_image, x, y + 1))

            if abs(((r + g + b) // 3) - ((r1 + g1 + b1) // 3)) > threshold:  # Changes the pixels to black if
                # contrast between the two pixels is high.
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:  # Changes the pixels to white is the contrast between the two pixels is low
                set_color(new_image, x, y, create_color(255, 255, 255))

    show(new_image)
    return new_image


def _avg_bright(colour: Tuple[int]) -> int:
    """Returns avg brightness of three colours
    written by anthony luo
    """
    r, g, b = colour
    return (r + g + b) / 3


def _new_col(colour: Tuple[int]) -> int:
    """ Returns a colour type from a colour
    written by Anthony Luo
    """
    # TODO: try to see if there's a way to integrate this directly into the program
    r, g, b = tuple(colour)
    return create_color(r, g, b)


def detect_edges_better(img: Image, thresh: int = 0,\
                        disp: bool = True, save: bool = False):
    """ return an image with the edge detects.
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

    for y in range(height - 1):  # starts at the first level, then moves down
        for x in range(width - 1):
            # compares brightness between two images and then resets colours.
            if abs(_avg_bright(tuple(get_color(img, x, y))) - _avg_bright( \
                    tuple(get_color(img, x, y + 1)))) > thresh or abs( \
                    _avg_bright(tuple(get_color(img, x, y))) - \
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


def flip_horizontal(image):
    h = get_height(image)
    w = get_width(image)
    new_image = create_image(w, h)
    for pixel in image:
        x, y, (r, g, b) = pixel

        new_color = create_color(r, g, b)
        set_color(new_image, x - 1, h - y - 1, new_color)
    show(new_image)
    return new_image


def flip_vertical(img):
    """
    A photo is displayed. The function is called and the rgb values for each /
    pixel is printed. ...
    ex:
    photo facing left, creates photo facing right

    "Written by Emilio Lindia: 101143244"

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
    END OF CODE


    CODE HAS BEEN ATTRIBUTED FROM GIVEN FILES FOUND ON CULEARN
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
        # Print(r,g,b)                    #Prints the r g b values of every pixel
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
