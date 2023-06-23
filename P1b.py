'''Program to read a string of 4 characters from the user. CP3a.pynvert every character in the string
to its next alphabet.'''

#without built in function

import string

def get_next_character(char):
    alphabet = string.ascii_letters

    if char in alphabet:
        current_index = alphabet.index(char)
        next_index = (current_index + 1) % len(alphabet)
        return alphabet[next_index]
    else:
        return char

user_input = input("Enter a string of 4 characters: ")

if len(user_input) != 4 or not user_input.isalpha():
    print("Invalid input. Please enter a string of exactly 4 alphabetic characters.")
else:
    converted_string = ""
    for char in user_input:
        converted_string += get_next_character(char)
    print("Converted string:", converted_string)
