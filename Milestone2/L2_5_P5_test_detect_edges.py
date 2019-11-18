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
    high                        should only return edge
    low                                            no edge
    low                                            no edge
make sure that there is no diagonal influence
    low    low    low    low    low
    low    low    high   low    low
    
This should create final test image
         1      2      3      4      5                  1      2       3       4       5
    1    high   low    low    low    high    --->     1   Edge   Blank   Blank   Blank   Edge
    2    low    low    high   low    low     --->     2   Blank  Edge    Blank   Blank   Edge
    3    low    high   high   low    high    --->     3   
    
Memefied by Anthony Luo    
'''

