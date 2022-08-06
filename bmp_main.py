from bmp_renderer import Render

frame = Render()

frame.glCreateWindow(20, 20)

frame.glViewPort(2, 2, 1, 1)

frame.glClearColor(0.25, 1, 0.50)

frame.glClear()

frame.glVertex(1, 1)

frame.glFinish("prueba.bmp")