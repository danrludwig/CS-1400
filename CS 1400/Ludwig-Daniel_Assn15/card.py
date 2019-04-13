class Card:
    HAND = ['Rock', 'Papers', 'Scissors']

    def __init__(self, card_id):
        self.id = card_id  # type: int
        self.value = int(self.id / 2) % 20 + 1  # type: int
        self.__coin = 'Heads' if self.id % 2 == 0 else 'Tails'  # type: str
        self.__hand = ''  # type: str

        if self.id <= 39:
            self.__hand = 'Rock'
        elif 39 < self.id <= 79:
            self.__hand = 'Paper'
        elif self.id > 79:
            self.__hand = 'Scissors'

    def __str__(self):
        return '{} of {} {}'.format(self.value, self.__hand, self.__coin)

    def __repr__(self):
        return repr('{}: {} of {} {}'.format(self.id, self.value, self.__hand, self.__coin))
