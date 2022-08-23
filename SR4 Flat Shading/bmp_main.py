from bmp_renderer import Render
from Vector import V3

frame = Render()

scale_factor = (1, 1, 1)
translate_factor = (0, -0.2, 0)

frame.glCreateWindow(1024, 1024)

frame.glViewPort(80, -200, 900, 900)

frame.glClearColor(1, 1, 1)

frame.glColor(0, 0, 0)


frame.draw_triangles(V3(10, 70), V3(50, 160), V3(70, 80))
    
#frame.load_model('girl.obj', scale_factor, translate_factor)

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