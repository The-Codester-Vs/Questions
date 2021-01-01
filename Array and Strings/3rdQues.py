
# ! Write a method to replace all spaces in a string with '%20'. You may assume that the string
# ! has sufficient space at the end to hold the additional characters, and that you are given the "true"
# ! length of the string.

# def replacee(string,lenght):
#     chr_lst = list(string)
#     string = ""
#     index = len(chr_lst)
    
#     for i in reversed(range(lenght)):
#         if chr_lst[i] == " ":
#             chr_lst[index - 3:index ] = "%20"
#             index -= 3
#         else:
#             chr_lst[index-1] = chr_lst[i]
#             index -= 1
    
#     return string.join(chr_lst)

def traling(text,lenght):
    return text.rstrip().replace(" ", "%20")
    
ar = "hello world"
print(traling(ar,len(ar)))
            