# -*- coding: utf-8 -*-
"""
Thomas Morris
Assignment 3
October 17, 2019
Implement a queue using linked lists. You should use your own class with the methods 
(enqueue(object), dequeue(), first(), len(), is_empty(), search()) and include a testing. 
Note that search(object) returns True (or False) to check if an object is in the Queue
Note:
Pages 264-266 in Data Structures and Algorithms were referenced
"""
class _Node:
        def __init__(self, element, enext):
            self._element = element
            self._next = enext
            
class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def len(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        #return but do not remove first element
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element
    
    def dequeue(self):
        #remove first element from queue
        if self.is_empty():
            raise Exception('Queue is empty')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element
    
    def enqueue(self, e):
        #add element to back of queue
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def search(self, key):
        #search the entire queue for the key element provided
        pos = self._head
        while pos:
            if pos._element == key:
                return True
            pos = pos._next
        return False

if __name__ == '__main__':
    l1 = LinkedQueue()
    l1.enqueue(5)
    l1.enqueue(73)
    l1.enqueue(9)
    l1.enqueue(8)
    l1.enqueue(16)
    l1.enqueue(57)
    l1.enqueue(95)
    print(l1.search(5))
    l1.dequeue()
    print(l1.search(5))
    print(l1.first())
    print(l1.len())
    print(l1.is_empty())
    print(l1.search(73))
    
    
            
        
    
    