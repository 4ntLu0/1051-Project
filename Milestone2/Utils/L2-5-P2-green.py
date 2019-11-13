from Cimpl import *

image = load_image('p2-original.jpg')  # loads the desired image from a given file


def green_filter( image1: Image ) -> Image:
    """Given an image from a selected file, the function sets all the pixels in the image to the color green and saves it as a new image. 
    Alia Nichol """
    image = copy(image1)  # creates a copy of the image so it is not overrided once the new image is created
    show(image)

    for x, y, (r, g, b) in image:  # reads through each pixel in the image
        green = create_color(0, g, 0)
        set_color(image, x, y, green)  # sets all the pixels of defined locations in that image to the color green

    save_as(image, 'green_channel.png') # saves the image 
    show(load_image('green_channel.png'))
    print('green_channel saved as new image')

    return image1


def test_green() -> None:
    '''  Test function for green filter that tests if all the pixels in the image have been changed to green.
    Written by Alia Nichol.
    >>> test_green()
    '''
    image1 = green_filter(image)

    for x, y, (r, g, b) in image1:
        if r == 0 and b == 0: # checks that all of the pixels are green, and not blue nor red
            print("PASS")
            return

    else:
        print("FAIL") # Fails if there are pixels of the color red or blue
        return
