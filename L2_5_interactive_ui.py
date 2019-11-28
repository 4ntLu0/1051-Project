"""ECOR 1051 Fall 2019 Project - Interactive User Interface from group L2-5. Submitted December 1, 2019. 
This code has been attributed from given files on cuLearn."""

# TODO:
#  - P8 need to finish the README (Contact info, the date, software"s name, small description, installation requirements, etc)
#  - make sure that the image is shown at the correct times and # of times
#  - complete the docstrings and the type annotations
#  - comment the code

from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical, Image
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, get_color, choose_file, copy
import os

all_commands = ["L", "S", "2", "3", "X", "T", "P", "E", "I", "V", "H", "Q"]


def prompt() -> str:
    """
    Prompts the user for an input. Checks validility of the input before returning the command.
    Written by:
    """
    command = input(
        "Please enter a command from the following list: \n L)oad Image S)ave-as \n 2)-tone 3)-tone X)treme contrast" \
            " T)int sepia P)osterize \n E)dge detect I)mproved edge detect V)ertical flip" \
            " H)orizontal flip \n Q)uit \n : ").upper()

    while command not in all_commands:
        print("No such command")
        command = input(
            "Please enter a command from the following list: \n L)oad Image S)ave-as \n 2)-tone 3)-tone X)treme" \
                " contrast T)int sepia P)osterize \n E)dge detect I)mproved edge detect V)ertical flip H)orizontal"\
                "flip \n Q)uit \n : ").upper()
    return command


def image_load() -> Image:
    """ prompts the user to enter a filename before loading and returning the image.
    Written by:
    """
    image = input("Name of image to load:")
    loaded_image = load_image(image)
    show(loaded_image)
    print("Image has been loaded")
    return loaded_image


def apply_filter(selection: str, loaded_image: Image) -> Image:
    """
    Applies the selected filter.
    Written by: Anthony Luo
    """

    functions = [extreme_contrast, sepia, posterize, flip_vertical, flip_horizontal]
    prompts = ["X", "T", "P", "V", "H"]

    if selection == "2":
        color1 = input("First colour:")
        color2 = input("Second colour:")
        new_image = two_tone(loaded_image, color1, color2)
        print("Two tone filter has been applied")
        return new_image

    elif selection == "3":
        color1 = input("First colour:")
        color2 = input("Second colour:")
        color3 = input("Third colour:")
        new_image = three_tone(loaded_image, color1, color2, color3)
        print("Three tone filter has been applied")
        return new_image

    elif selection == "E":
        thresh = int(input("Threshold: "))
        new_image = detect_edges(loaded_image, thresh)
        print("Edge Detection filter has been applied")
        return new_image

    elif selection == "I":
        thresh = int(input("Threshold: "))
        new_image = detect_edges_better(loaded_image, thresh)
        print("Improved Edge Detection filter has been applied")
        return new_image

    else:
        for index in range(len(prompts)):
            if selection == prompts[index]:
                fn = functions[index]
                img = fn(loaded_image)
                return img


def main():
    """ Runs the program!
    Written by:
    """
    is_loaded = False
    while True:
        command = prompt()
        if command == "L":
            is_loaded = True
            image = image_load()
            img = copy(image)

        elif command == "Q":
            print("Exiting program")
            exit()

        elif not is_loaded:
            print("No image loaded")
            prompt()

        elif command == "S":
            filename = input("What would you like the file to be saved as? (ex. new_image.jpg): ")
            save_as(img, filename)
            print("Image has been saved as:", filename)

        else:
            img = apply_filter(command, img)


if __name__ == "__main__":
    new_path = os.getcwd() + "/returns"  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
    main()
