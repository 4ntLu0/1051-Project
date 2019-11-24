from Cimpl import *

def vertical_test(Flipped_Image:Image, Original_Image: Image):
    """Return if the image is vertically flipped and how many errors are present
    
    >>>vertical_test('VFlipped.jpg','p2-original.jpg')
    
    Anthony Petrov
    """
    Original = load_image(Original_Image)
    Flipped = load_image(Flipped_Image)
    new_picture = copy(Flipped)
    
    
    for x in range(get_width(Flipped)):             #Flips the flipped image 
        for y in range(get_height(Flipped)):
            color = get_color(Flipped, x, y)
            set_color(new_picture, get_width(Flipped)-x-1, y, color)
    
    errors = 0     
    statement = ""
    
    for x, y, (r,g,b) in new_picture and Original:      #Compares the pixels in the new image and the original image 
        Flipped_Pixels = get_color(new_picture,x,y)
        Original_Pixels = get_color(Original, x, y)
        red, green, blue = Flipped_Pixels
        red1, green1, blue1 = Original_Pixels
        if red1 != red or green1 != green or blue1 != blue:       #If the pixels in each image do not match, then an error is added.
            errors+= 1
        if errors >0:
            statement = "This image is not vertically flipped. The image has" ,errors, "errors"
        if errors == 0:
            statement = "This image is vertically flipped"
    return statement 