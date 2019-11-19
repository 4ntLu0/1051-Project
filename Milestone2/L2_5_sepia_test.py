from Utils.Cimpl import *
from L2_5_P4_sepia import sepia

def sepiaTest(file: str) -> str:
    """Test function for the sepia filter that checks if all the r, g, b components have gotten the sepia filter applied to them. The function returns "PASS" if all the pixels are successfully changed. If "PASS" is returned, this indicates that the red component has increased by the correct percentage and the blue component has decreased by the correct percentage, ultimately applying the sepia filter. If not, the function returns "FAIL". 
    
    Written by Alia Nichol.
    """
    img = sepia(load_image(file), disp = False, save = False)
    
    img = create_image(3, 1)  # creates image
    set_color(img, 0, 0, create_color(10, 67, 201))
    set_color(img, 1, 0, create_color(59, 190, 198))
    set_color(img, 2, 0, create_color(23, 78, 254))
    

    test_img = sepia(img, disp = False, save = False)
    image_correct = 0
    pixel = 0
        
    for x, y, (r, g, b) in test_img:
        if 0<= r < 63:
            if r != r / 1.1 and b1 == float(b / 0.9):
                image_correct += 1
            else:
                image_correct -= 1
            
        elif 63<= r <= 191:
            if r1 == float(r / 1.15) and b1 == float(b / 0.85):
                image_correct += 1
            else:
                image_correct -= 1
    
        elif 191<= r <255 :
            if r1 == float(r / 1.08) and b1 == float(b / 0.93):
                image_correct += 1
            else:
                image_correct -= 1
            
        else:
            image_correct -= 1
    if image_correct == pixel:
        return print('lol'), pixel, image_correct
    else:
        return print('u suck'), pixel, image_correct

#if __name__ == '__main__':
    #sepiaTest()
           
        
        
    
            
        
            
        
        
    