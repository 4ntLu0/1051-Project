'''
Tests the posterize function: which basically sets each rgb to the midpoint?
          x <= 63  :   31         Case1
    63  < x <= 127 :   95         Case2
    127 < x <= 191 :  159         Case3
    191 < x <= 255 :  223         Case4
    255 < x        :  223         Case5
Different test scenarios:
--- Make sure that for each RGB component, they are set to the right values? ---
    Iterates through the 5 cases, with RGB offset slightly so as to not create a grayscale image.


Memefied by Anthony Luo
'''