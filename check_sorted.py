def checksorted(arr):
    for i in range(1,len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        else:
            return False
    return True

arr = [1, 2, 3, 4, 5]
print(checksorted(arr))