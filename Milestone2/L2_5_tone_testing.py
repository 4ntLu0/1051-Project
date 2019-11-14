from Utils.Cimpl import load_image, choose_file, show, set_color, save_as, create_color #change this later please
from Utils.simple_Cimpl_filters import grayscale
from typing import NewType
from L2_5_two_tone import twoTone
from L2_5_three_tone import threeTone
Image = NewType('Image', str)
from datetime import datetime

# TODO: write the rest of this code :(

tones = {'black' : (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'lime': (0, 255, 0), 'blue': (0, 0, 255),
         'yellow': (255, 255, 0), 'cyan': (0, 255, 255), 'magenta': (255, 0, 255), 'gray': (128, 128, 128)}


def testTwoTone():
    ''' Tests to ensure that two tone functions
    Written by Anthony Luoq
    :return:
    :rtype:
    '''


def testThreeTone():
    ''' Tests to ensure that three tone functions
    Written by Anthony Luo
    :return:
    :rtype:
    '''