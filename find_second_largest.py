arr = [10, 10, 10, 5]

largest = arr[0]
second = None

for i in range(1, len(arr)):

    if arr[i] > largest:
        second = largest
        largest = arr[i]

    elif arr[i] != largest:

        if second is None or arr[i] > second:
            second = arr[i]

if second is None:
    print("No second largest element")
else:
    print("Largest:", largest)
    print("Second Largest:", second)