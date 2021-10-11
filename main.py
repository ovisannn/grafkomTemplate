from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
from math import *
import shape

xPos = 20
yPos = 20

x = 0

direction = 1
# window's size variable
x_Window = 800
y_Window = 800

# canvas size variable
x_CanvasSize = 100
y_CanvasSize  = 100

#canvas background collor
r, g, b, a = 1, 1, 1, 1
def _setCanvas(x, y, r, g, b, a):
    glClearColor(r, g, b, a)
    gluOrtho2D(0, x, 0, y)

def _drawingArea():
    glClear(GL_COLOR_BUFFER_BIT)
    global xPos, yPos, direction
    
    if xPos >= x_CanvasSize and yPos >= y_CanvasSize:
        direction*=-1

    xPos += direction
    yPos += direction
    shape.Circle_polygon(xPos, yPos, 10, 100)


def bola_gerak_vertikal(direction):
    global yPos
    yPos+=10*direction
def bola_gerak_horizontal(direction):
    global xPos
    xPos+=10*direction

def controller(key, x, y):
    if key == GLUT_KEY_UP:
        bola_gerak_vertikal(1)
        print("atas")
    if key == GLUT_KEY_DOWN:
        bola_gerak_vertikal(-1)
        print("bawah")
    if key == GLUT_KEY_LEFT:
        bola_gerak_horizontal(-1)
        print("kiri")
    if key == GLUT_KEY_RIGHT:
        bola_gerak_horizontal(1)
        print("kanan")
    print(xPos,",", yPos)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)


if __name__ == "__main__":
  
    windowName = 'latihan grafkom'
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(x_Window, y_Window)
    glutInitWindowPosition(x_Window,y_Window)
    glutCreateWindow(windowName)
    glutDisplayFunc(_drawingArea)
    glutSpecialFunc(controller)
    _setCanvas(x_CanvasSize, y_CanvasSize, r, g, b, a)
    glutTimerFunc(50, update, 0)
    glutMainLoop()
