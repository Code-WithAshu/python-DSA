# The Brute Force method of removing duplicates is O(n^2)

def duplicate_removal(a):
    b=[]
    for i in a :
        if i not in b:
            b.append(i)
    print("The list after duplicate removal: ",b)
a=[1,2,3,4,2,1,2]
duplicate_removal(a)


# The Optimized method of removing duplicates has O(n)

def optimized(a):
    b=set()
    c=[]
    for i in a :
        if i not in b :
            b.add(i)
            c.append(i)
    print("opimized method: ",c)
a=[1,2,4,5,6,7,2,1,2,7]
optimized(a)
