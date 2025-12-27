# Binary Search Algorithm which has O(log n)

def Binary_Search(arr,target):
    low=0
    high=len(arr)-1
    for i in arr:
        mid=high+low//2
        if(a[mid]==target):
            return mid
        elif(a[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return -1
a=[1,2,5,7,12,20]
target=int(input("Enter the target element: "))
index=Binary_Search(a,target)
if index == -1:
    print("The target is not found")
else:
    print(f"The target is found at [{index+1}] position...")