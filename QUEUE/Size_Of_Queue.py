# The code has time complexity of O(1) and space complexity of O(n)
class Queue:
    def __init__(self, size):
        self.capacity = size
        self.q = [None] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def enqueue(self, data):
        if self.count == self.capacity:
            print("Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = data
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Underflow")
            return

        value = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    def size(self):
        return self.count


if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q.size())
    q.dequeue()
    print(q.size())

