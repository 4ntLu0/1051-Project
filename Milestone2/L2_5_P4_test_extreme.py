from L2_5_P4_extreme import extremeContrast
from Utils.Cimpl import create_color, set_color, save_as, show, load_image, Image, choose_file, copy
"""
test function that reviews the code for the contrasting filter to see if the pixels are properly
analyzed, if the original image changes and if the image has been contrasted

written by Emilio
"""


def test_extreme():
    image = load_image(choose_file())  # loads a file that you choose
    image1 = extremeContrast(image)  # image 1 is the updated version
    
    for x, y, (r, g, b) in image:
        print('this pixel has been analyzed correctly')  
        
    else:
        print('this pixel has not been analyzed correctly')  
    if image != image1:
        print('HAS THE ORIGINAL IMAGE BEEN CHANGED? : NO')
    else:
        print('HAS THE ORIGINAL IMAGE BEEN CHANGED? : YES')
        
               

    if image1 == extremeContrast(image1):
        print('the image contrast has: PASSED THE TEST')
    else:
        print('the image contrast has: FAILED THE TEST')


                

if __name__ == '__main__':
    test_extreme()
