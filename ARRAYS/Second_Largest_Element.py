# The Code has Time Complexity of O(n) and Space Complexity of O(1)
def second_largest(a):
    if len(a)<2:
        return None 
    largest=second_largest=float('-inf')
    for i in a :
        if i > largest : 
            second_largest=largest
            largest=i 
        elif i > second_largest and i != largest:
            second_largest=i
    return second_largest if second_largest!= float('-inf') else None

a=[1,2,4,5,6,7,3]
b=second_largest(a)
print("The Second Largest Number is: ",b)