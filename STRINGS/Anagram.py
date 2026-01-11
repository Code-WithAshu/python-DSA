# The Brute Force method has Time Complexity of O(nlogn) and Space Complexity of O(n)
def Anagram(s,t)->bool:
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)
s=input("Enter first string: ")
t=input("Enter the second string: ")
res=Anagram(s,t)
print(res)

# Optimized code has Time Complexity of O(n) and Space Complexity of O(1)
def Anagram(s, t) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all(c == 0 for c in count)

s=input("Enter the first string: ")
t=input("Enter the Second string: ")
res=Anagram(s,t)
print(res)

