from bmp_renderer import Render

frame = Render()

frame.glCreateWindow(1024, 1024)

frame.glViewPort(150, 150, 800, 800)

frame.glClear()

frame.glColor(1, 1, 0)

frame.glLine(1, 1 ,0 ,0)
frame.glLine(1, 0 ,0 ,1)
frame.glLine(1, 1 ,0 ,1)
frame.glLine(1, 0.2,0 ,0.5)
frame.glLine(0, 1 ,1 ,1)
frame.glLine(1, 1 ,0.6 ,0.2)

frame.glFinish('prueba.bmp')