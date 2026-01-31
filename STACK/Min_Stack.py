# Finding min in stack has time complexity of O(1) and space complexity of O(n)
class minstack:
    def __init__(self):
        self.items = [] 

    def push(self, number):
        if self.items == []:
            self.items.append([number, number])
        else:
            new_min = min(number, self.items[-1][1])
            self.items.append([number, new_min])

    def pop(self):
        self.items.pop() 

    def top(self):
        return self.items[-1][0]  # returns just the number 

    def getMin(self):
        return self.items[-1][1]  # returns the minimum 

s = minstack()
s.push(5)   # [[5,5]]
s.push(2)   # [[5,5],[2,2]] 
s.push(8)   # [[5,5],[2,2],[8,2]]

print(s.top())    # 8
print(s.getMin()) # 2
s.pop()           # [[5,5],[2,2]]
print(s.getMin()) # 2 


