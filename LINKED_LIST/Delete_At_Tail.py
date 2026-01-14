# Linked list deletion at tail and displaying which has the time complexity of O(n) and Space complexity of O(1)
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

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return

        # takes place when it has only one node
        if self.head.next is None:
            self.head = None
            return

        # takes place when it has more than one node 
        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

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

print("Before deleting end:")
ll.display()

ll.delete_end()
print("After deleting end:")
ll.display()
