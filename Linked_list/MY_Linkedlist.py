class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self,new_data):
        new_node = node(new_data)
        if self.head == None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def Insert_After(self,prev_node,new_data):
        if prev_node is None:
            print("Your Prev node is empty..")
            return
        
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete(self,key):
        temp = self.head
        if temp != None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp != None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return temp
        
        prev.next = temp.next
        temp = None 
    
    def search(self,x):
        temp = self.head
        while temp!= None:
            if temp.data == x:
                return True
            temp = temp.next
        return False
        
    @property
    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        return count
    

n = 13
insert = linked()

insert.append(12)
insert.append(13)
insert.append(14)
insert.push(11)
insert.Insert_After(insert.head,11.5)

insert.delete(n) 
insert.display()
print("Total numbers of node is this list are:",insert.count) 
print("The last node you deleted is:",n) 
if insert.search(12):
    print(True)
else:
    print(False) 
