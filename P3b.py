'''Write a program to
i) Shuffle the deck of cards.
ii)To choose one single card from deck.
iii)To create a random sample of size 2 from the available deck of cards.'''
#Without built in

# Define the ranks, suits, and deck of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [(rank, suit) for rank in ranks for suit in suits]

# Function to shuffle a list using Fisher-Yates algorithm
def shuffle_list(lst):
    num_cards = len(lst)
    for i in range(num_cards - 1, 0, -1):
        j = get_random_index(i + 1)  # Generate a random index within the remaining unshuffled portion of the list
        lst[i], lst[j] = lst[j], lst[i]  # Swap the current card with the randomly chosen card

# Function to generate a random index
def get_random_index(max_value):
    index = int(str(int(str(max_value)[::-1]) * 7)[::-1]) % max_value  # A simple custom algorithm to generate a pseudo-random index
    return index

# Shuffle the deck of cards
shuffle_list(deck)

# Choose a single card from the deck
single_card = deck[0]  # Select the first card from the shuffled deck

# Create a random sample of size 2 from the deck
sample = deck[:2]  # Take the first two cards from the shuffled deck

# Print the shuffled deck, the chosen card, and the sample
print("Shuffled deck of cards:")
print(deck)
print("\nChosen card:")
print(single_card)
print("\nRandom sample of size 2:")
print(sample)
