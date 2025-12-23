# The Time Complexity Of Delet At Beginning is O(n)

a=[1,2,3,4,5]
n=len(a)
for i in range(n-1):
    a[i]=a[i+1]
a.pop()
print(a)