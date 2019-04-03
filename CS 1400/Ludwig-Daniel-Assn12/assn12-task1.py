import turtle



class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def __draw_head(self):
        if self.__happy == True:
            turtle.setheading(0)
            turtle.showturtle()
            turtle.penup()
            turtle.width(1)
            turtle.goto(0, -100)
            turtle.pendown()
            turtle.fillcolor('yellow')
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
        else:
            turtle.setheading(0)
            turtle.showturtle()
            turtle.penup()
            turtle.width(1)
            turtle.goto(0, -100)
            turtle.pendown()
            turtle.fillcolor('red')
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()

    def __draw_eyes(self):
        if self.__dark_eyes == True:
            turtle.penup()
            turtle.goto(-30, 30)
            turtle.pendown()
            turtle.fillcolor('black')
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(30, 30)
            turtle.pendown()
            turtle.fillcolor('black')
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()
        else:
            turtle.penup()
            turtle.goto(-30, 30)
            turtle.pendown()
            turtle.fillcolor('blue')
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(30, 30)
            turtle.pendown()
            turtle.fillcolor('blue')
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()

    def __draw_mouth(self):
        if self.__smile == True:
            turtle.penup()
            turtle.goto(-40, -30)
            turtle.setheading(325)
            turtle.pendown()
            turtle.width(5)
            turtle.circle(70, 70)
            turtle.hideturtle()
        else:
            turtle.penup()
            turtle.goto(40, -30)
            turtle.setheading(325)
            turtle.pendown()
            turtle.width(5)
            turtle.circle(-70, -70)
            turtle.hideturtle()

    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
