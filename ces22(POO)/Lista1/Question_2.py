'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 2
'''
import turtle

#Functions:

def draw_poly(t, n, sz):
    '''
    Draws a regular polygon with 'n' sides. Each side has length 'sz'.

    Input :
        t  -> turtle.Turtle()
        n  -> integer
        sz -> float

    Output:
        None
    '''
    ext_angle = 360/n
    for i in range(n):
        t.fd(sz)
        t.lt(ext_angle)



#Main:
if __name__=='__main__':
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor((144, 238, 144))
    tess   = turtle.Turtle()
    tess.color((255, 105, 180))
    draw_poly(tess, 8, 50)
    screen.exitonclick()
