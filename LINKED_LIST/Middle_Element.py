# Finding the Middle element of the LinkedList which has the time complexity of O(n) and space complexity of O(1)
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

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

ll = LinkedList()
ll.insert_at_head(50)
ll.insert_at_head(40)
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)

print("Middle element:", ll.find_middle())
