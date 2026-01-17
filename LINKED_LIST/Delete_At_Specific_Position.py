# Linked list deletion at position and displaying which has the time complexity of O(n) and Space complexity of O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp.next and count < pos - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.insert_at_head(40)
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)

print("Before deletion:")
ll.display()

ll.delete_at_position(2)
print("After deletion:")
ll.display()
