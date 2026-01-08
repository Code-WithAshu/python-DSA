# Brute force method for left rotation which has the time complexity of O(n^2) and space Complexity O(1)
def left_rotation(arr,d):
    for i in range(d):
        ele=arr.pop(0)
        arr.append(ele)
    return arr
arr=[1,2,3,4,5]
d=int(input("Enter no of rotations: "))
res=left_rotation(arr,d)
print("Brute Force Method: ",res)

#  Optimized method by using reversal algorithm which has the time complexity of O(n) and space complexity of O(1)
def optimized(l,r):  
    while(l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1  

a=[1,2,3,4,5,6,7,8,9]
b=[]
d=int(input("Enter no  of rotation:")) 
l=len(a)-1
d=d%(l+1)

optimized(0,d-1)
optimized(d,l)
optimized(0,l)
print("Optimized Method: ",a)
