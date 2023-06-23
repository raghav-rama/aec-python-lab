'''Given a list of strings, count and print the number of strings where the string length is 2 or
more & the 1st & last characters are same.'''

string_list = ["hello", "world", "level", "programming", "racecar", "openai", "madam"]

count = 0  # Initialize count variable

print("Strings meeting the criteria:")
for string in string_list:
    if len(string) >= 2 and string[0] == string[-1]:
        print(string)
        count += 1

print("Number of strings meeting the criteria:", count)
