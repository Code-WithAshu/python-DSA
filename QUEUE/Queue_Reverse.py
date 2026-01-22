from collections import deque

# Brute Force Method Using stack has time complexity of O(n) and space complexity of O(n)
def reverse_queue_bruteforce(queue):
    stack = []
    while queue:
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    return queue

# Optimized Method In-place using deque has time complexity of O(n) and space complexity of O(1)
def reverse_queue_optimized(queue):
    queue.reverse()
    return queue

if __name__ == "__main__":
    q1 = deque([10,20,30,40])
    print("Original Queue:", q1)
    print("Brute Force Reversed Queue:", reverse_queue_bruteforce(q1))

    q2 = deque([50,60,70,80])
    print("Original Queue:", q2)
    print("Optimized Reversed Queue:", reverse_queue_optimized(q2))
