from bmp_renderer import Render
from Vector import V3
from Texture import *

frame = Render()

scale_factor = (0.1, 0.1, 0.1)
translate_factor = (0, -0.2, 0)

frame.glCreateWindow(4000, 4000)

frame.glViewPort(80, -200, 900, 900)

frame.lightPosition(1,-1,-1)

    
frame.load_model('Penguin.obj', scale_factor, translate_factor)

frame.glFinish('prueba.bmp')

'''
square = [
    (0.2, 0.2),
    (0.8, 0.2),
    (0.8, 0.8),
    (0.2, 0.8)
]

last_point = square[-1]

for point in square:
    frame.glLine(*last_point, *point)
    last_point = point
'''