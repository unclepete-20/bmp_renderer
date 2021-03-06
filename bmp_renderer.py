'''
@author Pedro Pablo Arriola Jimenez (20188)
@filename bmp_renderer.py
@description: BMP file renderer that works using concepts related
to framebuffers and low level code such as bytes.
'''

from random import randint
import struct


# Functions that will be needed to create low level structures.
def char(c):
    # 1 byte character
    c = struct.pack('=c', c.encode('ascii'))
    return c

def word(w):
    # 2 bytes character
    w = struct.pack('=h', w)   
    return w  


def dword(dw):
    # 4 bytes character
    dw = struct.pack('=l', dw)   
    return dw  

def color_select(r, g, b):
    '''
    Here we have the rgb spectrum transformed to byte code.
    The order of the inputs are not the way is used to due to difference
    in how Windows OS works with this type of data.
    '''
    r = abs(r)
    g = abs(g)
    b = abs(b)
    
    
    try:
        color = bytes([int(b), int(g), int(r)])
    except ValueError:
        print("Input value is incorrect! Try again using numbers this time...")
    else:
        if r <= 255 and g <= 255 and b <= 255:
            return color
        else:
            print("Input value out of range...")

# CONSTANTS AND VARIABLES

BLACK = color_select(0, 0, 0)
WHITE = color_select(255, 255, 255)
random_color = color_select(randint(0, 255), randint(0, 255), randint(0, 255))


# Class of type Render that will nest every function that will create a BMP file from scratch. 

class Render(object):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.FILE_SIZE = (14 + 40)
        self.PIXEL_COUNT = 3
        self.PLANE = 1
        self.BITS_PER_PIXEL = 24
        self.DIB_HEADER = 40
        self.pixels = 0
        self.clearColor = color_select(0, 0, 0)
        self.currColor = color_select(1, 1, 1)
        
        
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
    
    def glClear(self):
        self.framebuffer = [[self.clearColor for y in range(self.height)]
                       for x in range(self.width)]
    
    
    def glFinish(self, filename):
        with open(filename, 'wb') as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))

            # file size
            file.write(dword(self.FILE_SIZE + self.height * self.width * self.PIXEL_COUNT))
            file.write(dword(0))
            file.write(dword(self.FILE_SIZE))

            # Info Header
            file.write(dword(self.DIB_HEADER))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(self.PLANE))
            file.write(word(self.BITS_PER_PIXEL))
            file.write(dword(0))
            file.write(dword(self.width * self.height * self.PIXEL_COUNT))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.framebuffer[x][y])
            file.close()