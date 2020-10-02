import random

# This exercise aims to create a model of a Card and of a Deck using OOP/Classes.
# The Deck class uses Card objects.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []

        for s in self.suits:
            for v in self.values:
                self.cards.append(Card(s, v))
    
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, n):
        if n > self.count():
            n = self.count()
        popd = []
        for i in range(0, n):
            popd.append(self.cards.pop())
        return popd

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, n):
        return self._deal(n)

def add_draft(hand, draft):
    if type(draft) is Card:
        hand.append(draft)
    else:
        for c in draft:
            hand.append(c)
    return hand

# TESTS:
if __name__ == "__main__":
    deck_1 = Deck()
    print(deck_1)
    deck_1.shuffle()
    hand = []

    add_draft(hand, deck_1.deal_card())
    add_draft(hand, deck_1.deal_card())
    print(deck_1)
    print(hand)
    print("number of cards in HAND:", len(hand))
    print("*****************************")

    add_draft(hand, deck_1.deal_hand(12))
    print(deck_1)
    print(hand)
    print("number of cards in HAND:", len(hand))
    print("*****************************")
    # deck_1.shuffle()
    add_draft(hand, deck_1.deal_hand(50))
    print(deck_1)
    print("number of cards in HAND:", len(hand))

    deck_2 = Deck()
    for card in deck_2:
        print(card)
