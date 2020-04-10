import random

class Card():
    '''
    A simple card object.  Has a value and a suit.
    '''

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show_card(self):
        print(f'{self.value} of {self.suit}')


class Deck():
    '''A deck of cards.  Generates a list of card objects. Allows for shuffling and showing all cards.'''

    def __init__(self):
        self.cards = []

    def create_deck(self):
        for i, value in enumerate([x for x in ['Ace'] + list(range(2,11)) + ['Jack','Queen','King']]):
            for suit in ['Spades', 'Hearts','Diamonds','Clubs']:
                self.cards.append(Card(value, suit))

    def show_cards(self):
        for card in self.cards:
            card.show_card()

    def shuffle_cards(self):
        random.shuffle(self.cards)

class Player():
    '''Simple player.  Can draw cards and show hand.'''

    def __init__(self):
        self.hand = []

    def draw_cards(self, Deck, number_of_cards):
        for _ in range(number_of_cards):
            self.hand.append(Deck.cards.pop())

    def show_hand(self):
        for card in self.hand:
            card.show_card()


my_deck = Deck()

my_deck.create_deck()
#my_deck.show_cards()

print()

my_deck.shuffle_cards()

#my_deck.show_cards()

print(len(my_deck.cards)) # Before bob draws from the deck.

bob = Player()
bob.draw_cards(my_deck, 6)
bob.show_hand()

print(len(my_deck.cards)) # After bob draws from the deck.
