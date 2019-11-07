from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height


def combine():
    """ Combines three images red_channel, green_channel, and blue_channel (rgb) to form a
    full colour image saved to combined_image.jpg.
    Written by Anthony Luo
    """
    # loads images in
    r_img = load_image('red_channel.jpg')
    g_img = load_image('green_channel.jpg')
    b_img = load_image('blue_channel.jpg')

    # creates new image with hard dimensions.
    # TODO: create a way to dynamically assign height
    new_img = Image(width=640, height=480)

    # creates the different channels for RGB
    # TODO: figure out a way to store these in a numpy matrix?
    r_chan = []
    g_chan = []
    b_chan = []

    for x, y, (r, g, b) in r_img: #grabs r value
        r_chan.append(r)

    for x, y, (r, g, b) in g_img: # grabs g value
        g_chan.append(g)

    for x, y, (r, g, b) in b_img: # grabs b value
        b_chan.append(b)

    counter = 0
    for x, y, (r, g, b) in new_img:
        colour = create_color(r_chan[counter], g_chan[counter], b_chan[counter])
        set_color(new_img, x, y, colour)
        counter += 1

    save_as(new_img, 'combined_image.jpg')
    show(load_image('combined_image.jpg'))

combine()