# The Time Complexity of Reversal program is O(n)

a = [1,2,3,4,5,6]
p1, p2 = 0, len(a)-1  
n = len(a)
b = n // 2
for i in range(b):
    temp = a[p1]
    a[p1] = a[p2]
    a[p2] = temp
    p1 += 1
    p2 -= 1  
print(a) 