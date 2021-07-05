# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node butthe first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node. 

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        
    def append(self,new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        value = self.head 
        while value.next:
            value = value.next
        value.next = new_node
    
    def delete(self,key):
        temp = self.head
        if temp != None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp!= None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return temp

        prev.next = temp.next
        temp = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

ll = linkedList() 
ll.append(12)
ll.append(5)
ll.append(13)
ll.delete(5)
ll.display()

        