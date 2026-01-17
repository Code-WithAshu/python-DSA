# Searching a element in linked list which has the time complexity of O(n) and space complexity of O(1)
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

    def search(self, key):
        temp = self.head
        position = 0

        while temp:
            if temp.data == key:
                print(f"Element {key} found at position {position}")
                return
            temp = temp.next
            position += 1

        print(f"Element {key} not found")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.insert_at_head(50)
ll.insert_at_head(40)
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)

ll.display()

ll.search(30)
ll.search(100)
