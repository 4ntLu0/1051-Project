from Cimpl import load_image, create_color, set_color, show, Image, save_as
import os
os.remove('redImgLog.txt')

image = load_image('p2-original.jpg')  # reads in the image
show(image)  # shows original image
log = open('redImgLog.txt', 'a')

'''remember: we don't want to make changes to the original file - this step is just to make sure'''
new_image = image

for x, y, (r, g, b) in image:  # reads through the image pixel by pixel
    red = create_color(r, 0, 0)  # creates new colour
    # remaps each x,y coordinate to the new red channel
    set_color(new_image, x, y, red)
    str1 = 'X: ' + str(x) + ' Y: ' + str(y) +' WITH ORIGINAL R: ' + str(r) + ' G: ' + str(g) + ' B: '+str(b)+'| WITH NEW: R: ' + \
        str(red[0]) + ' G: ' + str(red[1]) + ' B: ' + str(red[2]) + '\n'
    log.write(str1)

save_as(new_image, 'red_channel.jpg')  # saves as new image
show(load_image('red_channel.jpg'))  # shows image to double check

print('end')
exit()

