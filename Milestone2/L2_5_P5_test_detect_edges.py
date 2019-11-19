from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, \
    create_image, show, save_as
from typing import Tuple
from L2_5_P5_detect_edges import detectEdges


def testEdgeDetector():
    ''' Tests to make sure that edge detection is functioning as it should with certain threshold values.
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
    '''
    error_list = []
    test_pass = True  # so far, all tests have passed.
    test_img, compare_img = _createImages(0)
    # this thresh of 100 is a decent average to be testing on.
    test_img = detectEdges(test_img, 100, False)
    print('### testing normal thresh ###')
    for x, y, (r, g, b) in test_img:
        if (r, g, b) == tuple(get_color(compare_img, x, y)):
            pass
        else:
            print('-- error at', x, y)
            print('test img: ', r, g, b, 'should be: ', tuple(get_color(compare_img, x, y)))
            test_pass = False

    test_img, compare_img = _createImages(1)
    # this thresh of 255 is higher than we should ever be getting
    test_img = detectEdges(test_img, 255, False)
    print('### testing high thresh ###')
    for x, y, (r, g, b) in test_img:
        if (r, g, b) == tuple(get_color(compare_img, x, y)):
            pass
        else:
            print('-- error at', x, y)
            print('test img:', r, g, b, 'should be:', tuple(get_color(compare_img, x, y)))
            test_pass = False

    if test_pass:
        print('### Testing done ### \n--- PASSES')
    else:
        print('### Testing done ### \n--- FAILS')

    print(error_list)


def _createImages(ver: int) -> Tuple[Image]:
    """ Creates the test images for each 'version' of the test.
    Written by Anthony Luo
    :param ver: version0: modified compare
                version1: non-modifide compare
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


if __name__ == '__main__':
    testEdgeDetector()
