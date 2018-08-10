import turtle


# Umgebung
def drawGrass(turtle):
    turtle.setheading(90)
    turtle.fillcolor('#054403')
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(-350, -300)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(800)
        turtle.right(90)
    turtle.end_fill()


def drawPath(turtle):
    turtle.setheading(90)
    turtle.color(0, 0, 0)
    turtle.fillcolor('#158000')
    turtle.penup()
    turtle.goto(-45, -287)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(10)
    turtle.forward(100)
    turtle.right(80)
    turtle.forward(40)
    turtle.right(80)
    turtle.forward(100)
    turtle.right(80)
    turtle.end_fill()
    turtle.setheading(90)


def drawCloud(turtle, x, y):
    turtle.setheading(90)
    turtle.fillcolor('#ffffff')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.color('#ffffff')
    for i in range(10):
        turtle.circle(40)
        turtle.right(36)
        turtle.forward(10)
    turtle.end_fill()
    turtle.setheading(90)


def drawGalgen(turtle):
    turtle.color(0, 0, 0)
    turtle.fillcolor('#907000')
    turtle.penup()
    turtle.goto(-160, -190)
    turtle.pendown()
    turtle.setheading(90)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)


# Player
def drawHead(turtle, x, y, size):
    turtle.setheading(0)
    turtle.color("white")
    turtle.fillcolor("black")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def drawHair(turtle, x, y):
    turtle.setheading(90)
    turtle.fillcolor("white")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.color("grey")
    for x in range(10):
        turtle.circle(10)
        turtle.right(16)
        turtle.forward(10)
    turtle.end_fill()
    turtle.setheading(90)


def drawBody(turtle):
    turtle.setheading(90)
    turtle.fillcolor("black")
    turtle.penup()
    # Neck
    turtle.goto(-15, 100)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(2):
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(100)
    turtle.end_fill()


def drawLeftLeg(turtle):
    turtle.setheading(90)
    turtle.fillcolor("black")
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(135)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.end_fill()

def drawRightLeg(turtle):
    turtle.setheading(90)
    turtle.fillcolor("black")
    turtle.penup()
    turtle.goto(-2, -6)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(45)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.end_fill()

def drawLeftHand(turtle):
    turtle.setheading(90)
    turtle.fillcolor("black")
    turtle.penup()
    turtle.goto(-20, 100)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(135)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.end_fill()

def drawRightHand(turtle):
    turtle.setheading(90)
    turtle.fillcolor("black")
    turtle.penup()
    turtle.goto(-2, 94)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(45)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.end_fill()

