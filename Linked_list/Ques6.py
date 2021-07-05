# Implement a function to check if a linked list is a palindrome. 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def ispal(self,string):
        return (string == string[::-1])
    
    def isPalindrome(self):
        current = self.head
        temp = []
        
        while current is not None:
            temp.append(current.data)
            current = current.next
        string = "".join(temp)
        return self.ispal(string)
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
            
llist = LinkedList() 
llist.head = Node('a') 
llist.head.next = Node('bc') 
llist.head.next.next = Node("d") 
llist.head.next.next.next = Node("dcb") 
llist.head.next.next.next.next = Node("a") 
print("It is Palindrome" if llist.isPalindrome() else "Not a Palindrome")