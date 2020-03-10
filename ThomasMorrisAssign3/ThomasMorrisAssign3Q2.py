"""
Thomas Morris
Assignment 3
October 17th, 2019
Instructions:
Implement the program which merges two sorted singly-linked lists 
and return it as a new list. The new list should be made by splicing 
together the nodes of the first two lists. 
You should use your own class and include a testing.
Note:
Pages 256-266 of Data Structures and Alogrithms were referenced 
"""

class Node:
    def __init__(self, element):
        self._element = element
        self._enext = None
            
class LinkedList:
    
    #initialize the head
    def __init__(self):
        self._head = None
        self._size = 0
        
    #add an element to the front of the list
    def add_first(self, e):
        newest = Node(e)
        newest._enext = self._head
        self._head = newest
        self._size += 1
        
    #print out the list    
    def printList(self):
        node = self._head
        while node:
            print(node._element, "-> ", end='')
            node = node._enext
        print("∅")
    
    #merge the two lists provided together using recursion
    def merge(self, l1, l2):
        #make a empty node
        l3 = None
        
        #stop recursing when either l1 or l2 head is null 
        #and then return the rest of the other list head
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        #compare the elements at each head to place them at the right spot
        #then make the recursive call to merge the list with the next element
        if l1._element <= l2._element:
            l3 = l1
            l3._enext = LinkedList().merge(l1._enext, l2)
        else:
            l3 = l2
            l3._enext = LinkedList().merge(l1, l2._enext)
            
        #return the new list that was created by the recursive calls
        return l3

if __name__ == '__main__':
    l1 = LinkedList()
    l1.add_first(4)
    l1.add_first(2)
    l1.add_first(1)
    l1.printList()
    l2 = LinkedList()
    l2.add_first(4)
    l2.add_first(3)
    l2.add_first(1)
    l2.printList()
    l3 = LinkedList()
    l3._head = l3.merge(l1._head,l2._head)
    l3.printList()
        
    
    
    
