def next_greater(arr):
    stack = []
    ans = []

    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    ans.reverse()

    return ans


arr = [4, 5, 2, 10, 8]
print(next_greater(arr))