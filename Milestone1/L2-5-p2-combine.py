from Cimpl import load_image, create_color, set_color, show, Image, save_as

r_img = load_image('red_channel.jpg')
g_img = load_image('green_channel.jpg')
b_img = load_image('blue_channel.jpg')

r_chan = []
g_chan = []
b_chan = []

for x, y, (r, g, b) in r_img:
    r_chan.append(r)

for x, y, (r, g, b) in g_img:
    g_chan.append(g)
    
for x, y, (r, g, b) in b_img:
    b_chan.append(b)