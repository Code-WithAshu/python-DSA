# The code has time complexity of O(n) and space complexity of O(1)
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

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return True

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first = self.head
        second = prev

        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next

        return True


ll = LinkedList()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(1)

print("Is Palindrome:", ll.is_palindrome())
