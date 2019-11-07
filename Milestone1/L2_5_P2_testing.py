from Cimpl import load_image, create_color, set_color, show, Image, save_as
import os
try:
    os.remove('redTestLog.txt')
except:
    pass

r_img = load_image('red_channel.jpg')
g_img = load_image('green_channel.jpg')
b_img = load_image('blue_channel.jpg')

show(r_img)
show(g_img)
show(b_img)

def test_red(file):
    print('testing red')
    log = open('redTestLog.txt', 'a')
    for x, y, (r, g, b) in file:
        if g == 0 and b == 0:
            pass
        else:
            str1 = 'fails at: ' + str(x) + ' , ' + str(y) + \
                ' |  with: ' + 'R: ' + str(r) + ' ' + 'G: ' + \
                str(g) + ' ' + 'B: ' + str(b) + '\n'
            log.write(str1)
            print(str1)
def test_green(file):
    print('testing green')
    for x, y, (r, g, b) in file:
        if r == 0 and b == 0:
            pass
        else:
            print('fails')
def test_blue(file):
    print('testing blue')
    for x, y, (r, g, b) in file:
        if r == 0 and g == 0:
            pass
        else:
            print('fails')

if __name__ == '__main__':
    test_red(r_img)