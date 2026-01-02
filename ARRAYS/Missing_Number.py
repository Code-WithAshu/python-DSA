# Finding the Missing number has Time Complexity O(n) and Space Complexity O(1)

def find_missing(arr):
    n = len(arr) + 1
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual

arr = [1, 2, 3, 4, 5, 7]
print(find_missing(arr)) 

