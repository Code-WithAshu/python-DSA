# Linked list deletion at head and displaying which has the time complexity of O(1) and Space complexity of O(1)
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

    def delete_first(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        self.head = self.head.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)

print("Before deleting first:")
ll.display()

ll.delete_first()
print("After deleting first:")
ll.display()


        
    

            