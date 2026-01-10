# Brute Force apporach which has time complexity of O(n^2) and Space complexity of O(1)
def first_non_repeat(s):
    n=len(s)
    for i in range(n):
        ch=s[i]
        count=0

        for j in range(n):
            if ch == s[j]:
                count+=1
        if count==1:
            return ch 
    return None
s=input("Enter the Word: ")
s=first_non_repeat(s)
print("Brute Force Method :",s)

# Optimized method using frequency dictionary method which has the time complexity of O(n) and space complexity of (k)
def optimized(s):
    count={}
    for i in s :
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    for j in s:
        if count[j]==1:
            return j
    
s=input("Enter the word: ")
s=optimized(s)
print("Optimized Method: ",s)
               
            
