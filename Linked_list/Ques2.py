# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,newData):
        newNode = node(newData)
        newNode.next = self.head
        self.head = newNode  
     
    # def append(self,newData):
    #     NewNode = node(newData)
    #     if self.head == None:
    #         self.head = NewNode 
    #         return
        
    #     value = self.head
    #     while value.next:
    #         value = value.next
    #     value.next = NewNode
    
    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def printNthFromLast(self, n):
        temp = self.head 
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
         
        if n > length: 
            print('Location is greater than the' +
                         ' length of LinkedList')
            return 
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print("The nth term of linked list is:",temp.data)
    
    @property
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    
ll = LinkedList()
ll.push(12)
ll.push(13)
ll.push(14)
ll.push(15)
ll.push(16)
ll.printNthFromLast(5)
print(f"The total number of node in this list:{ll.count()}")

         
        