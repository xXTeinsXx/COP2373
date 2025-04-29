# Poker
# Program that deals a Poker hand of five cards
# Written on Monday 7-8/4/25 by Bry.

import random

class Card:
    # Represents a standard playing card. 
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"
    
    def __lt__(self, other):
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        return self.rank < other.rank


class Deck:
    # Represents a deck of cards.
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def move_cards(self, hand, num):
        for i in range(num):
            if self.cards:
                hand.add_card(self.pop_card())


class Hand(Deck):
    # Represents a hand of playing cards.
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def deal_poker_hand(deck):
    # Deals a poker hand of 5 cards from the deck.
    hand = Hand("Poker Hand")
    deck.move_cards(hand, 5)
    return hand


def replace_cards(hand, deck, positions):
    # Replaces cards at specified positions (0-4) with new cards from the deck.
    # Convert positions to 0-based indexing
    positions = [pos - 1 for pos in positions]
    
    # Replace cards at the specified positions
    for pos in sorted(positions, reverse=True):
        if 0 <= pos < len(hand.cards):
            # Remove the card at position
            hand.cards.pop(pos)
            # Add a new card from the deck
            if deck.cards:
                hand.add_card(deck.pop_card())


def display_hand(hand):
    # Displays the cards in the hand with their positions.# 
    print(f"\n{hand.label}:")
    for i, card in enumerate(hand.cards):
        print(f"{i+1}. {card}")


def main():
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()
    
    # Deal initial poker hand
    hand = deal_poker_hand(deck)
    
    # Display initial hand
    display_hand(hand)
    
    # Ask user which cards to replace
    while True:
        try:
            user_input = input("\nEnter the positions of cards to replace (e.g., 1,3,5) or press Enter to keep all: ")
            if user_input.strip() == "":
                positions = []
                break
            
            positions = [int(pos.strip()) for pos in user_input.split(',')]
            
            # Validate positions
            if any(pos < 1 or pos > 5 for pos in positions):
                print("Invalid positions. Please enter numbers between 1 and 5.")
                continue
            
            break
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
    
    # Replace selected cards
    replace_cards(hand, deck, positions)
    
    # Display final hand
    print("\nAfter drawing new cards:")
    display_hand(hand)


# Checks to see if the user wants to run the code
def runcode():
    runcode = str(input("Do you want to run this code? (y/n): "))
    return runcode.casefold()

 # Asks the user if they want to run the code
while runcode() == "y":
     main()

# If the user doesn't want to run the code, the program will end    
else:
    print('Goodbye! 👋 See you next time!')