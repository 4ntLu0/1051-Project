from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, \
   create_image, show, save_as, copy


def detectEdges(image: Image, threshold: int, disp=True) -> Image:
    """ Using a selected image, this function alters the r, g, b components of an image to return a new image that looks like a pencil sketch (aka edge detected image). The pixels in the image are changed to either black or white depending on the threshold value inputed by the user. 
    
    Written by Alia Nichol (#101143486)
    
    >>> edgeDetect(image, 12)
    480 640 
    """

    # new_image = create_image(width, height - 1) # subtract one because you lose one row of data due to bottom row
    #print(height, width)

    new_image = copy(image)

    # begins at the first row and moves down through each row in the image
    for y in range(get_height(image) - 1):
        for x in range(get_width(image)):

            r, g, b = (get_color(image, x, y))
            r1, g1, b1 = (get_color(image, x, y + 1))

            if abs(((r + g + b) // 3) - ((r1 + g1 + b1) // 3)) > threshold:
                # changes the pixels to black if contrast between the two pixels is high
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:
                # changes the pixels to white is the contrast between the two pixels is low
                set_color(new_image, x, y, create_color(255, 255, 255))

    if disp:
        show(new_image)
    return new_image


if __name__ == '__main__':
    # by changing the threshold value, the ratio of white to black pixels
    detectEdges(load_image(choose_file()), 12)
    # changes


# def edgeTest() -> None:
    #fails = 0

    #threshold = int(input("Please enter a threshold value:"))
    #new_img = detect_edges(image, threshold)

    # for y in range(get_height(image) - 1):

        # for x in range(get_width(image) - 1):

            #r, g, b = tuple(get_color(image, x, y))
            #r1, g1, b1 = tuple(get_color(image, x, y + 1))
            #r2, g2, b2 = tuple(get_color(image, x + 1, y))

            # if abs(r +

    # if fails == 0:
        # print("PASS")
    # else:
        # print("FAIL")




