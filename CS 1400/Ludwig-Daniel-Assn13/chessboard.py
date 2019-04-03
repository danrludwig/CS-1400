import turtle


class Chessboard:

    def __init__(self, startX, startY, width, height):
        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height

    def __boardPerimeter(self):
        turtle.penup()
        turtle.goto(self.__startX, self.__startY)
        turtle.setheading(90)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)

    def __drawRectangle(self):
        turtle.penup()
        turtle.forward(self.__width / 8)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(self.__width / 8)
        turtle.left(90)
        turtle.forward(self.__height / 8)
        turtle.left(90)
        turtle.forward(self.__width / 8)
        turtle.left(90)
        turtle.forward(self.__height / 8)
        turtle.end_fill()
        turtle.left(90)
        turtle.forward(self.__width / 8)
        turtle.penup()


    def __drawAllRectangles(self):
        i = 1
        startY2 = (self.__startY + (self.__height / 8))
        startX2 = (self.__startX + (self.__width / 8))
        while i < 17:
            if i == 1:
                turtle.penup()
                turtle.goto(self.__startX, self.__startY)
                turtle.setheading(90)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.setheading(0)
                self.__drawRectangle()
                i += 1
            if i <= 4 and i != 1:
                self.__drawRectangle()
                i += 1
            if i == 5:
                turtle.goto(self.__startX, self.__startY)
                turtle.setheading(90)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.setheading(0)
                self.__drawRectangle()
                i += 1
            if i <= 8 and i > 5:
                self.__drawRectangle()
                i += 1
            if i == 9:
                turtle.goto(self.__startX, self.__startY)
                turtle.setheading(90)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.setheading(0)
                self.__drawRectangle()
                i += 1
            if i <= 12 and i > 9:
                self.__drawRectangle()
                i += 1
            if i == 13:
                turtle.goto(self.__startX, self.__startY)
                turtle.setheading(90)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.setheading(0)
                self.__drawRectangle()
                i += 1
            if i <= 16 and i > 13:
                self.__drawRectangle()
                i += 1
        while i >= 17 and i <= 32:
            if i == 17:
                turtle.goto(startX2, startY2)
                turtle.setheading(90)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.right(180)
                self.__drawRectangle()
                i += 1
            if i <= 20 and i != 17:
                self.__drawRectangle()
                i += 1
            if i == 21:
                turtle.goto(startX2, startY2)
                turtle.setheading(90)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.right(180)
                self.__drawRectangle()
                i += 1
            if i <= 24 and i > 21:
                self.__drawRectangle()
                i += 1
            if i == 25:
                turtle.goto(startX2, startY2)
                turtle.setheading(90)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.right(180)
                self.__drawRectangle()
                i += 1
            if i <= 28 and i > 25:
                self.__drawRectangle()
                i += 1
            if i == 29:
                turtle.goto(startX2, startY2)
                turtle.setheading(90)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.forward(self.__height / 8)
                turtle.left(90)
                turtle.forward(self.__width / 8)
                turtle.right(180)
                self.__drawRectangle()
                i += 1
            if i <= 32 and i > 29:
                self.__drawRectangle()
                i += 1

    def draw(self):
        turtle.speed(200)
        self.__boardPerimeter()
        self.__drawAllRectangles()
