from Cimpl import load_image, choose_file, get_color, Image, get_width, get_height, set_color, create_color, create_image, show, save_as

'''
should be creating image with predet contrast?
create rows of pixels, BRIGHT dark BRIGHT with a little variance in between (ie, two halves?)

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
    2    low    low    high   low    low     --->    2   Blank   Blank  Blank  Blank   Blank
    3    low    low    low    low    low     --->    3   Blank   Blank  Blank  Blank   Blank
    
    --- Side - Side testing:
        2,2 - 3,2 & 3,2 - 4,2.
    --- Up - Down testing:
        3,1 - 3, 2 & 3,2 - 3,3.
    --- Diagonal Testing
        2,1 & 2,3 & 3,2 & 4,1 & 4,3

Memefied by Anthony Luo    
'''

