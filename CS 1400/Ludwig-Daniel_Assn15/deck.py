from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 120):
            card = Card(i)
            self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards[:30]
