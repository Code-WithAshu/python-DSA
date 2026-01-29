# Binary Search using Recursion has time complexity of O(logn) and space complexity of O(logn)
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    
    return binary_search(arr, target, mid + 1, high)

arr = [1, 3, 5, 6, 7, 9, 12]
print(binary_search(arr, 7, 0, len(arr) - 1))  
print(binary_search(arr, 5, 0, len(arr) - 1))  




