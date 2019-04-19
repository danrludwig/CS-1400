from deck import Deck
deck = Deck()

def bubble_sort(list):
    count = 0
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) -1 -i):
            if list[j].getCardValue() > list[j+1].getCardValue():
                list[j], list[j+1] = list[j+1], list[j]
        count += 1
        print(count, ':', list)
    return list

def insertion_sort(list):
    count = 0
    for i in range(1, len(list)):
        j = i-1
        while list[j].getCardValue() > list[j+1].getCardValue() and j >= 0:
            list[j], list[j+1] = list[j+1], list[j]
            j -= 1
        count += 1
        print(count, ':', list)
    return(list)

def main():
    hand = []

    for i in range(20):
        card = deck.draw()
        hand.append(card)

    correct = False
    while not correct:
        sort = eval(input('1) bubble sort\n2) insertion sort\nWhich way would you like to sort? '))
        if sort == 1:
            bubble_sort(hand)
            correct = True
        elif sort == 2:
            insertion_sort(hand)
            correct = True
        else:
            print('Wrong input')

main()