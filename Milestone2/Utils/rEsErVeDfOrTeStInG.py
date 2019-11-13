from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, create_image
import os
from typing import NewType

original_img = load_image('p2-original.jpg')

Image = NewType('Image', str)

from L2_5_P2_combine import combine, testCombine
from L2_5_P2_red import createRed, testRed

createRed(load_image('p2-original.jpg'))
testRed(load_image('p2-original.jpg'))
combine()
testCombine()
