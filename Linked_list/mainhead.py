class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,Data):
        newNode  = node(Data)
        newNode.next = self.head
        self.head = newNode
    
    def append(self,data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            return

        value = self.head
        while value.next:
            value = value.next
        value.next = newNode
    
    def search(self,key):
        temp = self.head
        while temp != None:
            if temp.data == key:
                return True
        return False
    
    
    
    @property
    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
        
        
    def afterinsert(self,prev_node,new_data):
        if prev_node is None:
            print("Your pervious node is EMPTY.")
            return
        
        newnode = node(new_data)
        newnode.next = prev_node.next
        prev_node.next = newnode
    # @staticmethod(afterinsert(self,prev_node,new_data))
    @property
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    @property
    def removeOdds(self):
        while (self.head is not None) and (self.head.data % 2 == 1):
            self.head = self.head.next
        current_node = self.head
        while (current_node is not None) and (current_node.next is not None):
            if current_node.next.data % 2 == 1:
                 current_node.next = current_node.next.next
            else:
                current_node = current_node.next

# if __name__ == '__main__':
#     test = LinkedList()
#     test.push(23)
#     test.append(24)
#     test.afterinsert(test.head,25)
#     print('Total numbers of nodes are:',test.count)
    
    
    
      