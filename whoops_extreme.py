
def extreme_contrast( image: Image ):
    """ Given an image, the r, g, b components are altered to be extremely contrasted.
    Written by Alia Nichol (#101143486).
    >>> extreme_contrast("miss_sullivan.jpg")
    """

    for x, y, (r, g, b) in image:  # Reads through each pixel in the chosen image.
        if 0 < r < 127:
            contrast = create_color(0, g, b)
            set_color(image, x, y, contrast)
        elif 0 < g < 127:
            contrast = create_color(r, 0, b)
            set_color(image, x, y, contrast)
        elif 0 < b < 127:
            contrast = create_color(r, g, 0)
            set_color(image, x, y, contrast)
        elif 128 < r < 255:
            contrast = create_color(255, g, b)
            set_color(image, x, y, contrast)
        elif 128 < g < 255:
            contrast = create_color(r, 255, b)
            set_color(image, x, y, contrast)
        elif 128 < b < 255:
            contrast = create_color(r, g, 255)
            set_color(image, x, y, contrast)

    save_as(image, 'returns/contrast_channel.png')
    show(load_image('returns/contrast_channel.png'))
    print('contrast_channel saved as new image')

    return image
