from L2_5_P4_extreme import extreme_contrast
from Cimpl import create_color, set_color, save_as, show, load_image, Image,\
     choose_file, copy
"""
CODE ATTRIBUTED FROM FILES ON CULEARN
test function that reviews the code for the contrasting filter to see if the /
pixels are properly
analyzed, if the original image changes and if the image has been contrasted


HOW TO RUN CODE
Run the file
pixels of chosen image are analyzed and a contrasted version of the
image will appear
END OF CODE




written by Emilio: 101143244
"""


def test_extreme():
    
    image = load_image( choose_file ( ) )  # Loads a file that you choose
    
    
    for x, y, (r, g, b) in image:
        print('this pixel has been analyzed correctly')  
        
    else:
        print('this pixel has not been analyzed correctly')  
        
            
    if image == extreme_contrast(image):
        print('the image contrast has: PASSED THE TEST')
    else:
        print('the image contrast has: FAILED THE TEST')


                

if __name__ == '__main__':
    test_extreme()
