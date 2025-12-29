# The Time Complexity of the Brute Force method is O(n^2)

def target(a,tar):
    pair=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]== tar:
                pair.append([a[i],a[j]])
    return pair 
a=[1,2,3,4]
tar=5
result=target(a,tar)
print("The Pairs of Brute force method is  :",result)    

# The Time Compexity of Optimized method is O(n)

def optimized(a,tar):
    b=set()
    pair=[]
    for i in a :
        seen=tar-i
        if seen in b :
            pair.append([i,seen])
        
        b.add(i)
    return pair
a=[1,2,3,4]
tar=5
result=optimized(a,tar)
print("The pairs of Optimized method is : ",result )