from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
from math import *
import shape

def _setCanvas(x, y, r, g, b, a):
    glClearColor(r, g, b, a) 

    gluOrtho2D(0, x, 0, y)

def _drawingArea():
    #this function is where u can store ur drawing's coordinate
    shape.Circle_lines(30, 30, 10, 100)
    glBegin(GL_POLYGON)
    glColor3ub(171, 25, 255)    
    glVertex2f(70, 20) #d
    glVertex2f(20, 20) #a
    
    glColor3ub(25, 251, 255)
    glVertex2f(20, 50) #b 
    glVertex2f(70, 60) #c
    glEnd()
    glFlush()

    # shape.Circle_polygon(0,0,40,100)


if __name__ == "__main__":
    # recomended rasio = 16:9, 4:8, 16:10

    #variable configuration for main program

    # window's size variable
    x_Window = 800
    y_Window = 800

    # canvas size variable
    x_CanvasSize = 100
    y_CanvasSize  = 100

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