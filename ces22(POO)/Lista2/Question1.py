'''
Author : 
Date   : 06/05/2020
Title  : Question 1
'''
import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
    
draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num   = 0
initial_pos = tess.position() 
def advance_state_machine():
    global state_num
    if state_num == 0:# Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def change_color_red ():
    tess.fillcolor("red")

def change_color_green ():
    tess.fillcolor("green")

def change_color_bule ():
    tess.fillcolor("blue")

def increase_turtle_width():
    '''Increases the tess width by 1 if it is lesser than 20.'''
    if tess.width() < 20:
        tess.width(tess.width() + 1)

def decrease_turtle_width():
    '''Decreases the tess width by 1 if it is bigger than 1.'''
    if tess.width() > 1:
        tess.width(tess.width() - 1)

def increase_turtle_shapesize():
    '''Increases the tess shapesize by 1 if it is lesser than 20.'''
    if tess.shapesize()[0] < 20:
        tess.shapesize(tess.shapesize()[0] + 1)

def decrease_turtle_shapesize():
    '''Decreases the tess shapesize by 1 if it is bigger than 1.'''
    if tess.shapesize()[0] > 1:
        tess.shapesize(tess.shapesize()[0] - 1)

def fd ():
    tess.fd(10)

def bk ():
    tess.bk(10)

def lft ():
    tess.setx(tess.position()[0] - 10)

def rgt ():
    tess.setx(tess.position()[0] + 10)

def initial_position():
    global state_num
    tess.fillcolor("green")
    state_num = 0
    tess.setposition(*initial_pos)

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
'''Question1:'''
wn.onkeypress(change_color_red, "r")
wn.onkeypress(change_color_green, "g")
wn.onkeypress(change_color_bule, "b")

wn.onkeypress(increase_turtle_width, "+")
wn.onkeypress(decrease_turtle_width, "-")

wn.onkeypress(increase_turtle_shapesize, "p")
wn.onkeypress(decrease_turtle_shapesize, "l")

wn.onkeypress(fd, "Up")
wn.onkeypress(rgt, "Right")
wn.onkeypress(lft, "Left")
wn.onkeypress(bk, "Down")

wn.onkeypress(initial_position, "i")
'''EndQuestion1'''

wn.listen() # Listen for events
wn.mainloop()



