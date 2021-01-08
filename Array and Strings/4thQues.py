
#! Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
#! is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def OneEdit(s1,s2):
    if len(s1) == len(s2):
        return OneEditReplace(s1,s2)
    elif len(s1)+1 == len(s2):
        return oneEditInsert(s1,s2)
    elif len(s1) - 1 == len(s2):
        return oneEditInsert(s1,s2)
    
    return False

def OneEditReplace(s1,s2):
    editor = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if editor:
                return False
            editor = True
    
    return True

def oneEditInsert(s1,s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

if oneEditInsert("Vivek","Vivek"):
    print("True")
else:
    print("False")
    
if OneEditReplace("Male","Jale"):
    print("True")
else:
    print("False")
    
if OneEdit("vivek","vivek"):
    print("True")
else:
    print("False")
