# The Time Complexity of the product and sum is O(n)

a = [1,2,3,4,5,6]
sum, product = 0, 1
for i in a:
    sum += i
    product *= i

print("The sum is:", sum)    
print("The Product is:", product)  
