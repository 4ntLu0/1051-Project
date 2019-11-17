
from Cimpl import *

def grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image

def sepia(file: Image) -> Image:
    image = load_image(file)
    picture = grayscale(image)
    new_image = copy(picture)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        
        if r < 63:
            r *= 1.1
            b *= 0.9
            
        if 63 <= r <= 191:
            r *= 1.15
            b *= 0.85
            
        if r > 191:
            r *= 1.08
            b *= 0.93
            
        filter = create_color(r, g, b)
        set_color(new_image, x, y, filter)
        
    show(new_image)
    return new_image

def test_sepia(file) -> str:
    '''Test function for sepia filter that tests if all the pixels in the image have the sepia filter applied to them. The function returns 'PASS' if all pixels successfully changed. If not, the function returns 'FAIL'.
    '''    
    image1 = sepia(file)
    for x, y, (r, g, b) in file:
        for x,y, (r1,g1,b1) in image1:
            if r < 63:
                if r == r1 /1.1 and b == b1 / 0.9:
                    print("PASS")
            elif r <= 191:
                if r == r1/1.15 and b == b1 / 0.85: 
                    print("PASS")                
            elif r > 191:
                if r == r1/1.08 and b == b1 / 0.93:
                    print("PASS")
            else:        
                print ("FAIL")    
           
           
        
        
    
            
        
            
        
        
    