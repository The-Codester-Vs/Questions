
# ! Given two strings, write a method to decide if one is a permutation of the
# ! other. 
def permutation(str1,str2):
    if len(str1) != len(str2):
        return False
    str1, str2 = sorted(str1), sorted(str2)
    for i in range(len(str1) - 1):
        if str1[i] != str2[i]:
            return False
    return True


string1 = input("Enter the fist string: ")
string2 = input("Enter the second string: ") 

if permutation(string1,string2):
    print("They are similar.")
else:
    print("They are not similar.")

