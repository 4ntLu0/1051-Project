"""L2_5 SIPE interactive UI. Submitted December 1, 2019.
This code has been attributed from given files on cuLearn.
Contact information may be obtained from carleton university
Group Leader: Anthony Luo"""

from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
from simple_Cimpl_filters import grayscale
import os
from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple


def test_red(ori_img: Image):
    """ Tests the red image to ensure there are no traces of blue or green in the image.
    written by Anthony Luo
    :param ori_img: Original image
    :type ori_img: load_image('')
    >>> test_red( load_image(choose_image()))
    'Red PASSES"
    """
    create_red(ori_img, False, True)  # runs the red function in debugging mode.
    show(ori_img)  # shows the original image, to ensure that it is correct
    show(load_image("red_channel.png"))  # shows the red image, to ensure that it's correct.
    log = open("redImgLog.txt", "r")  # opens logger
    fail = False
    for line in log:
        if line[18:24] == str("000000"):  # double checks that last 6 digits (ggg,bbb) are all 0
            pass
        else:
            print("fails with log line: ", line, "\n")  # notifies user of fail
            print(line[18:24])
            fail = True  # has failed tests
    if fail:
        return ("1")  # error code 1
    else:
        print("Red PASSES")


def test_blue() -> None:
    """This is the test function for the blue filter.

    it tests if all pixels are blue or if they contain any traces of green or red.
    """
    image1 = create_blue("p2-original.jpg")

    for x, y, (r, g, b) in image1:
        if r == 0 and g == 0:  # if there is no trace of red or green
            print("PASS")  # passed the test
            return

    else:
        print("FAILS")
        return


def test_green() -> None:
    """Test function for green filter.

    Tests if the pixels are green.

    >>> test_green()
    """
    image = load_image(choose_file())
    image1 = green_filter(image)

    for x, y, (r, g, b) in image1:
        if r == 0 and b == 0:
            print("PASS")
            return

    else:
        print("FAIL")
        return


def test_combine():
    """Tests to ensure that combine is made up of the constituent rgb parts.
    >>> test_combine()
    "Combined image Passes"
    """
    log_r, log_g, log_b, log_rgb = combine(True)  # collects return from combine()

    # loads images
    r_img = load_image("red_image.png")
    g_img = load_image("green_image.png")
    b_img = load_image("blue_image.png")

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
    combined_img = load_image("combined_image.png")
    ori_img = load_image("p2-original.jpg")
    for x, y, (r, g, b) in ori_img:
        rgb.append((r, g, b))
    count = 0

    for x, y, (r, g, b) in combined_img:  # checks to ensure that rgb constituents are correct
        if (r_chan[count], g_chan[count], b_chan[count]) == (log_r[count], log_g[count], log_b[count]) and rgb[count] \
                == (r, g, b):
            pass
        else:
            print("fails at", x, y, r, g, b)
            exit()
        count += 1
    print("Combined image PASSES")


def test_horizontal():
    """
    Test function which tests the functionality of the filtwr which flips
    images horizontally.
    After importing the filter function, the test function creates an image
    of size 1,4 (in terms of x,y).
    The colours are retrieved from this new image and they are compared with
    that of another image of equal size, except reversed y order.(horizontally
    flipped)
    If the pixels match, the function has flipped the image properly

     " Written by Emilio Lindia: 101143244 "

    DOCSTRING TESTING (How to run the code)
    Code is run
    image of size (1,4) is displayed somewhere on screen
    Close the image
    Refer to shell
    If test was run correctly and the filter passed all tests, PASS should be
    printed
    END OF CODE


    CODE HAS BEEN ATTRIBUTED FROM GIVEN FILES FOUND ON CULEARN
    """
    image = create_image(1, 4)  # Creates image of size (1,4)
    set_color(image, 0, 0, create_color(0, 0, 0))
    set_color(image, 0, 1, create_color(1, 1, 1))
    set_color(image, 0, 2, create_color(3, 5, 4))
    set_color(image, 0, 3, create_color(10, 30, 6))

    flipped_image = create_image(1, 4)  # Creates image of size (1,4)
    set_color(flipped_image, 0, 0, create_color(10, 30, 6))
    set_color(flipped_image, 0, 1, create_color(3, 5, 4))
    set_color(flipped_image, 0, 2, create_color(1, 1, 1))
    set_color(flipped_image, 0, 3, create_color(0, 0, 0))
    # Notice this second image that is created possesses opposite RGB values
    # This accounts for the images to be identical, except for the fact that \
    # he flipped_image is the upside-down version

    result_image = flip_horizontal(image)

    for x, y, (r, g, b) in result_image:
        if (r, g, b) == tuple(get_color(flipped_image, x, y)):
            print("PASS")
        else:
            print("FAIL")


# If the images are equal, then the filter has properly flipped the image
# printing PASS will be an indication that this is the case
# Otherwise, FAIL would be printed

def _create_images(ver: int) -> Tuple[Image, Image]:
    """ Creates the test images for each "version" of the test.
    Written by Anthony Luo
    :param ver: version0: modified compare
                version1: non-modified compare
    :type ver: int
    """
    test_img = create_image(5, 3, create_color(30, 10, 20))
    set_color(test_img, 2, 1, create_color(250, 240, 230))
    compare_img = create_image(5, 3, create_color(255, 255, 255))
    if ver == 0:
        set_color(compare_img, 2, 0, create_color(0, 0, 0))
        set_color(compare_img, 2, 1, create_color(0, 0, 0))
        return test_img, compare_img
    if ver == 1:
        return test_img, compare_img


def test_edge_detect(pass_last_line: bool = True):
    """ Tests to make sure that edge detection is functioning as it should with certain threshold values.
    Test cases --- (high / low refer to brightness levels).
    directly below it is right colour
        high
        low
    make sure ones to left/right are not influenced
        low    high                 should not return edges at ALL
        low    high
    make sure that it is not influenced by the one above it
        high                        should only return:   edge
        low                                               no edge
        low                                               no edge
    make sure that there is no diagonal influence
        low    low    low    low    low
        low    low    high   low    low
        low    low    low    low    low

    This should create final test image below:
             1      2      3      4      5                    1       2      3      4       5
        1    low    low    low    low    low     --->    1   Blank   Blank  Edge   Blank   Blank
        2    low    low    high   low    low     --->    2   Blank   Blank  Edge   Blank   Blank
        3    low    low    low    low    low     --->    3   Blank   Blank  Blank  Blank   Blank

        --- Side - Side testing:
            2,2 - 3,2 & 3,2 - 4,2.
        --- Up - Down testing:
            3,1 - 3, 2 & 3,2 - 3,3.
        --- Diagonal Testing
            2,1 & 2,3 & 3,2 & 4,1 & 4,3

    The same test will be run with a threshold higher than expected, which should return a completely blank image.
    Written by Anthony Luo #101145222

    >>> detect_edges_better_test()
    ### testing normal thresh ###
    -- normal thresh testing done --

    ### testing high thresh ###
    -- high thresh testing done --

    ### Testing done ###
    --- PASSES ALL TESTS ---
    """
    error_list = []
    test_pass = True  # so far, all tests have passed.
    test_img, compare_img = _create_images(0)
    # this thresh of 100 is a decent average to be testing on.
    test_img = detect_edges(test_img, 100)
    print("### testing normal thresh ###")
    for x, y, (r, g, b) in test_img:
        if pass_last_line and y == 2:
            pass  # does not test last line as most edge-detectors are not equipped to handle this.
        elif (r, g, b) == tuple(get_color(compare_img, x, y)):
            pass
        else:
            print("-- error at", x, y)
            print("test img: ", r, g, b, "should be: ",
                  tuple(get_color(compare_img, x, y)))
            test_pass = False
    print("-- normal thresh testing done --\n")

    test_img, compare_img = _create_images(1)
    # this thresh of 255 is higher than we should ever be getting
    test_img = detect_edges(test_img, 255)
    print("### testing high thresh ###")
    for x, y, (r, g, b) in test_img:
        if pass_last_line and y == 2:
            pass  # does not test last line as most edge-detectors are not equipped to handle this.
        elif (r, g, b) == tuple(get_color(compare_img, x, y)):
            pass
        else:
            print("-- error at", x, y)
            print("test img:", r, g, b, "should be:",
                  tuple(get_color(compare_img, x, y)))
            test_pass = False
    print("-- high thresh testing done --\n")

    if test_pass:
        print("### Testing done ### \n--- PASSES ALL TESTS ---")
    else:
        print("### Testing done ### \n--- FAILS ---")

    print(error_list)

    def detect_edges_better_test() -> None:
        """Test function that checks if the r, g, b components have been correctly altered by the Improved Edge
        Detection filter.
        If the pixels are correctly changed to either white or black, the test function returns "PASS" to the user.
        If this is not the case,
        the test function returns "FAIL".

        Written by Alia Nichol (#101143486).
        >>> detect_edges_better_test(image)
        PASS

        >>> detect_edges_better_test(image)
        FAIL
        """

        original_image = create_image(7, 3, color=create_color(10, 10,
                                                               10))  # Creates image that is width 6 and height 2
        # set to a dark colour.
        bright = create_color(250, 250, 250)
        set_color(original_image, 1, 0, bright)
        set_color(original_image, 2, 1, bright)
        set_color(original_image, 2, 2, bright)
        set_color(original_image, 3, 0, bright)
        set_color(original_image, 3, 1, bright)
        set_color(original_image, 3, 2, bright)
        set_color(original_image, 4, 1, bright)

        expected_image = create_image(7, 3, color=create_color(255, 255,
                                                               255))  # Creates image that is width 6 and height 2
        # set to a bright colour.
        black = create_color(0, 0, 0)
        set_color(expected_image, 0, 0, black)
        set_color(expected_image, 1, 0, black)
        set_color(expected_image, 1, 1, black)
        set_color(expected_image, 1, 2, black)
        set_color(expected_image, 2, 0, black)
        set_color(expected_image, 3, 0, black)
        set_color(expected_image, 4, 0, black)
        set_color(expected_image, 4, 1, black)
        set_color(expected_image, 4, 2, black)

        actual_image = detect_edges_better(original_image, 100,
                                           False)  # The Improved Edge Detection filter is applied to original_image.

        for x, y, (r, g, b) in actual_image:
            if (r, g, b) == tuple(get_color(expected_image, x,
                                            y)):  # Checks if the pixels in the actual image equal the ones in the
                # expected image.
                print("PASS")
            else:
                print("FAIL")


def test_flip_vertical() -> Image:
    """ Writen by Abdelrahman Alatoom. Function tests that all values of the x axis of the inputted image (into the
    flip_vertical function) are assigned to to their negative counterparts"""
    image = load_image(choose_file())
    vertical_image = flip_vertical(image)
    for x in range(get_width(image)):

        for y in range(get_height(image)):
            original_colour = get_color(image, x, y)

    for x in range(get_width(vertical_image)):

        for y in range(get_height(vertical_image)):
            vertical_colour = get_color(vertical_image, -x, y)

    if original_colour == vertical_colour:
        print("Test Passed")
    else:
        print("Test Failed")


def test_extreme():
    """ written by emilio """
    image = load_image(choose_file())  # loads a file that you choose
    image1 = extreme_contrast(image)  # image 1 is the updated version

    for x, y, (r, g, b) in image:
        print("this pixel has been analyzed correctly")

    else:
        print("this pixel has not been analyzed correctly")
    if image != image1:
        print("HAS THE ORIGINAL IMAGE BEEN CHANGED? : NO")
    else:
        print("HAS THE ORIGINAL IMAGE BEEN CHANGED? : YES")

    if image1 == extremeContrast(image1):
        print("the image contrast has: PASSED THE TEST")
    else:
        print("the image contrast has: FAILED THE TEST")


def posterize_filter_test(image):
    """
    This function tests if the posterize filter works properly by checking
    if the rgb of each pixel in the original image were set to the correct
    quadrant, which resulted in the final image
    By: Abdelrahman Alatoom
    """

    final_image = posterize_filter(image)

    for pixel in image:
        x, y, (r, g, b) = pixel
        original_color = get_color(image, x, y)
        final_color = get_color(final_image, x, y)
        r, g, b = final_color

        if 0 <= original_color[0] <= 63:
            if r != 31:
                print("Filter not working properly")
                return
        if 64 <= original_color[0] <= 127:
            if r != 95:
                print("Filter not working properly")
                return
        if 128 <= original_color[0] <= 191:
            if r != 159:
                print("Filter not working properly")
                return
        if 192 <= original_color[0] <= 255:
            if r != 223:
                print("Filter not working properly")
                return

        if 0 <= original_color[1] <= 63:
            if g != 31:
                print("Filter not working properly")
                return
        if 64 <= original_color[1] <= 127:
            if g != 95:
                print("Filter not working properly")
                return
        if 128 <= original_color[1] <= 191:
            if g != 159:
                print("Filter not working properly")
                return
        if 192 <= original_color[1] <= 255:
            if g != 223:
                print("Filter not working properly")
                return

        if 0 <= original_color[2] <= 63:
            if b != 31:
                print("Filter not working properly")
                return
        if 64 <= original_color[2] <= 127:
            if b != 95:
                print("Filter not working properly")
                return
        if 128 <= original_color[2] <= 191:
            if b != 159:
                print("Filter not working properly")
                return
        if 192 <= original_color[2] <= 255:
            if b != 223:
                print("Filter not working properly")
                return
    print("Filter working properly")


def sepiaTest() -> None:
    """Test function for the sepia filter that checks if all the r, g, b components have gotten the sepia filter
    applied to them. The function returns "PASS" if all the pixels are successfully changed. If "PASS" is returned,
    this indicates that the red component has increased by the correct percentage and the blue component has
    decreased by the correct percentage, ultimately applying the sepia filter. If not, the function returns "FAIL".

    Written by Alia Nichol.
    """
    img = create_image(3, 1)  # creates image
    set_color(img, 0, 0, create_color(10, 20, 50))
    set_color(img, 1, 0, create_color(80, 100, 180))
    set_color(img, 2, 0, create_color(200, 240, 243))

    test_img = sepia(img, disp=False, save=True)
    # check to see if worked
    # print(get_color(test_img, 0, 0))
    # print(get_color(test_img, 1, 0))
    # print(get_color(test_img, 2, 0))

    if (get_color(test_img, 0, 0) == create_color(28, 26, 23)) and \
            (get_color(test_img, 1, 0) == create_color(138, 120, 102)) and \
            (get_color(test_img, 2, 0) == create_color(245, 227, 211)):
        print("pass")
    else:
        print("fails")


def _setCol(tone: Tuple[int]):
    """ returns a colour created from a tuple with three integers.
        Written by Anthony Luo
        :param tone:
        :return: Colour
        """
    r = tone[0]
    g = tone[1]
    b = tone[2]
    return create_color(r, g, b)


def testThreeTone():
    tones = ["black", "white", "red", "lime", "blue",
             "yellow", "cyan", "magenta", "gray"]
    colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
               (255, 0, 255), (128, 128, 128)]
    """ Tests to ensure that three tone functions, that is: for any scenario, the lightest, middle, and darkest
    areas correspond to the assigned colours.
    Written by Anthony Luo
    :return:
    :rtype:
    """

    img = create_image(3, 1)  # creates image

    # sets colours
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(128, 128, 128))
    set_color(img, 2, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for i in range(len(tones)):  # goes through all the tones, ensuring each one functions as expected
        image = copy(img)  # prevents loss of quality / information through repeated use of the same image
        print("\n--- testing", tones[i], tones[i - 1], tones[i - 2], "---")
        test_img = three_tone(image, tones[i], tones[i - 1], tones[i - 2])  # runs image through the function

        # set colours, to be compared with
        col1 = _setCol(colours[i])
        col2 = _setCol(colours[i - 1])
        col3 = _setCol(colours[i - 2])

        # compares colours and prints test results.
        if (get_color(test_img, 0, 0) == col1) and (get_color(test_img, 1, 0) == col2) and (
                get_color(test_img, 2, 0) == col3):
            print("Passed")
        else:
            print("Fails at:", tones[i], tones[i - 1], tones[i - 2])


def testTwoTone():
    tones = ["black", "white", "red", "lime", "blue",
             "yellow", "cyan", "magenta", "gray"]
    colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
               (255, 0, 255), (128, 128, 128)]

    """ Tests to ensure that two tone creates an image with the colours specified.
    Tests both ranges, both High (255, 255, 255) and Low (0, 0, 0), with all tones in all positions.
    Written by Anthony Luo
    :return:
    :rtype:
    """

    img = create_image(2, 1)  # creates image

    # sets two ranges for the colours ( low / high )
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for i in range(len(tones)):  # iterates through to ensure all tones are tested
        image = copy(img)
        print("\n--- testing", tones[i], tones[i - 1], "---")
        test_img = two_tone(image, tones[i], tones[i - 1])

        col1 = _setCol(colours[i])
        col2 = _setCol(colours[i - 1])
        if (get_color(test_img, 0, 0) == col1) and (get_color(test_img, 1, 0) == col2):
            print("Passed")
        else:
            print("Fails at:", tones[i], tones[i - 1])
