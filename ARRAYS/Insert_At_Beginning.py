# The Time Complexity of Insert At Beginning is O(n)

def insert(b):
    n=len(a)
    a.append(None)
    for i in range(n-1,-1,-1):
        a[i+1]=a[i]
    a[0]=b
a=[1,2,3]
b=int(input("enter a number to be inserted: "))
insert(b)
print(a)