from Utils.Cimpl import *
from L2_5_P4_sepia import sepia

def sepiaTest() -> None:
    """Test function for the sepia filter that checks if all the r, g, b components have gotten the sepia filter applied to them. The function returns "PASS" if all the pixels are successfully changed. If "PASS" is returned, this indicates that the red component has increased by the correct percentage and the blue component has decreased by the correct percentage, ultimately applying the sepia filter. If not, the function returns "FAIL". 
    
    Written by Alia Nichol.
    """
    img = sepia(load_image(choose_file()), disp = False)
    
    img = create_image(3, 1)  # creates image
    set_color(img, 0, 0, create_color(10, 67, 201))
    set_color(img, 1, 0, create_color(59, 190, 198))
    set_color(img, 2, 0, create_color(23, 78, 254))
    

    test_img = sepia(img, disp = False, save = False)
    for x, y, (r, g, b) in test_img:
        if 0<= r <= 63:
            if g == r / 1.1 and g == b / 0.9:
                print("PASS")
                
        elif r <= 191:
            if g == r / 1.15 and g == b / 0.85:
                print("PASS")
        
        elif r > 191:
            if g == r / 1.08 and g == b / 0.93:
                print("PASS")
                
        else:
            print("FAIL")

if __name__ == '__main__':
    sepiaTest()
           
        
        
    
            
        
            
        
        
    