'''Write a Program to print the following pattern.
A
B C D
E F G H I
J K L M N O P
Q R S T U V W X Y'''

def print_pattern():
    char_count = 65  # ASCII code for 'A'

    for i in range(5):  # Number of rows in the pattern
        for j in range(i*2+1):
            print(chr(char_count), end=" ")  # Convert ASCII code to character
            char_count += 1
        print()
print_pattern()


