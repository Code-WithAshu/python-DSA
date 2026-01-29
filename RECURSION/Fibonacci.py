# The code has time complexity of O(n^2) and space complexity of O(n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))   

# Manual Memoized Recursive (Optimized) has time complexity of O(n) and space complexity of O(n)
def fibonacci(n, memo={}):
    if n in memo:           
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(6))  
