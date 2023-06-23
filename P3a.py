'''Write a program to
i) Shuffle the deck of cards.
ii)To choose one single card from deck.
iii)To create a random sample of size 2 from the available deck of cards.'''
#Built in

import random

# Define the ranks, suits, and deck of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck of cards
random.shuffle(deck)

# Choose a single card from the deck
single_card = random.choice(deck)

# Create a random sample of size 2 from the deck
sample = random.sample(deck, k=2)

# Print the shuffled deck, the chosen card, and the sample
print("Shuffled deck of cards:")
print(deck)
print("\nChosen card:")
print(single_card)
print("\nRandom sample of size 2:")
print(sample)
