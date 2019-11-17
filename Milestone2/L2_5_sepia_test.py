def test_sepia () -> None:
    '''Test function for sepia filter that tests if all the pixels in the image have the sepia filter applied to them. The function returns 'PASS' if all pixels successfully changed. If not, the function returns 'FAIL'.
    '''    
    image1 = sepia(sep_img)
    
   
    for x,y,(r, g, b) in sep_img:
        if r < 63:
            if g == r /1.1 and b / 0.9:
                print("PASS")
                return
            
        elif r <= 191:
            if g == r/1.15 and b / 0.85: 
                print("PASS")
                return  
            
        elif r > 191:
            if g == r/1.08 and b / 0.93:
                print("PASS")
                return                  
        else:        
            print ("FAIL")
            return 
    