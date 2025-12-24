# The Time Complexity Of Inset At Position is O(n)

def insert(b,c):
    n = len(a)
    a.append(None)                
    for i in range(n - 1, c - 1, -1):  
        a[i + 1] = a[i]
    a[c] = b                        


a = [1, 2, 3, 4, 5, 6]
b = int(input("Enter a number: "))
c = int(input("Enter the position: "))
insert(b, c-1)
print(a)

