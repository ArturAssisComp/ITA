'''
Author: Artur Assis Alves
Date  : 07/04/2020
Title : Question 1
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
        

def draw_square (t, sz):
    '''
    Draws a regular polygon with 4 sides (square). Each side has length 'sz'.

    Input :
        t  -> turtle.Turtle()
        sz -> float

    Output:
        None
    '''
    draw_poly(t, 4, sz)

def successive_square (t, ini_sz, diff, n):
    '''
    Draws 'n' regular polygons with 4 sides (squares) with the same center but with sides
    following an arithmetic progression with common difference 'diff'. The first is a square
    of side 'ini_sz'.

    Input :
        t       -> turtle.Turtle()
        ini_sz  -> float
        diff    -> float
        n       -> integer

    Output:
        None
    '''
    for i in range(n):
        size = ini_sz + i*diff
        draw_square(t, size)
        #Moving to the next initial position.
        t.up()     #penup()
        t.bk(diff/2) #backward()
        t.rt(90)   #right() 
        t.fd(diff/2) #forward()
        t.lt(90)   #left()
        t.down()   #pendown()



#Main:
if __name__=='__main__':
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor((144, 238, 144))
    tess   = turtle.Turtle()
    tess.color((255, 105, 180))
    successive_square(tess, 20, 20, 5)
    screen.exitonclick()
