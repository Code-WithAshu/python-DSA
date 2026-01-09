# Brute force method for right rotation which has the time complexity of O(n x d) --> O(n^2) and space Complexity O(1)
def right_rotation(arr,d):
    for i in range(d):
        ele=arr.pop()
        arr.insert(0,ele)
    return arr
arr=[1,2,3,4,5]
d=int(input("enter the no of rotations:"))
res=right_rotation(arr,d)
print("Brute Force: ",res)

# Optimized method by using reversal algorithm which has the time complexity of O(n) and space complexity of O(1)
def optimized(l,r):  
    while(l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1  

a=[1,2,3,4,5,6]
b=[]
d=int(input("enter the no of rotations:")) 
l=len(a)-1
d=d%(l+1)

optimized(0,l)
optimized(0,d-1)
optimized(d,l)
print("Optimized Method: ",a)





































    
