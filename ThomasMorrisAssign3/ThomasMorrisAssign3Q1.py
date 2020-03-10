"""
Thomas Morris
Assignment 3
October 17th, 2019
Instructions:
Implement the circular double-ended queue (deque) 
which allows insertion and deletion from either front or rear end. 
Note:
This program was implemented with using information from pgs. 243-249 
in Data Structures and Algorithms by Goodrich, Tamassia, and Goldwasser
"""

class MyCircularDeque:
    #constructor to set the size of deque to be k
    DEFAULT_CAPACITY = 0
    
    def __init__(self, k):
        #Create an empty deque
        MyCircularDeque.DEFAULT_CAPACITY = k
        self._data = [None]*MyCircularDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        #Return the number of elements in the deque
        return self._size
    
    def isEmpty(self):
        #Return True if the deque is empty
        return self._size == 0
    
    def isFull(self):
        return self._size == MyCircularDeque.DEFAULT_CAPACITY
    
    def getFront(self):
        #Return but do not remove the first element at the front of the deque
        if self.isEmpty():
            return -1
        return self._data[self._front]
    
    def getRear(self):
        #Return the last element but do not remove it
        if self.isEmpty():
            return -1
        back = (self._front+self._size-1)%len(self._data)
        return self._data[back]
    
    def deleteFront(self):
        #Removes the first item in the deque, returns true if successful
        if self.isEmpty():
            return False
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return True
    
    def deleteLast(self):
        if self.isEmpty():
            return False
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return True
    
    def insertLast(self, e):
        #Adds an element to the back of the deque, returns True if successful
        if self.isFull():
            return False
        last = (self._front+self._size)%len(self._data)
        self._data[last] = e
        self._size += 1
        return True
    
    def insertFront(self, e):
        #Adds an element to the front of deque, returns True if successful
        if self.isFull():
            return False
        self._front = (self._front-1)%len(self._data)
        self._data[self._front] = e
        self._size += 1
        return True
    
if __name__ == "__main__":
     circularDeque = MyCircularDeque(3)
     print(circularDeque.insertLast(1))
     print(circularDeque.insertLast(2))
     print(circularDeque.insertFront(3))
     print(circularDeque.insertFront(4))
     print(circularDeque.getRear())
     print(circularDeque.isFull())
     print(circularDeque.deleteLast())
     print(circularDeque.insertFront(4))
     print(circularDeque.getFront())
     
     
    
    
        
    