arr = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]

for i in arr:
    if arr[i] == arr[i-1]:
        arr.remove(arr[i-1])
    else:
        continue

print(arr)