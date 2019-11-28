from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color, get_width, get_height, copy
from simple_Cimpl_filters import grayscale

tones = {'black' : (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'lime': (0, 255, 0), 'blue': (0, 0, 255),
         'yellow': (255, 255, 0), 'cyan': (0, 255, 255), 'magenta': (255, 0, 255), 'gray': (128, 128, 128)}

def two_tone(image, CR1: str, CR2: str):
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
    
    tone1r, tone1g, tone1b = tones[CR1]
    tone2r, tone2g, tone2b = tones[CR2]
    
    tone1 = create_color(tone1r, tone1g, tone1b)
    tone2 = create_color(tone2r, tone2g, tone2b)
    
    for x, y, (r, g, b) in image:
        average = ((r + g + b) / 3)

        if average <= 200:
            set_color(image, x, y, tone1)

        else:
            set_color(image, x, y, tone2)
    
    show(image)
    return image

if __name__ == '__main__':
    image = load_image(choose_file())  # Loads the desired image from a given file.
    show(image)
    new_image = copy(image)  
    ## Creates a copy of the image so it is not overrided when the new image is returned.
    two_tone(image, 'black', 'red')