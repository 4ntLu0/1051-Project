from Cimpl import *
image = load_image(choose_file())     
show(image)
new_image = copy(image)

def flip_horizontal(image):
    h= get_height(image)
    w = get_width(image)    
    new_image = create_image(w, h )
    for pixel in image:                  
        x,y,(r,g,b) = pixel
                        
        new_color = create_color(r,g,b)  
        set_color(new_image,x-1, h- y-1, new_color)  
    show(new_image)        
    
    
if __name__ == '__main__':
    flip_horizontal(new_image)

    