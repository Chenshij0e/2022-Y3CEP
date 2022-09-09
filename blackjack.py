#GAMEPLAY IS NOT ORIGINAL BUT ACCOUNT AND BETTING SYSTEM IS

import random
import time

suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

playing = True

#CLASS DEFINTIONS (CARDS):

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []  #start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) #creates a full deck of cards

    def __str__(self):
        deck_comp = ""  #start with an empty string
        for card in self.deck:
            deck_comp += "\n " + card.__str__()  #add each Card object's print string
        return "The deck has:" + deck_comp

    def shuffle(self):
        #shuffles the deck
        random.shuffle(self.deck)

    def deal(self):
        #removes one card from the deck
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  #start with an empty list as we did in the Deck class
        self.value = 0  #start with zero value
        self.aces = 0  #add an attribute to keep track of aces

    def add_card(self, card):
        #draw one card from deck
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "A":
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        #reduces the ace to a 1 if the sum of the hand is greater than 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
