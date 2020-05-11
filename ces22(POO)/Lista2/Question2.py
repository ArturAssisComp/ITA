'''
Author : 
Date   : 06/05/2020
Title  : Question 2
'''
import turtle # Tess becomes a traffic light.
import time

#Defining constants
DELAY_CONST = 1

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
delay       = DELAY_CONST
def advance_state_machine():
    global state_num, delay
    if state_num == 0:# Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        delay      = DELAY_CONST/2
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        delay      = DELAY_CONST
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def advance_ontime():
    global delay
    '''Pedestrian, push the 'walk' button ("space") to cross the street. '''
    delay = DELAY_CONST*2 #The first delay is bigger than the normal delay.
    for i in range(3):
        t1=time.time()
        time.sleep(delay)
        print(time.time() - t1)
        advance_state_machine()
        

wn.listen() # Listen for events
wn.onkeypress(advance_ontime, "space")

wn.mainloop()



