from Cimpl import *
def _adjust_component(r: int, g: int, b: int) -> int: #input RGB values
    
    for r in (r, g, b):
        
        if 0 < r <= 63:
                r = 31
            
        elif 63 < r <= 127:
                r = 95
            
        elif r > 127 and r <= 191:
                r = 159
            
        elif r > 191 and r <= 255:
                r = 223
            
    
    
    for g in (r, g, b):
        
        if g >= 0 and g <= 63:
                g = 31
        elif 63 < g <= 127:
                g = 95
            
        #for b in (r, g, b):
                        
          #  if b >= 0 and b <= 63:
               #         b = 31  
            
     
            
            return (r, g, b)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   # if (r >= 0 and r <= 63) and (g >= 0 and g <= 63) and (b >= 0 and b <= 63):
    #    return (31, 31, 31 )
    
    #elif (r >= 0 and r <= 63) and (g >= 0 and g <= 63) and (b >= 0 and b <= 63):
     #   return (31, 31, 31 )
    
   