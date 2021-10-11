from math import *

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def Circle_polygon(x_pos, y_pos, radius, sides): 
    glBegin(GL_POLYGON)   
    glColor3ub(3, 211, 252) 
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + x_pos  
        sine  = radius * sin(i*2*pi/sides) + y_pos   
        glVertex2f(cosine,sine)
    glEnd()
    glFlush()


def Circle_lines(x_pos, y_pos, radius, sides):
    glBegin(GL_LINE_STRIP)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + x_pos  
        sine  = radius * sin(i*2*pi/sides) + y_pos   
        glVertex2f(cosine,sine)
    glEnd()
    glFlush()