import random


class Deck:
    #needs to create the deck
    def __init__(self):
        self.cards = {
            'Clubs': list(range(1, 14)),
            'Diamonds': list(range(1, 14)),
            'Hearts': list(range(1, 14)),
            'Spades': list(range(1, 14))
        }


class Player(Deck):
    #needs to make a hand?
    # needs to have first draw (which is 2 cards)
    # then a continuous draw
    
    def __init__(self):
        
        self.success = 21
        Deck().__init__()
        #First draw of 2 cards, then remove from deck
        first_card_suit, first_card_number = random.choice(list(self.cards.items()))
        first_card_number = random.choice(first_card_number)
        del self.cards[first_card_suit][first_card_number - 1]
        self.deal_first = [first_card_suit, first_card_number]
        print(f'Your first card is the {self.deal_first[0]} of {self.deal_first[1]}')

        #Second draw of 2 cards, then remove from deck
        second_card_suit, second_card_number = random.choice(list(self.cards.items()))
        second_card_number = random.choice(second_card_number)
        del self.cards[second_card_suit][second_card_number - 1]
        self.deal_second = [second_card_suit, second_card_number]
        print(f'Your first card is the {self.deal_second[0]} of {self.deal_second[1]}')

        # setting the initial score
        self.score = int(self.deal_first[1] + self.deal_second[1])

    def draw(self):
        card_suit, card_number = random.choice(list(self.cards.items()))
        card_number = random.choice(card_number)
        del self.cards[card_suit][card_number - 1]
        self.deal = [card_suit, card_number]
        print(f'You have been dealt the {card_number} of {card_suit}')
        self.score += int(self.deal[1])
        print(f'this is your draw score {self.score}')

    def play(self):
        print(f'this is your play score {self.score}')
        if print(self.score) > 21:
            print(
                f'Woah there, have you forgotten the rules? Your score is {self.score}, that"s clearly not 21. ')
            return
        elif print(self.score) == 21:
            print(f'Congratulations!!! Your score is {self.score}, you have won! ')
        else:
            self.score = int(self.score)
            while print(self.score) < 21:
                checking = input(f'Your current score is {self.score}, would you like to keep playing? (Yes, No, Quit) ') 
                if checking == 'yes':
                    self.score = Player.draw(self)
                elif checking == 'no' or 'quit':
                    print('Goodbye! ')
                    break
                else:
                    print('Incorrect response')
                    return
            
# cont_play = input('Would you like to continue? (Yes, No, Quit)? ')
# if cont_play == 'yes':
#     return self.score
# elif cont_play == 'no' or 'quit':
#     print('Goodbye!')
    

# class Dealer(Player):
#     # needs to have his own hand
#     # needs to have functionality of 'hitting'
#     # store it's own value for blackjack
#     # show first card, and then every other card drawn
#     dealer_hand = []
#     def __init__(self):
#         super().__init__()


# class Human(Player):
#     # needs to have his own hand
#     # store it's own value for blackjack
#     # show all cards
#     def __init__(self):
#         super().__init__()

#     pass

class Game:
    # start the game
    # get human/dealer hand
    def __init__(self):
        play = input('Would you like to play BlackJack? (Yes / No / Quit) ').lower()
        if play == 'yes':
            print('Instructions: You will initially be dealt 2 cards. The goal of this game is to get your cards to total to 21, or the highest number possible without going over 21. ')
            Deck.__init__(self)
            Player.__init__(self)
            Player.play(self)
            Player.draw
        elif play == 'no' or 'quit':
            print('Thank you and take care. ')
        else:
            print(
                'You did not follow instructions. Please enter "Yes", "No", or "Quit" without any spaces. ')
            return

y = Game()


# def main():
#     pass


# main()
