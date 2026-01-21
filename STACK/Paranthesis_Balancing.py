def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)

        elif ch in ')}]':
            if not stack:
                return False

            top = stack.pop()
            if pairs[ch] != top:
                return False
    return len(stack) == 0

string = "{[()()]}"
print("Balanced" if is_balanced(string) else "Not Balanced")
