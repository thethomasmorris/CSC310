"""
Thomas Morris
October 3, 2019
Write/Test a stack (called Min Stack) that supports 
push, pop, top, and retrieving the minimum element in constant time.
"""
class MinStack:
    def __init__(self):
        self._data = []
        self._minStack = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        """
        use the second stack to hold the minimum value
        only push a value if it is less than or equal to the top of the min
        """
        if self.is_empty():
            self._minStack.append(e)
        elif self._minStack[-1] >= e:
                self._minStack.append(e)
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]

    def pop(self):
        """
        Check if the element being removed from the main stack
        is the same as the element in the min stack and remove it
        when they are equal
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        if self._data[-1] == self._minStack[-1]:
            self._minStack.pop()
        return self._data.pop()

    def getMin(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._minStack[-1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    print(minStack.getMin())
    minStack.push(0)
    print(minStack.getMin())
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
    minStack.push(-5)
    minStack.push(-5)
    minStack.push(2)
    minStack.push(7)
    print(minStack.getMin())
    minStack.pop()
    minStack.pop()
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    minStack.pop()
    print(minStack.getMin())
    
    

