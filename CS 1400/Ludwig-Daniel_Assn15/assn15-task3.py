from deck import Deck


def main():
    print('Welcome to the Gubbins Deck Checker\n')
    done = False
    deck = Deck()
    deck.shuffle()
    hand = deck.draw()
    while not done:
        print('New Hand\n')
        print('1) Sort by value')
        print('2) Sort by id')
        print('3) Find card')
        print('4) New hand')
        print('5) Quit')
        command = eval(input('Make a selection: '))
        if command == 1:
            selectionSortByValue(hand)
            for i in range(len(hand)):
                print(hand[i])
        if command == 2:
            selectionSortByHand(hand)
            for i in range(len(hand)):
                print(hand[i])
        if command == 3:
            value = eval(input('Enter a value: '))
            mano = eval(input('1) Rock\n'
                              '2) Paper\n'
                              '3)Scissors\n'
                              'Enter a hand: '))
            coin = eval(input('1) Heads\n'
                              '2) Tails\n'
                              'Enter a coin: '))
            hand_offset = [0, 40, 80]
            expected_id = hand_offset[mano - 1] + ((value - 1) * 2)
            if coin == 2:
                expected_id += 1
            print(expected_id)
            search_result = binary_search(hand, expected_id)
            if search_result > -1:
                print('The card is in your hand')
            else:
                print('The card is not in your hand')
        if command == 4:
            deck.shuffle()
            hand = deck.draw()
            for i in range(len(hand)):
                print(hand[i])
        if command == 5:
            done = True
        else:
            pass


def selectionSortByValue(cardList): #got how to do this function from the demo code the professor provided
    for i in range(len(cardList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(cardList)):
            # compare items to see if there's something smaller
            if cardList[currMinIndex].value > cardList[j].value:
                currMinIndex = j

        # Swap the lowest item and the current item
        if currMinIndex != i:
            cardList[i], cardList[currMinIndex] = cardList[currMinIndex], cardList[i]

def selectionSortByHand(cardList): #got how to do this function from the demo code the professor provided
    for i in range(len(cardList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(cardList)):
            # compare items to see if there's something smaller
            if cardList[currMinIndex].id > cardList[j].id:
                currMinIndex = j

        # Swap the lowest item and the current item
        if currMinIndex != i:
            cardList[i], cardList[currMinIndex] = cardList[currMinIndex], cardList[i]

def binary_search(hand, key): #got how to do this function from the demo code the professor provided
    low_point = 0
    high_point = 29
    while high_point >= low_point:
        print(low_point, high_point)
        mid = (high_point + low_point) // 2
        if key == hand[mid].id:
            return mid
        elif key < hand[mid].id:
            high_point = mid - 1
        else:
            low_point = mid + 1
    return -1

main()
