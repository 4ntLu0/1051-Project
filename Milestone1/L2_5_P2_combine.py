from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height


def combine( log = False ):
    """ Combines three single-colour images (red, green, and blue) into a final image.
    Written by Anthony Luo
    :param log: Determines whether or not to return a datalog
    :type log: Defaults to False, ie no log
    :return: returns logs as tuple if log
    """
    # loads images in
    r_img = load_image('red_channel.png')
    g_img = load_image('green_channel.png')
    b_img = load_image('blue_channel.png')

    # creates new image with hard dimensions.
    # TODO: create a way to dynamically assign height
    new_img = Image(width = 640, height = 480)

    # creates the different channels for RGB
    # TODO: figure out a way to store these in a numpy matrix?
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
        save_as(new_img, 'combined_image.png')  # save and show image
        show(load_image('combined_image.png'))
    else:  # this is the same as above, except it saves all the files.
        for x, y, (r, g, b) in new_img:
            colour = create_color(r_chan[counter], g_chan[counter], b_chan[counter])
            rgb.append(colour)
            set_color(new_img, x, y, colour)
            counter += 1

        save_as(new_img, 'combined_image.png')
        show(load_image('combined_image.png'))
        return (r_chan, g_chan, b_chan, rgb)


def testCombine():
    """Tests to ensure that combine is made up of the constituent rgb parts.
    TODO: I'm STILL not completely sure if this is how it's supposed to be...
    """
    log_r, log_g, log_b, log_rgb = combine(True)  # collects return from combine()

    # loads images
    r_img = load_image('red_image.png')
    g_img = load_image('green_image.png')
    b_img = load_image('blue_image.png')

    r_chan = []
    g_chan = []
    b_chan = []

    for x, y, (r, g, b) in r_img:  # grabs r value
        r_chan.append(r)

    for x, y, (r, g, b) in g_img:  # grabs g value
        g_chan.append(g)

    for x, y, (r, g, b) in b_img:  # grabs b value
        b_chan.append(b)

    rgb = []
    combined_img = load_image('combined_image.png')
    ori_img = load_image('p2-original.jpg')
    for x, y, (r, g, b) in ori_img:
        rgb.append((r, g, b))
    count = 0

    for x, y, (r, g, b) in combined_img:  # checks to ensure that rgb constituents are correct
        if (r_chan[count], g_chan[count], b_chan[count]) == (log_r[count], log_g[count], log_b[count]) and rgb[count] \
                == (r, g, b):
            pass
        else:
            print('fails at', x, y, r, g, b)
            exit()
        count += 1
    print('PASS')


testCombine()
