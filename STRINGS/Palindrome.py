# The  Time Complexity of the Brute Force method is O(n^2)

def palindrome(a):
    b=""
    for i in range (len(a)-1,-1,-1):
        b+=a[i]
    return b
a=input("Enter the String: ")
result=palindrome(a)
if a == result :
    print("It is a palindrome")
else: 
    print("It is not a palindrome")


# The Optimized Palindrome has Time Complexity of O(n)

def optimized(a):
    a=list(a)
    n=len(a)-1
    p1,p2=0,n
    for i in range(n//2):
        temp=a[p1]
        a[p1]=a[p2]
        a[p2]=temp
        p1+=1
        p2-=1
    
    return "".join(a)
a=input("Enter the String: ")
result=optimized(a)
if (result == a):
    print("It is a palindrome")
else: 
    print("It is not a palindrome")



















