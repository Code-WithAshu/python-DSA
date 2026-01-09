# Element by element search method which has time complexity of O(n^2)
def sum_pair(a, target):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == target:
                return a[i], a[j]  
    return None  

# Using Single loop with effective search (Hash-set) which as time complexity of O(n)
def optimized(a, tar):
    visited = set()
    pair = []
    for i in a:
        seen = tar - i
        if seen in visited:
            pair.append([i, seen])
        visited.add(i)
    return pair

a = [1, 2, 3, 4, 5, 6]
target = 7

print("Brute force:", sum_pair(a, target))
print("Optimized:", optimized(a, target))