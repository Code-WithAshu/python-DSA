# Stack Implementation of array for all operations has time complexity of O(1) and space complexity of O(n)
class stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        print(f"{data} pushed into the stack ")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack)==0    
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")

        else:
            print("Stack elements:",self.stack)
    
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped element:",s.pop())
print("Peek element:",s.peek())