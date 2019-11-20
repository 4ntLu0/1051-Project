from Cimpl import *

image = load_image(choose_file())

def posterize_filter(image) -> image:
    """ 
    This function takes an image and reduces the number of its colors, while
    maintaining the look of the original image
    By: Abdelrahman Alatoom
    """
    
    original_image = image
    final_image = image
    show(image)
    
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        original_color = get_color(original_image, x, y)
        final_color = _adjust_component(original_color)
        set_color(final_image, x, y, final_color)
        
    show(final_image)
    return final_image        

def _adjust_component(original_color: tuple) -> tuple:
    """
    The function determines the quadrant in which a component lies and
    returns the midpoint of that quadrant
    By: Abdelrahman Alatoom
    """
    r, g, b = original_color
    
    if 0 <= r <= 63:
        r = 31
    elif 64 <= r <= 127:
        r = 95
    elif 128 <= r <= 191:
        r = 159
    else: r = 223
    
    if 0 <= g <= 63:
        g = 31
    elif 64 <= g <= 127:
        g = 95
    elif 128 <= g <= 191:
        g = 159
    else: g = 223
    
    if 0 <= b <= 63:
        b = 31
    elif 64 <= b <= 127:
        b = 95
    elif 128 <= b <= 191:
        b = 159
    else: b = 223
    
    final_color = create_color(r, g, b)
    
    return final_color

def posterize_filter_test(image):
    """ 
    This function tests if the posterize filter works properly by checking
    if the rgb of each pixel in the original image were set to the correct
    quadrant, which resulted in the final image
    By: Abdelrahman Alatoom
    """
    
    final_image = posterize_filter(image)
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        original_color = get_color(image, x, y)
        final_color = get_color(final_image, x, y)
        r,g,b = final_color
        
        if 0 <= original_color[0] <= 63:
            if r != 31:
                print("Filter not working properly")
                return
        if 64 <= original_color[0] <= 127:
            if r != 95:
                print("Filter not working properly")
                return
        if 128 <= original_color[0] <= 191:
            if r != 159:
                print("Filter not working properly")
                return
        if 192 <= original_color[0] <= 255:
            if r != 223:
                print("Filter not working properly")
                return
        
        if 0 <= original_color[1] <= 63:
            if g != 31:
                print("Filter not working properly")
                return
        if 64 <= original_color[1] <= 127:
            if g != 95:
                print("Filter not working properly")
                return
        if 128 <= original_color[1] <= 191:
            if g != 159:
                print("Filter not working properly")
                return
        if 192 <= original_color[1] <= 255:
            if g != 223:
                print("Filter not working properly")
                return
            
        if 0 <= original_color[2] <= 63:
            if b != 31:
                print("Filter not working properly")
                return
        if 64 <= original_color[2] <= 127:
            if b != 95:
                print("Filter not working properly")
                return
        if 128 <= original_color[2] <= 191:
            if b != 159:
                print("Filter not working properly")
                return
        if 192 <= original_color[2] <= 255:
            if b != 223:
                print("Filter not working properly")
                return
    print("Filter working properly")