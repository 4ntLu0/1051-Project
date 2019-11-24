from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, create_image
import os
from typing import NewType

original_img = load_image('p2-original.jpg')

Image = NewType('Image', str)
checked = False


def createRed( img: Image, verify: bool = True, log: bool = False ):
    """ Saves a new image which constitutes only the red channel of an image img
    Written by Anthony Luo
    :param img: Original image
    :type img: Image
    :param verify: Whether or not to verify the image (ie, show it to the user)
    :type verify: bool
    :param log: whether or not to save image data to log files
    :type log: bool
    :return: None
    :rtype: NoneType
    >>> image = load_image(choose_image())
    >>> createRed(image)
    >>> show(image)
    """
    image = copy(img)
    if verify:
        show(image)  # shows the original image

    # checks if you are logging or not (once, at the start, instead of everytime)
    if log:
        try:
            os.remove('redImgLog.txt')
        except:
            pass
        red_log = open('redImgLog.txt', 'a')  # creates a NEW log file
        for x, y, (r, g, b) in image:  # reads through the image pixel by pixel
            red = create_color(r, 0, 0)  # creates new 'colour' tuple

            # remaps each x,y coordinate to new colour
            set_color(image, x, y, red)
        str1 = f'{x:03}' + f'{y:03}' + f'{r:03}' + f'{g:03}' + f'{b:03}' + f'{red[0]:03}' + \
               f'{red[1]:03}' + f'{red[2]:03}' + '\n'  # creates logger string
        red_log.write(str1)  # saves string
    else:
        for x, y, (r, g, b) in image:  # reads through the image pixel by pixel
            red = create_color(r, 0, 0)  # creates new 'colour' tuple

            # remaps each x,y coordinate to new colour
            set_color(image, x, y, red)

    save_as(image, 'red_channel.png')  # saves as a new image
    if verify:
        show(load_image('red_channel.png'))  # shows the image to double check

    print('red_channel created')  # notifies user


def testRed( ori_img: Image ):
    """ Tests the red image to ensure there are no traces of blue or green in the image.
    written by Anthony Luo
    :param ori_img: Original image
    :type ori_img: load_image('')
    >>> test_red( load_image(choose_image()))
    'Red PASSES'
    """
    createRed(ori_img, False, True)  # runs the red function in debugging mode.
    show(ori_img)  # shows the original image, to ensure that it is correct
    show(load_image('red_channel.png'))  # shows the red image, to ensure that it's correct.
    log = open('redImgLog.txt', 'r')  # opens logger
    fail = False
    for line in log:
        if line[18:24] == str('000000'):  # double checks that last 6 digits (ggg,bbb) are all 0
            pass
        else:
            print('fails with log line: ', line, '\n')  # notifies user of fail
            print(line[18:24])
            fail = True  # has failed tests
    if fail:
        return ('1')  # error code 1
    else:
        print('Red PASSES')



def createBlue( img ):
    """ the function createBlue displays the original image, once closed it displays the image with a blue filter

    -Emilio Lindia
    """
    image = copy(img)
    # image = load_image('p2-original.jpg')  # loads the original colourless picture
    show(image)  # shows original image

    new_image = image

    for x, y, (r, g, b) in image:  # examines all pixels
        blue = create_color(0, 0, b)  # creates a 100% blue filter

        set_color(new_image, x, y, blue)

    save_as(new_image, 'blue_channel.png')  # saves the blue filter as a new image
    show(load_image('blue_channel.png'))  # shows image

    print('blue_channel saved as new_image')
    return new_image


def test_blue() -> None:
    '''This is the test function for the blue filter.

    it tests if all pixels are blue or if they contain any traces of green or red.
    '''
    image1 = createBlue('p2-original.jpg')

    for x, y, (r, g, b) in image1:
        if r == 0 and g == 0:  # if there is no trace of red or green
            print("PASS")  # passed the test
            return

    else:
        print('FAILS')
        return


def green_filter( image1: Image ) -> Image:
    """Alia Nichol

    """
    image = copy(image1)  # creates a copy of the image so it is not overrided
    show(image)

    for x, y, (r, g, b) in image:  # reads through the image
        green = create_color(0, g, 0)
        set_color(image, x, y, green)  # sets all the pixels of defined locations in that image to the color

    save_as(image, 'green_channel.png')
    show(load_image('green_channel.png'))
    print('green_channel saved as new image')

    return image1


def test_green() -> None:
    '''Test function for green filter.

    Tests if the pixels are green.

    >>> test_green()
    '''
    image1 = green_filter(image)

    for x, y, (r, g, b) in image1:
        if r == 0 and b == 0:
            print("PASS")
            return

    else:
        print("FAIL")
        return


def combine( log = False ):
    """ Combines three single-colour images (red, green, and blue) into a final image.
    Written by Anthony Luo
    :param log: Determines whether or not to return a datalog
    :type log: Defaults to False, ie no log
    :return: returns logs as tuple if log
    >>> combine()
    >>> show(load_image('combined_image.png'))
    """
    # loads images in
    r_img = load_image('red_channel.png')
    g_img = load_image('green_channel.png')
    b_img = load_image('blue_channel.png')

    # creates new image with hard dimensions.
    # TODO: create a way to dynamically assign height
    new_img = create_image(640, 480)

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
    >>> testCombine()
    'Combined image Passes'
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
    print('Combined image PASSES')

if __name__ == '__main__':
    """main function to run all the things!
    Written by Anthony Luo
    """
    print('running red')
    createRed(original_img, True)
    print('done red' + '\n' + 'running green')
    green_filter(original_img)
    print('done green' + '\n' + 'running blue')
    createBlue(original_img)
    print('done blue' + '\n' + 'running combined')
    combine()
    while not checked:
        test_check = input('Test? [Y/N]')
        if test_check == 'Y':
            testRed(original_img)
            test_green()
            test_blue()
            testCombine()
            checked = True
        elif test_check == 'N':
            print('Done creating and combining images!')
            checked = True
        else: 
            print('Ipnut not recognized, please try again')
    print('exiting! byebye!')