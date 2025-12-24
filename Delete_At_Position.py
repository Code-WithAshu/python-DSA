# The Time Complexity of Delete At Position is O(n)

def delete(pos):  
    n = len(a)    
    for i in range(pos-1, n-1):  
        a[i] = a[i+1]
    a.pop()       


a = [1,2,3,4,5,6]
pos = int(input("enter the position: "))
delete(pos)
print(a)

