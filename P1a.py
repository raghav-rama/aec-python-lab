'''Program to read a string of 4 characters from the user. Convert every character in the string
to its next alphabet.'''

#Built in function

user_input = input("Enter a string of 4 characters: ")

if len(user_input) != 4 or not user_input.isalpha():
    print("Invalid input. Please enter a string of exactly 4 alphabetic characters.")
else:
    converted_string = ""
    for char in user_input:
        if char == 'z':
            converted_string += 'a'
        elif char == 'Z':
            converted_string += 'A'
        else:
            converted_string += chr(ord(char) + 1)
    print("Converted string:", converted_string)
