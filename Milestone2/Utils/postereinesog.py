from Cimpl import * 

# adjustment function, Author: PRAYANSHU NARAYAN S# 101144277
def _adjust_component(r, g , b)  -> tuple:
    """
    Author: PRAYANSHU NARAYAN S# 101144277
    Returns an image but filtered to posterize:
    Examples:
    >>> posterize_channel('p2-original.jpg')
    sets all the pixels in the file in posterize
    """  
    r2 = 0
    g2 = 0
    b2 = 0 
    if r <= 63 and r > 0:
        r2 = 32
    elif  r <= 127 and r > 64:
        r2 = 96
    elif r <= 191 and r > 128:
        r2 = 160
    elif r <= 255 and r > 192:
        r2 = 224
    
    if g <= 63 and g > 0:
        g2 = 32
    elif  g <= 127 and g > 64:
        g2 = 96
    elif g <= 191 and g > 128:
        g2 = 160
    elif g <= 255 and g > 192:
        g2 = 224
    
    if b <= 63 and b > 0:
        b2 = 32
    elif  b <= 127 and b > 64:
        b2 = 96
    elif b <= 191 and b > 128:
        b2 = 160
    elif b <= 255 and b > 192:
        b2 = 224
        
    
    
    return r2,g2,b2

# posterize function, Author: PRAYANSHU NARAYAN S# 101144277
def posterize(file: str)-> Image:
    """
    Author: PRAYANSHU NARAYAN S# 101144277
    Returns an image but filtered to posterize:
    Examples:
    >>> posterize('p2-original.jpg')
    sets all the pixels in the file in posterize
    
    """
    image = load_image(file)
    posterize_image = copy(image)
    
    for x, y, (r, g, b) in image:
        adjustColor = _adjust_component(r,g,b)
        r2 , g2 , b2 = adjustColor
        red = create_color(r2 ,g2 ,b2)
        set_color(posterize_image, x, y, red)       
    return posterize_image