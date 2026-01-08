# The Code has Time Complexity of O(n) and Space Complexity of O(1)
def second_smallest(a):
    if len(a)<2:
        return None 
    smallest=second_smallest=float("+inf")
    for i in a :
        if i < smallest:
            second_smallest=smallest
            smallest=i
        elif i<second_smallest and i!=smallest:
            second_smallest=i 
    return second_smallest if second_smallest != float('+inf') else None
a=[1,2,3,4,5,6,7,3,4]
b=second_smallest(a)
print("The Second Smallest Number is: ",b)