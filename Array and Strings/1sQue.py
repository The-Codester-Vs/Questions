
# ! Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# ! cannot use additional data structures?

def unique_character(string):
    char_set = [False]*128
    for char in string:
        val = ord(char)
        