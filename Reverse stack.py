
def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    stack.insert(0, temp)
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print("Reversed stack:", stack)
