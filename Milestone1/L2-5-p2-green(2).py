from Cimpl import *



def green_filter(image: Image) -> Image:
    """
    Given an image from a selected file, the function sets all the pixels in the image to the color green and saves it as a new image. 
    
    Written by Alia Nichol.
    
    """
    image = load_image('p2-original.jpg') #loads the desired image
    show(image) 
    image1 = copy(image) #creates a copy of the image so it is not overrided
    
    
    for x, y, (r, g, b) in image: # reads through the image
        green = create_color(0, g, 0)
        set_color(image1, x, y, green) # sets all the pixels of defined locations in that image to the color
        
  
    save_as(image1, 'green_channel.jpg')  # saves as a new image
    show(load_image('green_channel.jpg'))  # shows the image to double check

    print('green_channel saved as new image')

    return image1

def test_green() -> None:
    '''Test function for green filter that tests if all the pixels in the image are green. The function returns 'PASS' if all pixels successfully change to green. If not, the function returns 'FAIL'.
    '''
    image1 = green_filter('p2-original.jpg')
   
    for x,y,(r, g, b) in image1:
        if r ==0 and b ==0:
            print("PASS")
            return
       
    else:
        print ("FAIL")
        return 

        