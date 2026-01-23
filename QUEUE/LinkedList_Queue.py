# Linked List Implementation of Queue which has time complexity of O(1) and space complexity of O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        removed_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed_data

    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        return self.front.data


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("deleted element:",q.dequeue())
    print("Peek element:",q.peek())
    print("deleted element:",q.dequeue())
    print("deleted element:",q.dequeue())