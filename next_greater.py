def greater(arr, ind):
    for i in range(ind + 1, len(arr)):
        if arr[ind] < arr[i]:
            return arr[i]
    return -1


arr = [4, 5, 2, 10, 8]
ans = []

for i in range(len(arr)):
    ans.append(greater(arr, i))

print(ans)