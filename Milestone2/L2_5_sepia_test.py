
def sepia_test() -> None:
    """Test function for the sepia filter that checks if all the r, g, b components have gotten the sepia filter applied to them. The function returns "PASS" if all the pixels are successfully changed. If "PASS" is returned, this indicates that the red component has increased by the correct percentage and the blue component has decreased by the correct percentage, ultimately applying the sepia filter. If not, the function returns "FAIL". 
    
    Written by Alia Nichol.
    """
    image1 = sepia(choose_file())
    
    for x, y, (r, g, b) in image1:
        
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
            break
           
           
        
        
    
            
        
            
        
        
    