# Brute Force which has the Time Complexity of O(n^2) and Space Complexity of O(1)

def majority_element(a):
    c=0
    for i in range(len(a)) :
        for j in range(len(a)):
            if a[i]==a[j]:
                c+=1
    if (c> len(a)//2):
        return a[i]
a=[1,2,1,3,1]
result=majority_element(a)   
print("The Majority Element is: ",result)    


# optimized method (Boyer-Moore Voting Algorithm) which has the Time Complexity of O(n) and Space Complexity of O(1)
def optimized(a):
    c = 0
    candidate = None
    for i in a:
        if c == 0:
            candidate = i
            c += 1
        elif candidate == i:
            c += 1
        else:
            c -= 1

    c = 0
    for i in a:
        if i == candidate:
            c += 1
    return candidate, c

a = [1, 2, 3, 1, 1, 1]
candidate, c = optimized(a)   

if c > len(a) // 2:           
    print(f"The Majority element is {candidate}")
else:
    print("There is no majority element")
