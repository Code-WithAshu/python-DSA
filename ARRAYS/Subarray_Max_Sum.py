def subarray(a):
    l=len(a)
    b=[]
    for i in range(l):
        s=0
        for j in range(i,l):
            s+=a[j]
            b.append(s)
    return max(b)


# optimized method (Kadane's Algorithm)
def optimized(a):
    if not a:
        return 0
    max_sum = current_sum = a[0]
    for i in range(1, len(a)):
        current_sum = max(a[i], current_sum + a[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(subarray(arr))     
print(optimized(arr))    
