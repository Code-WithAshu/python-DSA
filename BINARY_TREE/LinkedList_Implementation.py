from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # insertion operation which has time and space complexity of O(n)
    def insertion(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left == None:
                current.left = new_node
                return
            queue.append(current.left)
            if current.right == None:
                current.right = new_node
                return
            queue.append(current.right)

    # Deletion operation has time and space complexity of O(n)
    def deletion(self, data):
        if self.root == None:
            return
        
        queue = deque([self.root])
        delete_node = None
        last_node = None
        parent_of_last = None
        
        while queue:
            current = queue.popleft()
            if current.data == data:
                delete_node = current
            
            if current.left:
                parent_of_last = current
                last_node = current.left
                queue.append(current.left)
            if current.right:
                parent_of_last = current
                last_node = current.right
                queue.append(current.right)
        
        if delete_node == None:
            return
        
        delete_node.data = last_node.data
        if parent_of_last.left == last_node:
            parent_of_last.left = None
        else:
            parent_of_last.right = None

    # Traversal operation has the time and space complexity of O(n)
    def traverse(self):
        if self.root == None:
            return
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            print(current.data, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


# Menu Interface
bt = BinaryTree()
while True:
    print("\nMenu\n1.Insert\n2.Delete\n3.print\n5.Exit")
    choice = input()
    match choice:
        case '1':
            bt.insertion(int(input("Enter data: ")))
        case '2':
            bt.deletion(int(input("Enter data to delete: ")))
        case '3':
            print("Tree:", end=" ")
            bt.traverse()
        case '5':
            break

