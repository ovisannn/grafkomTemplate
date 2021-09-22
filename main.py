from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
from math import *
import shape

def _setCanvas(x, y, r, g, b, a):
    glClearColor(r, g, b, a) 
    gluOrtho2D(x, 0, 0, y)

def _drawingArea():
    #this function is where u can store ur drawing's coordinate
    shape.Circle_lines(30, 30, 10, 100)



if __name__ == "__main__":
    # recomended rasio = 16:9

    #variable configuration for main program

    # window's size variable
    x_Window = 480
    y_Window = 360

    # canvas size variable
    x_CanvasSize = 200
    y_CanvasSize  = 200

    #canvas background collor
    r, g, b, a = 1, 1, 1, 1

    # window's name variable
    windowName = 'latihan grafkom'

    # main function for running program
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(x_Window, y_Window)
    glutInitWindowPosition(x_Window,y_Window)
    glutCreateWindow(windowName)
    glutDisplayFunc(_drawingArea)
    _setCanvas(x_CanvasSize, y_CanvasSize, r, g, b, a)
    glutMainLoop()