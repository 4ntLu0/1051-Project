from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
import os

all_commands = ["L", "l", "S", "s", "2", "3", "X", "x", "T", "t", "P", "p", "E", "e", "I", "i", "V", "v", "H", "h", "Q",
                "q"]


def prompt() -> str:
    """
    Prompts the user for an input. Checks validility of the input before the filter is applied.     
    """
    command = None
    while command not in all_commands:
        print("Prompt is not valid. Please Try Again.")
        command = input(
            "Please enter a command from the following list: \n L)oad Image S)ave-as \n 2)-tone 3)-tone X)treme contrast T)int sepia P)osterize \n E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip \n Q)uit \n : ")
        command = command.upper()
<<<<<<< HEAD
        return (command)
    
    
def image_load():
    
    
=======
    return command
>>>>>>> b3435bc9dea81f5ac2b52cb570076b1c369e7039


def image_load():
    image = input("Name of image to load:")
    loaded_image = load_image(image)  # use choose?
    show(loaded_image)
    print("Image has been loaded")
    load = True
    return loaded_image, load



def apply_filter(selection: str, image: Image) -> Image:
    """
    Applies the selected filter.
    """

    functions = [two_tone, three_tone, extreme_contrast, sepia, posterize, detect_edges, detect_edges_better,
                 flip_vertical, flip_horizontal]
    prompts = ['2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H']
    if selection == '2':
        color1 = input("First colour:")
<<<<<<< HEAD
        color2 = input("Seo
        # two tone filter selected
=======
        color2 = input("Second colour:")
        new_image = two_tone(loaded_image, color1, color2)
        show(new_image)
        print("Two tone filter has been applied")
>>>>>>> b3435bc9dea81f5ac2b52cb570076b1c369e7039
    elif selection == '3':
        color1 = input("First colour:")
        color2 = input("Second colour:")
        color3 = input("Third colour:")
        new_image = three_tone(loaded_image, color1, color2, color3)
        show(new_image)
        print("Three tone filter has been applied")        
    elif selection == 'E'
        thresh = input('Threshold: ')
        new_image = detect_edges(loaded_image, thresh)
        show(new_image)
        print("Edge Detection filter has been applied")
    elif selection == 'I':
        thresh = input('Threshold: ')
        new_image = detect_edges_better(loaded_image, thresh)
        show(new_image)
        print("Improved Edge Detection filter has been applied")
    else:
        for index in range(len(prompts)):
            if selection == prompts[index]:
                fn = functions[index]
                return fn(image)


def main():
    image = load_image(choose_file())
    is_loaded = False
    while True:
        command = prompt()
        if command == 'L':
            is_loaded = True
            image = image_load()
            img = copy(image)
        img = apply_filter(command, img)


if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
    main()
