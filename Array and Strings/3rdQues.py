
#  Write a method to replace all spaces in a string with '%20'. You may assume that the string
#  has sufficient space at the end to hold the additional characters, and that you are given the "true"
#  length of the string.

def replaceing1(string,length):
    chr_lst = list(string)
    string = ""
    index = len(chr_lst)
    
    for i in reversed(range(length)):
        if chr_lst[i] == "  ":
            chr_lst[index - 2:index ] = "%20"
            index -= 1
        else:
            chr_lst[index-1] = chr_lst[i]
            index -= 1
    
    return string.join(chr_lst)

def replacing2(text,length):
    return text.rstrip().replace(" ", "%20")
    
ar = "hello world How are you"
leth = len(ar)
print(replaceing1(ar,leth))
print(replacing2(ar,len(ar)))
