from polygon import Polygon

def main():
    valid1 = False
    valid2 = False

    while not valid1:
        sides1 = eval(input('Enter number of sides for first polygon: '))
        if sides1 < 3:
            print('You entered a number less than 3, please enter a number for a valid polygon')
        else: valid1 = True
    while not valid2:
        sides2 = eval(input('Enter number of sides for second polygon: '))
        if sides2 < 3:
            print('You entered a number less than 3, please enter a number for a valid polygon')
        else:
            valid2 = True

    polygon1 = Polygon(sides1)
    polygon2 = Polygon(sides2)

    print('The polygons combined equal a polygon with ', polygon1 + polygon2, 'sides.')
    while valid1 == True:
        if str(polygon1 - polygon2) < str(3):
            print('The first polygon minus the second polygon is too small to be a polygon because it has',
                  polygon1 - polygon2, 'sides.')
            valid1 = False
        else:
            print('The first polygon minus the second polygon equal a polygon with', polygon1 - polygon2, 'sides.')
            valid1 = False
    print('The first polygon is less than the second polygon:', polygon1 < polygon2)
    print('The first polygon is greater than the second polygon:', polygon1 > polygon2)
    print('The first polygon equals the second polygon: ', polygon1 == polygon2)
    print('The length of the first polygon is:', len(polygon1))
    print('The length of the second polygon is:', str(polygon2))

main()