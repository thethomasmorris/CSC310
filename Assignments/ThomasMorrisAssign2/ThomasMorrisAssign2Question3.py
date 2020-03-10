"""
Thomas Morris
October 3, 2019
Implement a program that can input an expression in postfix notation 
and output its value. 
"""

class Stack:  
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise Exception('Stack is Empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is Empty')
        return self._data.pop()
    
    def evalPost(self, exp): 
        for i in range(0,len(exp)):
            #check if it is a digit
            if exp[i].isdigit(): 
                self.push(exp[i]) 
            else:
                #otherwise it is an operator so evaluate the expression
                x = int(self._data.pop())
                y = int(self._data.pop())
                if exp[i] == "+":
                    self.push(y+x)
                elif exp[i] == "-":
                    self.push(y-x)
                elif exp[i] == "*":
                    self.push(y*x)
                elif exp[i] == "/":
                    self.push(y/x) 
                else:
                    raise Exception('There is an error with op')
        return self.pop()
        
if __name__ == '__main__':
    post = Stack()
    print(post.evalPost("52+83-*4/"))
    print(post.evalPost("11+"))
    print(post.evalPost("11+25*-5+6"))
    print(post.evalPost("89/123*-63+"))
    print(post.evalPost("45/*99+291"))
    