# Removing Loop in linked list has time complexity of O(n) and space complexity of O(1)
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

    def create_loop(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head.next   

    def remove_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            print("No loop found")
            return

        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = None
        print("Loop removed")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert_at_head(50)
ll.insert_at_head(40)
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)

ll.create_loop()      
ll.remove_loop()      
ll.display()          
