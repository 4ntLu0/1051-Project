from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
import os
import inspect

def prompt() ->str :
    """
    Prompts the user for an input. Checks validity before returning an
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

def apply_filter(selection, image: Image, additional1 = None, additional2 = None, additional3 = None) -> Image:
    """
    Applies the selected filter.
    """

    functions = [two_tone, three_tone, extreme_contrast, sepia, posterize, detect_edges, detect_edges_better, flip_vertical, flip_horizontal]
    prompts = ['2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H']
    if selection == '2':
        arg1 = input('Enter your first colour: ')
        arg2 = input('Enter your second colour:' )
        return two_tone(image, arg1, arg2)
    elif selection == '3':
        arg1 = input('Enter your first colour: ')
        arg2 = input('Enter your second colour: ')
        arg3 = input('Enter your third colour: ')
        return three_tone(image, arg1, arg2, arg3)
    elif selection == 'E':
        thresh = input('please enter your threshold value: ')
        return detect_edges(image, int(thresh))
    elif selection == 'I':
        thresh = input('Please enter you threshold value: ')
        return detect_edges_better(image, int(thresh))
    else:
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
    prompt()