from Cimpl import *

image = load_image(choose_file())
image = copy(image)

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)


def two_tone(image: Image, CR1, CR2: str) -> Image:
    '''
    
    Returns a copy of the loaded image with only the chosen two pixel colours
    
    Preconditions:
    
    colour_1 must be brighter than colour_2
    
    The only recognized colour inputs (for colour_1 and colour_2) are the 
    the following:
    
    black
    white
    red
    lime
    blue
    cyan
    magenta
    gray
    
    By: Abdelrahman Alatoom
    
    '''
    image = copy(image)

    for x, y, (r, g, b) in image:

        tone1 = create_color(CR2[0], CR2[1], CR2[2])
        tone2 = create_color(CR1[0], CR1[1], CR1[2])

        if ((r + g + b) / 3) <= 200:
            set_color(image, x, y, tone1)

        if ((r + g + b) / 3) >= 201:
            set_color(image, x, y, tone2)

    return show(image)


def three_tone(image: Image, CR1, CR2, CR3: str) -> Image:
    '''
    
    Returns a copy of the loaded image with only the three chosen pixel colours
    
    Preconditions:
    
    The only recognized colour inputs (for colour_1, colour_2, colour_3) are the the following:
    
    black
    white
    red
    lime
    blue
    cyan
    magenta
    gray
    
   
   
    >>>three_tone(image,black,blue,red)
    
    By: Abdelrahman Alatoom
    '''

    image = copy(image)

    for x, y, (r, g, b) in image:

        tone1 = create_color(CR1[0], CR1[1], CR1[2])
        tone2 = create_color(CR2[0], CR2[1], CR2[2])
        tone3 = create_color(CR3[0], CR3[1], CR3[2])

        if ((r + g + b) / 3) <= 84:
            set_color(image, x, y, tone2)

        if 85 <= ((r + g + b) / 3) <= 170:
            set_color(image, x, y, tone1)

        if ((r + g + b) / 3) >= 171:
            set_color(image, x, y, tone3)
    return show(image)