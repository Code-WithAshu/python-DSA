# Stack Implementation using LinkedList has time complexity of O(1) and space complexity of O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        if self.is_empty():
            print("Stack Underflow")
            return
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  
print("Popped element:", stack.pop())  
print("Peek element:", stack.peek())   
stack.display()  
