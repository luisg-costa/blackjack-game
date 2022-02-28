"""
Class Hand - make players hand
"""

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        # update value of Hand
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.aces > 0 and self.value > 21:
            for x in self.cards:
                if x.rank == 'Ace':
                    x.value = 1
