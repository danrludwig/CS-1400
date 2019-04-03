import turtle


class Circle:

    def __init__(self, circleSpecs):
        self.position = circleSpecs[0], circleSpecs[1] - circleSpecs[2]
        self.radius = circleSpecs[2]
        self.color = str(circleSpecs[3])

    def draw(self):
        self.setColor()
        self.setPosition()
        self.drawCircle()

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

    def setPosition(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.setheading(0)
        turtle.pendown()

    def drawCircle(self):
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        turtle.hideturtle()
