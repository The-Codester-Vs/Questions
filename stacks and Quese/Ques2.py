# Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time. 
from collections import deque
 
 
class MinStack:
    def __init__(self):
 

        self.s = deque()
 
        
        self.min = None
 
    def push(self, x):
 
        if not self.s:
            self.s.append(x)
            self.min = x
 
        elif x > self.min:
            self.s.append(x)
 
        else:
            self.s.append(2*x - self.min)
            self.min = x
 
    # Removes the top element from the stack and returns it
    def pop(self):
 
        if not self.s:
            self.print("Stack underflow!!")
 
        top = self.s[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.s.pop()
 
    # Returns the minimum element from the stack in constant time
    def minimum(self):
 
        return self.min
 

if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(3)
    print(s.minimum())
 
    s.push(10)
    print(s.minimum())
 
    s.push(5)
    print(s.minimum())
 
    s.push(3)
    print(s.minimum())
 
    # s.pop()
    # print(s.minimum())
 
    # s.pop()
    # print(s.minimum())