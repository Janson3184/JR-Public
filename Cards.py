import random
#   Input validation packages here?  Checks to see if user entering proper values?


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

    def __init__(self, has_joker=False):
        self.cards = []
        self.create_deck(has_joker)

    def create_deck(self, has_joker=False):
        '''Create a stack of cards.  May include a standard pair of Jokers.'''
        for i, value in enumerate([x for x in ['Ace'] + list(range(2,11)) + ['Jack','Queen','King']]):
            for suit in ['Spades', 'Hearts','Diamonds','Clubs']:
                self.cards.append(Card(value, suit))

        if has_joker:
            for suit in ['Joker']:
                for color in ['red','black']:
                    self.cards.append(Card(color,suit))

    def empty_deck(self):
        self.cards = []
        print('Deck is now emptied')

    def show_cards(self):
        print(f'There are {len(self.cards)} cards')
        for card in self.cards:
            card.show_card()

    def shuffle_cards(self):
        random.shuffle(self.cards)

class Player():
    '''Simple player.  Can draw cards and show hand.'''

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw_cards(self, Deck, number_of_cards):
        '''Select a number of cards from a deck.  Place those cards in hand.'''

        try:
            assert number_of_cards > 0
        except AssertionError as e:
            print(f'{self.name}: You must draw at least positive 1 card!!!')
        print(f'{self.name} is drawing {number_of_cards} cards' if number_of_cards != 1 else f'{self.name} is drawing {number_of_cards} card')

        for i in range(number_of_cards):
            self.inspect_deck(Deck)
            self.hand.append(Deck.cards.pop())

    def inspect_deck(self, Deck):
        '''Generate a new deck if there are no more cards.'''
        if len(Deck.cards) == 0:
            Deck.create_deck()

    def put_deck_in_the_fire(self, Deck):
        '''Just completely obliterate the deck.'''
        Deck.cards = []

    def show_hand(self):
        '''Display all cards in hand.'''
        print(f'{self.name} is showing a hand.')
        for card in self.hand:
            card.show_card()


my_deck = Deck(has_joker=True)
other_deck = Deck()

other_deck.empty_deck()
other_deck.show_cards()



#my_deck.show_cards()

print()

my_deck.shuffle_cards()

#my_deck.show_cards()

print(len(my_deck.cards)) # Before bob draws from the deck.

bob = Player('Bob')
bob.draw_cards(my_deck, 5)
bob.show_hand()

print(len(my_deck.cards)) # After bob draws from the deck.

#bob.put_deck_in_the_fire(my_deck)
my_deck.show_cards()
