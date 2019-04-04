import turtle
import random

tr = turtle.Turtle()
tr.showturtle()


def done():
    turtle.done()


def reset():
    tr.reset()


def setup():
    tr.speed(0)
    turtle.setup(width=1000, height=800)

def setRandomColor():
    numColor = random.randint(0,3)
    if numColor == 3:
        tr.color('blue')
    if numColor == 1:
        tr.color('red')
    if numColor == 2:
        tr.color('green')


def drawRectangle(width, height, rotation):
    setRandomColor()
    tr.pendown()
    tr.forward(width)
    tr.left(90)
    tr.forward(height)
    tr.left(90)
    tr.forward(width)
    tr.left(90)
    tr.forward(height)
    tr.left(90)


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    tr.setheading(rotation)
    setup()
    tr.penup()
    tr.goto(centerX, centerY)
    for i in range(count):
        if i <= count:
            tr.right(360 / count)
            tr.forward(offset)
            drawRectangle(width, height, rotation)
            tr.penup()
            tr.goto(centerX, centerY)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    tr.setheading(0)
    setup()
    for i in range(count):
        if i <= count:
            tr.penup()
            tr.goto(centerX, centerY)
            tr.forward(offset)
            setRandomColor()
            tr.pendown()
            tr.right(90)
            tr.right(360 / count)
            tr.circle(radius)
            tr.left(90)


def drawSuperPattern(num):
    for i in range(int(num)):
        if i <= num:
            centerX = random.randint(-300, 300)
            centerY = random.randint(-400, 400)
            offset = random.randint(0, 100)
            radius = random.randint(0, 100)
            count = random.randint(20, 300)
            width = random.randint(5, 300)
            height = random.randint(5, 300)
            rotation = random.randint(0, 360)
            whichShape = random.randint(0, 2)
            if whichShape == 1:
                drawCirclePattern(centerX, centerY, offset, radius, count)
            if whichShape == 2:
                drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
