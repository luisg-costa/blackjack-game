class Game:
    def __init__(self):
        self.playing = True

    @staticmethod
    def hit(game_deck, hand):
        hand.add_cards(game_deck.deal())

    def hit_or_stand(self, game_deck, hand):
        while True:
            hit_stand = input('Do you want hit or stand? (Hit or Stand)').capitalize()
            if hit_stand not in ['Hit', 'Stand']:
                print('Please insert a correct input.')
            elif hit_stand == 'Hit':
                Game.hit(game_deck, hand)
                break
            else:
                self.playing = False
                break

    @staticmethod
    def show_some(player_hand, dealer):
        print('Player cards:')
        for card in player_hand.cards:
            print(card)
        print(f'Value: {player_hand.value}')
        print('\n')
        print('Dealer cards:')
        print(dealer.cards[0])
        print('hidden card')

    @staticmethod
    def show_all(player_hand, dealer):
        print('Player cards:')
        for card in player_hand.cards:
            print(card)
        print(f'Value Player Hand: {player_hand.value}')
        print('\n')
        print('Dealer cards:')
        for card in dealer.cards:
            print(card)
        print(f'Value Dealer Hand: {dealer.value}')

    @staticmethod
    def player_busts(chips):
        print('Player loses!')
        chips.lose_bet()

    @staticmethod
    def player_wins(chips):
        print('Player wins!')
        chips.win_bet()

    @staticmethod
    def dealer_busts(chips):
        print('Dealer busts!')
        chips.win_bet()

    @staticmethod
    def dealer_wins(chips):
        print('Dealer wins!')
        chips.lose_bet()

    @staticmethod
    def push(chips):
        print('Its a tie!')
        chips.amount += chips.bet