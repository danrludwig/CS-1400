import turtle
tr = turtle.Turtle()
tr.showturtle()

startX, startY = eval(input('Enter at start positions: '))
width = float(input('Enter the width: ') or 250)
height = float(input('Enter the height: ') or 250)

# if height == None:
#     height = float(250)
# if width == None:
#     width = float(250)

# height = float(height)
# width = float(width)

def boardPerimeter():
    tr.penup()
    tr.goto(startX, startY)
    tr.setheading(90)
    tr.pendown()
    tr.right(90)
    tr.forward(width)
    tr.left(90)
    tr.forward(height)
    tr.left(90)
    tr.forward(width)
    tr.left(90)
    tr.forward(height)

def drawRectangle():
    tr.penup()
    tr.forward(width / 8)
    tr.pendown()
    tr.begin_fill()
    tr.forward(width / 8)
    tr.left(90)
    tr.forward(height / 8)
    tr.left(90)
    tr.forward(width / 8)
    tr.left(90)
    tr.forward(height / 8)
    tr.end_fill()
    tr.left(90)
    tr.forward(width / 8)
    tr.penup()


def drawAllRectangles():
    i = 1
    startY2 = (startY + (height / 8))
    startX2 = (startX + (width / 8))
    while i < 17:
        if i == 1:
            tr.penup()
            tr.goto(startX, startY)
            tr.setheading(90)
            tr.left(90)
            tr.forward(width / 8)
            tr.setheading(0)
            drawRectangle()
            i += 1
        if i <= 4 and i != 1:
            drawRectangle()
            i += 1
        if i == 5:
            tr.goto(startX, startY)
            tr.setheading(90)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.left(90)
            tr.forward(width / 8)
            tr.setheading(0)
            drawRectangle()
            i += 1
        if i <= 8 and i > 5:
            drawRectangle()
            i += 1
        if i == 9:
            tr.goto(startX, startY)
            tr.setheading(90)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.left(90)
            tr.forward(width / 8)
            tr.setheading(0)
            drawRectangle()
            i += 1
        if i <= 12 and i > 9:
            drawRectangle()
            i += 1
        if i == 13:
            tr.goto(startX, startY)
            tr.setheading(90)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.left(90)
            tr.forward(width / 8)
            tr.setheading(0)
            drawRectangle()
            i += 1
        if i <= 16 and i > 13:
            drawRectangle()
            i += 1
    while i >= 17 and i <= 32:
        if i == 17:
            tr.goto(startX2, startY2)
            tr.setheading(90)
            tr.left(90)
            tr.forward(width / 8)
            tr.right(180)
            drawRectangle()
            i += 1
        if i <= 20 and i != 17:
            drawRectangle()
            i += 1
        if i == 21:
            tr.goto(startX2, startY2)
            tr.setheading(90)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.left(90)
            tr.forward(width / 8)
            tr.right(180)
            drawRectangle()
            i += 1
        if i <= 24 and i > 21:
            drawRectangle()
            i += 1
        if i == 25:
            tr.goto(startX2, startY2)
            tr.setheading(90)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.left(90)
            tr.forward(width / 8)
            tr.right(180)
            drawRectangle()
            i += 1
        if i <= 28 and i > 25:
            drawRectangle()
            i += 1
        if i == 29:
            tr.goto(startX2, startY2)
            tr.setheading(90)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.forward(height / 8)
            tr.left(90)
            tr.forward(width / 8)
            tr.right(180)
            drawRectangle()
            i += 1
        if i <= 32 and i > 29:
            drawRectangle()
            i += 1

def drawChessboard():
    tr.speed(200)
    boardPerimeter()
    drawAllRectangles()
    tr.hideturtle()
    turtle.done()


drawChessboard()