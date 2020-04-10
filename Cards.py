import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        


    def show_card(self):
        print(f'I am the {self.value} of {self.suit}!')


class Deck():
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
    def __init__(self):
        self.hand = []

    def draw_card(self, Deck):
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

print(len(my_deck.cards))

bob = Player()
bob.draw_card(my_deck)
bob.show_hand()

print(len(my_deck.cards))
