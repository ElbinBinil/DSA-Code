arr = [2, 4, 1, 7, 3]
for i in range(1, len(arr)):
    value = arr[i]
    j = i-1
    while j >= 0 and arr[j] > value:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = value
print(arr)
