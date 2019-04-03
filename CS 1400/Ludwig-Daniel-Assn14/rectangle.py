import turtle


class Rectangle:

    def __init__(self, rectangleSpecs):
        self.position = (rectangleSpecs[0], rectangleSpecs[1])
        self.width = rectangleSpecs[2]
        self.height = rectangleSpecs[3]
        self.color = str(rectangleSpecs[4])

    def draw(self):
        self.setPosition()
        self.setColor()
        self.drawRectangle()

    def setPosition(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.setheading(0)
        turtle.pendown()

    def setColor(self):
        color = ['yellow', 'red', 'blue', 'green']
        if self.color == '1':
            turtle.fillcolor(color[0])
        if self.color == '2':
            turtle.fillcolor(color[1])
        if self.color == '3':
            turtle.fillcolor(color[2])
        if self.color == '4':
            turtle.fillcolor(color[3])

    def drawRectangle(self):
        turtle.showturtle()
        turtle.begin_fill()
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.end_fill()
        turtle.hideturtle()