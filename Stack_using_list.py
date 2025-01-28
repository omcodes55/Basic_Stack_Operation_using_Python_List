class stack:
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack = [x] + self.stack
        print(f"Pushed Element = {x}")
        print("Stack:", self.stack, "\n")
    
    def pop(self):
        if self.isempty():
            print("Stack is Empty, can't pop")
        else:
            print(f"Popped Element = {self.stack[0]}")
            self.stack.pop(0)
            print("Remaining Stack:", self.stack, "\n")
        
    def peek(self):
        if self.isempty():
            print("Stack is Empty, can't peek")
        else:
            print(f"Top of the stack = {self.stack[0]}")
            print("Stack:", self.stack, "\n")
        
    def isempty(self):
        return len(self.stack) == 0
        
# Example usage
s1 = stack()
s1.push(10)
s1.push(5)
s1.push(20)
s1.pop()
s1.peek()