from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height

r_img = load_image('red_channel.jpg')
g_img = load_image('green_channel.jpg')
b_img = load_image('blue_channel.jpg')

new_img = r_img

r_chan = []
g_chan = []
b_chan = []

for x, y, (r, g, b) in r_img:
    r_chan.append(r)

for x, y, (r, g, b) in g_img:
    g_chan.append(g)

for x, y, (r, g, b) in b_img:
    b_chan.append(b)

counter = 0
for x, y, (r, g, b) in new_img:
    colour = create_color(r_chan[counter], g_chan[counter], b_chan[counter])
    set_color(new_img, x, y, colour)
    counter += 1

save_as(new_img, 'combined_image.jpg')
show(load_image('combined_image.jpg'))

