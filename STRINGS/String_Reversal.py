# Reversal using concatenation has Time Complexity of O(n^2)
def reversal(a):
    global b
    b=" "
    for i in range (len(a)-1,-1,-1):
        b+=a[i]


# Optimzed Reversal has Time Complexity of O(n)
def optimized(a):
    a=list(a)
    p1,p2=0,len(a)-1
    n=len(a)
    b=n//2
    for i in range (b):
        temp=a[p1]
        a[p1]=a[p2]
        a[p2]=temp
        p1+=1
        p2-=1

    return "".join(a)

a=input("Enter the string:")
reversal(a)
result=optimized(a)
print("The reversal is ",b)
print("The String reversal using optimized is ",result)




















 