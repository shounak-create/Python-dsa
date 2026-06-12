arr = [1, 2, 3, 5]

n = len(arr) + 1

expected_sum = n * (n + 1) // 2

actual_sum = 0
for i in range(len(arr)):
    actual_sum += arr[i]

missing = expected_sum - actual_sum

print(missing)