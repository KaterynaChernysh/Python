import turtle
import Tkinter
from body_parts import *
#Background
def draw_background(turtle):
    turtle.speed(900)
    drawGrass(turtle)
    drawPath(turtle)
    drawCloud(turtle,120,160)
    drawCloud(turtle,-150,35)
    drawGalgen(turtle)    #with rope
# Palayer
def draw_man(turtle, guesses):
    turtle.speed(900)
    if guesses == 1:
        drawHead(turtle, -10, 100, 30) #Head/Hair
    elif guesses == 2:
        drawBody(turtle)
    elif guesses == 3:
        drawLeftLeg(turtle)
    elif guesses == 4:
        drawRightLeg(turtle)
    elif guesses == 5:
        drawLeftHand(turtle)
    elif guesses == 6:
        drawRightHand(turtle)









