# The Time Complexity of Min Element is O(n)

a=[1,2,5,7,3,4]
min_ele=a[0]
for i in a :
    if i < min_ele:
        min_ele=i
print("The min element is:",min_ele)