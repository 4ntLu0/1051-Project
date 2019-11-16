from Cimpl import load_image, create_color, set_color, show, Image, save_as, copy

image = load_image(choose_file())  # loads the desired image from a given file
show(image)
image1 = copy(image) #creates a copy of the image so it is not overrided when the new image is returned

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)

def two_tone(image: Image, c1:str, c2:str, c3: str)-> Image:
    """ Given an 
    Written by Alia Nichol
    """
    colour = [c1, c2, c3]
    new_colour = []
    
    for i in range(2):
        if colour[i] == "black": # if either component in 
            new_colour += black 
        if colour[i] == "white":
            new_colour += white
        if colour[i] == "red":
            new_colour += red
        if colour[i] == "lime":
            new_colour += lime
        if colour[i] == "blue":
            new_colour += blue
        if colour[i] == "yellow":
            new_colour += yellow
        if colour[i] == "cyan":
            new_colour += cyan
        if colour[i] == "magenta":
            new_colour += magenta
        if colour[i]== "gray":
            new_colour += gray
    
    average = ((r + g + b) / 3)
    
    for x,y, (r, g, b) in image:
        if average < 84:
            pixel = (new_colour[0], new_colour[1], new_colour[2])
        if 85 < average < 170:
            pixel = (new_colour[3], new_colour[4], new_colour[5])
        if 171 < pixel < 255:
            pixel = (new_colour[6], new_colour[7], new_colour[8])
            
    set_colour(image, x, y, pixel)
        
    save_as(image, 'three_tone_channel.png') # saves the image 
    show(load_image('three_tone_channel.png'))
    print('three_tone_channel saved as new image')           
    
   
    #for x, y, (r, g, b) in image:  # reads through each pixel in the image
     #   if 0 < ((r + g + b) / 3) < 127:
     #       twotone = create_color(0, 0, 0)
    #        set_color(image, x, y, twotone) 
      #  elif 128 < ((r + g + b) / 3) < 255:
      #      twotone = create_color(255, 255, 255)
      #      set_color(image, x, y, twotone)
        
            
            
    