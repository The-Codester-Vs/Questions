
# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
# class linked:
#     def __init__(self):
#         self.head = None
    
#     def push(self,new_data):
#         new_node = node(new_data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def append(self,New_data):
#         new_node = node(New_data)
#         if self.head == None:
#             self.head = new_node
#             return
        
#         value = self.head
#         while value.next:
#             value = value.next
#         value.next = new_node
#         return new_node
    
    
    
#     def delete(self,x):
#         temp = self.head
#         if temp is None:
#             return temp
        
#         if temp is not None:
#             if temp.data == x:
#                 self.head = temp.next
#                 temp = None
#                 return
        
#         while temp is not None:
#             if temp.data == x:
#                 break 
#             prev = temp
#             temp = temp.next
        
#         prev.next = temp.next
#         temp = None
    
#     def insertAfter(self,prevNode,NewData):
#         if prevNode is None:
#             print("Your previous node is empty")
#             return

#         newNode = node(NewData)
#         newNode.next = prevNode.next
#         prevNode.next = newNode
        
#     @property
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp =  temp.next  
    
#     @property  
#     def removeOdds(self):
#         while (self.head is not None) and (self.head.data % 2 ==1) :
#             self.head = self.head.next
#         current_node = self.head
#         while (current_node is not None) and (current_node.next is not None):
#             if current_node.next.data % 2 == 1:
#                  current_node.next = current_node.next.next
#             else:
#                 current_node = current_node.next
        
        

# if __name__ == '__main__':
#     llist = linked()
#     # llist.push(12)
#     llist.append(12)
#     llist.append(14)
#     llist.append(15)
#     llist.append(20)
#     llist.removeOdds
#     llist.display
     
        