
#! String Compression: Implement a method to perform basic string compression using the counts
#! of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
#! "compressed" string would not become smaller than the original string, your method should return
#! the original string. You can assume the string has only uppercase and lowercase letters (a - z). 


def string_Compression(string):
    compressed= []
    count = 0 
    for i in range(len(string)):
        
        if i != 0 and string[i] != string[i-1]:
            compressed.append(string[i-1] + str(count))
            count = 0
        count += 1
        
    if count:
        compressed.append(string[-1] + str(count))
    
    return min(string,"".join(compressed),key=len)

print(string_Compression('aaabbbbcccddd'))
print(string_Compression("aaabbbbccccc"))
print(string_Compression("aaabbbccc"))
    