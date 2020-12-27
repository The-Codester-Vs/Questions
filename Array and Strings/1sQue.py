
# ! Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# ! cannot use additional data structures?

def unique_character(string):
    if len(string) > 128:
        return False
    
    character = [False] * 128
    for char in string:
        val = ord(char)
        if character[val]:
            return False
        character[val] = True

    return True

# unique_character("vivek")
string = input("Enter the string: ")

if unique_character(string):
    print("This string have a unique character!")
else:
    print("This string does not have a unique character!")
