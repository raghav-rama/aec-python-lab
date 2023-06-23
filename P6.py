'''Write a python program to accept a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.'''

def remove_duplicates_and_sort_words(input_string):
    # Split the input string into words
    words = input_string.split()

    # Remove duplicate words using a set
    unique_words = set(words)

    # Sort the unique words alphabetically
    sorted_words = sorted(unique_words)

    # Return the sorted words as a list
    return sorted_words

# Accept input sequence from the user
input_sequence = input("Enter a sequence of whitespace separated words: ")

# Call the function to remove duplicates and sort the words
result = remove_duplicates_and_sort_words(input_sequence)

# Print the result
print("Words after removing duplicates and sorting them:")
print(result)
