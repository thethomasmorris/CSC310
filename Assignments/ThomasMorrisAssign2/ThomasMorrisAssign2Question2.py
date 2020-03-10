"""
Thomas Morris
October 3, 2019
Write/Test a program which evaluate arithmetic expression using your 
own stack class. Please follow the lecture slides Stack, pp. 15-17.
"""

class Stack:  
    def __init__(self):
        self._data = []

    def size(self):
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
    
class Eval:
    valStk = Stack()
    opStk = Stack()
    def doOp():
        x = int(Eval.valStk.pop())
        y = int(Eval.valStk.pop())
        op = Eval.opStk.pop()
        if op == "+":
            Eval.valStk.push(y+x)
        elif op == "-":
            Eval.valStk.push(y-x)
        elif op == "*":
            Eval.valStk.push(y*x)
        elif op == "/":
            Eval.valStk.push(y/x)
        elif op == "<":
            Eval.valStk.push(y<x)
        elif op == ">":
            Eval.valStk.push(y>x)
        elif op == "≤":
            Eval.valStk.push(y<=x)
        elif op == "≥":
            Eval.valStk.push(y>=x)
        else:
            raise Exception('There is an error with op')
    
    def prec(item):
        if item == "$":
            return 0
        elif item == "<" or item == ">" or item == "≤" or item == "≥":
            return 1
        elif item == "+" or item == "-":
            return 2
        elif item == "*" or item == "/":
            return 3
        else:
            raise Exception('There is an error with prec')
    
    def repeatOps(refOp):
        while (Eval.valStk.size() > 1) and (Eval.prec(refOp) <= Eval.prec(Eval.opStk.top())):
            Eval.doOp()
            
    def evalExp(self, exp):
        for i in range(0,len(exp)):
            #check if it is digit
            if exp[i].isdigit():
                Eval.valStk.push(exp[i])
            else:
                #otherwise its an operator
                Eval.repeatOps(exp[i])
                Eval.opStk.push(exp[i])
        #send the end operator
        Eval.repeatOps("$")
        #return the value left at the top of the stack
        return Eval.valStk.top()
    
    def reset(self):
        Eval.valStk = Stack()
        Eval.opStk = Stack()
            
    
    
if __name__ == '__main__':
    print(Eval().evalExp("4+5-9>4"))
    Eval().reset()
    print(Eval().evalExp("6/6+8-4*3+6*4"))
    Eval().reset()
    print(Eval().evalExp("7/6+8-7*3+7*4"))
    Eval().reset()
    print(Eval().evalExp("7/6+8-7<3+7*4"))
        