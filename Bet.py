"""
Bet - control players bets
"""

class Bet:

    def __init__(self, total=100):
        self.amount = total
        self.bet = 0

    def win_bet(self):
        self.amount += self.bet

    def lose_bet(self):
        self.amount -= self.bet

    def take_bet(self):
        while True:
            try:
                user_bet = int(input('Please, input a value of your bet: '))
            except:
                print('Please input a correct value.')
            else:
                if user_bet > self.amount:
                    print('You dont have enough chips for this bet')
                else:
                    self.bet = user_bet
                    print('Bet placed')
                    break
