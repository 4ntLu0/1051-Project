<<<<<<< HEAD
from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
import os

all_commands = ["L", "l", "S", "s", "2", "3", "X", "x", "T", "t", "P", "p", "E", "e", "I", "i", "V", "v", "H", "h", "Q", "q"]

def prompt() ->str :
    """
    Prompts the user for an input. Checks validility of the input before the filter is applied. 
    
    
    """
    command = None
    while command not in all_commands:
        print("Prompt is not valid. Please Try Again.")
        command = input("Please enter a command from the following list: \n L)oad Image S)ave-as \n 2)-tone 3)-tone X)treme contrast T)int sepia P)osterize \n E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip \n Q)uit \n Command:")
        
        return(command)

def is_valid():
    """
    checks the validity of the input
    :return:
    :rtype:
    """

def apply_filter(selection: str, image: Image) -> Image:
    """
    Applies the selected filter.
    """

    functions = [two_tone, three_tone, extreme_contrast, sepia, posterize, detect_edges, detect_edges_better, flip_vertical, flip_horizontal]
    prompts = ['2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H']
    for index in range(len(prompts)):
        if selection == prompts[index]:
            fn = functions[index]
            return fn(image)
    

def main():
    image = load_image(choose_file())
    while True:
        image = apply_filter(prompt(), image)

if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
=======
from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
import os

all_commands = ["L", "S", "2", "3", "X", "T", "P", "E", "I", "V", "H", "Q"]

def prompt() ->str :
    """
    Prompts the user for an input. Checks validility of the input before the filter is applied. 
    """
    command = None
    while command not in all_commands:
        print("Prompt is not valid. Please Try Again.")
        command = input("Please enter a command from the following list: \n L)oad Image S)ave-as \n 2)-tone 3)-tone X)treme contrast T)int sepia P)osterize \n E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip \n Q)uit \n Command:")
        
        return(command)

def is_valid():
    """
    checks the validity of the input
    :return:
    :rtype:
    """

def apply_filter(selection: str, image: Image) -> Image:
    """
    Applies the selected filter.
    """
    

def main():
    image = load_image(choose_file())
    while True:
        image = apply_filter(prompt(), image)

if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
>>>>>>> bb89ede549898162a93559a0cd6927469e9b5969
    prompt()