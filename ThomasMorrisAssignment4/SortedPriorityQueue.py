from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        #empty priority queue
        self._data = PositionalList()
        
    def __len__(self):
        #number of items in priority queue
        return len(self._data)
    
    def add(self, key, value):
        #add key-value pair
        #._Item defined by base class
        newest = self._Item(key, value)
        walk = self._data.last()
        #look for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)
    
    def min(self):
        #returns but does not remove the tuple with min key
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        #removes and returns the tuple with minimum key
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key)
    
    def __iter__(self):
        #iteration of the map's keys
        for item in self._data:
            yield item