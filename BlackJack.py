"""
Blackjack Game . 1 Dealer machine . 1 Human Player
"""

# imports
from Deck import Deck
from Hand import Hand
from Bet import Bet
from GameControl import Game

if __name__ == '__main__':

    # welcome message
    print('Welcome to Blackjack Game!')
    player_name = input('Please insert your name: ')
    print(f'Welcome {player_name}. Lets start the game!')
    bet = Bet()
    
    while True:
        game = Game()
        deck = Deck()
        deck.shuffle()

        player = Hand()
        dealer = Hand()

        player.add_cards(deck.deal())
        player.add_cards(deck.deal())

        dealer.add_cards(deck.deal())
        dealer.add_cards(deck.deal())

        bet.take_bet()
        print('\n')
        print('*************** BET **********************')
        print('Amount = ' + str(bet.amount))
        print('Bet = ' + str(bet.bet))
        print('\n')

        game.show_some(player, dealer)
        print('\n')
        
        while game.playing:
            game.hit_or_stand(deck, player)
            game.show_some(player, dealer)
            player.adjust_for_ace()
            if player.value > 21:
                game.player_busts(bet)
                break
            
        if player.value <= 21:
            while dealer.value < 17:
                game.hit(deck, dealer)
                dealer.adjust_for_ace()
            game.show_all(player, dealer)

            if dealer.value > 21:
                game.dealer_busts(bet)

            elif dealer.value > player.value:
                game.dealer_wins(bet)

            elif dealer.value < player.value:
                game.player_wins(bet)

            else:
                game.push(bet)

        print(f'{player_name} have ' + str(bet.amount) + ' chips')
        if bet.amount == 0:
            print('you lose, goodbye')
            break
        play_again = ''
        while play_again == '':
            play_again = input('Do you want play again? (Y or N)').upper()
            if play_again not in ['Y', 'N']:
                print('Please insert a correct input (Y or N)')
                play_again = ''
        if play_again == 'N':
            print(f'See you next time {player_name}')
            break
