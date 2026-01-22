# Queue Implementation of Array for  all operations has time complexity of O(1) and space complexity of O(n)
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return
        
        self.rear += 1
        self.queue[self.rear] = value
        self.count += 1
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        
        value = self.queue[self.front]
        self.front += 1
        self.count -= 1
        print(f"Dequeued: {value}")
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front element:", q.peek())

q.dequeue()
q.dequeue()

q.enqueue(40)
q.enqueue(50)
