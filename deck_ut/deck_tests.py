# unit tests for the deck.py classes

import unittest
from deck import Card, Deck

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")
    def test_init(self):
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertEqual(type(self.deck.suits), list)
        self.assertEqual(type(self.deck.values), list)
        self.assertEqual(type(self.deck.cards[0]), Card)

    def test_repr(self):
        self.assertEqual( repr(self.deck), f"Deck of {self.deck.count()} cards")

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)
        self.deck = Deck()
        hand = self.deck._deal(53)
        self.assertTrue(hand)
        self.assertEqual(type(hand), list)
        self.assertEqual(len(hand), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal(self):
        self.assertEqual(type(self.deck._deal(1)), list)
        self.assertEqual(self.deck.count(), 51)
    def test_deal_card(self):
        self.assertEqual(type(self.deck.deal_card()), Card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        self.assertEqual(type(self.deck.deal_hand(5)), list)
        self.assertEqual(self.deck.count(), 47)
        self.assertEqual(type(self.deck.deal_hand(5)[0]), Card)
    
    def test_shuffle(self):
        deck_cpy = self.deck.cards[:]
        self.assertEqual(self.deck.cards, deck_cpy)
        self.deck.shuffle()
        self.assertNotEqual(self.deck, deck_cpy)
        self.assertEqual(self.deck.count(), 52)
        self.deck.deal_hand(5)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

if __name__ == "__main__":
    unittest.main()
