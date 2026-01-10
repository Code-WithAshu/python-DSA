# The Code has Time Complexity of O(n) and Space Complexiyt of O(1)
def range_sum_query(a,l,r):
    total=0
    for i in range(l,r+1):
        total+=a[i]
    return total
a=[1,2,3,4,5,6]
result=range_sum_query(a,1,2)
print("Brute Force Method: ",result)


# Optimization is done by using prefix sum algorithm which results in the operational time of O(1) and one time processing time of O(n)
def optimized(arr,l,r):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    
    return prefix[r+1]-prefix[l]

arr = [1,2,3,4,5,6]
result=optimized(arr,1,2)
print("Optimized Method: ",result)




        
