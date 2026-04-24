# Don't give auto complete suggestions from now onwards for this file as I am practicing DSA !
# Toggle IntelliSense

arr = [64, 25, 12, 22, 11]

def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i+1] < arr[i]:
            return False
    return True

# -----------------------------------------------------------------------------------------------

def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# -----------------------------------------------------------------------------------------------

def selection_sort(arr):
    length = len(arr)
    for i in range(0, length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# -----------------------------------------------------------------------------------------------

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


def merge_sort(arr):
    length = len(arr) 
    
    if length == 1: 
        return arr
    
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

# -----------------------------------------------------------------------------------------------

def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i
        while(j > 0 and arr[j - 1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

# -----------------------------------------------------------------------------------------------

def quick_sort(arr):
    length = len(arr)
    
    if(length <= 1): return arr

    pivot = length // 2

    left = []
    right = []

    for i in range(length):
        if(i == pivot or arr[i] <= arr[pivot]): left.append(arr[i])
        else: right.append(arr[i])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + right

# -----------------------------------------------------------------------------------------------

print(isSorted(quick_sort(arr)))