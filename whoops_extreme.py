from Cimpl import *


def extreme_contrast( image ):
    """ Given an image, the r, g, b components are altered to be extremely contrasted.
    Written by Alia Nichol (#101143486).
    >>> extreme_contrast("miss_sullivan.jpg")
    """

    for x, y, (r, g, b) in image:  # Reads through each pixel in the chosen image.
        if 0 < r <= 127:
            contrast = create_color(0, g, b)
            set_color(image, x, y, contrast)
        else:
            contrast = create_color(255, g, b)
            set_color(image, x, y, contrast)  
            
        if 0 < g <= 127:
            contrast = create_color(r, 0, b)
            set_color(image, x, y, contrast)
        else:
            contrast = create_color(r, 255, b)
            set_color(image, x, y, contrast)
            
        if 0 < b <= 127:
            contrast = create_color(r, g, 0)
            set_color(image, x, y, contrast)
        else:
            contrast = create_color(r, g, 255)
            set_color(image, x, y, contrast)            
       
    save_as(image, 'returns/contrast_channel.png')
    show(load_image('returns/contrast_channel.png'))
    print('contrast_channel saved as new image')

    return image

if __name__ == '__main__':
    image = load_image(choose_file())  # Loads the desired image from a given file.
    show(image)
    new_image = copy(image)  
    ## Creates a copy of the image so it is not overrided when the new image is returned.
    extreme_contrast(image)