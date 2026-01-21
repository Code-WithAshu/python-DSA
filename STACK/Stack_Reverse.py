#  Using recursive method, the code has time complexity of O(n^2) and space complexity of O(n)
def insert_at_bottom(stack, value):
    if not stack:
        stack.append(value)
        return

    top = stack.pop()
    insert_at_bottom(stack, value)
    stack.append(top)

def reverse_stack(stack):
    if not stack:
        return

    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

stack = [1, 2, 3]   
reverse_stack(stack)
print(stack)


# Optimized method using extra stack has time complexity of O(n) and space complexity of O(n)
def reverse_stack(stack):
    temp_stack = []

    while stack:
        temp_stack.append(stack.pop())

    return temp_stack

stack = [1, 2, 3]
stack = reverse_stack(stack)
print(stack)

    