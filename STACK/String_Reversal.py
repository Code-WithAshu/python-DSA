# Brute force method has time complexity of O(n) and space complexity of O(n)
def is_palindrome(s):
    stack = []

    for ch in s:
        stack.append(ch)

    for ch in s:
        if ch != stack.pop():
            return False
    return True

string = "madam"
print("Palindrome" if is_palindrome(string) else "Not Palindrome")


# optimized method using pointer has time complexity of O(n) and space complexity of O(1)
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

string = "madam"
print("Palindrome" if is_palindrome(string) else "Not Palindrome")

