from Cimpl import load_image, create_color, set_color, show, Image, save_as

def createBlue(image_path):
    """ the function createBlue displays the original image, once closed it displays the image with a blue filter
    
    -Emilio Lindia
    """
    image = load_image('p2-original.jpg')  # loads the original colourless picture
    show(image)  # shows original image
    
    new_image = image
    
    for x, y, (r, g, b) in image:  # examines all pixels
        blue = create_color(0, 0, b)  # creates a 100% blue filter
        
        set_color(new_image, x, y, blue)
    
    save_as(new_image, 'blue_channel.jpg')  # saves the blue filter as a new image
    show(load_image('blue_channel.jpg'))  # shows image 
    
    print('blue_channel saved as new_image')    
    return new_image


def test_blue() -> None:
    '''This is the test function for the blue filter. 
    
    it tests if all pixels are blue or if they contain any traces of green or red.
    '''
    image1 = createBlue('p2-original.jpg')
   
    for x,y,(r, g, b) in image1:
        if r ==0 and g ==0:  # if there is no trace of red or green
            print("PASS") #passed the test
            return
       
    else:
        print ('FAILS')
        return