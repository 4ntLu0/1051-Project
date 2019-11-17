from Cimpl import *

image = load_image(choose_file())
show(image)
new_image = copy(image) #creates the copy to prevent it from being overwritten

def _adjust_component(comp: int)-> int:  #enters a red, green, or blue component
    
    if 0 <= comp <= 63:
        return 31    
    elif 63 < comp <= 127:
        return 95   
    elif 127 < comp <= 191:
        return 159    
    elif 191 < comp <= 255:
        return 223
    elif comp > 255:
        return 223
    elif comp < 0:
        return 31
#the midpoint of it's quadrant is returned





def posterize(image: Image) -> Image:
    
    new_image = copy(image)
    for pixel in image:
        x,y,(r,g,b) = pixel
        (r,g,b) = (_adjust_component(r),_adjust_component(g),_adjust_component(b))
        new_color = create_color(r,g,b)
        set_color (new_image, x, y, new_color)
    show(new_image)
    return image  


posterize(image)