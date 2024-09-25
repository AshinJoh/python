class stack:
    def __init__(self) -> None:
        self.stk = []

    def is_empty(self):
        return len(self.stk) == 0

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stk.pop()
        else:
            return "Underflow"

    def peek(self):
        if not self.is_empty():
            return self.stk[-1]
        return "Underflow"

    def display(self):
        return self.stk
    

myStack = stack()

myStack.push(5)
myStack.push(10)
myStack.push(15)

print(myStack.display())
print(myStack.pop())
print(myStack.peek())