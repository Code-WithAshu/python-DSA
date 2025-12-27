# The Time Complexity of the Linear Search is O(n)

def Linear_Search(a, target):
    for ind, val in enumerate(a):
        if target == val:
            return ind
    return -1

a=[1,5,6,3,7,10,22,52,61]
target = int(input("Enter the Target number: "))
ind = Linear_Search(a, target)

if ind == -1:
    print("Not found....")
else:
    print("Found the target at index", ind)
    