class Cards():
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False

    def __eq__(self, other):
        return self.card == other.card

    def __str__(self):
        return self.card


if __name__ == '__main__':
    card1 = Cards('egg', 'A1')
    card2 = Cards('egg', 'B1')
    card3 = Cards('hut', 'D4')

    print(card1 == card2)
    print(card1 == card3)
    print(card1)
