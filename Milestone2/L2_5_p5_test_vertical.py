from Cimpl import *
image = load_image(choose_file())



def flip_vertical(image: image) -> Image:
    
    
   
    vertical_image = copy(image)

    for x in range(get_width(image)):
        for y in range(get_height(image)):
            flipped_color = get_color(image, -x, y)
            set_color(vertical_image, x, y, flipped_color)

    show(vertical_image)
    return vertical_image


def test_flip_vertical(image: Image) -> Image:
    """ Writen by Abdelrahman Alatoom (101147742). Function tests that all values of the x axis of the inputted image (into the flip_vertical function) are assigned to to their negative counterparts"""
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
        
    
    
