# Stack Last-in-first-out Data Structure Day-1


class Stack:
    stack_elements = []

    def push(self, element):
        self.stack_elements.append(element)
    
    def pop(self):
        if len(self.stack_elements) >= 1:
            return self.stack_elements.pop()
        else:
            raise Exception('Stack is empty')

    def top(self):
        if len(self.stack_elements) >= 1:
            return self.stack_elements[-1]
        else:
            raise Exception('Stack is empty')
        
    def size(self):
        return len(self.stack_elements)
    

# Queue First-in-first-out Data Structure


class Queue:
    def __init__(self) -> None:
        self.arr = []
    
    def isEmpty(self):
        return len(self.arr) == 0
           
    def enQueue(self, item):
        self.arr.append(item)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue from an empty queue")
        element = self.arr.pop(0)
        return element
    
    def front(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        element = self.arr[0]
        return element
    
    def size(self):
        return len(self.arr)
    
    
#  Circular Queue


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.k = k
        self.arr = [None] * k
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.arr[self.rear] = value
            self.size+=1
            self.rear = (self.rear + 1) % self.k
            return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.size -= 1
            self.front = (self.front + 1) % self.k
            return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear - 1]
        
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
    
    