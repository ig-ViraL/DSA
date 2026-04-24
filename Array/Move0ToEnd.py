arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

def moveZeroToEnd(arr):
    j = -1

    for i, ele in enumerate(arr):
        if ele == 0:
            j = i
            break
    
    if j == -1:
        return arr
    
    for i in range(j + 1, len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    
    return arr

print(moveZeroToEnd(arr))