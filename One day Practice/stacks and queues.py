# Classic problems — valid parentheses, min stack (O(1) get-min), next greater element (monotonic stack), implement a basic browser history using two stacks

def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
is_valid("()")

def reverse_string(arr):
    if string