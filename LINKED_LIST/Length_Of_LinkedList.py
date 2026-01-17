# Finding Lenght of the LinkedList which has the time complexity of O(n) and Space complexity of O(1)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def length(self):
        temp=self.head
        count=0

        while temp is not None:
            count+=1
            temp=temp.next 
        return count 
    
ll = LinkedList()
ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(40)
print("The Length of the linked list: ",ll.length())



        