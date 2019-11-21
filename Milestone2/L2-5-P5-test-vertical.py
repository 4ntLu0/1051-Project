from Cimpl import*
from L2_5_P5_vertical import *


def test_flip_vertical(image: Image) -> Image:
    """ Writen by Abdelrahman Alatoom. Function tests that all values of the x axis of the inputted image (into the flip_vertical function) are assigned to to their negative counterparts"""
    vertical_image = flip_vertical(image)
    for x in range(get_width(image)):
        
        for y in range(get_height(image)):
            original_colour = get_color(image, x, y)
        
        
    for x in range(get_width(vertical_image)):
        
        for y in range(get_height(vertical_image)):
            vertical_colour = get_color(vertical_image, -x, y)
            
    if original_colour == vertical_colour:
        print('Test Passed')
    else: print('Test Failed')
    
if __name__ == '__main__':
    limg = load_image("miss_sullivan.jpg")
    image = copy(limg)
    test_flip_vertical(image)