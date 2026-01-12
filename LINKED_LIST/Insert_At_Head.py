# Linked list insertion at head and displaying which has the time complexity of O(1) and Space complexity of O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(10)
ll.print_list()
