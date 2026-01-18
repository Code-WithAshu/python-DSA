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

    # Creating a cycle for testig
    def create_cycle(self):
        if self.head is None or self.head.next is None:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head.next   # Cycle has created 

    # Brute Force Cycle Detection has Space Complexity of O(n)
    def cycle_finder(self):
        visited = set()
        current = self.head

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

    # Optimized Cycle Detection has Space Complexity of O(1)
    def optimized(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.insert_at_head(40)

ll.create_cycle()  

print("Brute Force : Cycle Exists ?", ll.cycle_finder())
print("Optimized   : Cycle Exists ?", ll.optimized())
