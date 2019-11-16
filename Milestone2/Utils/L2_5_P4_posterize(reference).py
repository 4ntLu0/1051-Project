
from Cimpl import *
image = load_image(choose_file())
image = copy(image)
show(image)
new_image = image #creates copy to prevent it from being overwritten


#def posterize(x):
"""
    if x== 1 or x ==2 or x==3 or x== 4:
        return _adjust_component(x)
    else:
        print('Error inserting quadrant number, there are only 4 quadrants')
    """    
    
    
new_image = image
    
for x, y, (r, g, b) in image:  # examines all pixels
    posterize = create_color(_adjust_component(1) ,_adjust_component(2) , _adjust_component(3) )  
    
    set_color(new_image, x, y, blue)
    
save_as(new_image, 'blue_channel.jpg')  # saves the blue filter as a new image
show(load_image('blue_channel.jpg'))  # shows image 
new_image = image

for x, y, (r, g, b) in image:  # examines all pixels
    blue = create_color(0, 0, b)  # creates a 100% blue filter

    set_color(new_image, x, y, blue)

save_as(new_image, 'blue_channel.jpg')  # saves the blue filter as a new image
show(load_image('blue_channel.jpg'))  # shows image 

print('blue_channel saved as new_image')
new_image = image

for x, y, (r, g, b) in image:  # examines all pixels
    blue = create_color(0, 0, b)  # creates a 100% blue filter

    set_color(new_image, x, y, blue)
save_as(new_image, 'blue_channel.jpg')  # saves the blue filter as a new image
show(load_image('blue_channel.jpg'))  # shows image 
print('blue_channel saved as new_image')



# def _adjust_component(quadrant: int)-> int:
    #if quadrant == 1:       #if the quadrant is labelled as quadrant 1
        #return 31           # return the midpoint of quadrant 1
    #elif quadrant == 2:
     #   return 95
    #elif quadrant == 3:
     #   return 159
    #elif quadrant == 4:
     #   return 223   
    #else:
     #   print('Error inserting quadrant number, there are only 4 quadrants')
    