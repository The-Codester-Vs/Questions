 
# ! Given an image represented by an NxN matrix, where each pixel in the image is 4
# ! bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first,last  = layer , n - layer - 1
        for i in range(first,last):
            # saving top
            top = matrix[layer][i]
            # left --> top
            matrix[layer][i] = matrix[-i - 1][layer]
            print("left to top",matrix)
            # bottom --> left
            matrix[ - i -1][ layer ] = matrix[-layer -1 ][-i- 1]
            print("bottom to left",matrix)
            # right ---> Bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer -1]
            print("right to bottom", matrix)
            # top ---> right 
            matrix[i][-layer- 1] = top
            print("Top to right",matrix)
            
    return matrix
        
matrix = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
    ]
print("",rotate_matrix(matrix))

