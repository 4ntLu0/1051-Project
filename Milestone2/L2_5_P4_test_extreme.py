from L2_5_P4_contrast import extremeContrast
from Utils.Cimpl import create_color, set_color, save_as, show, load_image, Image, choose_file, copy



def testExtreme():
    image = load_image(choose_file())  # this is going to have to be a created image, but as of right now it is the
    # original image
    image1 = extremeContrast(image)  # image 1 is the updated version
    if image != image1:
        print('HAS THE ORIGINAL IMAGE BEEN CHANGED? : YES')
    else:
        print('HAS THE ORIGINAL IMAGE BEEN CHANGED? : NO')

    if image1 == extremeContrast(image):
        print('the image contrast has: PASSED THE TEST')
    else:
        print('the image contrast has: FAILED THE TEST')


if __name__ == '__main__':
    testExtreme()

"""
for x, y, (r, g, b) in image:
    print('Passed')
    if 0 < r < 127:
        print('Pass')
    else:
        print('fail')
   """
