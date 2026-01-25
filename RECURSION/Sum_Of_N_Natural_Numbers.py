# Sum of n numbers by using recursion which has the time complexity of O(n) and space complexity of O(n)
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = int(input("Enter number: "))
total = sum_n(n)
print("Sum of N natural numbers:", total)
