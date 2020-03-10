"""
Thomas Morris
Insertion-sort program using a priority queue implemented with a sorted list.
November 8th, 2019
"""

from SortedPriorityQueue import SortedPriorityQueue

def insertion_sort(C, S):
    #add number from collection to sorted priority queue
    j = 0
    for i in C:
        S.add(i, j)
        j += 1
    
    L = []
    while not S.is_empty():
        L.append(S.remove_min())
        
    return L

if __name__ == '__main__':
    #create a sorted priority queue
    S = SortedPriorityQueue()
    #create a collection of numbers
    C = [7,4,8,2,5,3]
    
    print(C)
    C = insertion_sort(C,S)
    print(C)
    
  
    


    

