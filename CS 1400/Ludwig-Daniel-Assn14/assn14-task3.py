import turtle
from circle import Circle
from rectangle import Rectangle


def main():
    end = False
    objects = []

    while not end:
        print('- Enter Circle [1]: ')
        print('- Enter Rectangle [2]: ')
        print('- Remove Shape [3]: ')
        print('- Draw Shapes [4]: ')
        print('- Exit [5]: ')
        command = input('Enter a number corresponding with an action: ')
        if command == '1':
            realColor = False
            circleSpecs = []
            startX = eval(input('Enter X position: '))
            startY = eval(input('Enter Y position: '))
            radius = eval(input('Enter radius: '))
            while not realColor:
                color = eval(input('Enter number for color (yellow[1], red[2], blue[3], green[4]: '))
                if color in range(1,5):
                    realColor = True
                else:
                    print('Invalid color number. Try again out of 1, 2, 3, or 4.')
            circleSpecs.append(str(startX))
            circleSpecs.append(str(startY))
            circleSpecs.append(str(radius))
            circleSpecs.append(str(color))
            objects.append('_'.join(circleSpecs))
        if command == '2':
            realColor = False
            rectangleSpecs = []
            startX = eval(input('Enter X position: '))
            startY = eval(input('Enter Y position: '))
            width = eval(input('Enter width: '))
            height = eval(input('Enter height: '))
            while not realColor:
                color = eval(input('Enter number for color (yellow[1], red[2], blue[3], green[4]: '))
                if color in range(1,5):
                    realColor = True
                else:
                    print('Invalid color number. Try again out of 1, 2, 3, or 4.')
            rectangleSpecs.append(str(startX))
            rectangleSpecs.append(str(startY))
            rectangleSpecs.append(str(width))
            rectangleSpecs.append(str(height))
            rectangleSpecs.append(str(color))
            objects.append('_'.join(rectangleSpecs))
        if command == '3':
            count = 0
            num = 0
            while count < len(objects):
                print(objects[num], '(' + str(num) + ')')
                count += 1
                num += 1
            shape = eval(input('Enter which shape to remove: '))
            del objects[shape]
        if command == '4':
            turtle.clear()
            for shape_string in objects:
                shape_parameters = [int(number_string) for number_string in shape_string.split('_')]
                if len(shape_parameters) == 4:
                    my_circle = Circle(shape_parameters)
                    my_circle.draw()
                elif len(shape_parameters) == 5:
                    Rectangle(shape_parameters).draw()
                else:
                    print('weird shit in here: {}'.format(shape_parameters))
        if command == '5':
            end = True

main()